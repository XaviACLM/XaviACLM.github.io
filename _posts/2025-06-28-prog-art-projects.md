---
layout: static-post
title: Misc mini-projects
---

### Subway maps

![Subway maps mockup](/post_assets/metro.png)

A graphical tool for drawing metro maps. The interface can be a bit opaque, since this is designed to have exactly the tools that I want from it - it's actually the seventh iteration of a long-running project. Although it can be used as one, this isn't really meant as an utility tool, rather I only made the maps because I think they look nice - I have a few of them printed out. Code [here](/post_assets/metro_tk_editor.7z).

### Icosahedron worldmap

![Dymaxion](/post_assets/dymaxion.png)

A dymaxion projection made more to look nice than to be useful (but isn't that all world maps). Decently optimized source code, repo [here](https://github.com/XaviACLM/icosahedron-worldmap).

### Collatz-graph

![Collatz graph](/post_assets/treesticle7.png)

A representation of the [Collatz graph](https://en.wikipedia.org/wiki/Collatz_conjecture#Other_formulations_of_the_conjecture). this is one of those instances where a discrete/combinatorial structure is large and organic enough that it serves well as a skeleton around which to build something nice-looking. Branch width is for strahler numbers, color for value, left/right turns are for halving/tripling steps. 

### Turing-complete one-liners

![step one-liner](/post_assets/one-liner.jpg)

A single-line brainfuck interpreter written in python. See how it was made from the ground up [here](/post_assets/oneline_buildup.py). In some way it bothers me that this uses lambdas, because it's almost a non-statement that inline functions would make one-liners turing complete if you're familiar with the lambda calculus (I'm not). I suspect a more standard imperative language might be embeddable in python one-liners, using ternaries/comprehensions for flow control and the walrus for state updates, but never got around to trying to implement this.
