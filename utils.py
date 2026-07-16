import os
from PIL import Image
import customtkinter as ctk


def centralizar_janela(janela, largura, altura):
    """
    Coloca a janela no centro da tela
    """

    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()

    x = int((tela_largura / 2) - (largura / 2))
    y = int((tela_altura / 2) - (altura / 2))

    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def arquivo_existe(caminho):
    """
    Verifica se um arquivo existe
    """
    return os.path.exists(caminho)


def carregar_imagem(caminho, tamanho):
    """
    Carrega imagens para o CustomTkinter
    """

    if arquivo_existe(caminho):
        imagem = Image.open(caminho)

        return ctk.CTkImage(
            light_image=imagem,
            dark_image=imagem,
            size=tamanho
        )

    return None


def calcular_porcentagem(acertos, total):
    """
    Calcula a porcentagem de acertos
    """

    if total == 0:
        return 0

    return int((acertos / total) * 100)


def limpar_texto(texto):
    """
    Remove espaços extras
    """

    return texto.strip()
