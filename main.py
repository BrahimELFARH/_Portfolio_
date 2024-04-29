import streamlit as st
from PIL import Image

# Chargement de la feuille de style externe
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


#####################
# Header 
st.write('''
# Brahim EL FARH
##### *Portfolio* 
''')

image = Image.open('image/BE.jpg')
st.image(image, width=150)

st.markdown('## 📰 Mon actualité', unsafe_allow_html=True)
st.info('''
- Actuellement en troisième année de Bachelor Universitaire de Technologie (BUT) en Sciences des Données à l'IUT Paris - Rives de Seine - Université Paris Cité, je suis engagé en tant que Data Analyst en alternance chez Pro BTP Groupe. Mon rôle consiste à contribuer activement à la manipulation et à l'analyse de données, fournissant ainsi des éclairages essentiels pour la prise de décisions au sein de l'entreprise.

- Parallèlement à mon travail, je suis actuellement candidat à plusieurs programmes de Master ainsi qu'à des écoles d'ingénieurs spécialisées dans le domaine de la Science des Données. Mon objectif est de continuer à approfondir mes connaissances et compétences dans ce domaine en poursuivant mes études supérieures.

- De plus, je suis à la recherche d'une nouvelle opportunité d'alternance. Je suis convaincu que cette expérience supplémentaire enrichira encore davantage mon parcours professionnel et me permettra d'appliquer mes connaissances dans un nouvel environnement professionnel stimulant."
''')

# téléchargement du CV
def download_cv():
    with open("CV/CV_BRAHIM_ELFARH.pdf", "rb") as file: 
        cv = file.read()
    st.download_button(
        label="Télécharger mon CV",
        data=cv,
        file_name="CV_BRAHIM_ELFARH.pdf",
        mime="application/pdf",
    )

download_cv()

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="#top">Brahim EL FARH</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#education">🎓  Diplômes et formations</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">🧳 Expériences professionnelles</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projet">📁 Projets réalisés</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">📮 Me contacter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)


#####################
st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown('''
## 🎓 Diplômes et formations
''')
logo_ecole = "image/cite.jpeg"
st.write("🗓️ Depuis septembre 2022")
st.image(logo_ecole, width=200) 
with st.expander(label="BUT Science des données | IUT - Paris Rives de Seine"):
            st.write(

                    """
                    Spécialité : Visualisation et conception d'outils décisionels

                    Compétences techniques acquises :
                    - Exploration approfondie de données
                    - Préparation et nettoyage de données
                    - Développement de tableaux de bord interactifs 
                    - Utilisation d'outils et de frameworks variés 
                    - Manipulation de grands ensembles de données (Big data)
                    - Modélisation prédictive avancée
                    - Programmation orienté objet
                    - Machine Learning

                    Compétances en communication :
                    - Communication efficace des résultats techniques et des insights aux parties prenantes non techniques.
                    - Capacité à présenter des rapports et à donner des présentations orales claires et persuasives.
                    - Compétences en rédaction pour élaborer des rapports techniques, des documentations et des présentations.
                    - Utilisation de langage professionnel et adapté à différents contextes.
                    - Maîtrise de l'anglais professionnel pour la communication écrite et orale dans un contexte professionnel.
                    """
                    )
st.write("🗓️ De septembre 2021 à juin 2022")
st.image(logo_ecole, width=200) 
with st.expander(label="DUT Informatique | IUT - Paris Rives de Seine"):
            st.write(

                    """
                    Compétences techniques acquises :
                    - Programmation avancée
                    - Compréhension des structures de données et algorithmes
                    - Gestion de bases de données grâce au langage SQL
                    - Développement web
                    - Pratiques de développement logiciel
                    """
                    )
st.write("🗓️ Obtenu en 2021")
logo_lycee = "image/lycee.png"
st.image(logo_lycee, width=80) 
with st.expander(label="Baccalauréat économique et social | Lycée René Cassin"):
            st.write(

                    """
                    Spécialité : Mathématique (obtenu avec la mention assez-bien)

                    Compétences acquises :
                    - Analyse économique
                    - Méthodologie de recherche
                    - Compétences mathématiques
                    - Compréhension des sciences sociales
                    - Bonne communication écrite et orale
                    """
                    )

#####################
st.markdown('<div id="work-experience"></div>', unsafe_allow_html=True)
st.markdown('''
## 🧳 Expériences professionnelles
''')
st.write("🗓️ Depuis janvier 2023")
logo_btp = "image/btp.png"
st.image(logo_btp, width=120) 
with st.expander(label="Data Analyst | Pro BTP Groupe"):
            st.write(
            """
            Principales Missions :

            - Contribuer à l’accompagnement de la mise en œuvre de la stratégie commerciale du Groupe

            - Concevoir, assurer le suivi, le support et l'analyse de l’activité, des résultats et des indicateurs de performance sur le périmètre concerné et proposer des actions d'amélioration de concert avec les managers commerciaux

            - Conseiller, assister et accompagner le pilotage des équipes du Réseau, des Vacances, de la gestion, de l'Action sociale Régionale et des métiers transverses

            - Participer à la création et l'optimisation des outils de suivi de pilotage, concevoir des tableaux de bord et en assurer la traçabilité
            
            - Réaliser des études statistiques et de données pour les Directions du Groupe

            - Identifier les besoins du terrain en matière de moyens et ressources humaines, techniques, outils, métiers...

            - Accompagner, déployer, former et assurer un support sur les outils auprès du réseau commercial
            """
        )

#####################
st.markdown('<div id="projet"></div>', unsafe_allow_html=True)
st.markdown('''
## 📁 Projets réalisés
''')
st.write(
                    """
                    Data Analyst - PRO BTP Groupe

                    🗓️ 2023-2024
                    """            
)
logo_btp = "image/btp.png"
with st.expander(label="Elaboration d'un tableau de bord automatisé permettant de suivre l'activité d'une nouvelle assurance santé dédiée aux chats et aux chiens"):
            st.write(
                    
                    """
                    - Éxploration approfondie des données pour obtenir une compréhension approfondie des besoins de l'assurance santé avant de passer à la phase de développement.
                    - Préparation des données à l'aide de SAS pour garantir leur qualité et leur adéquation aux besoins spécifiques du tableau de bord.
                    - Mise en place d'une nouvelle table répondant aux besoins spécifiques de la mission et intégration de cette table dans l'espace de production pour l'alimentation du tableau de bord.
                    - Présentation du tableau de bord aux collaborateurs pour validation avant sa mise en ligne, assurant ainsi sa pertinence et sa fiabilité opérationnelle.
                    - Publication du tableau de bord au réseau pour une utilisation opérationnelle, permettant aux utilisateurs de suivre en temps réel l'activité de l'assurance santé et de prendre des décisions éclairées.
                    - Contribution à l'amélioration continue du tableau de bord en tenant compte des retours des utilisateurs et en apportant des ajustements nécessaires pour répondre aux besoins évolutifs de l'entreprise.
                    """
                    )
with st.expander(label="Création tableau de bord interactif pour challenger les performances commerciales (Spotfire)"):
            st.write(
                    
                    """
                    Contexte : Les pilotes commerciaux lancent des challenges de vente périodiques pour stimuler les performances des équipes commerciales. Les commerciaux s'engagent à relever des défis de performance, avec des récompenses basées sur leur classement. J'ai eu l'opportunité de concevoir un tableau de bord hebdomadaire pour suivre les ventes des commerciaux des trois marché de l'entreprise (Particuliers, Entreprises, Artisans), facilitant ainsi la gestion et la récompense des performances.                    
                    - Programmation des règles du challenge et des calculs dans SAS pour établir les classements et déterminer les récompenses.                   
                    - Le projet représentait un défi stimulant, combinant des aspects techniques de programmation SAS avec des enjeux stratégiques de motivation des équipes commerciales.  
                    - Contribution significative à la réalisation du projet en fournissant un outil efficace aux pilotes commerciaux pour animer et piloter les initiatives de vente, contribuant ainsi à l'amélioration des performances commerciales globales.                  
"""
                    )
st.write(
                    """
                    BUT Science Des données - IUT Paris Rives de Seine

                    🗓️ 2023-2024
                    """            
)
with st.expander(label="Développement d'une application web interactive de comparaison de villes (Streamlit)"):
            st.write(
                    """
                    lien : https://city-fighting-brahim-ben-gilles.streamlit.app/
                    - Conceptualisation et développement d'une interface web interactive nommée "City Fighting".
                    - Utilisation du framework Streamlit et de bibliothèques de visualisation de données pour créer une expérience utilisateur immersive et attrayante, inspirée de l'univers du jeu vidéo Street Fighter.
                    - Collecte et traitement de données provenant de diverses sources telles que les API météorologiques, les bases de données démographiques et les données sur l'emploi.
                    - Intégration de ces données dans l'interface web pour permettre la comparaison de différentes villes sur des aspects variés de la vie urbaine.
                    - Gestion des défis liés à la gestion et à l'intégration de données provenant de sources diverses tout en assurant la cohérence et la fiabilité des informations présentées aux utilisateurs.
                    - Acquisition d'une expérience précieuse dans le domaine de la science des données en traversant les différentes étapes du processus de développement, de la collecte et du traitement des données à la conception de l'interface utilisateur et au déploiement de l'application en production.
                    - Objectif de fournir une plateforme ludique et éducative permettant aux utilisateurs d'explorer et de comparer les caractéristiques clés de différentes villes, facilitant ainsi la compréhension des dynamiques urbaines modernes.
                    """
            )
with st.expander(label="En partenariat avec la SNCF, conception d'un outil décisionnel sur l'outil Dataiku pour optimiser les investissements de la SNCF en favorisant une transition vers des modes de transport plus durables."):
            st.write(
                    """
                    - Recherche et collecte de données pertinentes sur les opérations de la SNCF afin d'alimenter l'outil décisionnel.
                    - Préparation et nettoyage des données sur Dataiku pour garantir leur qualité et leur cohérence, en vue de l'analyse et de la génération de rapports.
                    - Utilisation des fonctionnalités d'analyse de Dataiku pour explorer les données, identifier les tendances et les opportunités, et générer des rapports détaillés sur les performances et les impacts des investissements de la SNCF.
                    - Présentation des résultats aux intervenants de la SNCF, en mettant en avant les insights clés et les recommandations pour optimiser les investissements et encourager la transition vers des modes de transport plus durables.
                    - À partir des résultats de l'analyse et des discussions avec les intervenants de la SNCF, proposition de plans d'actions stratégiques visant à maximiser les avantages économiques et environnementaux des investissements de la SNCF dans des modes de transport durables.
                    """
            )
with st.expander(label="Comparaison d'Architectures de Réseaux de Neurones sur les Données CIFAR-10"):
            st.write(
                    """
                    Dans ce projet, j'ai utilisé la base de données CIFAR-10 pour comparer les performances de deux architectures de réseaux de neurones : un réseau de neurones multicouches (MLP) et un réseau de neurones convolutionnel (CNN).
                    - Utilisation de graphiques et de statistiques descriptives pour analyser la répartition des classes dans les ensembles d'entraînement et de test, ainsi que les caractéristiques des images.
                    - Choix d'une architecture MLP et d'une architecture CNN pour la classification des images CIFAR-10.
                    - Normalisation des données en soustrayant la moyenne et en divisant par l'écart-type pour chaque canal couleur.
                    - Entraînement des modèles sur les données d'entraînement avec suivi de la précision et du coût au fil des itérations.
                    - Comparaison des performances des deux architectures de réseaux de neurones en termes de précision et de coût au fur et à mesure de l'entraînement.
                    - Analyse des avantages et des inconvénients de chaque architecture en fonction des résultats obtenus.
                    
                    Ce projet a démontré l'importance de choisir la bonne architecture de réseau de neurones en fonction du problème à résoudre. Les résultats que j'ai obtenus m'ont permis de sélectionner la meilleure architecture pour la classification des images CIFAR-10, en tenant compte à la fois de la précision et de la complexité du modèle.
                    
                    En fournissant un notebook Jupyter contenant des cellules Markdown pour les réponses aux questions et des cellules de code pour les programmes, ce projet a mis en valeur ma capacité à analyser des données, à comparer des modèles et à communiquer efficacement les résultats.

                    """
            )
st.write(
                    """
                    🗓️ 2022-2023
                    """            
)
with st.expander(label="Description et Prévision de Séries Temporelles avec R"):
            st.write(
                    """
                    Dans le cadre de l'analyse des séries temporelles de production d'électricité pour l'Administration américaine de l'information sur l'énergie (EIA), j'ai utilisé le langage de programmation R pour explorer et analyser les données sur une période de 21 ans, de 2001 à 2021.
                    - Utilisation de filtres de moyennes mobiles pour détecter les tendances annuelles dans les séries temporelles.
                    - Création de courbes de régression pour illustrer les tendances globales.
                    - Utilisation de méthodes statistiques pour calculer les coefficients saisonniers pour chaque période de l'année.
                    - Utilisation de la méthode de décomposition pour séparer les séries en composantes saisonnières, tendancielles et résiduelles.
                    - Application de méthodes de correction des variations saisonnières pour obtenir des séries temporelles ajustées.
                    - Création d'un rapport complet avec R Markdown, incluant des captures d'écran des graphiques générés et des explications détaillées des résultats obtenus.
                    """
            )
with st.expander(label="Conception d'une application Rshiny, fournissant des informations (KPI) sur les meilleurs streamers de la plateforme Twitch, pour aider des investisseurs à selectionner la chaîne avec laquelle ils voudraient collaborer."):
            st.write(
                    """
                    - Traitement de données complexes sur les 1000 plus gros streamers de Twitch en 2020.
                    - Création de pages décrivant statistiquement les données, avec une attention particulière à l'aspect visuel.
                    - Réalisation d'une analyse multivariée des variables et des individus pour un profilage précis.
                    - Présentation claire et concise des informations essentielles, facilitant la prise de décision des investisseurs.               """
            )
with st.expander(label="Optimisation Tactique : Construire l'Équipe idéale dans Football Manager grâce à la Data Science"):
            st.write(
                    """
                    Objectif Projet : Développer des compétences avancées en intégration de données et en analyse pour répondre à la question clé : "Comment constituer l'équipe idéale dans Football Manager ?"

                    - Expertise dans la collecte, l'intégration et l'analyse approfondie des données pertinentes de Football Manager.
                    - Conception d'un tableau de bord interactif avec Rshiny, offrant des visualisations intuitives pour faciliter les décisions tactiques et stratégiques.
                    - Application de méthodologies statistiques avancées pour anticiper les performances des joueurs et guider les choix de gestion d'équipe.
                    - Présentation claire et persuasive des résultats lors de débriefings oraux, assurant une compréhension approfondie des conclusions et des stratégies suggérées.
                    """
            )
with st.expander(label="Intégration de données et analyse statistique pour résoudre la problématique suivante : Quelle est la zone géographique idéale pour un futur basketteur aux États-Unis ?"):
            st.write(
                    """
                    - Recherches de données pertinentes sur le web.
                    - Collecte, préparation, et intégration des données.
                    - Développement d'un tableau de bord (Power BI) intuitives facilitant la prise de décision.                    """
            )
with st.expander(label='Aider un responsable marketing à identifier les clients les plus appétants à la campagne marketing'):

            st.write(
                    
                    """
                    - Exploitation base de données relationnelle
                    - Transfert des données sur Power Bi
                    - Correctement interpréter et prendre en compte le besoin du client
                    - Création d'un reporting dynamique permettant au client d'identifier en quelques clics les réponses à sa problématique"
                    """
                    )
st.write(
                    """

                    🗓️ 2021-2022
                    """            
)
with st.expander(label="Aider une compagnie à prédire les clients qui seraient intéressés à souscrire à son assurance voyage"):

            st.write(
                    
                    """
                    - Nettoyage et préparation des données avec SAS
                    - Identification des données pertinentes par rapport à la demande
                    - Création de reportings pour apporter une aide à la décision
                    - Apporter une réponse claire et détaillée à la problématique de prévision
                    """
                    )
with st.expander(label="Création de la BDD d’un supermarché permettant de prévoir les besoins de main-d'oeuvre"):

            st.write(
                    
                    """
                    - Création de Base de Données Relationnelles à travers la modélisation,l’implémentation, l’alimentation, la validation, l’utilisation et la BDR
                    - Création de tableaux de bords
                    - Apporter une réponse à la problématique de prévision
                    - Présentation des résultats en soutenance orale
                    """
                    )
with st.expander(label="Création de reportings dans le but de conseiller un magasin de DVD, souhaitant améliorer ses ventes"):

            st.write(
                    
                    """
                    - Exploitation base de données relationnelles
                    - Identification des données pertinentes
                    - Création de tableaux de bords, en s'adaptant au niveau d'expertise, à la culture et au statut du destinataire
                    - Proposition d'actions d'améliorations pour le client
                    """
                    )
with st.expander(label="Analyse Statistique et Datavisualisation des Données de l'affaire ENRON :"):
            st.write(
                    
                    """
                    - Importation des données brutes dans un système de gestion de bases de données (Spark), suivi d'une extraction ciblée des informations pertinentes à l'aide de requêtes SQL pour une préparation efficace des données.
                    - Utilisation de R pour explorer et analyser les données, générer des rapports détaillés et créer des représentations visuelles percutantes pour une meilleure compréhension des tendances et des corrélations.
                    - Élaboration d'un rapport technique mettant en lumière les aspects informatiques du processus, décrivant les étapes de traitement des données, les algorithmes utilisés, et les choix méthodologiques effectués.
                    - Préparation d'un rapport d'analyse statistique détaillant les résultats obtenus, incluant des analyses descriptives, des tests statistiques pertinents, et des interprétations des résultats pour fournir des insights significatifs.
                    - Présentation des conclusions et des découvertes lors d'une soutenance orale, en mettant l'accent sur les aspects clés du projet de manière claire et convaincante, tout en illustrant les implications pratiques des résultats obtenus.                    """
                    )
with st.expander(label="Lecture et Ecriture de fichiers - Python"):
            st.write(
                    """
                    - Élaboration d'un script Python permettant la création d'un fichier de données au format CSV à partir d'un fichier original au format spécifique non conventionnel.
                    """
)
with st.expander(label="Étude du Parcours Professionnel des Diplômés de DUT STID de l'IUT Paris - Rives de Seine : Conception d'un Questionnaire sur LimeSurvey."):
            st.write(
                    """
                    - Exploitation des Résultats à l'Aide de Requêtes SQL pour Extraire des Informations Significatives.
                    - Création de Graphiques Pertinents sous Excel pour Illustrer les Tendances et Résultats de l'Enquête.
                    - Calcul de Corrélations entre Variables pour Dévoiler des Liens Subtils dans les Résultats de l'Enquête.
                    - Présentation Structurée de l'Enquête lors d'une Soutenance Orale, Mettant en Avant les Conclusions Clés et les Implications pour l'IUT et ses Diplômés.

                    """
)  

#####################
st.markdown('<div id="social-media"></div>', unsafe_allow_html=True)
st.markdown('''
## 📮 Me contacter
'''
)
st.write("📧 Email: brahim.elfarh.pro@gmail.com")
st.write("☎️ Téléphone: +33 6 56 88 38 86")
st.markdown("ℹ️ [LinkedIn](https://www.linkedin.com/in/brahim-el-farh-0521a4235/?originalSubdomain=fr)", unsafe_allow_html=True)

