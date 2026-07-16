import os
import pygame


# Inicializa o sistema de áudio
pygame.mixer.init()


def tocar_som(nome):
    """
    Toca um som dentro da pasta assets/sons
    """

    caminho = os.path.join(
        "assets",
        "sons",
        nome
    )

    if os.path.exists(caminho):
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play()
    else:
        print("Som não encontrado:", caminho)


def som_acerto():
    tocar_som("acerto.wav")


def som_erro():
    tocar_som("erro.wav")


def som_clique():
    tocar_som("clique.wav")


def som_final():
    tocar_som("final.wav")
