"""
Client LLM pour l'API HuggingFace Inference.

Ce module fournit une interface simplifiée pour interagir avec les LLM
disponibles via l'API HuggingFace Inference.

IMPORTANT : Les modèles comme Mistral utilisent l'API "chat" (conversational)
et non "text-generation". Ce module utilise chat_completion().
"""

import os
import logging
from typing import Optional, List, Dict
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class LLMClient:
    """
    Client pour interagir avec les LLM via HuggingFace Inference API.
    
    Utilise l'API chat_completion pour les modèles de type conversationnel
    (Mistral, Zephyr, etc.).
    
    Attributes:
        model_name: Identifiant du modèle HuggingFace
        client: Instance de InferenceClient
        timeout: Timeout en secondes
    
    Example:
        >>> client = LLMClient()
        >>> response = client.generate("Bonjour, comment ça va ?")
        >>> print(response)
    """
    
    # Modèles recommandés (gratuits via l'API Inference)
    RECOMMENDED_MODELS = [
        "mistralai/Mistral-7B-Instruct-v0.2",  # Recommandé - bon compromis
        "HuggingFaceH4/zephyr-7b-beta",         # Alternative
        "microsoft/Phi-3-mini-4k-instruct",     # Plus léger
    ]
    
    def __init__(
        self,
        model_name: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout: int = 60
    ):
        """
        Initialise le client LLM.
        
        Args:
            model_name: Identifiant du modèle (défaut: depuis .env ou Mistral-7B-v0.2)
            api_token: Token HuggingFace (défaut: depuis .env)
            timeout: Timeout en secondes pour les requêtes
            
        TODO pour l'étudiant :
        1. Récupérer le nom du modèle (paramètre > env > défaut)
        2. Récupérer le token API
        3. Vérifier que le token est présent
        4. Créer l'instance InferenceClient
        
        Raises:
            ValueError: Si le token API n'est pas défini
        """
        # TODO: Récupérer le modèle
        # self.model_name = model_name or os.getenv(
        #     "LLM_MODEL", 
        #     self.RECOMMENDED_MODELS[0]
        # )
        
        # TODO: Récupérer le token
        # self.api_token = api_token or os.getenv("HF_API_TOKEN")
        # if not self.api_token:
        #     raise ValueError(
        #         "HF_API_TOKEN non défini. "
        #         "Configurez-le dans .env ou passez-le en paramètre."
        #     )
        
        # TODO: Créer le client
        # self.timeout = timeout
        # self.client = InferenceClient(
        #     token=self.api_token,
        #     timeout=self.timeout
        # )
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def generate(
        self,
        prompt: str,
        max_tokens: int = 500,
        temperature: float = 0.7,
        system_prompt: Optional[str] = None
    ) -> str:
        """
        Génère une réponse en utilisant l'API chat.
        
        Args:
            prompt: Le prompt utilisateur à envoyer
            max_tokens: Nombre maximum de tokens à générer
            temperature: Contrôle la créativité (0=déterministe, 1=créatif)
            system_prompt: Prompt système optionnel pour le contexte
            
        Returns:
            La réponse générée par le modèle
            
        TODO pour l'étudiant :
        1. Construire la liste des messages
        2. Ajouter le system prompt si fourni
        3. Ajouter le message utilisateur
        4. Appeler self.client.chat_completion()
        5. Extraire et retourner le contenu de la réponse
        
        Exemple de structure des messages :
            messages = [
                {"role": "system", "content": "Tu es un assistant..."},
                {"role": "user", "content": "Ma question"}
            ]
        
        Exemple d'appel chat_completion :
            response = self.client.chat_completion(
                model=self.model_name,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            content = response.choices[0].message.content
        """
        # TODO: Construire les messages
        # messages: List[Dict[str, str]] = []
        # 
        # if system_prompt:
        #     messages.append({"role": "system", "content": system_prompt})
        # 
        # messages.append({"role": "user", "content": prompt})
        
        # TODO: Appeler l'API
        # response = self.client.chat_completion(
        #     model=self.model_name,
        #     messages=messages,
        #     max_tokens=max_tokens,
        #     temperature=temperature
        # )
        
        # TODO: Extraire et retourner la réponse
        # return response.choices[0].message.content.strip()
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def generate_with_context(
        self,
        question: str,
        context: str,
        max_tokens: int = 500
    ) -> str:
        """
        Génère une réponse basée sur un contexte fourni (pour RAG).
        
        Args:
            question: La question de l'utilisateur
            context: Le contexte récupéré (FAQ pertinentes)
            max_tokens: Nombre maximum de tokens
            
        Returns:
            La réponse générée
            
        TODO pour l'étudiant :
        1. Définir un system_prompt adapté au RAG
        2. Construire le prompt avec le contexte
        3. Appeler self.generate()
        """
        # TODO: Implémenter
        # system_prompt = """Tu es un assistant FAQ pour une collectivité territoriale.
        # Base tes réponses UNIQUEMENT sur le contexte fourni.
        # Si le contexte ne permet pas de répondre, dis-le clairement."""
        # 
        # prompt = f"""Contexte:
        # {context}
        # 
        # Question: {question}
        # 
        # Réponds de manière claire et concise."""
        # 
        # return self.generate(
        #     prompt=prompt,
        #     max_tokens=max_tokens,
        #     temperature=0.3,
        #     system_prompt=system_prompt
        # )
        
        raise NotImplementedError("À implémenter par l'étudiant")
    
    def is_available(self) -> bool:
        """
        Vérifie si le client est opérationnel.
        
        Returns:
            True si le modèle répond correctement
        """
        try:
            self.generate("Test", max_tokens=5)
            return True
        except Exception:
            return False


# Fonction utilitaire
def get_llm_client() -> LLMClient:
    """Retourne une instance configurée du client LLM."""
    return LLMClient()


# Test rapide si exécuté directement
if __name__ == "__main__":
    print("Test du client LLM")
    print("-" * 40)
    
    # TODO: Décommenter une fois implémenté
    # try:
    #     client = LLMClient()
    #     print(f"Modèle: {client.model_name}")
    #     
    #     response = client.generate(
    #         "Quel est le rôle d'une mairie ? Réponds en une phrase.",
    #         max_tokens=100
    #     )
    #     print(f"Réponse: {response}")
    # except Exception as e:
    #     print(f"Erreur: {e}")
    
    print("Client LLM - À implémenter")