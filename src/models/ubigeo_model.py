import os, json

PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
DATA_DIR = os.path.join(PARENT_DIR, 'data')

class _IDepartament:
    id  : str
    name: str

class _IProvince:
    id           : str
    name         : str
    department_id: str

class _IDistrict:
    id           : str
    name         : str
    province_id  : str
    department_id: str

with open(os.path.join(DATA_DIR, 'peru_departamentos.json')) as _f:
    _data_departments: list[_IDepartament] = json.load( _f )

with open(os.path.join(DATA_DIR, 'peru_provincias.json')) as _f:
    _data_provinces: list[_IProvince] = json.load( _f )

with open(os.path.join(DATA_DIR, 'peru_distritos.json')) as _f:
    _data_district: list[_IDistrict] = json.load( _f )

def get_departments():
    return _data_departments

def get_provinces(id_department: str):
    print( id_department )
    return [ x for x in _data_provinces if x['department_id'] == id_department ]

def get_district(id_department: str, id_province):
    return [ x for x in _data_district if (x['department_id'] == id_department and x['province_id'] == id_province) ]
