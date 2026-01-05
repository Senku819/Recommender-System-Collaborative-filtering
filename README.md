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


Installation rapide :
```bash

# installer les dépendances
pip install pandas numpy
```



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

 configuration

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


