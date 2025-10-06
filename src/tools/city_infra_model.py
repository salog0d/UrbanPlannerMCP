import requests
from schemas.population_schema import PopulationRequest, PopulationResponse
from core.settings import Settings as settings

class InfaModelEndpoints:

    @staticmethod
    def get_model(payload: PopulationRequest)->PopulationResponse:
        response = requests.post(
            f"{settings.infra_model_host}/api/pca",
            json=payload.model_dump(by_alias=True),
            timeout=30
        )
        print(response.json())
