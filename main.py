import customtkinter as ctk

# Configuração da aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class JHMakerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("JH Maker App")
        self.geometry("900x600")
        self.resizable(False, False)

        # Cor de fundo
        self.configure(fg_color="#101010")

        # Título
        self.titulo = ctk.CTkLabel(
            self,
            text="JH Maker App",
            font=("Arial", 40, "bold")
        )
        self.titulo.pack(pady=80)

        # Texto inicial
        self.texto = ctk.CTkLabel(
            self,
            text="Verificador de idade digital",
            font=("Arial", 20)
        )
        self.texto.pack(pady=20)

        # Botão iniciar
        self.botao = ctk.CTkButton(
            self,
            text="Começar",
            width=250,
            height=50,
            font=("Arial", 18),
            command=self.iniciar
        )
        self.botao.pack(pady=50)


    def iniciar(self):
        print("Iniciando verificação de idade...")


if __name__ == "__main__":
    app = JHMakerApp()
    app.mainloop()
