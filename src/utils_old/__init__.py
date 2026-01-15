"""
Module utilitaires pour le projet FAQ Intelligent.
"""

from .llm_client import LLMClient
from .embeddings import EmbeddingManager

__all__ = [
    "LLMClient",
    "EmbeddingManager",
]