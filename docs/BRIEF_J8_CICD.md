# Brief J8 - CI/CD avec GitHub Actions

## Objectif

Automatiser l'exécution des tests et le déploiement via GitHub Actions pour garantir la qualité du code à chaque modification.

---

## Qu'est-ce que CI/CD ?

### CI - Continuous Integration (Intégration Continue)

**Objectif** : Détecter les bugs automatiquement à chaque push.

```
┌─────────┐     ┌─────────┐
│  Push   │────▶│  Test   │
│  Code   │     │         │
└─────────┘     └─────────┘
```

### CD - Continuous Deployment (Déploiement Continu)

**Objectif** : Déployer automatiquement si tous les tests passent.

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  Build  │────▶│  Test   │────▶│ Deploy  │
│         │     │         │     │         │
└─────────┘     └─────────┘     └─────────┘
```

---

## Compétences visées (REAC)

| Compétence | Description |
|------------|-------------|
| C18 | Automatiser les phases de tests via intégration continue |
| C19 | Créer un processus de livraison continue |

---

## Structure des fichiers

```
.github/
└── workflows/
    ├── ci.yml      # Pipeline CI (tests uniquement)
    └── cicd.yml    # Pipeline CI/CD (tests + déploiement)
```

---

## Pipeline CI (ci.yml)

### Déclencheurs

```yaml
on:
  push:
    branches: [main, develop]    # Push sur main ou develop
  pull_request:
    branches: [main]             # PR vers main
```

### Job

| Job | Rôle |
|-----|------|
| `test` | Exécuter tous les tests pytest |

### Visualisation

```
┌─────────┐
│  TEST   │
│         │
│ unit    │
│ integ   │
│ systeme │
│ coverage│
└─────────┘
```

### Quand l'utiliser ?

- Phase de développement
- Projets sans déploiement automatique
- Validation des Pull Requests

---

## Pipeline CI/CD (cicd.yml)

### Jobs

| Job | Rôle | Dépend de |
|-----|------|-----------|
| `build` | Vérifier que l'app se construit | - |
| `test` | Exécuter tous les tests | build |
| `deploy` | Déployer en production | test |

### Visualisation

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  BUILD  │────▶│  TEST   │────▶│ DEPLOY  │
│         │     │         │     │         │
│ install │     │ pytest  │     │ (main   │
│ verify  │     │ coverage│     │  only)  │
└─────────┘     └─────────┘     └─────────┘
     │               │               │
     └───────────────┴───────────────┘
              needs (dépendances)
```

### Condition de déploiement

```yaml
deploy:
  needs: test
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
```

Le déploiement s'exécute **uniquement** si :
- ✅ Tous les tests passent
- ✅ Push sur la branche `main`
- ❌ Pas sur les Pull Requests

---

## Anatomie d'un workflow

```yaml
# Nom affiché dans GitHub
name: CI Pipeline

# Déclencheurs
on:
  push:
    branches: [main]

# Liste des jobs
jobs:
  # Un job
  test:
    name: 🧪 Tests              # Nom affiché
    runs-on: ubuntu-latest      # Environnement
    
    # Étapes du job
    steps:
      # Étape 1 : Récupérer le code
      - name: Checkout code
        uses: actions/checkout@v4
      
      # Étape 2 : Installer Python
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      
      # Étape 3 : Commande bash
      - name: Run tests
        env:
          HF_API_TOKEN: ${{ secrets.HF_API_TOKEN }}
        run: pytest tests/ -v
```

### Éléments clés

| Élément | Description |
|---------|-------------|
| `name` | Nom affiché dans l'interface GitHub |
| `on` | Événements qui déclenchent le workflow |
| `jobs` | Liste des jobs à exécuter |
| `runs-on` | Système d'exploitation (ubuntu-latest) |
| `needs` | Job(s) qui doivent réussir avant |
| `steps` | Liste des étapes du job |
| `uses` | Action GitHub pré-construite |
| `run` | Commande bash à exécuter |
| `env` | Variables d'environnement |
| `secrets` | Secrets GitHub (tokens, clés) |

---

## Configuration des secrets

Les secrets permettent de stocker des informations sensibles (tokens, mots de passe).

### Ajouter un secret

1. Aller dans **Settings** > **Secrets and variables** > **Actions**
2. Cliquer **New repository secret**
3. Ajouter :
   - `HF_API_TOKEN` : Votre token HuggingFace

### Utilisation dans le workflow

```yaml
env:
  HF_API_TOKEN: ${{ secrets.HF_API_TOKEN }}
```

---

## Commandes utiles

### Actions GitHub courantes

```yaml
# Récupérer le code
- uses: actions/checkout@v4

# Installer Python
- uses: actions/setup-python@v5
  with:
    python-version: '3.10'

# Cache pip (accélère les builds)
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

### Commandes bash

```yaml
# Installer les dépendances
- run: pip install -r requirements.txt

# Lancer les tests
- run: pytest tests/ -v

# Tests avec couverture
- run: pytest --cov=src --cov-report=xml
```

---

## Bonnes pratiques

### 1. Ordre des jobs

```
build → test → deploy
```

Chaque job attend que le précédent réussisse.

### 2. Fail fast

Si le build échoue, inutile de lancer les tests.

### 3. Cache des dépendances

```yaml
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
```

Accélère les builds suivants en réutilisant les dépendances.

### 4. Secrets pour les tokens

Ne jamais mettre de token dans le code !

```yaml
# ❌ Mauvais
env:
  HF_API_TOKEN: hf_xxxxxxxxxxxxx

# ✅ Bon
env:
  HF_API_TOKEN: ${{ secrets.HF_API_TOKEN }}
```

### 5. Déploiement conditionnel

```yaml
if: github.ref == 'refs/heads/main' && github.event_name == 'push'
```

Déployer uniquement depuis main.

---

## Travail à réaliser

### Étape 1 : Créer la structure

```bash
mkdir -p .github/workflows
```

### Étape 2 : Pipeline CI

1. Créer `.github/workflows/ci.yml`
2. Configurer lint + test
3. Ajouter le secret `HF_API_TOKEN`
4. Pousser et vérifier que le pipeline passe ✅

### Étape 3 : Pipeline CI/CD

1. Créer `.github/workflows/cicd.yml`
2. Ajouter le job build
3. Ajouter le job deploy (simulé)
4. Tester sur une branche develop puis main

### Étape 4 : Vérification

- [ ] Pipeline visible dans l'onglet **Actions** de GitHub
- [ ] Badge de statut dans le README
- [ ] Tous les jobs passent ✅

---

## Ajouter un badge de statut

Dans votre README.md :

```markdown
![CI](https://github.com/VOTRE_USERNAME/VOTRE_REPO/workflows/CI%20Pipeline/badge.svg)
```

Exemple de rendu : ![CI](https://img.shields.io/badge/CI-passing-brightgreen)

---

## Dépannage

| Problème | Solution |
|----------|----------|
| Secret non disponible | Vérifier le nom exact dans Settings > Secrets |
| Permission denied | Vérifier les permissions du workflow |
| Tests qui échouent | Lancer `pytest` en local d'abord |
| Module not found | Vérifier le PYTHONPATH ou les imports |
| Timeout | Augmenter le timeout ou optimiser les tests |

---

## Livrables attendus

| Livrable | Description |
|----------|-------------|
| `.github/workflows/ci.yml` | Pipeline CI fonctionnel |
| `.github/workflows/cicd.yml` | Pipeline CI/CD complet |
| Secret `HF_API_TOKEN` | Configuré dans GitHub |
| Screenshot | Pipeline GitHub Actions vert ✅ |

---

## Pour aller plus loin

- Ajouter des notifications Slack/Discord en cas d'échec
- Configurer un déploiement réel (Heroku, Railway, Docker)
- Ajouter des tests de performance dans le pipeline
- Mettre en place un environnement de staging