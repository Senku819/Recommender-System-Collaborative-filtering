# Recommender-System-Collaborative-filtering
# Mini-Projet 14 — Système de recommandation (Collaborative Filtering)

Ce projet implémente un système de recommandation **User-Based Collaborative Filtering** : on recommande des films à un utilisateur cible en trouvant des utilisateurs similaires (cosine similarity) et en utilisant leurs notes pour prédire les films non vus. [file:1]

## Prérequis

- Python 3.10+ (testé aussi sur Python 3.13) [file:2]
- Bibliothèques :
  - pandas
  - numpy

Installation :
```bash
pip install pandas numpy
Le placement des les fichiers comme suit :

Coolaborative Filtering Python/
├── Recommendation_System.py
└── ml-latest-small/
    ├── ratings.csv
    └── movies.csv
##Exécution:
Ouvrir un terminal dans le dossier du projet puis exécuter : [file:2]

bash
python Recommendation_System.py
