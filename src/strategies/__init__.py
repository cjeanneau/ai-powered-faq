"""
Module des stratégies de réponse FAQ.

Ce module contient les 3 stratégies à implémenter :
- StrategyALLM : LLM seul
- StrategyBRAG : Recherche sémantique + LLM (RAG)
- StrategyCQA : Recherche sémantique + Q&A extractif

Chaque stratégie hérite de BaseStrategy et doit implémenter :
- initialize() : Initialisation des ressources
- _generate_answer() : Génération de la réponse
"""

from .base import BaseStrategy, FAQResponse

# Import des stratégies (avec gestion des erreurs pour le développement progressif)
try:
    from .strategy_a_llm import StrategyALLM, StrategyA
except ImportError:
    StrategyALLM = None
    StrategyA = None

try:
    from .strategy_b_rag import StrategyBRAG, StrategyB
except ImportError:
    StrategyBRAG = None
    StrategyB = None

try:
    from .strategy_c_qa import StrategyCQA, StrategyC
except ImportError:
    StrategyCQA = None
    StrategyC = None

# Import des solutions formateur (si disponibles)
try:
    from .strategy_a_llm_solution import StrategyALLMSolution
except ImportError:
    StrategyALLMSolution = None

try:
    from .strategy_b_rag_solution import StrategyBRAGSolution
except ImportError:
    StrategyBRAGSolution = None

try:
    from .strategy_c_qa_solution import StrategyCQASolution
except ImportError:
    StrategyCQASolution = None


__all__ = [
    # Classes de base
    "BaseStrategy",
    "FAQResponse",
    # Stratégies étudiants
    "StrategyALLM",
    "StrategyBRAG", 
    "StrategyCQA",
    # Alias courts
    "StrategyA",
    "StrategyB",
    "StrategyC",
    # Solutions formateur
    "StrategyALLMSolution",
    "StrategyBRAGSolution",
    "StrategyCQASolution",
]