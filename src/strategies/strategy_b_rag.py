"""
Stratégie B : Recherche sémantique + LLM (RAG simplifié)

Cette stratégie combine :
1. Recherche sémantique pour trouver les FAQ pertinentes
2. Génération de réponse par LLM avec le contexte récupéré

C'est une version simplifiée de l'architecture RAG (Retrieval-Augmented Generation).

Avantages attendus :
- Réponses basées sur des données réelles de la FAQ
- Réduction des hallucinations
- Possibilité de citer les sources

Inconvénients attendus :
- Plus complexe à implémenter
- Dépendant de la qualité des embeddings
- Latence plus élevée (2 étapes)
"""

import os
from dotenv import load_dotenv
import logging
from typing import Dict, Any, List
from sentence_transformers import SentenceTransformer, util
from huggingface_hub import InferenceClient

from .base import BaseStrategy, FAQResponse

# Chargement des variables d'environnement
load_dotenv()

# Configuration du logger
logger = logging.getLogger(__name__)

class StrategyBRAG(BaseStrategy):
    """
    Stratégie RAG simplifiée : recherche sémantique + génération LLM.
    
    Workflow :
    1. Encoder la question en embedding
    2. Rechercher les FAQ les plus similaires (top_k)
    3. Construire un prompt avec le contexte récupéré
    4. Générer la réponse avec le LLM
    5. Retourner la réponse avec les sources
    """
    
    def initialize(self) -> None:
        """
        Initialise les modèles d'embeddings et le client LLM.
        
        TODO pour l'étudiant :
        1. Récupérer les configurations depuis les variables d'environnement
        2. Charger le modèle d'embeddings (SentenceTransformer)
        3. Créer le client LLM (InferenceClient)
        4. Construire l'index des embeddings de la base FAQ
        
        Variables d'environnement attendues :
        - EMBEDDING_MODEL : Modèle d'embeddings (défaut: "sentence-transformers/all-MiniLM-L6-v2")
        - LLM_MODEL : Modèle LLM (défaut: "mistralai/Mistral-7B-Instruct-v0.2")
        - HF_API_TOKEN : Token HuggingFace
        - TOP_K_RESULTS : Nombre de FAQ à récupérer (défaut: 3)
        - CONFIDENCE_THRESHOLD : Seuil de similarité minimal (défaut: 0.5)
        
        Raises:
            ValueError: Si HF_API_TOKEN n'est pas défini
        """
        # TODO: Récupérer la configuration
        # self.embedding_model_name = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
        # self.llm_model_name = os.getenv("LLM_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")
        # self.api_token = os.getenv("HF_API_TOKEN")
        # self.top_k = int(os.getenv("TOP_K_RESULTS", 3))
        # self.confidence_threshold = float(os.getenv("CONFIDENCE_THRESHOLD", 0.5))
        
        # TODO: Charger le modèle d'embeddings (local, pas d'API)
        # logger.info(f"Chargement du modèle d'embeddings: {self.embedding_model_name}")
        # self.embedding_model = SentenceTransformer(self.embedding_model_name)
        
        # TODO: Créer le client LLM
        # self.llm_client = InferenceClient(token=self.api_token, timeout=60)
        
        # TODO: Construire l'index
        # self._build_index()
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def _build_index(self) -> None:
        """
        Construit l'index des embeddings pour toutes les FAQ.
        
        TODO pour l'étudiant :
        1. Extraire le texte de chaque FAQ (question + réponse)
        2. Encoder tous les textes en embeddings
        3. Stocker les embeddings pour la recherche
        
        Note : Cette méthode est appelée une seule fois à l'initialisation.
        Les embeddings sont conservés en mémoire pour les recherches ultérieures.
        """
        # TODO: Préparer les textes
        # On combine question + réponse pour une meilleure recherche
        # self.faq_texts = []
        # for faq in self.faq_base:
        #     text = f"{faq['question']} {faq.get('answer', '')}"
        #     self.faq_texts.append(text)
        
        # TODO: Encoder tous les textes
        # self.faq_embeddings = self.embedding_model.encode(
        #     self.faq_texts,
        #     convert_to_tensor=True,
        #     show_progress_bar=False
        # )
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def _search_similar(self, question: str) -> List[Dict[str, Any]]:
        """
        Recherche les FAQ les plus similaires à la question.
        
        TODO pour l'étudiant :
        1. Encoder la question en embedding
        2. Calculer la similarité cosinus avec tous les embeddings FAQ
        3. Trier par score décroissant
        4. Retourner les top_k résultats
        
        Args:
            question: La question de l'utilisateur
            
        Returns:
            Liste de dicts avec {"faq": dict_faq, "score": float}
        
        Hint : Utilisez util.cos_sim() de sentence_transformers
        """
        # TODO: Encoder la question
        # q_emb = self.embedding_model.encode(question, convert_to_tensor=True)
        
        # TODO: Calculer les similarités
        # similarities = util.cos_sim(q_emb, self.faq_embeddings)[0]
        
        # TODO: Récupérer les top_k indices
        # top_indices = similarities.argsort(descending=True)[:self.top_k]
        
        # TODO: Construire les résultats
        # results = []
        # for idx in top_indices:
        #     idx = int(idx)
        #     results.append({
        #         "faq": self.faq_base[idx],
        #         "score": float(similarities[idx])
        #     })
        # return results
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def _build_context(self, similar_faqs: List[Dict[str, Any]]) -> str:
        """
        Construit le contexte pour le LLM à partir des FAQ récupérées.
        
        TODO pour l'étudiant :
        Formater les FAQ en un texte lisible que le LLM pourra utiliser.
        
        Args:
            similar_faqs: Liste de dicts {"faq": ..., "score": ...}
            
        Returns:
            Texte formaté pour le prompt
        
        Format suggéré :
            [FAQ 1]
            Q: Comment obtenir un acte de naissance ?
            R: Vous pouvez faire la demande en ligne...
            
            [FAQ 2]
            ...
        """
        # TODO: Formater le contexte
        # parts = []
        # for i, item in enumerate(similar_faqs, 1):
        #     faq = item["faq"]
        #     parts.append(f"[FAQ {i}]\nQ: {faq['question']}\nR: {faq['answer']}\n")
        # return "\n".join(parts)
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def _call_llm(self, question: str, context: str) -> str:
        """
        Appelle le LLM avec le contexte pour générer la réponse.
        
        TODO pour l'étudiant :
        1. Construire le prompt système (instructions pour le LLM)
        2. Construire le prompt utilisateur (contexte + question)
        3. Appeler chat_completion
        4. Extraire et retourner la réponse
        
        Args:
            question: La question originale
            context: Le contexte construit à partir des FAQ
            
        Returns:
            La réponse générée par le LLM
        
        Important : Instructez le LLM de répondre UNIQUEMENT en français
        et de se baser sur le contexte fourni.
        """
        # TODO: Construire les prompts
        # system_prompt = """Tu es un assistant FAQ pour une collectivité territoriale française.
        # Réponds UNIQUEMENT en français et en te basant sur le contexte fourni.
        # Si le contexte ne permet pas de répondre, dis-le clairement."""
        
        # user_prompt = f"""Contexte (FAQ officielles):
        # {context}
        # 
        # Question: {question}
        # 
        # Réponds de manière claire et concise."""
        
        # TODO: Appeler le LLM
        # messages = [
        #     {"role": "system", "content": system_prompt},
        #     {"role": "user", "content": user_prompt}
        # ]
        # response = self.llm_client.chat_completion(
        #     model=self.llm_model_name,
        #     messages=messages,
        #     max_tokens=400,
        #     temperature=0.3  # Plus déterministe pour les FAQ
        # )
        # return response.choices[0].message.content.strip()
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def _generate_answer(self, question: str) -> FAQResponse:
        """
        Génère une réponse en combinant recherche sémantique et génération LLM.
        
        TODO pour l'étudiant :
        1. Rechercher les FAQ similaires
        2. Vérifier si le meilleur score dépasse le seuil de confiance
        3. Si non, retourner une réponse "pas d'information"
        4. Si oui, construire le contexte et appeler le LLM
        5. Préparer la liste des sources
        6. Retourner la FAQResponse complète
        
        Args:
            question: La question posée par l'utilisateur
            
        Returns:
            FAQResponse avec la réponse, la confiance et les sources
        """
        # TODO: Rechercher les FAQ similaires
        # similar_faqs = self._search_similar(question)
        # best_score = similar_faqs[0]["score"] if similar_faqs else 0
        
        # TODO: Vérifier le seuil
        # if best_score < self.confidence_threshold:
        #     return FAQResponse(
        #         answer="Je n'ai pas trouvé d'information pertinente dans notre FAQ.",
        #         confidence=best_score,
        #         strategy="rag",
        #         sources=[]
        #     )
        
        # TODO: Générer la réponse
        # context = self._build_context(similar_faqs)
        # answer_text = self._call_llm(question, context)
        
        # TODO: Préparer les sources
        # sources = [
        #     {
        #         "id": item["faq"].get("id"),
        #         "question": item["faq"]["question"],
        #         "score": round(item["score"], 3)
        #     }
        #     for item in similar_faqs
        # ]
        
        # TODO: Retourner la réponse
        # return FAQResponse(
        #     answer=answer_text,
        #     confidence=best_score,
        #     strategy="rag",
        #     sources=sources
        # )
        
        raise NotImplementedError("À implémenter par l'étudiant")


# Alias pour la compatibilité
StrategyB = StrategyBRAG


# Point d'entrée pour les tests manuels
if __name__ == "__main__":
    print("Stratégie B (RAG) - À implémenter")