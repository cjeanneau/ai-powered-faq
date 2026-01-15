"""
SOLUTION FORMATEUR - Gestionnaire d'Embeddings

Ce fichier contient l'implémentation complète et fonctionnelle du gestionnaire d'embeddings.
"""

import os
import numpy as np
from typing import Union, Optional, List, Tuple
from dotenv import load_dotenv

load_dotenv()

try:
    from sentence_transformers import SentenceTransformer
    HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    HAS_SENTENCE_TRANSFORMERS = False


class EmbeddingManager:
    """Gestionnaire d'embeddings - VERSION SOLUTION."""
    
    RECOMMENDED_MODELS = {
        "fast": "all-MiniLM-L6-v2",
        "accurate": "all-mpnet-base-v2",
        "multilingual": "paraphrase-multilingual-MiniLM-L12-v2"
    }
    
    def __init__(self, model_name: Optional[str] = None):
        """Initialise le gestionnaire d'embeddings."""
        if not HAS_SENTENCE_TRANSFORMERS:
            raise RuntimeError(
                "sentence-transformers n'est pas installé. "
                "Installez-le avec: pip install sentence-transformers"
            )
        
        self.model_name = model_name or os.getenv(
            "EMBEDDING_MODEL", 
            self.RECOMMENDED_MODELS["fast"]
        )
        
        print(f"[EmbeddingManager] Chargement du modèle: {self.model_name}")
        self.model = SentenceTransformer(self.model_name)
        self.embedding_dim = self.model.get_sentence_embedding_dimension()
        print(f"[EmbeddingManager] Dimension des embeddings: {self.embedding_dim}")
    
    def encode(
        self, 
        texts: Union[str, List[str]], 
        normalize: bool = True,
        show_progress: bool = False
    ) -> np.ndarray:
        """Encode un ou plusieurs textes en embeddings."""
        single_text = isinstance(texts, str)
        if single_text:
            texts = [texts]
        
        embeddings = self.model.encode(
            texts,
            normalize_embeddings=normalize,
            show_progress_bar=show_progress,
            convert_to_numpy=True
        )
        
        if single_text:
            return embeddings[0]
        return embeddings
    
    def similarity(
        self, 
        query_embedding: np.ndarray, 
        corpus_embeddings: np.ndarray
    ) -> np.ndarray:
        """Calcule la similarité cosinus entre une requête et un corpus."""
        # Si les vecteurs sont normalisés, cosine = dot product
        if corpus_embeddings.ndim == 1:
            return np.dot(query_embedding, corpus_embeddings)
        return np.dot(corpus_embeddings, query_embedding)
    
    def search(
        self, 
        query: str, 
        corpus: List[str], 
        corpus_embeddings: Optional[np.ndarray] = None,
        top_k: int = 5
    ) -> List[Tuple[int, float]]:
        """Recherche les textes les plus similaires à une requête."""
        # Encoder la requête
        query_emb = self.encode(query)
        
        # Encoder le corpus si nécessaire
        if corpus_embeddings is None:
            corpus_embeddings = self.encode(corpus, show_progress=len(corpus) > 100)
        
        # Calculer les similarités
        scores = self.similarity(query_emb, corpus_embeddings)
        
        # Trier et retourner top_k
        top_k = min(top_k, len(corpus))
        top_indices = np.argsort(scores)[-top_k:][::-1]
        
        return [(int(idx), float(scores[idx])) for idx in top_indices]


# Test
if __name__ == "__main__":
    print("=" * 50)
    print("Test du gestionnaire d'embeddings (Solution)")
    print("=" * 50)
    
    manager = EmbeddingManager()
    
    # Corpus de test
    corpus = [
        "Comment obtenir un acte de naissance ?",
        "Où puis-je déposer mes déchets verts ?",
        "Quels sont les horaires de la mairie ?",
        "Comment faire une demande de permis de construire ?",
        "Où se trouve la déchetterie la plus proche ?",
        "Comment inscrire mon enfant à l'école ?",
        "Quels documents pour un mariage ?",
        "Comment obtenir une carte d'identité ?"
    ]
    
    print("\n1. Encodage du corpus...")
    corpus_embeddings = manager.encode(corpus)
    print(f"   Shape: {corpus_embeddings.shape}")
    
    print("\n2. Test de recherche...")
    queries = [
        "Je voudrais un extrait de naissance",
        "Où jeter mes feuilles mortes ?",
        "À quelle heure ouvre la mairie ?"
    ]
    
    for query in queries:
        print(f"\n   Query: '{query}'")
        results = manager.search(query, corpus, corpus_embeddings, top_k=3)
        for idx, score in results:
            print(f"   [{score:.3f}] {corpus[idx]}")