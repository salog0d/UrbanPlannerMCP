from pydantic import BaseModel
from enum import Enum

class Constructions(str, Enum):
    PARK = "park"
    SCHOOL = "school"

class UnequalityIndicatorsRequest(BaseModel):
    cve_ent: int
    cve_mun: int
    cve_sun: str
    cvegeo: str
    sun: str
    gmu: str
    iisu_sun: str
    iisu_cd: str

    POBTOT: int

    Empleo: int
    E_basica: int
    E_media: int
    E_superior: int
    Salud_cama: int
    Salud_cons: int
    Abasto: int
    Espacio_ab: int
    Cultura: int
    Est_Tpte: int

    geometry_wkt: str
    lat: float
    lon: float

class UnequalityIndicatorsResponse(BaseModel):
    lat: float
    lon: float
    construction: Constructions