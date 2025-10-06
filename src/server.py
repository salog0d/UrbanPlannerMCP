from __future__ import annotations
from mcp.server.fastmcp import FastMCP
from schemas.population_schema import (
    PopulationRequest,
    PopulationResponse
)

from schemas.inequality_indicators_schema import (
    UnequalityIndicatorsRequest,
    UnequalityIndicatorsResponse,
)

from core.settings import get_settings

from tools.city_infra_model import InfaModelEndpoints
from tools.population_inequalities_model import InequalityModel

from prompts import _prompts as _prompts   
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
