import customtkinter as ctk
from perguntas import TelaPerguntas


class TelaInicial(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.configure(
            fg_color="#202124"
        )

        # ==========================
        # TÍTULO
        # ==========================

        self.logo = ctk.CTkLabel(
            self,
            text="🛡️ JH Maker",
            font=("Segoe UI", 30, "bold")
        )

        self.logo.pack(
            pady=(30, 5)
        )

        self.subtitulo = ctk.CTkLabel(
            self,
            text="Confirmação Inteligente de Idade",
            font=("Segoe UI", 16)
        )

        self.subtitulo.pack()

        # ==========================
        # CARD
        # ==========================

        self.card = ctk.CTkFrame(
            self,
            width=360,
            height=560,
            corner_radius=25
        )

        self.card.pack(
            pady=25
        )

        self.card.pack_propagate(False)

        # ==========================
        # NOME
        # ==========================

        self.lbl_nome = ctk.CTkLabel(
            self.card,
            text="Nome"
        )

        self.lbl_nome.pack(
            pady=(25, 5)
        )

        self.nome = ctk.CTkEntry(
            self.card,
            width=290,
            height=42,
            placeholder_text="Digite seu nome"
        )

        self.nome.pack()

        # ==========================
        # IDADE
        # ==========================

        self.lbl_idade = ctk.CTkLabel(
            self.card,
            text="Idade"
        )

        self.lbl_idade.pack(
            pady=(20, 5)
        )

        self.idade = ctk.CTkEntry(
            self.card,
            width=290,
            height=42,
            placeholder_text="Digite sua idade"
        )

        self.idade.pack()

        # ==========================
        # PESO
        # ==========================

        self.lbl_peso = ctk.CTkLabel(
            self.card,
            text="Peso (Kg)"
        )

        self.lbl_peso.pack(
            pady=(20, 5)
        )

        self.peso = ctk.CTkEntry(
            self.card,
            width=290,
            height=42,
            placeholder_text="Digite seu peso"
        )

        self.peso.pack()

        # ==========================
        # BARRA
        # ==========================

        self.barra = ctk.CTkProgressBar(
            self.card,
            width=290,
            height=12
        )

        self.barra.pack(
            pady=30
        )

        self.barra.set(0)

        # ==========================
        # STATUS
        # ==========================

        self.status = ctk.CTkLabel(
            self.card,
            text="Preencha seus dados para continuar.",
            font=("Segoe UI", 13)
        )

        self.status.pack()

        # ==========================
        # BOTÃO
        # ==========================

        self.botao = ctk.CTkButton(
            self.card,
            text="CONTINUAR",
            width=250,
            height=48,
            corner_radius=15,
            font=("Segoe UI", 16, "bold"),
            command=self.continuar
        )

        self.botao.pack(
            pady=35
        )

        # ==========================
        # RODAPÉ
        # ==========================

        self.rodape = ctk.CTkLabel(
            self,
            text="© JH Maker 2026",
            font=("Segoe UI", 12)
        )

        self.rodape.pack(
            side="bottom",
            pady=15
        )


    # ==========================
    # CONTINUAR
    # ==========================

    def continuar(self):

        nome = self.nome.get().strip()
        idade = self.idade.get().strip()
        peso = self.peso.get().strip()

        # --------------------------
        # Verificar campos vazios
        # --------------------------

        if nome == "":
            self.status.configure(
                text="⚠️ Digite seu nome."
            )
            return

        if idade == "":
            self.status.configure(
                text="⚠️ Digite sua idade."
            )
            return

        if peso == "":
            self.status.configure(
                text="⚠️ Digite seu peso."
            )
            return

        # --------------------------
        # Converter números
        # --------------------------

        try:

            idade = int(idade)
            peso = float(peso)

        except ValueError:

            self.status.configure(
                text="⚠️ Idade ou peso inválidos."
            )

            return

        # --------------------------
        # Animação da barra
        # --------------------------

        self.status.configure(
            text="Verificando informações..."
        )

        self.barra.set(0)

        self.after(150, lambda: self.barra.set(0.20))
        self.after(300, lambda: self.barra.set(0.40))
        self.after(450, lambda: self.barra.set(0.60))
        self.after(600, lambda: self.barra.set(0.80))
        self.after(750, lambda: self.barra.set(1.00))

        self.after(
            900,
            lambda: self.status.configure(
                text="✅ Dados confirmados!"
            )
        )

        # --------------------------
        # Abrir perguntas
        # --------------------------

        self.after(
            1300,
            lambda: self.abrir_perguntas(
                nome,
                idade,
                peso
            )
        )



    # ==========================
    # ABRIR PERGUNTAS
    # ==========================

    def abrir_perguntas(self, nome, idade, peso):

        self.status.configure(
            text="Abrindo perguntas..."
        )

        self.barra.set(1)

        # Remove a tela inicial
        self.destroy()

        # Cria a tela de perguntas
        tela = TelaPerguntas(
            self.master,
            nome,
            idade,
            peso
        )

        # Exibe a nova tela
        tela.pack(
            fill="both",
            expand=True
        )


    # ==========================
    # LIMPAR CAMPOS
    # ==========================

    def limpar_campos(self):

        self.nome.delete(0, "end")
        self.idade.delete(0, "end")
        self.peso.delete(0, "end")

        self.barra.set(0)

        self.status.configure(
            text="Preencha seus dados para continuar."
        )

    # ==========================
    # RESETAR TELA
    # ==========================

    def resetar(self):

        self.limpar_campos()

        self.nome.focus()

    # ==========================
    # FECHAR APLICAÇÃO
    # ==========================

    def fechar(self):

        self.master.destroy()


    # ==========================
    # ANIMAÇÃO DE ENTRADA
    # ==========================

    def animar_entrada(self):
        self.barra.set(0)
        self.status.configure(
            text="Bem-vindo ao JH Maker!"
        )

    # ==========================
    # ATUALIZAR STATUS
    # ==========================

    def atualizar_status(self, texto):
        self.status.configure(text=texto)
