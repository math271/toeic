# -*- coding: utf-8 -*-
"""
Fabrique site/index.html a partir de ../flashcards.html.

flashcards.html reste la SOURCE UNIQUE : il est ecrit pour etre publie en
artifact (Claude fournit alors <!doctype>, <head> et <body>). Pour un
hebergement normal il faut ajouter cette enveloppe nous-memes, plus ce qu'il
faut pour l'ecran d'accueil de l'iPhone et le fonctionnement hors ligne.

Relancer ce script apres toute modification de flashcards.html, puis pousser.
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "..", "flashcards.html")
DEST = os.path.join(HERE, "index.html")

TITRE = "TOEIC Flashcards"          # sans prenom : la page est publique

src = io.open(SRC, encoding="utf-8").read()

# On separe la feuille de style (qui ira dans <head>) du corps de la page.
coupe = src.index("</style>") + len("</style>")
tete, corps = src[:coupe], src[coupe:]

tete = re.sub(r"<title>.*?</title>\s*", "", tete, flags=re.S)
tete = re.sub(r'<meta name="viewport"[^>]*>\s*', "", tete)

html = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titre}</title>

<!-- Ecran d'accueil iOS : l'appli s'ouvre en plein ecran, sans barre Safari -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="TOEIC">
<meta name="mobile-web-app-capable" content="yes">
<meta name="theme-color" content="#F5F4EF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#131920" media="(prefers-color-scheme: dark)">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" href="icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
{tete}
</head>
<body>
{corps}
<script>
// Hors ligne : le service worker garde une copie de l'appli.
if ("serviceWorker" in navigator) {{
  addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {{}}));
}}
</script>
</body>
</html>
""".format(titre=TITRE, tete=tete.strip(), corps=corps.strip())

io.open(DEST, "w", encoding="utf-8").write(html)

nb = html.count('{d:"')
print("index.html ecrit :", len(html), "octets,", nb, "cartes")
assert "<!doctype html>" in html and "</body>" in html
assert "Bérengère" not in html, "le prenom ne doit pas apparaitre sur une page publique"
assert nb > 300, "cartes manquantes"
print("controles OK")
