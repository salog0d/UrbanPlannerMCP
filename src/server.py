from mcp.server.fastmcp import FastMCP
from schemas.poulation_schema import (
    PopulationRequest,
    PopulationResponse
)

from __future__ import annotations

from src.schemas.inequality_indicators_schema import (
    UnequalityIndicatorsRequest,
    UnequalityIndicatorsResponse,
)

from src.core.settings import get_settings

from src.tools.city_infra_model import InfaModelEndpoints
from src.tools.population_inequalities_model import InequalityModel

from src.prompts import _prompts as _prompts  
from src.resources import _resources as _resources  

settings = get_settings()
mcp = FastMCP(settings.app_name, stateless_http=settings.stateless_http)

@mcp.tool(
    name="City Infrastructure Model",
    description="Analyzes urban infrastructure distribution and service availability using demographic and spatial indicators.",
)
def run_city_infra_model(request: PopulationRequest) -> PopulationResponse:
    return InfaModelEndpoints.get_pca(request)

@mcp.tool(
    name="Population Inequality Model",
    description="Evaluates socioeconomic and spatial inequalities in population data using government and NASA datasets.",
)
def run_population_inequalities_model(
    request: UnequalityIndicatorsRequest,
) -> UnequalityIndicatorsResponse:
    return InequalityModel.get_model(request)

if __name__ == "__main__":
    mcp.run(transport=getattr(settings, "transport", "rest"))
