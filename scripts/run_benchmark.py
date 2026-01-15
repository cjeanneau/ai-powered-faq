"""
Script de benchmark des stratégies FAQ.

Ce script exécute les 3 stratégies sur le golden set et enregistre les résultats
pour une évaluation comparative.

Auteur: [Votre nom]
Date: [Date]
"""

import json
import time
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import sys

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class BenchmarkResult:
    """Résultat d'une exécution de stratégie sur une question."""
    question_id: str
    question: str
    question_type: str
    strategy: str
    answer: str
    latency_ms: float
    confidence: Optional[float]
    error: Optional[str]
    timestamp: str


class BenchmarkRunner:
    """
    Exécute le benchmark des stratégies sur le golden set.
    
    Cette classe orchestre l'exécution des 3 stratégies sur chaque question
    du jeu de test et collecte les métriques de performance.
    """
    
    def __init__(self, golden_set_path: str, faq_base_path: str, output_dir: str):
        """
        Initialise le runner de benchmark.
        
        Args:
            golden_set_path: Chemin vers le fichier golden_set.json
            faq_base_path: Chemin vers le fichier faq_base.json
            output_dir: Répertoire de sortie pour les résultats
        """
        self.golden_set_path = Path(golden_set_path)
        self.faq_base_path = Path(faq_base_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Charger les données
        self.golden_set = self._load_golden_set()
        self.faq_base = self._load_faq_base()
        
        logger.info(f"Golden set chargé: {len(self.golden_set)} questions")
        logger.info(f"Base FAQ chargée: {len(self.faq_base)} entrées")
        
        # Initialiser les stratégies
        self.strategies = self._init_strategies()
        
        # Résultats
        self.results: List[BenchmarkResult] = []
    
    def _load_golden_set(self) -> List[Dict[str, Any]]:
        """
        Charge le golden set depuis le fichier JSON.
        
        Returns:
            Liste des questions du golden set
            
        TODO:
            1. Ouvrir le fichier golden_set_path
            2. Parser le JSON
            3. Extraire la liste des questions (clé "golden_set")
            4. Retourner la liste
            
        Hint:
            - Utilisez json.load() pour charger le fichier
            - Gérez les erreurs potentielles (fichier non trouvé, JSON invalide)
        """
        # TODO: Implémenter le chargement du golden set
        # try:
        #     with open(self.golden_set_path, 'r', encoding='utf-8') as f:
        #         data = json.load(f)
        #     return data.get("golden_set", [])
        # except FileNotFoundError:
        #     logger.error(f"Fichier non trouvé: {self.golden_set_path}")
        #     raise
        # except json.JSONDecodeError as e:
        #     logger.error(f"Erreur de parsing JSON: {e}")
        #     raise
        
        raise NotImplementedError("Implémenter _load_golden_set")
    
    def _load_faq_base(self) -> List[Dict[str, Any]]:
        """
        Charge la base FAQ depuis le fichier JSON.
        
        Returns:
            Liste des entrées FAQ
            
        TODO:
            1. Ouvrir le fichier faq_base_path
            2. Parser le JSON
            3. Extraire la liste des FAQ (clé "faq")
            4. Retourner la liste
        """
        # TODO: Implémenter le chargement de la base FAQ
        raise NotImplementedError("Implémenter _load_faq_base")
    
    def _init_strategies(self) -> Dict[str, Any]:
        """
        Initialise les 3 stratégies à benchmarker.
        
        Returns:
            Dictionnaire {nom_stratégie: instance_stratégie}
            
        TODO:
            1. Importer les classes de stratégies depuis src.strategies
            2. Instancier chaque stratégie avec la base FAQ
            3. Gérer les erreurs (stratégie non implémentée)
            4. Retourner le dictionnaire des stratégies disponibles
            
        Imports nécessaires:
            from src.strategies.strategy_a_llm import StrategyALLM
            from src.strategies.strategy_b_rag import StrategyBRAG
            from src.strategies.strategy_c_qa import StrategyCQA
            
        Note:
            Utilisez try/except pour chaque stratégie afin de pouvoir
            exécuter le benchmark même si une stratégie n'est pas implémentée.
        """
        # TODO: Implémenter l'initialisation des stratégies
        #
        # Exemple:
        # strategies = {}
        # 
        # try:
        #     from src.strategies.strategy_a_llm import StrategyALLM
        #     strategies["strategy_a_llm"] = StrategyALLM(faq_base=self.faq_base)
        #     logger.info("  ✓ Stratégie A (LLM) initialisée")
        # except Exception as e:
        #     logger.warning(f"  ✗ Stratégie A (LLM) non disponible: {e}")
        # 
        # ... (même chose pour B et C)
        # 
        # if not strategies:
        #     raise RuntimeError("Aucune stratégie n'a pu être initialisée")
        # 
        # return strategies
        
        raise NotImplementedError("Implémenter _init_strategies")
    
    def run_single_question(
        self, 
        question: Dict[str, Any], 
        strategy_name: str
    ) -> BenchmarkResult:
        """
        Exécute une stratégie sur une question unique.
        
        Args:
            question: Dictionnaire contenant la question du golden set
            strategy_name: Nom de la stratégie à utiliser
            
        Returns:
            BenchmarkResult avec les métriques d'exécution
            
        TODO:
            1. Récupérer la stratégie depuis self.strategies
            2. Mesurer le temps de début (time.perf_counter())
            3. Appeler la méthode answer() de la stratégie
            4. Mesurer le temps de fin
            5. Calculer la latence en millisecondes
            6. Extraire la réponse et la confiance du résultat
            7. Créer et retourner un BenchmarkResult
            
        Gestion d'erreurs:
            - En cas d'exception, capturer l'erreur et la stocker dans le résultat
            - Ne pas faire échouer tout le benchmark pour une erreur isolée
        """
        # TODO: Implémenter l'exécution sur une question
        #
        # strategy = self.strategies.get(strategy_name)
        # 
        # if strategy is None:
        #     return BenchmarkResult(
        #         question_id=question["id"],
        #         question=question["question"],
        #         question_type=question.get("type", "unknown"),
        #         strategy=strategy_name,
        #         answer="",
        #         latency_ms=0,
        #         confidence=None,
        #         error=f"Stratégie {strategy_name} non disponible",
        #         timestamp=datetime.now().isoformat()
        #     )
        # 
        # try:
        #     start_time = time.perf_counter()
        #     response = strategy.answer(question["question"])
        #     end_time = time.perf_counter()
        #     latency_ms = (end_time - start_time) * 1000
        #     
        #     # La réponse est une FAQResponse (dataclass qui se comporte comme un dict)
        #     answer = response.answer if hasattr(response, 'answer') else str(response)
        #     confidence = response.confidence if hasattr(response, 'confidence') else None
        #     
        #     return BenchmarkResult(...)
        # except Exception as e:
        #     ...
        
        raise NotImplementedError("Implémenter run_single_question")
    
    def run_benchmark(self) -> List[BenchmarkResult]:
        """
        Exécute le benchmark complet.
        
        Itère sur toutes les questions du golden set et toutes les stratégies.
        
        Returns:
            Liste de tous les BenchmarkResult
            
        TODO:
            1. Pour chaque question du golden set:
                a. Pour chaque stratégie:
                    - Appeler run_single_question()
                    - Ajouter le résultat à self.results
                    - Logger la progression
            2. Retourner self.results
            
        Logging attendu:
            - Début du benchmark (nombre de questions, stratégies)
            - Progression (toutes les 5 questions par exemple)
            - Fin du benchmark avec statistiques globales
        """
        # TODO: Implémenter le benchmark complet
        raise NotImplementedError("Implémenter run_benchmark")
    
    def save_results(self, filename: Optional[str] = None) -> Path:
        """
        Sauvegarde les résultats au format JSON.
        
        Args:
            filename: Nom du fichier (optionnel, généré automatiquement sinon)
            
        Returns:
            Chemin du fichier créé
            
        TODO:
            1. Générer un nom de fichier avec timestamp si non fourni
            2. Convertir les résultats en dictionnaires (asdict)
            3. Créer la structure JSON avec métadonnées:
               - timestamp
               - nombre de questions
               - stratégies testées
               - résultats
            4. Sauvegarder le fichier JSON
            5. Retourner le chemin du fichier
        """
        # TODO: Implémenter la sauvegarde des résultats
        raise NotImplementedError("Implémenter save_results")
    
    def generate_summary(self) -> Dict[str, Any]:
        """
        Génère un résumé statistique du benchmark.
        
        Returns:
            Dictionnaire avec les statistiques par stratégie:
            - latence moyenne, min, max
            - taux d'erreur
            - nombre de réponses
            
        TODO:
            1. Grouper les résultats par stratégie
            2. Pour chaque stratégie, calculer:
               - latence_moyenne
               - latence_min
               - latence_max
               - taux_erreur (pourcentage de résultats avec error != None)
               - nombre_questions
            3. Retourner le dictionnaire de statistiques
        """
        # TODO: Implémenter le résumé statistique
        raise NotImplementedError("Implémenter generate_summary")
    
    def print_summary(self):
        """Affiche un résumé formaté du benchmark."""
        summary = self.generate_summary()
        
        print("\n" + "="*60)
        print("RÉSUMÉ DU BENCHMARK")
        print("="*60)
        
        for strategy_name, stats in summary.items():
            print(f"\n{strategy_name}:")
            print(f"  Questions: {stats['nombre_questions']}")
            if stats.get('latence_moyenne_ms') is not None:
                print(f"  Latence moyenne: {stats['latence_moyenne_ms']:.0f}ms")
                print(f"  Latence min/max: {stats['latence_min_ms']:.0f}ms / {stats['latence_max_ms']:.0f}ms")
            print(f"  Taux d'erreur: {stats['taux_erreur']:.1f}%")
        
        print("\n" + "="*60)


def main():
    """
    Point d'entrée principal du script de benchmark.
    
    TODO:
        1. Définir les chemins vers les fichiers de données
        2. Vérifier que les fichiers existent
        3. Créer une instance de BenchmarkRunner
        4. Exécuter le benchmark
        5. Sauvegarder les résultats
        6. Afficher le résumé
        
    Chemins attendus (relatifs au projet):
        - data/golden_set.json
        - data/faq_base.json
        - results/ (dossier de sortie)
    """
    # Configuration des chemins
    project_root = Path(__file__).parent.parent
    golden_set_path = project_root / "data" / "golden_set.json"
    faq_base_path = project_root / "data" / "faq_base.json"
    output_dir = project_root / "results"
    
    # Vérifier que les fichiers existent
    if not golden_set_path.exists():
        logger.error(f"Golden set non trouvé: {golden_set_path}")
        sys.exit(1)
    
    if not faq_base_path.exists():
        logger.error(f"Base FAQ non trouvée: {faq_base_path}")
        sys.exit(1)
    
    # TODO: Implémenter le main
    # 1. Créer le runner
    # runner = BenchmarkRunner(
    #     golden_set_path=str(golden_set_path),
    #     faq_base_path=str(faq_base_path),
    #     output_dir=str(output_dir)
    # )
    # 
    # 2. Lancer le benchmark
    # runner.run_benchmark()
    # 
    # 3. Sauvegarder les résultats
    # output_path = runner.save_results()
    # 
    # 4. Afficher le résumé
    # runner.print_summary()
    # 
    # print(f"\nRésultats sauvegardés dans: {output_path}")
    
    logger.info("Benchmark terminé.")


if __name__ == "__main__":
    main()