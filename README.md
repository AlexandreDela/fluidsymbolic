[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pylint](https://img.shields.io/badge/code%20quality-pylint-blue)](https://github.com/PyCQA/pylint)
[![Flake8](https://img.shields.io/badge/code%20quality-flake8-blueviolet)](https://github.com/PyCQA/flake8)
[![pytest](https://img.shields.io/badge/pytest-passing-brightgreen)](.)


## Documentation

The documentation is available in html [here](https://alexandredela.github.io) (generated by Sphinx).
This module is a module designed to help deal with object-oriented logging.

## How to use

`pip install fluidsymbolic` and that's it!

It requires sympy because it's for symbolic mathematics 
 and matplotlib for animations.

## Goal
Plot some fluid mechanics equation using symbolic mathematics using sympy,
scipy integrate, matplotlib and matplotlib animations.

## Rationale

While reading Tony S. Yu's article on animated stream functions and vorticity, 
I noticed many scripts were severely outdated.
Therefore I had this project to remake everything 
in a more modern fashion.


How to use?
-----------

Examples are available inside the **example** folder.

How does it work?
-----------------

UNFINISHED PROJECT
Project abandonned, check the src/test files for examples.

Limitations
-----------

This module only assumes 2D flows, the speed on the vertical axis 
is supposed to be negligible.

## Sources of inspiration
      

*'Eléments d'analyse pour l'étude de quelques 
modèles d'écoulement de fluides visqueux incompressibles'* by *Franck Boyer, Pierre Fabrie* (ISBN 3-540-29818-5) 
as well as [Tony S. Yu's articles on the matter](https://tonysyu.github.io)