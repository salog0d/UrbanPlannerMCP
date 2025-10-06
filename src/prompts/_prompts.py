from mcp.server.fastmcp import PromptTemplate, register_prompt

@register_prompt("urban_analysis")
def urban_analysis_prompt(_ctx: dict) -> PromptTemplate:
    return PromptTemplate(
        name="urban_analysis",  # <-- corregido (antes: urban_ansalysis)
        description="Analiza indicadores urbanos con base en los datos recibidos.",
        template=(
            "Analiza los siguientes datos de zonas urbanas y resume patrones:\n"
            "{data}\n"
            "Filtrado por: {filters}\n"
            "Objetivos: {objectives}\n"
            "Devuelve un análisis estructurado en JSON."
        ),
        input_variables=["data", "filters", "objectives"],
    )

@register_prompt("compare_zones")
def compare_zones_prompt(_ctx: dict) -> PromptTemplate:
    return PromptTemplate(
        name="compare_zones",
        description="Compara dos zonas urbanas en términos de calidad e infraestructura.",
        template=(
            "Compara las zonas:\nZona A: {zone_a}\nZona B: {zone_b}\n"
            "Devuelve diferencias clave."
        ),
        input_variables=["zone_a", "zone_b"],
    )
