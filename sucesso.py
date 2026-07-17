import customtkinter as ctk


class TelaSucesso(ctk.CTkFrame):

    def __init__(self, master, nome, idade, peso):
        super().__init__(master)

        self.master = master

        self.configure(fg_color="#202124")

        # ==========================
        # TÍTULO
        # ==========================

        ctk.CTkLabel(
            self,
            text="🎉 JH Maker",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=(35, 10))

        ctk.CTkLabel(
            self,
            text="Confirmação concluída!",
            font=("Segoe UI", 18)
        ).pack()

        # ==========================
        # CARD
        # ==========================

        card = ctk.CTkFrame(
            self,
            width=350,
            height=420,
            corner_radius=25
        )

        card.pack(pady=35)
        card.pack_propagate(False)

        # ==========================
        # ÍCONE
        # ==========================

        ctk.CTkLabel(
            card,
            text="✅",
            font=("Segoe UI", 70)
        ).pack(pady=(25, 10))

        # ==========================
        # DADOS
        # ==========================

        ctk.CTkLabel(
            card,
            text=f"Nome: {nome}",
            font=("Segoe UI", 18)
        ).pack(pady=8)

        ctk.CTkLabel(
            card,
            text=f"Idade: {idade} anos",
            font=("Segoe UI", 18)
        ).pack(pady=8)

        ctk.CTkLabel(
            card,
            text=f"Peso: {peso} Kg",
            font=("Segoe UI", 18)
        ).pack(pady=8)

        ctk.CTkLabel(
            card,
            text="✔ Dados confirmados com sucesso!",
            font=("Segoe UI", 16, "bold"),
            text_color="#00C853"
        ).pack(pady=20)

        # ==========================
        # BOTÃO VOLTAR
        # ==========================

        ctk.CTkButton(
            card,
            text="🔄 Voltar ao início",
            width=240,
            height=45,
            command=self.voltar
        ).pack(pady=10)

        # ==========================
        # BOTÃO FECHAR
        # ==========================

        ctk.CTkButton(
            card,
            text="❌ Fechar",
            width=240,
            height=45,
            fg_color="#C62828",
            hover_color="#B71C1C",
            command=self.master.destroy
        ).pack(pady=10)

        # ==========================
        # RODAPÉ
        # ==========================

        ctk.CTkLabel(
            self,
            text="© JH Maker 2026",
            font=("Segoe UI", 12)
        ).pack(side="bottom", pady=15)

    # ==========================
    # VOLTAR
    # ==========================

    def voltar(self):

        from telas import TelaInicial

        self.destroy()

        TelaInicial(self.master).pack(
            fill="both",
            expand=True
        )
