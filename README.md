# 🤖 Assistant FAQ Intelligent - Collectivité Territoriale

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Description

API REST d'assistance FAQ pour la Communauté de Communes Val de Loire Numérique. L'assistant répond aux questions des citoyens sur les démarches administratives en s'appuyant sur une base de connaissances structurée.

## 🎯 Vue d'ensemble du projet

```mermaid
flowchart TB
    subgraph INPUT["📥 Entrée"]
        Q[/"❓ Question utilisateur"/]
        FAQ[("📚 Base FAQ60-80 Q/R")]
    end

    subgraph STRATEGIES["🔄 Benchmark des 3 Stratégies"]
        direction TB
        
        subgraph SA["Stratégie A : LLM Seul"]
            A1["Prompt système contextualisé"] --> A2["🤖 LLM Mistral-7B"]
            A2 --> A3["Réponse générée"]
        end
        
        subgraph SB["Stratégie B : RAG Simplifié"]
            B1["🔍 Recherche sémantique"] --> B2["📄 Top-K FAQ pertinentes"]
            B2 --> B3["🤖 LLM +Contexte"]
            B3 --> B4["Réponse augmentée"]
        end
        
        subgraph SC["Stratégie C : Q&A Extractif"]
            C1["🔍 Recherche sémantique"] --> C2["📄 Top-K FAQ pertinentes"]
            C2 --> C3["🎯 Modèle Q&A RoBERTa"]
            C3 --> C4["Réponse extraite"]
        end
    end

    subgraph EVAL["📊 Évaluation"]
        E1["Golden Set25-30 questions"]
        E2["Métriques :• Exactitude 30%• Pertinence 20%• Hallucinations 20%• Latence 15%• Complexité 15%"]
        E3["📈 Rapport Benchmark"]
    end

    subgraph API["🚀 API Production"]
        F1["FastAPI/api/v1/ask"]
        F2["Stratégie retenue"]
        F3["📋 Logs & Monitoring"]
    end

    subgraph CICD["⚙️ CI/CD"]
        G1["pytest"]
        G2["GitHub Actions"]
        G3["Docker"]
    end

    Q --> SA
    Q --> SB
    Q --> SC
    FAQ --> B1
    FAQ --> C1

    A3 --> E1
    B4 --> E1
    C4 --> E1
    E1 --> E2
    E2 --> E3

    E3 -->|"Recommandation"| F2
    F2 --> F1
    F1 --> F3

    F1 --> G1
    G1 --> G2
    G2 --> G3

    style SA fill:#ffebee,stroke:#c62828
    style SB fill:#e3f2fd,stroke:#1565c0
    style SC fill:#e8f5e9,stroke:#2e7d32
    style EVAL fill:#fff3e0,stroke:#ef6c00
    style API fill:#f3e5f5,stroke:#7b1fa2
    style CICD fill:#eceff1,stroke:#546e7a
```

### 🔀 Comparaison des Stratégies - Exemple

```mermaid
flowchart LR
    subgraph QUESTION["Question"]
        Q["Comment obtenir un acte de naissance ?"]
    end

    subgraph STRAT_A["🅰️ LLM Seul"]
        direction TB
        SA1["Prompt + Question"]
        SA2["LLM génère depuis ses connaissances"]
        SA1 --> SA2
    end

    subgraph STRAT_B["🅱️ RAG"]
        direction TB
        SB1["Encode question en embedding"]
        SB2["Recherche FAQ similaires"]
        SB3["LLM génère avec contexte FAQ"]
        SB1 --> SB2 --> SB3
    end

    subgraph STRAT_C["🅲 Q&A Extractif"]
        direction TB
        SC1["Encode question en embedding"]
        SC2["Recherche FAQ similaires"]
        SC3["Modèle extrait réponse du texte"]
        SC1 --> SC2 --> SC3
    end

    Q --> SA1
    Q --> SB1
    Q --> SC1

    SA2 --> RA["💬 Réponse potentiellement hallucinée"]
    SB3 --> RB["💬 Réponse contextualisée"]
    SC3 --> RC["💬 Réponse exacte extraite"]

    style STRAT_A fill:#ffebee
    style STRAT_B fill:#e3f2fd
    style STRAT_C fill:#e8f5e9
```

## 🏗️ Architecture du projet

```txt
.
├── src/
│   ├── strategies/          # Les 3 stratégies de réponse
│   │   ├── __init__.py
│   │   ├── base.py          # Classe abstraite commune
│   │   ├── strategy_a_llm.py
│   │   ├── strategy_b_rag.py
│   │   └── strategy_c_qa.py
│   ├── api/                 # API FastAPI
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes.py
│   │   └── models.py
│   ├── utils/               # Utilitaires
│   │   ├── __init__.py
│   │   ├── embeddings.py
│   │   ├── llm_client.py
│   │   └── logging_config.py
│   └── tests/               # Tests
│       ├── __init__.py
│       ├── test_strategies.py
│       ├── test_api.py
│       └── test_regression.py
├── data/
│   ├── faq_base.json        # Base FAQ fournie
│   ├── golden_set.json      # Jeu de test fourni
│   └── grille_evaluation.csv
├── docs/
│   ├── BRIEF_PROJET.md
│   ├── NOTE_CADRAGE.md
│   ├── RAPPORT_VEILLE.md
│   └── RAPPORT_BENCHMARK.md
├── scripts/
│   ├── run_benchmark.py
│   └── evaluate_results.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## 🚀 Installation

### Prérequis

- Python 3.10 ou supérieur
- pip ou conda
- Git
- (Optionnel) Docker

### Installation locale

1. **Cloner le repository**
```bash
git clone <votre-repo>
cd projet-faq-intelligent
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**
```bash
cp .env.example .env
# Éditer .env avec votre token HuggingFace si nécessaire
```

5. **Vérifier l'installation**
```bash
python -c "import sentence_transformers; print('OK')"
```

### Installation Docker (optionnel)

```bash
docker-compose up --build
```

## 📖 Utilisation

### Lancer l'API

```bash
uvicorn src.api.main:app --reload --port 8000
```

L'API est accessible sur `http://localhost:8000`

Documentation interactive : `http://localhost:8000/docs`

### Tester une question

```bash
curl -X POST "http://localhost:8000/api/v1/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "Comment obtenir un acte de naissance ?"}'
```

### Lancer les tests

```bash
# Tous les tests
pytest

# Avec couverture
pytest --cov=src --cov-report=html

# Tests de non-régression uniquement
pytest src/tests/test_regression.py -v
```

### Exécuter le benchmark

```bash
python scripts/run_benchmark.py
```

## 🔧 Configuration

### Variables d'environnement

| Variable | Description | Défaut |
|----------|-------------|--------|
| `HF_API_TOKEN` | Token HuggingFace (optionnel pour modèles publics) | - |
| `LLM_MODEL` | Modèle LLM à utiliser | `mistralai/Mistral-7B-Instruct-v0.2` |
| `EMBEDDING_MODEL` | Modèle d'embeddings | `all-MiniLM-L6-v2` |
| `LOG_LEVEL` | Niveau de logging | `INFO` |
| `CONFIDENCE_THRESHOLD` | Seuil de confiance minimal | `0.5` |

## 📊 Métriques exposées

L'endpoint `/metrics` expose :

- `faq_requests_total` : Nombre total de requêtes
- `faq_response_latency_seconds` : Latence moyenne
- `faq_low_confidence_total` : Nombre de réponses "je ne sais pas"

## 📝 Documentation

- [Brief projet](docs/BRIEF_PROJET.md)
- [Note de cadrage](docs/NOTE_CADRAGE.md)
- [Rapport de veille](docs/RAPPORT_VEILLE.md)
- [Rapport de benchmark](docs/RAPPORT_BENCHMARK.md)

## 🧪 Tests

Le projet inclut :

- **Tests unitaires** : Validation des fonctions individuelles
- **Tests d'intégration** : Validation des endpoints API
- **Tests de non-régression** : Validation sur le golden set avec seuil de qualité

## 👤 Auteur

Rémi Julien

## 📄 Licence

MIT
