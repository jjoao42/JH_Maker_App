import customtkinter as ctk


class TelaInicial(ctk.CTkFrame):
    def __init__(self, parent, iniciar_callback):
        super().__init__(parent)

        self.configure(fg_color="#101010")

        titulo = ctk.CTkLabel(
            self,
            text="JH Maker App",
            font=("Arial", 40, "bold")
        )
        titulo.pack(pady=80)

        texto = ctk.CTkLabel(
            self,
            text="Verificador de idade digital",
            font=("Arial", 20)
        )
        texto.pack(pady=20)

        botao = ctk.CTkButton(
            self,
            text="Começar",
            width=250,
            height=50,
            font=("Arial", 18),
            command=iniciar_callback
        )
        botao.pack(pady=50)


class TelaPergunta(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#101010")

        self.titulo = ctk.CTkLabel(
            self,
            text="Pergunta 1",
            font=("Arial", 30, "bold")
        )
        self.titulo.pack(pady=50)

        self.pergunta = ctk.CTkLabel(
            self,
            text="Carregando pergunta...",
            font=("Arial", 20)
        )
        self.pergunta.pack(pady=30)

        self.resposta = ctk.CTkEntry(
            self,
            width=300,
            height=40,
            placeholder_text="Digite sua resposta"
        )
        self.resposta.pack(pady=20)

        self.botao = ctk.CTkButton(
            self,
            text="Responder"
        )
        self.botao.pack(pady=30)


class TelaFinal(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(fg_color="#101010")

        titulo = ctk.CTkLabel(
            self,
            text="Parabéns! 🎉",
            font=("Arial", 40, "bold")
        )
        titulo.pack(pady=100)

        texto = ctk.CTkLabel(
            self,
            text="Verificação concluída.",
            font=("Arial", 20)
        )
        texto.pack()
