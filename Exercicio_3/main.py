import os
from os.path import join


def pede_pasta():
    verificacao = True
    while verificacao:
        print("insira o caminho para a pasta pretendida")
        pasta = input()
        if os.path.isdir(pasta):
            return pasta

def calcula_tamanho_pasta(pasta):
    tamanhoTotal = 0
    ficheiros = os.listdir(pasta)
    for ficheiro in ficheiros:
        if os.isfile(join(pasta, ficheiro)):
            tamanhoTotal += os.path.getsize(join(pasta, ficheiro))/1024

    return tamanhoTotal


def main():
    pasta = pede_pasta()
    print("O tamanho total das pastas e subpastas é" + calcula_tamanho_pasta(pasta))


if __name__ == "__main__":
  main()