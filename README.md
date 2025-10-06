
##  UrbanPlannerMCP

UrbanPlannerMCP provides an **MCP-compliant service layer** for urban planning analysis.
It exposes modular analytical tools that can be streamed or called programmatically by orchestrators, allowing you to evaluate city infrastructure, demographic distributions, and social inequalities.

This server serves as the **analytical engine** for the broader *Urban Planner AI* ecosystem, connecting models, schemas, and prompt templates in a consistent and reusable manner.

---

##  Features

* **MCP Server Integration** – Built on [`fastmcp`](https://github.com/modelcontextprotocol/fastmcp) for stateless and streaming tool execution.
* **Tool Modularization** – Tools like `CityInfraModel` and `PopulationInequalitiesModel` expose well-defined analytical functions.
* **Structured Schemas** – Type-safe Pydantic schemas for population and inequality data.
* **Prompt Templates** – Custom prompt builders for LLM-based urban analysis and comparison tasks.
* **Configuration Layer** – Centralized `Settings` class for environment variables and API integration.
* **Extensible Architecture** – Ready to integrate new tools and models (e.g., for housing, emissions, or mobility).

---

##  Project Structure

```
src/
├── core/
│   ├── __init__.py
│   └── settings.py              # Global settings (API keys, env vars)
│
├── prompts/
│   ├── __init__.py
│   └── _prompts.py              # LLM prompt templates for analyses
│
├── schemas/
│   ├── __init__.py
│   ├── inequality_indicators_schema.py  # Inequality metrics schema
│   └── poulation_schema.py              # Population & demographics schema
│
├── tools/
│   ├── __init__.py
│   ├── city_infra_model.py              # MCP tool for city infrastructure analysis
│   ├── population_inequalities_model.py # MCP tool for population inequality modeling
│   └── server.py                        # Main FastMCP server configuration
│
├── .env.example
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

##  Core Modules

### `core/settings.py`

Centralizes all configuration and environment variable management, including:

* API keys (Google Maps, NASA datasets, etc.)
* Database URLs
* Model host settings (`mcp_host`)

### `prompts/_prompts.py`

Contains reusable **prompt templates** for:

* Urban zone comparison
* Infrastructure pattern summarization

### `schemas/`

Defines input/output structures for MCP tools:

* `PopulationRequest`, `PopulationResponse`
* `UnequalityIndicatorsRequest`, `UnequalityIndicatorsResponse`

### `tools/`

Each file defines an **MCP tool** via `@mcp.tool` decorator:

* `city_infra_model.py`: Evaluates infrastructure coverage and accessibility.
* `population_inequalities_model.py`: Computes inequality metrics across regions.

### `tools/server.py`

Main entrypoint for running the **FastMCP server**.

---

##  Running Locally

### 1. Clone the Repository

```bash
git clone https://github.com/salog0d/UrbanPlannerMCP.git
cd UrbanPlannerMCP
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# or
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Copy `.env.example` to `.env` and update credentials:

```bash
cp .env.example .env
```

### 5. Run the MCP Server

```bash
python -m src.tools.server
```

---

##  Example Tools

### City Infrastructure Model

```python
@mcp.tool(
    name="City Infrastructure Model",
    description="Analyzes urban infrastructure distribution and service availability using demographic and spatial indicators.",
)
def run_city_infra_model(request: PopulationRequest) -> PopulationResponse:
    """Analyzes infrastructure density, accessibility, and service coverage across city zones."""
    return ...
```

### Population Inequality Model

```python
@mcp.tool(
    name="Population Inequality Model",
    description="Evaluates socioeconomic and spatial inequalities in population data using government and NASA datasets.",
)
def run_population_inequalities_model(
    request: UnequalityIndicatorsRequest,
) -> UnequalityIndicatorsResponse:
    """Calculates inequality metrics such as employment, education, and health access disparities."""
    return ...
```

---

##  Dependencies

| Library                | Purpose                           |
| ---------------------- | --------------------------------- |
| `fastmcp`              | MCP server and tool orchestration |
| `pydantic`             | Schema validation                 |
| `requests`             | External API calls                |
| `pandas`, `numpy`      | Data manipulation                 |
| `geopandas`, `shapely` | Geospatial processing             |
| `scikit-learn`         | ML-based urban analytics          |

---

##  Future Extensions

* Integration with **AWS ECS** or **Lambda** for scalable inference.
* **OpenStreetMap** and **Google Places** ingestion.
* **Snowflake** data warehouse connection for faster queries.
* **Dashboard visualization** layer using Streamlit or React.

---

##  License

This project is licensed under the **MIT License**.
See [LICENSE](LICENSE) for details.

---

Would you like me to include a **badges section** (Python version, license, last commit, etc.) and a **diagram of the module relationships** at the top for a more polished GitHub presentation?


