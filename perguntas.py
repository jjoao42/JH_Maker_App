# Banco de perguntas do JH Maker App

perguntas = [
    {
        "pergunta": "Quanto é 5 + 7?",
        "resposta": "12"
    },
    {
        "pergunta": "Quanto é 10 × 3?",
        "resposta": "30"
    },
    {
        "pergunta": "Quanto é 50 - 18?",
        "resposta": "32"
    },
    {
        "pergunta": "Quanto é 8 × 8?",
        "resposta": "64"
    },
    {
        "pergunta": "Quanto é 100 ÷ 4?",
        "resposta": "25"
    }
]


def pegar_pergunta(numero):
    """
    Retorna uma pergunta pelo número
    """
    if numero < len(perguntas):
        return perguntas[numero]

    return None


def verificar_resposta(numero, resposta_usuario):
    """
    Verifica se a resposta está correta
    """
    pergunta = pegar_pergunta(numero)

    if pergunta:
        return resposta_usuario.strip() == pergunta["resposta"]

    return False
