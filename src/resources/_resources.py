from mcp.server.fastmcp import register_resource
import json, os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

@register_resource("urban_indicators")
def get_urban_indicators() -> dict:
    path = os.path.join(DATA_DIR, "indicators.json")
    data = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    return {
        "name": "urban_indicators",
        "description": "Listado de indicadores urbanos y su categoría.",
        "data": data,
    }

@register_resource("model_specs")
def get_model_specs() -> dict:
    return {
        "models": [
            {"name": "PCA_Infrastructure", "endpoint": "/fit"},
            {"name": "Population_Inequality", "endpoint": "/recommend"},
        ]
    }
