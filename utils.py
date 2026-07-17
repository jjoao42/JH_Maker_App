import customtkinter as ctk


def centralizar_janela(janela, largura=420, altura=780):
    """
    Centraliza a janela na tela.
    """

    janela.update_idletasks()

    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)

    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def limpar_entry(entry):
    """
    Limpa um CTkEntry.
    """

    entry.delete(0, "end")


def definir_status(label, texto):
    """
    Altera o texto de um CTkLabel.
    """

    label.configure(text=texto)


def atualizar_barra(barra, valor):
    """
    Atualiza a barra de progresso.
    """

    barra.set(valor)


def bloquear_botao(botao):
    """
    Desativa um botão.
    """

    botao.configure(state="disabled")


def desbloquear_botao(botao):
    """
    Ativa um botão.
    """

    botao.configure(state="normal")


def bloquear_entry(entry):
    """
    Desativa um campo de texto.
    """

    entry.configure(state="disabled")


def desbloquear_entry(entry):
    """
    Ativa um campo de texto.
    """

    entry.configure(state="normal")
