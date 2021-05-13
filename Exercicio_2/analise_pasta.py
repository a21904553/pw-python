import csv
import os
from os import *
from os.path import join
from matplotlib import pyplot as plt


def pede_pasta():
    verificacao = True
    while verificacao:
        print("insira o caminho para a pasta pretendida")
        if os.path.isdir(input):
            return input()

def faz_calculos(caminho):
    dic_info = {}
    ficheiros = os.listdir(caminho)
    for ficheiro in ficheiros:
        if os.isfile(join(caminho, ficheiro)):
            tipo = os.path.splittext(ficheiro)
            if tipo[1] in dic_info:
                dic_info[tipo[1]]["volume"] += os.path.getsize(join(caminho, ficheiro))/1024
                dic_info[tipo[1]]["quantidade"] += 1
            else:
                dic_info[tipo[1]] = {}
                dic_info[tipo[1]]["volume"] = os.path.getsize(join(caminho, ficheiro))/1024
                dic_info[tipo[1]]["quantidade"] = 1

    return dic_info

def guarda_resultados(dicionario, caminho):
        nome = os.path.basename(caminho) + ".csv"
        ficheiro = open(nome, 'w', newline='')
        campos = ["Extensao", "Quantidade", "Tamanho[kByte]"]
        escrita = csv.DictWriter(ficheiro, campos)
        escrita.writeheader()
        for extencao in dicionario:
            novaLinha = [extencao, str(dicionario[extencao]["quantidade"]), str(dicionario[extencao]["volume"])]
            escrita = csv.DictWriter(ficheiro, novaLinha)
            escrita.writeheader()
        print(f"Os Resultados Foram Guardados No Ficheiro: ´{nome}`")

def faz_grafico_queijos(dicionario):
    lista_chaves = []
    lista_valores = []
    for tamanho in dicionario:
        lista_chaves.append(tamanho)
        lista_valores.append(dicionario[tamanho]["volume"])

    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title("Tipos de ficheiros")
    plt.show()

def faz_grafico_barras(dicionario):
    lista_chaves = []
    lista_valores = []
    for tamanho in dicionario:
        lista_chaves.append(tamanho)
        lista_valores.append(dicionario[tamanho]["quantidade"])

    plt.bar(lista_chaves, lista_valores)
    plt.title("Tipos de ficheiros")
    plt.show()