"""
Stratégie C : Q&A Extractif

Cette stratégie combine :
1. Recherche sémantique pour trouver les FAQ pertinentes
2. Modèle de Question-Answering extractif pour extraire la réponse

Contrairement à la stratégie B, ici on n'utilise PAS de LLM génératif.
Le modèle Q&A pointe directement vers la portion de texte qui répond à la question.

Avantages attendus :
- Réponses exactes issues de la base FAQ
- Pas d'hallucinations possibles (extraction pure)
- Score de confiance natif du modèle Q&A
- Plus rapide (pas de génération)

Inconvénients attendus :
- Réponses moins fluides / naturelles
- Limité au contenu exact de la FAQ
- Peut échouer si la formulation est trop différente
"""

import os
from dotenv import load_dotenv
import logging
from typing import Dict, Any, List
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

from .base import BaseStrategy, FAQResponse

# Chargement des variables d'environnement
load_dotenv()

# Configuration du logger
logger = logging.getLogger(__name__)

class StrategyCQA(BaseStrategy):
    """
    Stratégie Q&A extractive : recherche sémantique + extraction de réponse.
    
    Workflow :
    1. Encoder la question en embedding
    2. Rechercher les FAQ les plus similaires
    3. Construire un contexte à partir des réponses FAQ
    4. Utiliser un modèle Q&A pour extraire la réponse du contexte
    5. Retourner la réponse extraite avec les sources
    
    Note : Cette stratégie ne nécessite PAS de token HuggingFace car
    le modèle Q&A s'exécute localement.
    """
    
    def initialize(self) -> None:
        """
        Initialise les modèles d'embeddings et le pipeline Q&A.
        
        TODO pour l'étudiant :
        1. Récupérer les configurations depuis les variables d'environnement
        2. Charger le modèle d'embeddings (SentenceTransformer)
        3. Charger le pipeline Q&A (transformers)
        4. Construire l'index des embeddings
        
        Variables d'environnement attendues :
        - EMBEDDING_MODEL : Modèle d'embeddings (défaut: "sentence-transformers/all-MiniLM-L6-v2")
        - QA_MODEL : Modèle Q&A (défaut: "deepset/roberta-base-squad2")
        - TOP_K_RESULTS : Nombre de FAQ à récupérer (défaut: 3)
        - CONFIDENCE_THRESHOLD : Seuil de similarité minimal (défaut: 0.3)
        
        Note : Le modèle Q&A s'exécute en local, pas besoin de token API.
        """
        # TODO: Récupérer la configuration
        # self.embedding_model_name = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
        # self.qa_model_name = os.getenv("QA_MODEL", "deepset/roberta-base-squad2")
        # self.top_k = int(os.getenv("TOP_K_RESULTS", 3))
        # self.confidence_threshold = float(os.getenv("CONFIDENCE_THRESHOLD", 0.3))
        
        # TODO: Charger le modèle d'embeddings
        # logger.info(f"Chargement du modèle d'embeddings: {self.embedding_model_name}")
        # self.embedding_model = SentenceTransformer(self.embedding_model_name)
        
        # TODO: Charger le pipeline Q&A
        # Le pipeline "question-answering" extrait des réponses d'un contexte
        # logger.info(f"Chargement du pipeline Q&A: {self.qa_model_name}")
        # self.qa_pipeline = pipeline("question-answering", model=self.qa_model_name)
        
        # TODO: Construire l'index
        # self._build_index()
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def _build_index(self) -> None:
        """
        Construit l'index des embeddings pour toutes les FAQ.
        
        TODO pour l'étudiant :
        Même logique que pour la stratégie B.
        Encoder question + réponse de chaque FAQ.
        """
        # TODO: Préparer et encoder les textes
        # self.faq_texts = []
        # for faq in self.faq_base:
        #     text = f"{faq['question']} {faq.get('answer', '')}"
        #     self.faq_texts.append(text)
        # 
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
        Même logique que pour la stratégie B.
        
        Args:
            question: La question de l'utilisateur
            
        Returns:
            Liste de dicts avec {"faq": dict_faq, "score": float}
        """
        # TODO: Implémenter (même code que stratégie B)
        # q_emb = self.embedding_model.encode(question, convert_to_tensor=True)
        # similarities = util.cos_sim(q_emb, self.faq_embeddings)[0]
        # top_indices = similarities.argsort(descending=True)[:self.top_k]
        # 
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
        Construit le contexte pour l'extraction Q&A.
        
        TODO pour l'étudiant :
        Pour le Q&A extractif, on utilise principalement les RÉPONSES
        des FAQ comme contexte (c'est là que se trouve l'information à extraire).
        
        Args:
            similar_faqs: Liste de dicts {"faq": ..., "score": ...}
            
        Returns:
            Texte de contexte concaténé
        
        Note : Contrairement à la stratégie B, on concatène simplement
        les réponses car le modèle Q&A va extraire un passage de ce texte.
        """
        # TODO: Concaténer les réponses
        # parts = []
        # for item in similar_faqs:
        #     faq = item["faq"]
        #     parts.append(faq.get("answer", ""))
        # return " ".join(parts)
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def _generate_answer(self, question: str) -> FAQResponse:
        """
        Génère une réponse en combinant recherche et extraction Q&A.
        
        TODO pour l'étudiant :
        1. Rechercher les FAQ similaires
        2. Vérifier si le meilleur score dépasse le seuil
        3. Construire le contexte
        4. Appeler le pipeline Q&A : self.qa_pipeline(question=..., context=...)
        5. Extraire la réponse et le score Q&A
        6. Gérer le cas où le score Q&A est trop faible (fallback)
        7. Calculer un score de confiance combiné
        8. Retourner la FAQResponse
        
        Args:
            question: La question posée par l'utilisateur
            
        Returns:
            FAQResponse avec la réponse extraite
        
        Le pipeline Q&A retourne un dict avec :
        - 'answer': le texte extrait
        - 'score': score de confiance (0-1)
        - 'start': position de début dans le contexte
        - 'end': position de fin
        """
        # TODO: Rechercher les FAQ similaires
        # similar_faqs = self._search_similar(question)
        # best_retrieval_score = similar_faqs[0]["score"] if similar_faqs else 0
        
        # TODO: Vérifier le seuil
        # if best_retrieval_score < self.confidence_threshold:
        #     return FAQResponse(
        #         answer="Je n'ai pas trouvé d'information pertinente.",
        #         confidence=best_retrieval_score,
        #         strategy="qa_extractive",
        #         sources=[]
        #     )
        
        # TODO: Construire le contexte et extraire
        # context = self._build_context(similar_faqs)
        # qa_result = self.qa_pipeline(question=question, context=context)
        # answer_text = qa_result.get("answer", "").strip()
        # qa_score = qa_result.get("score", 0.0)
        
        # TODO: Fallback si la réponse est vide ou le score trop faible
        # Si le modèle Q&A n'arrive pas à extraire, on peut retourner
        # directement la réponse de la meilleure FAQ
        # if not answer_text or qa_score < 0.01:
        #     best_faq = similar_faqs[0]["faq"]
        #     answer_text = best_faq.get("answer", "Information non disponible.")
        #     qa_score = best_retrieval_score * 0.5  # Score réduit
        
        # TODO: Préparer les sources
        # sources = [
        #     {
        #         "id": item["faq"].get("id"),
        #         "question": item["faq"]["question"],
        #         "score": round(item["score"], 3)
        #     }
        #     for item in similar_faqs
        # ]
        
        # TODO: Calculer la confiance combinée (retrieval + extraction)
        # combined_confidence = (best_retrieval_score + qa_score) / 2
        
        # TODO: Retourner la réponse
        # return FAQResponse(
        #     answer=answer_text,
        #     confidence=round(combined_confidence, 3),
        #     strategy="qa_extractive",
        #     sources=sources,
        #     metadata={
        #         "qa_score": round(qa_score, 3),
        #         "retrieval_score": round(best_retrieval_score, 3)
        #     }
        # )
        
        raise NotImplementedError("À implémenter par l'étudiant")


# Alias pour la compatibilité
StrategyC = StrategyCQA


# Point d'entrée pour les tests manuels
if __name__ == "__main__":
    print("Stratégie C (Q&A Extractif) - À implémenter")