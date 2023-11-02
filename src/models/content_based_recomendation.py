import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus                     import stopwords
from nltk.tokenize                   import word_tokenize
from sklearn.metrics.pairwise        import linear_kernel

from src.entities.article_entity    import ArticleEntity
from src.datasources.supabase.index import supabase

"""
    Este algoritmo usa similitud de cosenos
"""
class ContentBasedRecomendation:

    @staticmethod
    def select_articles() -> list[ ArticleEntity ]:
        
        # TODO: meterle filtros a esta busqueda
        articles    = supabase.table('articles').select('title, description, category_id, change_to').execute()
        categories  = supabase.table('categories').select('*').execute()

        for article in articles.data:
            category_id         = article['category_id']
            category            = next(c for c in categories.data if c['id'] == category_id)
            article['category'] = category['name']

        return articles.data
    
    
    @staticmethod
    def _clear_words(text: str) -> str:

        stop_words     = set( stopwords.words( 'spanish' ) )
        words          = word_tokenize( text )
        filtered_words = [ word for word in words if word.lower() not in stop_words ]

        string = " ".join(filtered_words).lower()
        text_prepared = re.sub(r'[\W\s]', ' ', string)

        return text_prepared
    
    def recomendation(self, title: str):

        data = self.select_articles()
        data = [ { **row, 'description': self._clear_words( row['description'] ) } for row in data ]
        data = [ {**d, 'corpus': f"{d['description']} {d['category']}"} for d in data ]
        
        df = pd.DataFrame( data )
        
        tf_corpus = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0.0, stop_words='english')

        tfidf_matrix_corpus = tf_corpus.fit_transform( df['corpus'] )
        cosine_sim_corpus   = linear_kernel( tfidf_matrix_corpus, tfidf_matrix_corpus )

        recommendations_found =  self._corpus_recomendation(df, cosine_sim_corpus, title)

        return recommendations_found
    
    @staticmethod
    def _corpus_recomendation(data, cosine_sim_corpus, title):
        
        titles  = data['title']
        indices = pd.Series(data.index, index=data['title'])

        idx    = indices[ title ]

        sim_scores = list(enumerate(cosine_sim_corpus[ idx ]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:21]

        articles_indices = [ i[0] for i in sim_scores ]

        response = titles.iloc[ articles_indices ]
        
        return response