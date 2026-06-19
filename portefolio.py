import streamlit as st
from datetime import datetime
import pandas as pd
import random

# Configuration de la page
st.set_page_config(
    page_title="Thioro SYLLA | Géomaticienne Passionnée",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# STYLE CHALEUREUX ET HUMAIN - ANIMATIONS DIMINUÉES
# ============================================
st.markdown("""
<style>
    /* Police et ambiance générale */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Animation douce mais très légère pour tout le site */
    .main {
        animation: fadeIn 0.5s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    /* Header avec effet de verre - pas d'animation */
    .glass-header {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    /* Badges doux - animation supprimée */
    .soft-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 30px;
        font-size: 0.85rem;
        display: inline-block;
        margin: 0.2rem;
        /* transition et hover supprimés */
    }
    
    /* Cartes avec effet très léger - animation réduite */
    .human-card {
        background: white;
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        transition: all 0.2s ease;  /* transition plus rapide */
        border: 1px solid #f0f0f0;
    }
    
    .human-card:hover {
        transform: translateY(-2px);  /* déplacement plus petit */
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);  /* ombre plus légère */
    }
    
    /* Citation du jour - pas d'animation */
    .quote-box {
        background: linear-gradient(135deg, #ffe6e6 0%, #ffe6f0 100%);
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        font-style: italic;
        margin: 1rem 0;
    }
    
    /* Progrès personnalisé */
    .custom-progress {
        background: #e0e0e0;
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
    }
    
    .custom-progress-fill {
        background: linear-gradient(90deg, #667eea, #764ba2);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;  /* animation plus rapide */
    }
    
    /* Boutons doux */
    .soft-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 1.5rem;
        border-radius: 30px;
        cursor: pointer;
        transition: all 0.2s ease;
        text-align: center;
        display: inline-block;
    }
    
    .soft-button:hover {
        transform: translateY(-1px);  /* déplacement minimal */
        box-shadow: 0 3px 10px rgba(102,126,234,0.3);
    }
    
    /* Timeline - pas d'animation */
    .timeline-item {
        border-left: 3px solid #667eea;
        padding-left: 1.5rem;
        margin: 1.5rem 0;
        position: relative;
    }
    
    .timeline-item::before {
        content: "●";
        position: absolute;
        left: -0.8rem;
        top: 0;
        color: #667eea;
        font-size: 1.2rem;
    }
    
    /* Suppression de l'animation sur les cartes de loisirs */
    .loisir-card {
        text-align: center;
        padding: 1rem;
        background: #f9f9f9;
        border-radius: 15px;
        transition: none;  /* pas d'animation */
    }
    
    .loisir-card:hover {
        transform: none;  /* pas de mouvement */
        background: #f0f0f0;  /* juste un changement de couleur subtil */
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# DONNÉES PERSONNALISABLES (TA VRAIE VIE)
# ============================================

# 👤 IDENTITÉ
PRENOM = "Thioro"
NOM = "SYLLA"
PHOTO_EMOJI = "🌿"
VILLE = "Kaolack, Sénégal"
TITRE_ACCROCHE = "Technicienne en Géomatique passionnée par la modernisation administrative"

# 📧 CONTACT
EMAIL = "syllathioro069@gmail.com"
TELEPHONE = "+221 77 808 02 76"
LINKEDIN = "https://linkedin.com/in/thiorosylla"
GITHUB = "https://github.com/thiorosylla"

# 🎯 BIO PROFESSIONNELLE
BIO = """
Passionnée par **la modernisation administrative** et **la gestion des données territoriales**, 
j'allie mon expertise technique en **SIG et Topographie** avec les outils numériques 
pour développer des solutions innovantes. Mon objectif ? **Optimiser l'aménagement du territoire** 
et rendre les données géographiques accessibles à tous.
"""

# 🌟 MES VALEURS
MES_VALEURS = [
    "🤝 **L'humain d'abord** : Je crée des outils que les gens aiment utiliser",
    "🌍 **Impact positif** : Mes projets servent le territoire et ses habitants",
    "📚 **Apprentissage continu** : Je me forme chaque semaine",
    "💡 **Innovation responsable** : Des solutions durables et éthiques"
]

# 💼 EXPÉRIENCES PROFESSIONNELLES
EXPERIENCES = [
    {
        "titre": "Technicienne Géomaticienne",
        "entreprise": "Communauté d'Agglomération de Dakar",
        "periode": "2022 - Aujourd'hui",
        "description": "assistante géometre/technicienne SIG",
        "realisations": [
            "modernisation du suivi des dossiers via la mise en place d'une base de données relationnelle (Microsoft Access) Autonomisation de rapports statistiques pour améliorer le traitement des données étudiantes Coordination logistique entre les différents services départementaux",
            "Réalisation de levés topographiques de precision pour des projets d'aménagement",
            "Création des cartes théamatiques pour l'aide a la décision administrative",
            "Numérisation et mise a jour de plans cadastraux via AutoCad",
            "Création d'un portail cartographique pour les citoyens",
            "Automatisation des mises à jour cadastrales (gain de 15h/semaine)",
            "Formation de 20 agents aux outils SIG"
        ]
    },
    {
        "titre": "Apprentie Géomaticienne",
        "entreprise": "",
        "periode": "2025 - 2026",
        "description": "Support technique et développement d'outils",
        "realisations": [
            "Développement d'une application mobile pour relevés terrain",
            "Migration des bases de données vers PostgreSQL/PostGIS",
            "Création de cartes thématiques pour l'urbanisme"
        ]
    }
]

# 🎓 FORMATIONS
FORMATIONS = [
    {
        "diplome": "Baccalareat Langue et Cévilisation Moderne",
        "ecole": "Lycée Valdiodio Ndiaye",
        "annee": "2019-2020",
        "mention": "Mention Bien"
    },
    {
        "diplome": "Brevet de Technichien Superieur en Geomatique",
        "ecole": "CTD - G15",
        "annee": "2025-2026",
        "mention": "Mention Assez Bien"
    },
    {
        "diplome": "Formation en informatique",
        "ecole": "Formation Continue",
        "annee": "2024",
        "mention": "Certifiée"
    }
]

# 🛠️ COMPÉTENCES TECHNIQUES
COMPETENCES_TECH = {
    "SIG & Cartographie": {
        "QGIS": 95,
        "ArcGIS Pro": 85,
        "MapInfo": 70
    },
    "Bases de données spatiales": {
        "PostgreSQL/PostGIS": 90,
        "Spatialite": 75,
        "Oracle Spatial": 60
    },
    "Développement": {
        "Python (GeoPandas)": 85,
        "Streamlit": 80,
        "JavaScript (Leaflet)": 75,
        "SQL": 90
    },
    "Topographie": {
        "AutoCAD": 85,
        "Covadis": 80,
        "Tacheométrie": 90
    }
}

# 🚀 PROJETS RÉALISÉS
PROJETS = [
    {
        "nom": "📱 Carto'Mobile",
        "description": "Application mobile pour relevés terrain hors-ligne",
        "contexte": "Les agents terrain avaient besoin d'un outil simple",
        "solution": "App avec carte interactive et formulaire personnalisé",
        "resultats": "Gain de 50% de temps sur les relevés",
        "technologies": ["Python", "Streamlit", "Folium", "SQLite"],
        "image": "📱",
        "lien": "https://github.com/projet-cartomobile"
    },
    {
        "nom": "🏙️ Portail Urbanisme",
        "description": "Plateforme de consultation des documents d'urbanisme",
        "contexte": "Les citoyens peinaient à trouver les infos d'urbanisme",
        "solution": "Portail web avec visualisation cartographique",
        "resultats": "+200% de consultations en 3 mois",
        "technologies": ["PostGIS", "Leaflet", "Django", "Bootstrap"],
        "image": "🏙️",
        "lien": "https://github.com/projet-urbanisme"
    },
    {
        "nom": "🗺️ Atlas Interactif",
        "description": "Atlas cartographique dynamique du territoire",
        "contexte": "Centraliser les données éparpillées",
        "solution": "Dashboard interactif avec filtres et analyses",
        "resultats": "Une source de vérité unique pour les élus",
        "technologies": ["QGIS", "Python", "Streamlit", "Plotly"],
        "image": "🗺️",
        "lien": "https://github.com/projet-atlas"
    }
]

# 📖 CITATIONS INSPIRANTES
CITATIONS = [
    "« La carte n'est pas le territoire, mais elle nous aide à le comprendre. »",
    "« Une bonne donnée spatiale vaut mieux qu'un long discours. »",
    "« La géomatique au service de l'humain, c'est ma mission. »",
    "« Chaque projet est une aventure cartographique. »"
]

# 🎯 OBJECTIFS PERSONNELS
OBJECTIFS = [
    "📚 Apprendre le Machine Learning pour l'analyse spatiale",
    "🌍 Contribuer à des projets open-source géomatiques",
    "👩‍🏫 Devenir formatrice SIG pour les collectivités",
    "💡 Créer une communauté de géomaticiennes passionnées"
]

# 🎨 LOISIRS & PASSIONS
LOISIRS = [
    {"nom": "Randonnée", "emoji": "🥾", "description": "J'explore les cartes IGN sur le terrain"},
    {"nom": "Photographie", "emoji": "📸", "description": "Je capture les paysages que je cartographie"},
    {"nom": "Bénévolat", "emoji": "🤝", "description": "OpenStreetMap & cartographie participative"},
    {"nom": "Lecture", "emoji": "📚", "description": "Romans et revues géographiques"}
]

# ============================================
# INTERFACE PRINCIPALE - ACCUEIL CHALEUREUX
# ============================================

# Header avec message de bienvenue personnalisé
heure = datetime.now().hour
if heure < 12:
    salutation = "Bonjour"
elif heure < 18:
    salutation = "Bon après-midi"
else:
    salutation = "Bonsoir"

st.markdown(f"""
<div class='glass-header'>
    <div style='display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;'>
        <div>
            <p style='color: #667eea; font-size: 0.9rem; margin: 0;'>{salutation} !</p>
            <h1 style='margin: 0; font-size: 2.5rem;'>{PRENOM} {{NOM}}</h1>
            <p style='font-size: 1.1rem; color: #666; margin-top: 0.3rem;'>{TITRE_ACCROCHE}</p>
        </div>
        <div style='text-align: center;'>
            <div style='font-size: 5rem;'>{PHOTO_EMOJI}</div>
            <p style='margin: 0; font-size: 0.8rem; color: #999;'>📍 {VILLE}</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Citation aléatoire du jour
citation_du_jour = random.choice(CITATIONS)
st.markdown(f"""
<div class='quote-box'>
    <p style='margin: 0; font-size: 0.95rem;'>{citation_du_jour}</p>
    <p style='margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #999;'>✨ Citation du jour</p>
</div>
""", unsafe_allow_html=True)

# ============================================
# MENU DE NAVIGATION
# ============================================

menu = st.radio(
    "",
    ["🌿 Accueil", "💼 Mon Parcours", "🚀 Mes Projets", "🛠️ Compétences", "💬 Me Contacter"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")

# ============================================
# PAGE ACCUEIL
# ============================================

if menu == "🌿 Accueil":
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("## ")
        st.markdown(BIO)
        
        st.markdown("## 🌟 Mes valeurs")
        for valeur in MES_VALEURS:
            st.markdown(valeur)
    
    with col2:
        st.markdown("## 📬 Contact rapide")
        with st.form("contact_rapide"):
            nom_rapide = st.text_input("Ton prénom")
            email_rapide = st.text_input("Ton email")
            message_rapide = st.text_area("Un petit message ?", height=100)
            
            if st.form_submit_button("💌 Envoyer", use_container_width=True):
                if nom_rapide and email_rapide and message_rapide:
                    st.success(f"Merci {nom_rapide} ! Je te réponds rapidement ✨")
                    st.balloons()
                else:
                    st.warning("Remplis tous les champs stp 🙏")
        
        st.markdown("---")
        st.markdown("## 🎯 Mes objectifs")
        for obj in OBJECTIFS:
            st.markdown(obj)
    
    # Loisirs - version sans animation
    st.markdown("---")
    st.markdown("## 💫 En dehors du travail")
    
    cols = st.columns(4)
    for idx, loisir in enumerate(LOISIRS):
        with cols[idx]:
            st.markdown(f"""
            <div style='text-align: center; padding: 1rem; background: #f9f9f9; border-radius: 15px;'>
                <div style='font-size: 2rem;'>{loisir['emoji']}</div>
                <strong>{loisir['nom']}</strong>
                <p style='font-size: 0.8rem; color: #666; margin-top: 0.5rem;'>{loisir['description']}</p>
            </div>
            """, unsafe_allow_html=True)

# ============================================
# PAGE MON PARCOURS
# ============================================

elif menu == "💼 Mon Parcours":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("## 📊 Chiffres clés")
        st.metric("🗺️ Projets SIG", "12+", "3 en cours")
        st.metric("📍 Communes accompagnées", "25+", "")
        st.metric("👥 Agents formés", "50+", "Satisfaction 95%")
        st.metric("📅 Années d'expérience", "4", "")
    
    with col2:
        st.markdown("## 💼 Expériences professionnelles")
        for exp in EXPERIENCES:
            with st.container():
                st.markdown(f"""
                <div class='timeline-item'>
                    <strong style='font-size: 1.1rem;'>{exp['titre']}</strong><br>
                    <span style='color: #667eea;'>{exp['entreprise']}</span>
                    <span style='color: #999; font-size: 0.9rem;'> | {exp['periode']}</span>
                    <p style='margin: 0.5rem 0 0 0;'>{exp['description']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                for realisation in exp['realisations']:
                    st.markdown(f"✓ {realisation}")
                st.markdown("---")
    
    st.markdown("## 🎓 Formation")
    cols = st.columns(3)
    for idx, formation in enumerate(FORMATIONS):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class='human-card'>
                <h4 style='margin: 0; color: #667eea;'>{formation['diplome']}</h4>
                <p style='margin: 0.3rem 0;'>{formation['ecole']}</p>
                <p style='margin: 0; font-size: 0.8rem; color: #999;'>{formation['annee']}</p>
                <p style='margin: 0.5rem 0 0 0; font-size: 0.9rem;'>{formation['mention']}</p>
            </div>
            """, unsafe_allow_html=True)

# ============================================
# PAGE MES PROJETS
# ============================================

elif menu == "🚀 Mes Projets":
    st.markdown("## 🚀 Découvre mes réalisations")
    st.markdown("*Chaque projet raconte une histoire, chaque solution répond à un vrai besoin*")
    
    for projet in PROJETS:
        with st.expander(f"{projet['image']} {projet['nom']}", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**📖 Contexte :** {projet['contexte']}")
                st.markdown(f"**✨ Solution :** {projet['solution']}")
                st.markdown(f"**📈 Résultats :** {projet['resultats']}")
                
                st.markdown("**🛠️ Technologies :**")
                tech_html = " ".join([f"<span class='soft-badge'>{tech}</span>" for tech in projet['technologies']])
                st.markdown(tech_html, unsafe_allow_html=True)
            
            with col2:
                st.link_button("🔗 Voir sur GitHub", projet['lien'], use_container_width=True)
                st.markdown(f"<div style='font-size: 3rem; text-align: center; margin-top: 1rem;'>{projet['image']}</div>", unsafe_allow_html=True)

# ============================================
# PAGE COMPÉTENCES
# ============================================

elif menu == "🛠️ Compétences":
    st.markdown("## 🛠️ Mes compétences techniques")
    st.markdown("*Des outils maîtrisés pour des projets impactants*")
    
    for domaine, competences in COMPETENCES_TECH.items():
        st.markdown(f"### {domaine}")
        cols = st.columns(len(competences))
        for idx, (comp, niveau) in enumerate(competences.items()):
            with cols[idx]:
                st.markdown(f"**{comp}**")
                st.progress(niveau/100, text=f"{niveau}%")
        st.markdown("---")
    
    # Soft skills
    st.markdown("## 💫 Soft skills")
    soft_skills = [
        "🎯 **Analyse des besoins métier** : Comprendre avant d'agir",
        "🤝 **Pédagogie** : Former et transmettre avec passion",
        "📊 **Gestion de projet** : Méthodes agiles adaptées",
        "💬 **Communication** : Vulgarisation technique",
        "🔍 **Résolution de problèmes** : Trouver des solutions créatives"
    ]
    
    for skill in soft_skills:
        st.markdown(skill)

# ============================================
# PAGE CONTACT
# ============================================

elif menu == "💬 Me Contacter":
    st.markdown("## 💬 Parlons de ton projet !")
    st.markdown("*Je suis toujours ravie d'échanger autour de la géomatique et des données territoriales*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📞 Me joindre")
        st.markdown(f"""
        <div style='background: #f9f9f9; padding: 1.5rem; border-radius: 15px;'>
            <p>📧 <strong>Email :</strong> {EMAIL}</p>
            <p>📱 <strong>Téléphone :</strong> {TELEPHONE}</p>
            <p>📍 <strong>Localisation :</strong> {VILLE}</p>
            <p>💼 <strong>LinkedIn :</strong> <a href='{LINKEDIN}'>Thioro SYLLA</a></p>
            <p>🐙 <strong>GitHub :</strong> <a href='{GITHUB}'>thiorosylla</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### ✨ Envoie-moi un message")
        with st.form("contact_complet"):
            nom_complet = st.text_input("Ton nom complet")
            email_complet = st.text_input("Ton email")
            telephone_complet = st.text_input("Ton téléphone (optionnel)")
            sujet = st.selectbox("Sujet", ["Demande de devis", "Collaboration", "Information", "Autre"])
            message_complet = st.text_area("Ton message", height=150)
            
            col_check1, col_check2 = st.columns(2)
            with col_check1:
                newsletter = st.checkbox("Je veux recevoir des news 📧")
            with col_check2:
                rdv = st.checkbox("Je préfère un appel 📞")
            
            if st.form_submit_button("💌 Envoyer mon message", use_container_width=True):
                if nom_complet and email_complet and message_complet:
                    st.success(f"Merci {nom_complet} ! Je te réponds dans les 24h ✨")
                    st.balloons()
                    st.snow()
                else:
                    st.error("N'oublie pas ton nom, email et message 🙏")
    
    # Disponibilités
    st.markdown("---")
    st.markdown("## 📅 Mes disponibilités")
    st.info("""
    🌟 **Actuellement disponible** pour :
    - Missions de conseil en géomatique
    - Développement d'outils sur mesure
    - Formations SIG personnalisées
    - Accompagnement à la modernisation administrative
    
    💬 N'hésitez pas à me contacter pour discuter de votre projet !
    """)

# ============================================
# SIDEBAR - INFOS PERSONNELLES
# ============================================

with st.sidebar:
    st.markdown(f"""
    <div style='text-align: center; padding: 1rem;'>
        <div style='font-size: 6rem;'>{PHOTO_EMOJI}</div>
        <h2 style='margin: 0;'>{PRENOM} {NOM}</h2>
        <p style='color: #667eea; margin: 0;'>Technicienne en Géomatique</p>
        <p style='font-size: 0.8rem; color: #999;'>🎂 27 ans | 📍 {VILLE}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Petit message sans animation
    st.markdown("### ☀️ Mon état d'esprit")
    humeur = random.choice(["💪 Motivée", "✨ Créative", "🎯 Focus", "🤝 Envie d'échanger"])
    st.markdown(f"*{humeur} pour de nouveaux projets !*")
    
    st.markdown("---")
    
    # Derniers articles/blogue
    st.markdown("### 📖 Je partage")
    st.markdown("""
    - 📄 Les bases de données spatiales
    - 🗺️ Créer une carte avec Streamlit
    - 🌍 Mon expérience OpenStreetMap
    """)
    
    st.markdown("---")
    
    # Téléchargement CV
    st.markdown("### 📄 Mon CV")
    st.markdown("*(Bientôt disponible)*")
    
    # Badge passion - sans animation
    st.markdown("---")
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea20 0%, #764ba220 100%); padding: 0.5rem; border-radius: 10px; text-align: center;'>
        <p style='margin: 0; font-size: 0.8rem;'>🌍 La géomatique au service<br>de l'humain et des territoires</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================

st.markdown("---")
st.markdown(f"""
<div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea10 0%, #764ba210 100%); border-radius: 20px; margin-top: 2rem;'>
    <p style='margin: 0; font-size: 0.9rem;'>✨ Merci de votre visite ✨</p>
    <p style='margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #999;'>
    {PRENOM} - Technicienne en Géomatique - {datetime.now().year}
    </p>
</div>
""", unsafe_allow_html=True)
