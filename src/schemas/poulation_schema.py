from pydantic import BaseModel, Field


class PopulationRequest(BaseModel):
    pobtot: int = Field(description="Total population.")
    pobmas: int = Field(description="Male population.")
    pobfem: int = Field(description="Female population.")
    pob0_14: int = Field(description="Population aged 0–14.")
    pob15_29: int = Field(description="Population aged 15–29.")
    pob30_59: int = Field(description="Population aged 30–59.")
    p_60: int = Field(description="Population aged 60 and over.")
    p_cd_t: int = Field(description="People with disabilities (total).")
    graproes: float = Field(description="Average years of schooling (15+ total).")
    graproes_f: float = Field(description="Average years of schooling (15+ women).")
    graproes_m: float = Field(description="Average years of schooling (15+ men).")

    vivtot: int = Field(description="Total dwellings (inhabited + uninhabited + temporary).")
    vivpar: int = Field(description="Total private dwellings (inhabited + uninhabited + temporary).")
    tvipahab: int = Field(description="Inhabited private dwellings.")
    vivnohab: int = Field(description="Uninhabited private dwellings (vacant + temporary use).")
    prom_ocup: float = Field(description="Average occupants per inhabited private dwelling.")
    pro_ocup_c: float = Field(description="Average occupants per room in inhabited private dwellings.")
    v3masocu: int = Field(description="Inhabited dwellings with ≥3 occupants per room (count).")
    v3masocu_p: float = Field(description="Inhabited dwellings with ≥3 occupants per room (percentage).")

    vph_pidt: int = Field(description="Dwellings with floor other than dirt (count).")
    vph_pidt_p: float = Field(description="Dwellings with floor other than dirt (percentage).")
    vph_c_el: int = Field(description="Dwellings with electricity (count).")
    vph_c_el_p: float = Field(description="Dwellings with electricity (percentage).")
    vph_exsa: int = Field(description="Dwellings with toilet/sanitary system (count).")
    vph_exsa_p: float = Field(description="Dwellings with toilet/sanitary system (percentage).")
    vph_dren: int = Field(description="Dwellings with drainage (count).")
    vph_dren_p: float = Field(description="Dwellings with drainage (percentage).")

    recucall_c: str = Field(description="Street surface type (paved, cobblestone, etc.).")
    rampas_c: bool = Field(description="Wheelchair ramp present.")
    pasopeat_c: bool = Field(description="Pedestrian crossing present.")
    banqueta_c: bool = Field(description="Sidewalk present.")
    guarnici_c: bool = Field(description="Curb present.")
    ciclovia_c: bool = Field(description="Bike lane present.")
    ciclocar_c: bool = Field(description="Cycle track present.")
    alumpub_c: bool = Field(description="Street lighting present.")
    letrero_c: bool = Field(description="Street name sign present.")
    telpub_c: bool = Field(description="Public phone present.")
    arboles_c: bool = Field(description="Trees or palms present.")
    drenajep_c: bool = Field(description="Storm drain present.")
    transcol_c: bool = Field(description="Public transport present.")
    acesoper_c: bool = Field(description="Pedestrian access restriction (gate/barrier) present.")
    acesoaut_c: bool = Field(description="Vehicle access restriction present.")
    puessemi_c: bool = Field(description="Semi-fixed stand present.")
    puesambu_c: bool = Field(description="Mobile stand present.")
    lat: float
    lon: float

class PopulationResponse(BaseModel):
    weak_component: str
    weak_score: float
    worst_feature: str
    worse_feaure_z: float
    recommended_intervention: str
    aggregation: str
    method: str
    n_obs_in_zone: int