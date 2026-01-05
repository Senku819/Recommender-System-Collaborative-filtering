# Recommender-System-Collaborative-filtering

Mini-projet 14 — Système de recommandation (Collaborative Filtering)

Ce projet implémente un système de recommandation User-Based Collaborative Filtering : on recommande des films à un utilisateur cible en trouvant des utilisateurs similaires (similarité cosinus) et en agrégeant leurs notes pour proposer des suggestions.

---

## Contenu

- `Recommendation_System.py` — script principal qui charge les données, calcule les similarités entre utilisateurs et génère des recommandations.
- `ml-latest-small/` — dossier contenant les fichiers de données (MovieLens small) :
  - `ratings.csv`
  - `movies.csv`

Exemple d'arborescence :
```
Collaborative-Filtering-Python/
├── Recommendation_System.py
└── ml-latest-small/
    ├── ratings.csv
    └── movies.csv
```

---

## Prérequis

- Python 3.10+ (testé également sur Python 3.13)
- Bibliothèques Python :
  - pandas
  - numpy

Il est recommandé d'utiliser un environnement virtuel (venv, conda, etc.).

Installation rapide :
```bash
# créer et activer un environnement virtuel (optionnel mais recommandé)
python -m venv .venv
# sous macOS / Linux
source .venv/bin/activate
# sous Windows (PowerShell)
.venv\Scripts\Activate.ps1

# installer les dépendances
pip install pandas numpy
```

Si vous voulez, je peux préparer un fichier `requirements.txt` contenant les dépendances.

---

## Données (MovieLens)

Les fichiers `ratings.csv` et `movies.csv` proviennent du jeu de données MovieLens (version "ml-latest-small"). Vous pouvez le télécharger depuis la page officielle : [MovieLens datasets](https://grouplens.org/datasets/movielens/).

Placez `ratings.csv` et `movies.csv` dans le dossier `ml-latest-small/` à la racine du projet.

---

## Exécution

Ouvrir un terminal dans le dossier du projet puis lancer :
```bash
python Recommendation_System.py
```

Arguments ou configuration
- Si votre script accepte des arguments (chemin vers les fichiers, identifiant d'utilisateur, nombre de recommendations, etc.), précisez-les dans le script ou passez-les en ligne de commande selon l'implémentation actuelle.
- Par défaut, le script suppose que les fichiers sont dans `ml-latest-small/ratings.csv` et `ml-latest-small/movies.csv`. Modifiez les chemins dans le script si nécessaire.

---

## Exemple de sortie attendue

Le script devrait afficher une liste de films recommandés pour l'utilisateur cible, par exemple :
```
Recommendations for user 123:
1. The Shawshank Redemption (1994) — predicted rating: 4.8
2. The Godfather (1972) — predicted rating: 4.7
3. ...
```

(Format exact dépend de l'implémentation dans `Recommendation_System.py`.)

---

## Bonnes pratiques & améliorations possibles

- Normaliser les notes par utilisateur (centrage) avant calcul de similarité.
- Tester plusieurs mesures de similarité (cosinus, corrélation de Pearson).
- Ajouter filtrage ou un seuil pour éviter recommandations basées sur très peu de votes.
- Implémenter une version Item-Based Collaborative Filtering pour comparaison.
- Ajouter des tests unitaires et un notebook d'exploration (facultatif).

---

## Licence & Auteurs

- Auteur : Senku819
- Licence : à préciser (MIT, GPL, etc.) — ajoutez un fichier `LICENSE` si nécessaire.

---

## Contact

Pour toute question ou demande d'amélioration, ouvrez une issue sur le dépôt GitHub ou contactez l'auteur directement.
