"""
Module de gestion des embeddings pour la recherche sémantique.

Ce module utilise sentence-transformers pour encoder des textes en vecteurs
denses (embeddings) qui peuvent ensuite être comparés par similarité cosinus.
"""

import os
import numpy as np
from typing import Union, Optional
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Import conditionnel
try:
    from sentence_transformers import SentenceTransformer
    HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    HAS_SENTENCE_TRANSFORMERS = False


class EmbeddingManager:
    """Gestionnaire d'embeddings pour la recherche sémantique.
    
    Utilise sentence-transformers pour générer des embeddings de texte.
    Ces embeddings peuvent ensuite être utilisés pour la recherche par similarité.
    
    Attributes:
        model_name: Nom du modèle sentence-transformers
        model: Instance du modèle chargé
        embedding_dim: Dimension des vecteurs générés
    """
    
    # Modèles recommandés
    RECOMMENDED_MODELS = {
        "fast": "all-MiniLM-L6-v2",           # Rapide, 384 dimensions
        "accurate": "all-mpnet-base-v2",       # Plus précis, 768 dimensions
        "multilingual": "paraphrase-multilingual-MiniLM-L12-v2"  # Multilingue
    }
    
    def __init__(self, model_name: Optional[str] = None):
        """Initialise le gestionnaire d'embeddings.
        
        Args:
            model_name: Nom du modèle à utiliser (défaut: depuis .env ou MiniLM)
            
        TODO pour l'étudiant :
        1. Vérifier que sentence-transformers est installé
        2. Charger le modèle
        3. Déterminer la dimension des embeddings
        """
        # TODO: Implémenter l'initialisation
        #
        # Étapes suggérées :
        #
        # 1. Vérifier les dépendances
        # if not HAS_SENTENCE_TRANSFORMERS:
        #     raise RuntimeError(
        #         "sentence-transformers n'est pas installé. "
        #         "Installez-le avec: pip install sentence-transformers"
        #     )
        #
        # 2. Récupérer le nom du modèle
        # self.model_name = model_name or os.getenv(
        #     "EMBEDDING_MODEL", 
        #     self.RECOMMENDED_MODELS["fast"]
        # )
        #
        # 3. Charger le modèle
        # print(f"Chargement du modèle d'embeddings: {self.model_name}")
        # self.model = SentenceTransformer(self.model_name)
        #
        # 4. Récupérer la dimension
        # self.embedding_dim = self.model.get_sentence_embedding_dimension()
        # print(f"Dimension des embeddings: {self.embedding_dim}")
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def encode(
        self, 
        texts: Union[str, list[str]], 
        normalize: bool = True,
        show_progress: bool = False
    ) -> np.ndarray:
        """Encode un ou plusieurs textes en embeddings.
        
        Args:
            texts: Un texte ou une liste de textes à encoder
            normalize: Normaliser les vecteurs (recommandé pour cosine similarity)
            show_progress: Afficher une barre de progression
            
        Returns:
            Array numpy de shape (n_texts, embedding_dim)
            Si un seul texte est fourni, retourne un array 1D
            
        TODO pour l'étudiant :
        1. Gérer le cas d'un texte unique vs liste
        2. Appeler le modèle pour encoder
        3. Normaliser si demandé
        """
        # TODO: Implémenter l'encodage
        #
        # Étapes suggérées :
        #
        # 1. Convertir en liste si nécessaire
        # single_text = isinstance(texts, str)
        # if single_text:
        #     texts = [texts]
        #
        # 2. Encoder avec le modèle
        # embeddings = self.model.encode(
        #     texts,
        #     normalize_embeddings=normalize,
        #     show_progress_bar=show_progress
        # )
        #
        # 3. Retourner au bon format
        # if single_text:
        #     return embeddings[0]
        # return embeddings
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def similarity(
        self, 
        query_embedding: np.ndarray, 
        corpus_embeddings: np.ndarray
    ) -> np.ndarray:
        """Calcule la similarité cosinus entre une requête et un corpus.
        
        Args:
            query_embedding: Embedding de la requête (1D array)
            corpus_embeddings: Embeddings du corpus (2D array)
            
        Returns:
            Array de scores de similarité
            
        TODO pour l'étudiant :
        Implémenter le calcul de similarité cosinus.
        
        Note : Si les vecteurs sont normalisés, cosine similarity = dot product
        """
        # TODO: Implémenter la similarité
        #
        # Pour des vecteurs normalisés :
        # return np.dot(corpus_embeddings, query_embedding)
        #
        # Version générale (si non normalisés) :
        # query_norm = query_embedding / np.linalg.norm(query_embedding)
        # corpus_norms = corpus_embeddings / np.linalg.norm(corpus_embeddings, axis=1, keepdims=True)
        # return np.dot(corpus_norms, query_norm)
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def search(
        self, 
        query: str, 
        corpus: list[str], 
        corpus_embeddings: Optional[np.ndarray] = None,
        top_k: int = 5
    ) -> list[tuple[int, float]]:
        """Recherche les textes les plus similaires à une requête.
        
        Args:
            query: Texte de la requête
            corpus: Liste des textes du corpus
            corpus_embeddings: Embeddings pré-calculés (optionnel, pour optimisation)
            top_k: Nombre de résultats à retourner
            
        Returns:
            Liste de tuples (index, score) triés par score décroissant
            
        TODO pour l'étudiant :
        1. Encoder la requête
        2. Encoder le corpus si nécessaire
        3. Calculer les similarités
        4. Retourner les top_k résultats
        """
        # TODO: Implémenter la recherche
        #
        # Étapes suggérées :
        #
        # 1. Encoder la requête
        # query_emb = self.encode(query)
        #
        # 2. Encoder le corpus si pas déjà fait
        # if corpus_embeddings is None:
        #     corpus_embeddings = self.encode(corpus, show_progress=True)
        #
        # 3. Calculer les similarités
        # scores = self.similarity(query_emb, corpus_embeddings)
        #
        # 4. Trier et retourner top_k
        # top_indices = np.argsort(scores)[-top_k:][::-1]
        # return [(idx, scores[idx]) for idx in top_indices]
        
        raise NotImplementedError("À implémenter par l'étudiant")


# Point d'entrée pour les tests manuels
if __name__ == "__main__":
    print("Test du gestionnaire d'embeddings")
    print("-" * 40)
    
    # TODO: Décommenter une fois implémenté
    # manager = EmbeddingManager()
    # 
    # # Test d'encodage
    # texts = [
    #     "Comment obtenir un acte de naissance ?",
    #     "Où puis-je déposer mes déchets verts ?",
    #     "Quels sont les horaires de la mairie ?"
    # ]
    # 
    # embeddings = manager.encode(texts)
    # print(f"Shape des embeddings: {embeddings.shape}")
    # 
    # # Test de recherche
    # query = "Je voudrais un extrait de naissance"
    # results = manager.search(query, texts, embeddings, top_k=2)
    # 
    # print(f"\nRequête: {query}")
    # print("Résultats:")
    # for idx, score in results:
    #     print(f"  [{score:.3f}] {texts[idx]}")
    
    print("Gestionnaire d'embeddings - À implémenter")