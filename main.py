import customtkinter as ctk

from telas import TelaInicial


# ============================================
# Configurações do aplicativo
# ============================================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # -----------------------------
        # Janela
        # -----------------------------

        self.title("JH Maker")

        largura = 420
        altura = 780

        self.geometry(f"{largura}x{altura}")
        self.minsize(largura, altura)
        self.maxsize(largura, altura)

        self.resizable(False, False)

        # Centralizar a janela

        self.update_idletasks()

        x = (self.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.winfo_screenheight() // 2) - (altura // 2)

        self.geometry(f"{largura}x{altura}+{x}+{y}")

        # Cor de fundo

        self.configure(fg_color="#202124")

        # -----------------------------
        # Tela Atual
        # -----------------------------

        self.tela_atual = None

        self.abrir_tela(TelaInicial)

    # ============================================
    # Trocar de tela
    # ============================================

    def abrir_tela(self, tela, *args):

        if self.tela_atual is not None:
            self.tela_atual.destroy()

        self.tela_atual = tela(self, *args)
        self.tela_atual.pack(fill="both", expand=True)


# ============================================
# Iniciar
# ============================================

if __name__ == "__main__":

    app = App()
    app.mainloop()
