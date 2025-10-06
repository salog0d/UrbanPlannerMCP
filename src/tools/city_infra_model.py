import requests
from src.schemas.poulation_schema import PopulationRequest, PopulationResponse
from src.core.settings import Settings as settings

class InfaModelEndpoints:

    @staticmethod
    def get_pca(payload: PopulationRequest)->PopulationResponse:
        response = requests.post(
            f"{settings.infra_model_host}/api/pca",
            json=payload.model_dump(by_alias=True),
            timeout=30
        )
        print(response.json())
