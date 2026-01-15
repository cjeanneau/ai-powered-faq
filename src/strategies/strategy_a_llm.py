"""
Stratégie A : LLM seul

Cette stratégie utilise uniquement un LLM avec un prompt système contextualisé
pour répondre aux questions. Le LLM s'appuie sur ses connaissances internes
et le contexte fourni dans le prompt.

Avantages attendus :
- Simplicité d'implémentation
- Pas de pré-traitement des données
- Réponses fluides et naturelles

Inconvénients attendus :
- Risque d'hallucinations
- Pas d'accès direct à la base FAQ
- Réponses potentiellement génériques
"""

import os
from dotenv import load_dotenv
import logging
from typing import Dict, Any, List
from huggingface_hub import InferenceClient

from .base import BaseStrategy, FAQResponse

# Chargement des variables d'environnement
load_dotenv()

# Configuration du logger
logger = logging.getLogger(__name__)

class StrategyALLM(BaseStrategy):
    """
    Stratégie utilisant uniquement un LLM pour répondre aux questions.
    
    Le LLM reçoit un prompt système décrivant le contexte (collectivité territoriale)
    et génère une réponse basée sur ses connaissances générales.
    
    Workflow :
    1. Recevoir la question
    2. Construire le prompt avec le contexte
    3. Appeler le LLM via l'API chat_completion
    4. Analyser la réponse pour estimer la confiance
    5. Retourner la FAQResponse
    """
    
    def initialize(self) -> None:
        """
        Initialise le client LLM HuggingFace.
        
        TODO pour l'étudiant :
        1. Récupérer le nom du modèle depuis les variables d'environnement
        2. Récupérer le token API HuggingFace
        3. Créer une instance de InferenceClient
        4. Définir le prompt système pour contextualiser le LLM
        
        Variables d'environnement attendues :
        - LLM_MODEL : Nom du modèle (défaut: "mistralai/Mistral-7B-Instruct-v0.2")
        - HF_API_TOKEN : Token d'authentification HuggingFace
        
        Raises:
            ValueError: Si HF_API_TOKEN n'est pas défini
        """
        # TODO: Récupérer la configuration
        # self.model_name = os.getenv("LLM_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")
        # self.api_token = os.getenv("HF_API_TOKEN")
        #
        # if not self.api_token:
        #     raise ValueError("HF_API_TOKEN requis pour la stratégie LLM")
        
        # TODO: Créer le client
        # self.client = InferenceClient(token=self.api_token, timeout=60)
        
        # TODO: Définir le prompt système
        # Ce prompt contextualise le LLM pour répondre aux questions de la collectivité
        # self.system_prompt = """Tu es un assistant FAQ pour une collectivité territoriale française.
        # ...
        # """
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def _generate_answer(self, question: str) -> FAQResponse:
        """
        Génère une réponse en utilisant uniquement le LLM.
        
        TODO pour l'étudiant :
        1. Construire les messages pour l'API chat (system + user)
        2. Appeler self.client.chat_completion()
        3. Extraire le texte de la réponse
        4. Détecter si le LLM exprime une incertitude
        5. Calculer un score de confiance
        6. Retourner une FAQResponse
        
        Args:
            question: La question posée par l'utilisateur
            
        Returns:
            FAQResponse avec la réponse générée
        
        Exemple d'appel chat_completion :
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": question}
            ]
            response = self.client.chat_completion(
                model=self.model_name,
                messages=messages,
                max_tokens=500,
                temperature=0.5
            )
            answer_text = response.choices[0].message.content
        """
        # TODO: Construire les messages
        # messages = [
        #     {"role": "system", "content": self.system_prompt},
        #     {"role": "user", "content": question}
        # ]
        
        # TODO: Appeler le LLM
        # response = self.client.chat_completion(
        #     model=self.model_name,
        #     messages=messages,
        #     max_tokens=500,
        #     temperature=0.5
        # )
        # answer_text = response.choices[0].message.content.strip()
        
        # TODO: Détecter l'incertitude et calculer la confiance
        # Indices : chercher des phrases comme "je ne suis pas sûr", 
        # "cette question ne concerne pas", etc.
        # confidence = self._estimate_confidence(answer_text)
        
        # TODO: Retourner la réponse
        # return FAQResponse(
        #     answer=answer_text,
        #     confidence=confidence,
        #     strategy="llm_only",
        #     sources=[],
        #     metadata={"model": self.model_name}
        # )
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def _estimate_confidence(self, response: str) -> float:
        """
        Estime un score de confiance basé sur la réponse du LLM.
        
        TODO pour l'étudiant :
        Implémenter une heuristique simple pour estimer la confiance.
        
        Suggestions :
        - Chercher des marqueurs d'incertitude ("je ne suis pas sûr", "peut-être")
        - Chercher des aveux d'ignorance ("hors de mon domaine", "je ne peux pas")
        - Vérifier que la réponse n'est pas trop courte
        
        Args:
            response: La réponse générée par le LLM
            
        Returns:
            Score entre 0.0 et 1.0
        """
        # TODO: Implémenter l'estimation de confiance
        #
        # Exemple d'heuristique :
        # ignorance_indicators = [
        #     "je ne suis pas en mesure",
        #     "je ne peux pas répondre",
        #     "hors de mon domaine",
        # ]
        # 
        # is_uncertain = any(ind in response.lower() for ind in ignorance_indicators)
        # return 0.5 if is_uncertain else 0.7
        
        raise NotImplementedError("À implémenter par l'étudiant")


# Alias pour la compatibilité avec les imports existants
StrategyA = StrategyALLM


# Point d'entrée pour les tests manuels
if __name__ == "__main__":
    import json
    from dotenv import load_dotenv
    load_dotenv()
    
    print("Test de la Stratégie A (LLM seul)")
    print("-" * 40)
    
    # Charger la base FAQ
    # with open("data/faq_base.json", "r", encoding="utf-8") as f:
    #     faq_data = json.load(f).get("faq", [])
    # 
    # strategy = StrategyALLM(faq_base=faq_data)
    # 
    # question = "Comment obtenir un acte de naissance ?"
    # response = strategy.answer(question)
    # 
    # print(f"Question : {question}")
    # print(f"Réponse : {response.answer}")
    # print(f"Confiance : {response.confidence}")
    
    print("Stratégie A - À implémenter")