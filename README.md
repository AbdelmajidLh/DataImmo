# Projet DataImmo - Analyse de Transactions Immobilières en France

Ce projet GitHub vise à fournir un exemple concret d'analyse de transactions immobilières en France en utilisant des requêtes SQL. L'objectif est de démontrer comment créer et utiliser une base de données SQL pour répondre à des questions pertinentes dans le domaine de l'immobilier.

## Contenu du Projet

1. **Création de la Base de Données et des Tables**: Ce dossier contient les instructions SQL pour créer la base de données "dataimmo" ainsi que les tables nécessaires (T_COMMUNE, T_LOCAL, T_BIEN).

2. **Données**: Ce dossier contient les fichiers CSV (`commune.csv`, `local.csv` et `bien.csv`) contenant des données de transactions immobilières en France.

3. **Scripts SQL**: Ce dossier contient des exemples de requêtes SQL pour analyser les données. Le fichier `queries.sql` comprend des requêtes illustratives pour répondre à des questions courantes.

4. **Code Python**: Ce dossier contient un script Python (`dataimmo.py`) qui automatise le processus de création de la base de données, l'importation des données depuis les fichiers CSV, et la génération d'un script SQL avec des requêtes pertinentes.

## Utilisation

1. **Création de la Base de Données**: Exécutez les instructions SQL du dossier "Création de la Base de Données et des Tables" pour créer la base de données et les tables requises.

2. **Importation des Données**: Assurez-vous que les fichiers CSV (`commune.csv`, `local.csv` et `bien.csv`) sont dans le dossier "Données". Exécutez le script Python `dataimmo.py` pour importer les données dans la base de données.

3. **Analyse des Données**: Utilisez les exemples de requêtes SQL du dossier "Scripts SQL" pour effectuer différentes analyses sur les transactions immobilières.

4. **Génération de Scripts SQL**: Le script Python génère automatiquement un fichier `queries.sql` contenant des requêtes SQL prêtes à l'emploi pour répondre à diverses questions.

## Contributions

Toutes les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, ajouter des fonctionnalités ou corriger des erreurs, n'hésitez pas à soumettre des pull requests.

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.

N'hésitez pas à explorer et à utiliser ce projet GitHub pour apprendre et mettre en pratique l'analyse de données immobilières à l'aide de SQL.