import requests
from src.schemas.poulation_schema import UnequalityIndicatorsRequest, UnequalityIndicatorsResponse
from src.core.settings import Settings as settings

class InequalityModel:

    @staticmethod
    def get_model(payload: UnequalityIndicatorsRequest)->UnequalityIndicatorsResponse:
        response = requests.post(
            f"{settings.population_model_host}/api/pca",
            json=payload.model_dump(by_alias=True),
            timeout=30
        )
        print(response.json())
