from .acessorio import *
from collections import Counter

def calcula_linhas(nomeFicheiro):
    return len(ler_texto(nomeFicheiro))


def calcula_carateres(nomeFicheiro):
    return len(ler_linhas(nomeFicheiro))


def calcula_palavra_comprida(nomeFicheiro):
    return max(ler_texto(nomeFicheiro).split(), key = len())

def calcula_ocorrencia_de_letras(nomeFicheiro):
    return Counter(ler_texto(nomeFicheiro).lower())