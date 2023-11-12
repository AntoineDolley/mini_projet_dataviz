# Dashboard des Startups aux États-Unis - Analyse des Données

## Introduction
Ce projet présente un dashboard interactif qui fournit une analyse approfondie des startups aux États-Unis. Il permet aux utilisateurs d'explorer les données relatives à la localisation, aux relations, au financement et au statut des startups.

## Utilisation de Git
Ce projet a été développé en utilisant Git pour le contrôle de version. Les mises à jour régulières ont été poussées sur le dépôt.

## Données Utilisées
Les données pour ce projet comprennent les informations sur les startups aux États-Unis, y compris leur emplacement, le nombre de relations, les fonds reçus, et leur statut final ('acquired' ou 'closed'). Ses données sont issues du [data sprint #5](https://aiplanet.com/challenges/32/data-sprint-5-startup-success-prediction-32/overview/about) organisé par aiplanet.
Pour les cartes nous avons utilisé des données geographiques des etats des Etats-Unis fournit par [Eric Celeste](https://eric.clst.org/tech/usgeojson/).

## User Guide
Pour configurer le projet localement :
1. Clonez le dépôt avec `git clone https://github.com/AntoineDolley/mini_projet_dataviz.git`.
2. Allez dans le dossier installé.
3. Installez les dépendances requises avec `pip install -r requirements.txt`.
4. Lancez l'application depuis votre terminal avec `python main.py`.
5. Allez a l'url `http://127.0.0.1:8050/`
6. Utilisez le menu déroulant pour sélectionner les différentes cartes et graphiques visualisez le nombre de startups, les relations moyennes et les taux de réussite par région.
7. Explorez les cartes pour voir l'impact de l'emplacement sur les startups 
8. Explorez les histogrammes pour comprendre l'impact des relations et des fonds sur le succès des startups.

## Developper Guide

Ce guide fournit un aperçu de l'architecture du code pour aider les développeurs à comprendre, modifier ou étendre la base de code.

### Aperçu

Le projet est structuré en plusieurs modules Python, chacun ayant un rôle spécifique :

- `main.py` : C'est le point d'entrée de l'application. Il orchestre l'initialisation de l'application et fait le lien avec les autres modules.

- `dashboard.py` : Définit la fonction `create_dashboard` qui assemble l'application Dash, intégrant des cartes et des graphiques générés à partir des données.

- `data.py` : Contient la fonction `open_and_process_data` pour lire et prétraiter les données, convertissant les données brutes en un DataFrame pandas structuré.

- `geodata.py` : Fournit la fonction `get_geodata` qui récupère les données géographiques dans un GeoDataFrame GeoPandas, pour utilisation dans les cartes et `update_geojson` pour ajouter des données au geojson.

- `graphs.py` : Inclut des fonctions comme `histofunding` qui créent des représentations visuelles des données, telles que des histogrammes, en utilisant la bibliothèque Plotly.

- `map.py` : Contient des fonctions telles que `create_3maps_dict` pour configurer les visualisations de cartes, utilisant la bibliothèque Folium pour le rendu des cartes.

### Interactions entre les Modules

- `main.py` sert de chef d'orchestre, faisant appel à `dashboard.py` pour initialiser l'application du tableau de bord.
- `dashboard.py` dépend à son tour de `map.py` et `graphs.py` pour générer les composants visuels du tableau de bord.
- `data.py` et `geodata.py` sont utilisés pour fournir respectivement les données traitées et les données géographiques aux composants visuels.

### Étendre le Code

Pour étendre la fonctionnalité ou ajouter de nouvelles caractéristiques au projet :

1. Identifiez le module où l'ajout s'intègre le mieux ou envisagez de créer un nouveau module si la fonctionnalité est suffisamment distincte.
2. Suivez les modèles existants pour les fonctions de traitement des données et de visualisation.
3. Assurez-vous que toutes les nouvelles sources de données sont intégrées dans le flux de prétraitement de `data.py`.
4. Si de nouveaux composants visuels sont ajoutés, mettez à jour `dashboard.py` pour les inclure dans la mise en page de l'application Dash.
5. Mettez à jour `main.py` s'il y a des changements significatifs dans l'initialisation de l'application ou son déroulement.

Pour des instructions plus détaillées sur l'utilisation et la personnalisation des modules individuels, référez-vous aux commentaires en ligne et aux docstrings dans chaque fichier.

---

## Visualisations

### Chloropleth Map des États-Unis
- **Nombre de startups par région** : La majorité des startups sont situées en Californie, New York, Massachusetts, Washington et Texas, avec une concentration significative en Californie.
- **Relations moyennes par région** : Les moyennes régionales des relations sont généralement élevées, avec des valeurs comme 8,7 à New York et 8,4 en Californie. L'Indiana présente une moyenne de 19, ce qui pourrait être dû à un échantillon de taille réduite.
- **Proportion de réussite des startups par région** : Un score de 0,7 est considéré comme un bon taux de réussite, avec des scores de 0,7 à New York et de 0,68 en Californie. L'Oregon se distingue avec un taux de réussite de 0,857.

### Graphique en Barres - Proportion de Réussite par Secteur
- **Secteurs variés** : La plupart des secteurs ont un taux de réussite autour de 0,60 à 0,65, à l'exception de l'e-commerce qui est plus bas à 0,44 et de l'entreprise qui est plus élevé à 0,77.

### Histogrammes
- **Succès basé sur les relations** : Il y a une corrélation positive entre le nombre de relations et la proportion de réussite. Les entreprises avec plus de deux relations sont plus fréquentes, tandis que celles avec plus de 30 sont rares.
- **Succès basé sur les fonds** : Une tendance similaire est observée avec les fonds; plus le financement est élevé, plus le taux de réussite augmente. La majorité des entreprises ont des fonds entre 0 et 16 millions, avec quelques-unes recevant plus de 80 millions.

## Conclusions Principales
- **Localisation et Succès** : La distribution géographique des startups influence leur succès, avec des pôles majeurs de l'innovation aux États-Unis notamment la Californie.
- **Importance des Relations** : Les relations sont un facteur clé du succès des startups, comme le montre la corrélation avec des taux de réussite élevés.
- **Financement** : Le financement est également crucial, les données indiquant une plus grande probabilité de succès pour les startups bien financées.
- **Hubs** : La Californie et New York sont les principaux hubs de startups.
- **Relations** : Une corrélation positive a été observée entre le nombre de relations d'une startup et son taux de réussite.

## Statut des Startups
- **'Acquired' vs 'Closed'** : Le statut final des startups est utilisé comme indicateur de succès, avec 'acquired' indiquant une acquisition (et donc un succès) et 'closed' indiquant une fermeture de l'entreprise.

---

Pour une exploration interactive des données, veuillez lancer le dashboard Python accompagnant ce fichier.

## 
