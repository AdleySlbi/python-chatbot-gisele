# coding: utf-8

"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""
from lib import get_classer
from data import newsSet

excec = {
    'hello': 1,
    'tiao': 0,
    'question': 0,
    'tomate': 0,
    'classico': 0,
    'panini': 0
}

def ma_loop(value):
    newsClassifier = get_classer()
    classification = newsClassifier.classify(value)
    # [('tiao', 0.0), ('question', 0.0), ('hello', 0.0)]
    category = classification[0][0]
    score = classification[0][1]

    if score > 0:
        # newsSet.append({'text': value, 'category': category})
        excec[category] += 1
        if category == 'hello': return hello()
        if category == 'question': return question()
        if category == 'tiao': return tiao()
        if category == 'classico': return classico(value)
        if category == 'tomate': return tomate()
        if category == 'panini': return panini()
    return pascompris(value)

def question(value=None):
    value = raw_input("A propos ?")
    return ma_loop(value)

def classico(value=None):
    if 'Evra' in value:
        print 'Oui, il était très mauvais'
        value = raw_input("Vous avez une autre question ?")
        return ma_loop(value)

    if 'PSG' in value:
        print 'Effectivement, très fort'
        value = raw_input("Vous voulez savoir comment evra à jour ?")
        return ma_loop(value)


def hello(value=None):
    if excec['hello'] is 1:
        value = raw_input("Bonjour Adley! Alors on ne sait pas quoi manger? Qu'avez vous dans votre frigo?")
    elif excec['hello'] is 2:
        value = raw_input("Oui, bonjour, quelle est votre question, je peux vous aider ?")
    elif excec['hello'] is 3:
        value = raw_input("Oui, je vous écoute nous sommes à votre service ?")
    elif excec['hello'] is 4:
        value = raw_input("Bonjour, j'ai compris pour la quatrieme fois !!, je vous écoute")
    else:
        value = raw_input("Bonjour,")


    return ma_loop(value)

def pascompris(value=None):
    value = raw_input("Je n'ai pas compris, pouvez vous réessayer?")
    return ma_loop(value)

def tiao(value=None):
    print "Aurevoir et merci de votre visite!"


def tomate(value=None):
    value = raw_input("Super, je vous propose : un panini, une tomate mozarella")
    return ma_loop(value)

def panini(value=None):
    value = raw_input("Voilà la recette de la du Panini!")



hello()