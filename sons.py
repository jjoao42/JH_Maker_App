import winsound


def tocar_acerto():
    """
    Som de resposta correta.
    """
    try:
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
    except Exception:
        pass


def tocar_erro():
    """
    Som de resposta incorreta.
    """
    try:
        winsound.MessageBeep(winsound.MB_ICONHAND)
    except Exception:
        pass


def tocar_confirmacao():
    """
    Som de confirmação final.
    """
    try:
        winsound.MessageBeep(winsound.MB_OK)
    except Exception:
        pass


def tocar_alerta():
    """
    Som de alerta.
    """
    try:
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    except Exception:
        pass


def tocar_pergunta():
    """
    Som ao exibir uma nova pergunta.
    """
    try:
        winsound.Beep(800, 150)
    except Exception:
        pass
