import customtkinter as ctk


class TelaSucesso(ctk.CTkFrame):
    def __init__(self, parent, pontos=0, porcentagem=0):
        super().__init__(parent)

        self.configure(fg_color="#101010")


        titulo = ctk.CTkLabel(
            self,
            text="🎉 Verificação concluída!",
            font=("Arial", 35, "bold")
        )
        titulo.pack(pady=70)


        resultado = ctk.CTkLabel(
            self,
            text=f"Pontuação: {pontos}\nAproveitamento: {porcentagem}%",
            font=("Arial", 22)
        )
        resultado.pack(pady=30)


        if porcentagem >= 60:
            mensagem = "✅ Idade confirmada!"
        else:
            mensagem = "❌ Não foi possível confirmar."


        status = ctk.CTkLabel(
            self,
            text=mensagem,
            font=("Arial", 25, "bold")
        )
        status.pack(pady=30)


        botao = ctk.CTkButton(
            self,
            text="Fechar",
            width=200,
            height=45,
            command=parent.destroy
        )
        botao.pack(pady=40)
