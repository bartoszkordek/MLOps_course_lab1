# MLOps Course – Lab 1  🚀

## 📘 Project Description

The goal of this project is to introduce core MLOps concepts by building a simple, reproducible Machine Learning application.

The project focuses on:

- implementing a basic ML workflow (data → model → evaluation)  
- training a model using scikit-learn  
- managing configuration using environment variables and YAML files  
- separating code from configuration  
- ensuring reproducibility of experiments  
- exposing basic functionality via a REST API (FastAPI)  

This project represents an early stage of the MLOps lifecycle, focusing on **development and experimentation**, rather than production deployment.

---
## 📌 Project Scope

The goal of this project is to introduce core MLOps concepts by building a simple, configurable Machine Learning application.

The project focuses on:

- implementing a basic ML workflow (data loading → preprocessing → model training → evaluation)  
- using **pandas** for data handling and **scikit-learn** for model training  
- managing configuration via **environment variables (.env)** and **YAML files**  
- separating configuration from code for better reproducibility  
- structuring the project as a Python package  
- exposing basic functionality through a **FastAPI** application  

This project represents an early stage of the MLOps lifecycle, focusing on **development, configuration, and reproducibility**, 
rather than production deployment.

---
## 🏗️ Project Structure
```text
.
├── main.py                   # Main entry point for the ML pipeline
├── api.py                    # Model serving API (FastAPI)
├── api/                      # Source code  
│   └── models/               # API schemas
├── config/                   # Environment configuration   
├── models/                   # Trained and serialized models
├── tests/                    # Unit and integration tests (pytest) 
├── .dockerignore             # Files and folders to be ignored by Docker
├── .gitignore                # Files and folders to be ignored by Git
├── .pre-commit-config.yaml   # Hooks for code formatting and linting
├── .sops.yaml                 # SOPS configuration for secret encryption
├── inference.py              # Logic for model prediction
├── training.py               # Data loading and model training
├── Dockerfile                # Docker configuration for the app
├── docker-compose.yml        # Multi-container orchestration
├── pyproject.toml            # Project metadata and dependencies (uv)
├── uv.lock                   # Locked dependency versions (uv)
├── pytest.ini                # Pytest configuration and markers
└── README.md                 # Project documentation
```

---

## ⚙️ Requirements
- uv
- gpg
- Docker
- Docker Compose
### `uv` installation:

```bash
pip install uv
```
or (macOS / Linux):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
or via Homebrew
```bash
brew install uv
```

---
## 🔧 Installation
Clone repository
```bash
git clone https://github.com/bartoszkordek/MLOps_course_homework1.git
cd MLOps_course_homework1
```
Verify `uv` installation by running:
```bash
uv --version
```

Initialize the Python project in a current directory
```bash
uv venv --python 3.12
uv init
```

Activate environment:
```bash
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate   # Windows
```
To deactivate environment:
```bash
deactivate
```

Before running server train and save model. To do it run `traning.py` script.
```bash
uv run traning.py
```

Run the actual application server, exposed on port 8000:
```bash
uv run uvicorn app:app --reload --port 8000
```

---
## 🔮 Using the API

### Server address

```bash
curl http://localhost:8000/
```
**Response:**
```json
{
  "message": "Welcome to the ML API" 
}
```
### System health check
```bash
curl -X GET "http://localhost:8000/health"
```
**Sample response:**
```json
{
  "status":"ok"
}
```

### Prediction
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
```

Sample response:
```json
{
  "prediction": "setosa"
}
```

---
## 🧪 Unit Testing
The project includes an extensive set of **unit tests** using [pytest](https://docs.pytest.org/).  

Run the tests using the following command:
```bash
uv run pytest tests -rP
```

## 📊 Model

The project includes training a simple Machine Learning model using scikit-learn based on [iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)

- model is trained within the project  
- used for demonstration and educational purposes  
- no advanced optimization or tuning  

---
## 🧠 MLOps Focus

This project introduces fundamental MLOps practices:

- configuration management (dotenv, YAML)  
- reproducibility of experiments  
- separation of concerns (data, config, logic)  
- integrating ML code into an application  

It reflects the early stages of the ML lifecycle, before deployment and monitoring.

---
## ⚠️ Limitations

- no advanced feature engineering  
- no experiment tracking  
- no CI/CD pipeline  
- no production deployment  

The project is focused on learning MLOps foundations.

---
## 🐳 Containerization

The application is containerized using Docker, which ensures:

- consistent runtime environment
- easy deployment
- reproducibility across machines

Build the Docker image:
```bash
docker build -t sentiment-analysis-app .
```

Run the Docker container:
```bash
docker run --rm -p 8000:8000 sentiment-analysis-app
```

To stop the container, press Ctrl+C in the terminal where it's running or:
```bash
docker ps -a # then <copy container-id> you want to delete
docker stop <container-id>
```

or using Docker Compose:
```bash
docker compose up
```

Turn off with
```bash
docker compose down
```
---
## 🧠 Tech Stack
- **Python 3.12** – core language

### API & Serving
- **FastAPI** – REST API for model inference
- **Uvicorn** – ASGI server

### Machine Learning
- **pandas** – data processing  
- **scikit-learn** – model training 

### Configuration
- **python-dotenv** – environment variables  
- **pydantic-settings** – config management  
- **PyYAML** – YAML configuration  
- **sops** - secrets management

### Testing
- **pytest** – test framework
- **httpx** – API testing

### Code Quality
- **ruff** – linting & formatting
- **xenon** – code complexity monitoring
- **pre-commit** – git hooks

### Environment & Packaging
- **pyproject.toml** – dependency and project management
- **uv** – package installer (with custom PyTorch index)

### Containerization
- **Docker** – containerized deployment
- **Docker Compose** - orchestration
---
## 📖 API Documentation
Once the server is running, the interactive documentation is available at:
**Swagger UI**: http://127.0.0.1:8000/docs

---
## 🪪 License
This project is released under the MIT License.
