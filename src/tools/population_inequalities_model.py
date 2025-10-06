import requests
from schemas.inequality_indicators_schema import (
    UnequalityIndicatorsRequest,
    UnequalityIndicatorsResponse,
)
from core.settings import Settings as settings

class InequalityModel:

    @staticmethod
    def get_model(payload: UnequalityIndicatorsRequest)->UnequalityIndicatorsResponse:
        response = requests.post(
            f"{settings.population_model_host}/api/pca",
            json=payload.model_dump(by_alias=True),
            timeout=30
        )
        print(response.json())
