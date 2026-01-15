"""
Client LLM pour l'API HuggingFace Inference.
SOLUTION FORMATEUR - Version corrigée pour Mistral chat API.

Ce module gère les appels à l'API HuggingFace pour la génération de texte
avec les modèles de type "chat/conversational".
"""

import os
import logging
from typing import Optional, List, Dict, Any
from huggingface_hub import InferenceClient

logger = logging.getLogger(__name__)


class LLMClient:
    """
    Client pour interagir avec les LLM via HuggingFace Inference API.
    
    Supporte les modèles de type "conversational" (chat) comme Mistral.
    """
    
    def __init__(
        self, 
        model_name: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout: int = 60
    ):
        """
        Initialise le client LLM.
        
        Args:
            model_name: Nom du modèle HuggingFace (défaut: depuis .env)
            api_token: Token API HuggingFace (défaut: depuis .env)
            timeout: Timeout en secondes pour les requêtes
        """
        self.model_name = model_name or os.getenv(
            "LLM_MODEL", 
            "mistralai/Mistral-7B-Instruct-v0.2"
        )
        self.api_token = api_token or os.getenv("HF_API_TOKEN")
        self.timeout = timeout
        
        if not self.api_token:
            raise ValueError(
                "HF_API_TOKEN non défini. "
                "Configurez-le dans .env ou passez-le en paramètre."
            )
        
        # Initialiser le client
        self.client = InferenceClient(
            token=self.api_token,
            timeout=self.timeout
        )
        
        logger.info(f"LLMClient initialisé avec le modèle: {self.model_name}")
    
    def generate(
        self, 
        prompt: str, 
        max_tokens: int = 500,
        temperature: float = 0.7,
        system_prompt: Optional[str] = None
    ) -> str:
        """
        Génère une réponse en utilisant l'API chat (conversational).
        
        Args:
            prompt: Le prompt utilisateur à envoyer au modèle
            max_tokens: Nombre maximum de tokens à générer
            temperature: Contrôle la créativité (0=déterministe, 1=créatif)
            system_prompt: Prompt système optionnel pour le contexte
            
        Returns:
            La réponse générée par le modèle
        """
        try:
            # Construire les messages
            messages: List[Dict[str, str]] = []
            
            # Ajouter le system prompt si fourni
            if system_prompt:
                messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            
            # Ajouter le message utilisateur
            messages.append({
                "role": "user",
                "content": prompt
            })
            
            logger.debug(f"Envoi de {len(messages)} message(s) au modèle {self.model_name}")
            
            # Appeler l'API chat
            response = self.client.chat_completion(
                model=self.model_name,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            # Extraire le contenu de la réponse
            content = response.choices[0].message.content
            
            logger.debug(f"Réponse reçue: {len(content)} caractères")
            return content.strip()
            
        except Exception as e:
            logger.error(f"Erreur lors de la génération LLM: {e}")
            raise
    
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
        """
        system_prompt = """Tu es un assistant FAQ pour une collectivité territoriale française.
Tu réponds aux questions des citoyens de manière claire, précise et professionnelle.
Base tes réponses UNIQUEMENT sur le contexte fourni.
Si le contexte ne permet pas de répondre, dis-le clairement."""

        prompt = f"""Contexte (informations de la FAQ):
{context}

Question du citoyen: {question}

Réponds de manière claire et concise en te basant sur le contexte ci-dessus."""

        return self.generate(
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.3,  # Plus déterministe pour les FAQ
            system_prompt=system_prompt
        )
    
    def generate_faq_response(
        self,
        question: str,
        max_tokens: int = 500
    ) -> str:
        """
        Génère une réponse FAQ sans contexte (stratégie A - LLM seul).
        
        Args:
            question: La question de l'utilisateur
            max_tokens: Nombre maximum de tokens
            
        Returns:
            La réponse générée
        """
        system_prompt = """Tu es un assistant FAQ pour une collectivité territoriale française (mairie, communauté de communes).
Tu réponds aux questions des citoyens sur les démarches administratives.
Si tu n'es pas sûr de la réponse ou si la question sort de ton domaine de compétence, dis-le clairement.
Réponds en français de manière professionnelle et concise."""

        return self.generate(
            prompt=question,
            max_tokens=max_tokens,
            temperature=0.5,
            system_prompt=system_prompt
        )


# Fonction utilitaire pour usage simple
def get_llm_client() -> LLMClient:
    """Retourne une instance configurée du client LLM."""
    return LLMClient()


# Test rapide si exécuté directement
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    
    logging.basicConfig(level=logging.INFO)
    
    print("Test du client LLM corrigé...")
    
    try:
        client = LLMClient()
        
        # Test simple
        response = client.generate(
            prompt="Quel est le rôle d'une mairie ? Réponds en une phrase.",
            max_tokens=100
        )
        print(f"\n✓ Test réussi!")
        print(f"Réponse: {response}")
        
    except Exception as e:
        print(f"\n✗ Erreur: {e}")