# TOEIC Flashcards

Application de flashcards en répétition espacée pour préparer le TOEIC : 572 cartes,
143 de vocabulaire et 175 de grammaire. Une page, aucune dépendance, aucun compte.

**→ https://math271.github.io/toeic/**

## Utilisation

Sur téléphone, ouvrir le lien puis ajouter la page à l'écran d'accueil
(iPhone : Partager → *Sur l'écran d'accueil*). L'appli s'ouvre alors en plein écran
et fonctionne **sans connexion**.

La progression est enregistrée dans le navigateur de l'appareil, jamais envoyée
ailleurs — donc propre à chaque appareil.

## Contenu

| Famille | Paquets | Cartes |
|---|---|---|
| Vocabulaire | temps verbaux, verbes irréguliers, bureau, finance, voyages, RH, faux-amis | 143 |
| Grammaire | 16 sections : nature du mot, accord sujet-verbe, le verbe, passif, gérondif/infinitif, modaux, prépositions, déterminants, quantité, relatifs, pronoms, mots de liaison, conditionnel, ordre des mots, mots confondus, expressions figées | 175 |

Les cartes de grammaire portent au verso le numéro de la règle dont elles sont tirées
(« Règle 70 · fiche 2 »), pour faire le lien avec la fiche de cours correspondante.

## Mettre à jour

`index.html` est **généré**, il ne faut pas l'éditer à la main. La source est
`flashcards.html`, conservée hors du dépôt avec les fiches de cours.

```
python build.py    # régénère index.html depuis ../flashcards.html
git commit -am "..." && git push
```

GitHub Pages redéploie tout seul en une minute environ. Le service worker sert la
dernière version en ligne et ne garde le cache que pour l'usage hors connexion.
