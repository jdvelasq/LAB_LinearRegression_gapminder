"""
Calificación del laboratorio
-----------------------------------------------------------------------------------------
"""

import sys

import preguntas


def test_01():
    preguntas.pregunta_01()


def test_02():
    preguntas.pregunta_02()


def test_03():
    preguntas.pregunta_03()


def test_04():
    preguntas.pregunta_04()


test = {
    "01": test_01,
    "02": test_02,
    "03": test_03,
    "04": test_04,
}[sys.argv[1]]

test()
