# The Others — Story Arc Brief

## Concept

"The Others" est un arc narratif optionnel pour la page Story, à insérer entre Act III (Creation) et un éventuel Act IV ou épilogue.

L'idée centrale : raconter les personnes qui t'ont influencé — pas des mentors au sens classique, pas une liste de remerciements, mais des **fragments anonymes ou semi-anonymes**. Une scène précise. Une phrase entendue une fois. Un geste qui a changé quelque chose sans que la personne le sache.

---

## Ce qui le distingue des autres arcs

La plupart des sections de Story parlent de toi. "The Others" est la seule qui regarde ailleurs — et c'est précisément ce qui lui donne de la profondeur. Elle dit : *je ne me suis pas construit seul*.

Ce n'est pas sentimental. C'est factuel et humain.

---

## Ton de la section

- Fragments courts, presque elliptiques
- Anonymat partiel ou total — les personnes ne sont pas nommées, ou seulement par un prénom, un rôle, une relation
- Pas de moral à la fin de chaque fragment. Juste la scène et ce qu'elle a laissé
- Visuellement : citations courtes qui apparaissent progressivement, comme des étoiles qui s'allument — cohérent avec la DA cosmos du site

---

## Structure suggérée

```
[Eyebrow]  The Others

[Titre]    Some people leave a mark
           without meaning to.

[Fragment 1]  Une phrase, une scène, 1-3 lignes max
[Fragment 2]  Une phrase, une scène, 1-3 lignes max
[Fragment 3]  ...
[Fragment 4]  ...
[Fragment 5]  ...

[Clôture]  Une ligne finale, sobre.
```

3 à 6 fragments est l'idéal. En dessous, ça manque d'ampleur. Au-dessus, ça perd de son impact.

---

## Ce que tu dois apporter

Du contenu réel. C'est la condition sine qua non de cet arc.

Quelques questions pour t'aider à chercher :

- Quelqu'un t'a-t-il dit une phrase qui a changé ta façon de voir quelque chose ?
- Y a-t-il une personne croisée brièvement — un prof, un inconnu, quelqu'un en compétition — dont l'attitude t'a marqué ?
- Un moment où quelqu'un a fait quelque chose de simple mais qui t'a appris quelque chose sur toi ?
- Une personne qui n'a probablement aucune idée de l'effet qu'elle a eu ?

Les réponses n'ont pas besoin d'être dramatiques. Les meilleurs fragments sont souvent les plus ordinaires.

---

## Implémentation technique

L'arc s'intègre dans `story-v6.html` comme une nouvelle section `.act`, après Act III.

Structure HTML indicative :

```html
<section class="act" id="act-others">
  <div class="narrow">
    <p class="act-label reveal">The Others</p>
    <h2 class="reveal reveal-delay-1">Some people leave a mark<br>without meaning to.</h2>

    <div class="others-list">
      <p class="other-fragment reveal reveal-delay-2">"..."</p>
      <p class="other-fragment reveal reveal-delay-3">"..."</p>
      <!-- etc. -->
    </div>

    <p class="others-close reveal">...</p>
  </div>
</section>
```

CSS : même logique que les autres acts — fond transparent, texte centré, apparition au scroll. Les fragments peuvent avoir un léger `padding-left` et une `border-left: 1px solid var(--violet)` pour les distinguer visuellement du reste.

---

## Quand revenir à cet arc

Quand tu as du matériel réel à mettre dedans. Pas avant.
Un arc vide ou générique ferait plus de mal que pas d'arc du tout.
