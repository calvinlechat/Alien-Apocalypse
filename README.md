# Alien-Apocalypse

Jeu de tir arcade type **Space Invaders** en **Python & Pyxel**, développé en binôme en **6 heures** lors de la **Nuit du Code** (le 13 mars 2024, en classe de Première, année scolaire 2023–2024) par **Calvin Lechat** et **Thibault L.**

---

## Présentation

Dans **Alien-Apocalypse**, vous pilotez un vaisseau galactique chargé d'empêcher une invasion extraterrestre d'atteindre la Terre, tout en survivant aux assauts ennemis.

L'objectif est de réaliser le **meilleur score possible** en éliminant des vagues d'aliens de plus en plus rapides et résistantes. Plus votre score grimpe, plus la difficulté augmente, avec l'apparition d'aliens de différentes couleurs et un rythme d'apparition de plus en plus soutenu.

---

## Fonctionnalités & Mécaniques

* **Système de score & difficulté progressive** : chaque alien détruit rapporte des points ; l'augmentation du score accélère l'apparition des ennemis et introduit des vagues plus coriaces (aliens de différentes couleurs).
* **Double jauge de survie** :
  * **Vie de la Terre** : diminue à chaque fois qu'un alien franchit le bas de l'écran (l'axe des abscisses).
  * **Vie du vaisseau** : diminue en cas de collision directe avec un alien.
* **Pack de soin** : apparaît aléatoirement sur le terrain avec un long temps de réapparition pour vous aider à tenir le plus longtemps possible.

---

## Contrôles

* **Déplacement du vaisseau** : direction grâce au touches Z Q S D*
* **Tirer** : `Clic gauche` de la souris

---

## Installation & Lancement

Assure-toi d'avoir **Python 3** et la bibliothèque **Pyxel** installés :

```bash
pip install pyxel
```

### Récupérer le projet

```bash
git clone [https://github.com/calvinlechat/Alien-Apocalypse.git](https://github.com/calvinlechat/Alien-Apocalypse.git)
```

### Lancer le jeu

```bash
cd Alien-Apocalypse
python Alien-Apocalypse.py
```

---

## Technique & Contexte

* **Technologie** : Python + [Pyxel](https://github.com/kitao/pyxel)
* **Contexte** : Projet réalisé en 6h dans le cadre de la **Nuit du Code 2024** (13/03/2024 — Première, 2023–2024).
