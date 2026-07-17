import customtkinter as ctk
from datetime import datetime
from sons import tocar_acerto, tocar_erro, tocar_confirmacao


class TelaPerguntas(ctk.CTkFrame):

    def __init__(self, master, nome, idade, peso):
        super().__init__(master)

        self.master = master
        self.nome = nome
        self.idade = idade
        self.peso = peso

        self.configure(fg_color="#202124")

        # ==========================
        # TÍTULO
        # ==========================

        self.titulo = ctk.CTkLabel(
            self,
            text="🧠 Confirmação de Idade",
            font=("Segoe UI", 28, "bold")
        )
        self.titulo.pack(pady=(25, 5))

        self.subtitulo = ctk.CTkLabel(
            self,
            text=f"Olá, {self.nome}!",
            font=("Segoe UI", 16)
        )
        self.subtitulo.pack()

        # ==========================
        # CARD
        # ==========================

        self.card = ctk.CTkFrame(
            self,
            width=360,
            height=520,
            corner_radius=25
        )

        self.card.pack(pady=30)
        self.card.pack_propagate(False)

        # ==========================
        # BARRA
        # ==========================

        self.barra = ctk.CTkProgressBar(
            self.card,
            width=280,
            height=12
        )

        self.barra.pack(pady=(25, 20))
        self.barra.set(0)

        # ==========================
        # PERGUNTA
        # ==========================

        self.lbl_pergunta = ctk.CTkLabel(
            self.card,
            text="",
            wraplength=300,
            font=("Segoe UI", 18, "bold")
        )

        self.lbl_pergunta.pack(pady=20)

        # ==========================
        # RESPOSTA
        # ==========================

        self.resposta = ctk.CTkEntry(
            self.card,
            width=250,
            height=40,
            placeholder_text="Digite sua resposta"
        )

        self.resposta.pack()

        # ==========================
        # STATUS
        # ==========================

        self.status = ctk.CTkLabel(
            self.card,
            text=""
        )

        self.status.pack(pady=15)

        # ==========================
        # BOTÃO
        # ==========================

        self.botao = ctk.CTkButton(
            self.card,
            text="CONFIRMAR",
            width=220,
            height=45,
            command=self.verificar
        )

        self.botao.pack(pady=20)

        # Índice da pergunta
        self.indice = 0

        # Carregar perguntas
        self.carregar_perguntas()


    # ==========================
    # CARREGAR PERGUNTAS
    # ==========================

    def carregar_perguntas(self):

        if self.idade == 6:

            self.perguntas = [
                ("Quanto é 2 + 2?", "4")
            ]

        elif self.idade == 7:

            self.perguntas = [
                ("Quanto é 5 + 3?", "8")
            ]

        elif self.idade == 8:

            self.perguntas = [
                ("Quanto é 9 - 4?", "5")
            ]

        elif self.idade == 9:

            self.perguntas = [
                ("Quanto é 6 × 7?", "42")
            ]

        elif self.idade == 10:

            self.perguntas = [
                ("Quanto é 32 × 2?", "64"),
                ("Quanto é 96 ÷ 3?", "32")
            ]

        elif self.idade == 11:

            self.perguntas = [
                ("Quanto é a raiz quadrada de 81?", "9"),
                ("Quanto é 12 × 12?", "144")
            ]

        elif self.idade == 12:

            self.perguntas = [
                ("Quanto é a raiz quadrada de 169?", "13"),
                ("Quanto é 15²?", "225")
            ]

        elif self.idade == 13:

            self.perguntas = [
                ("Quanto é 2³?", "8"),
                ("Quanto é a raiz quadrada de 225?", "15")
            ]

        elif self.idade == 14:

            self.perguntas = [
                ("Quanto é 7³?", "343"),
                ("Quanto é a raiz quadrada de 400?", "20")
            ]

        elif self.idade >= 18:

            self.pergunta_maior()

            return

        else:

            self.perguntas = []

            self.lbl_pergunta.configure(
                text="Ainda não existem perguntas para essa idade."
            )

            self.botao.configure(
                state="disabled"
            )

            return

        self.lbl_pergunta.configure(
            text=self.perguntas[0][0]
        )

        self.barra.set(0)


    # ==========================
    # MAIOR DE IDADE
    # ==========================

    def pergunta_maior(self):

        self.lbl_pergunta.configure(
            text="Confirme sua data de nascimento"
        )

        self.resposta.destroy()

        self.dia = ctk.CTkEntry(
            self.card,
            width=120,
            height=40,
            placeholder_text="Dia"
        )
        self.dia.pack(pady=5)

        self.mes = ctk.CTkEntry(
            self.card,
            width=120,
            height=40,
            placeholder_text="Mês"
        )
        self.mes.pack(pady=5)

        self.ano = ctk.CTkEntry(
            self.card,
            width=120,
            height=40,
            placeholder_text="Ano"
        )
        self.ano.pack(pady=5)

        self.status.configure(
            text="Digite sua data de nascimento."
        )

        self.barra.set(0.5)

    # ==========================
    # CONFIRMAR MAIOR DE IDADE
    # ==========================

    def verificar_maior(self):

        try:

            dia = int(self.dia.get())
            mes = int(self.mes.get())
            ano = int(self.ano.get())

            hoje = datetime.now()

            idade_calculada = hoje.year - ano

            if (hoje.month, hoje.day) < (mes, dia):
                idade_calculada -= 1

            if idade_calculada == self.idade:

                tocar_confirmacao()

                self.barra.set(1)

                self.status.configure(
                    text=f"✅ Parabéns {self.nome}!\nSua idade foi confirmada."
                )

                self.botao.configure(
                    state="disabled"
                )

            else:

                tocar_erro()

                self.status.configure(
                    text="❌ A idade informada não corresponde."
                )

        except ValueError:

            self.status.configure(
                text="⚠️ Digite uma data válida."
            )


    # ==========================
    # VERIFICAR RESPOSTA
    # ==========================

    def verificar(self):

        # --------------------------
        # Maior de idade
        # --------------------------

        if self.idade >= 18:
            self.verificar_maior()
            return

        resposta = self.resposta.get().strip()

        correta = self.perguntas[self.indice][1]

        if resposta == correta:

            tocar_acerto()

            self.indice += 1

            progresso = self.indice / len(self.perguntas)
            self.barra.set(progresso)

            if self.indice >= len(self.perguntas):

                self.status.configure(
                    text=f"✅ Parabéns {self.nome}!\n"
                         f"Sua idade foi confirmada.\n"
                         f"Peso: {self.peso} Kg."
                )

                self.botao.configure(
                    state="disabled"
                )

                self.resposta.configure(
                    state="disabled"
                )

                return

            self.resposta.delete(0, "end")

            self.lbl_pergunta.configure(
                text=self.perguntas[self.indice][0]
            )

            self.status.configure(
                text="✅ Correto! Continue..."
            )

        else:

            tocar_erro()

            self.status.configure(
                text="❌ Resposta incorreta."
            )

            self.resposta.delete(0, "end")

            self.resposta.focus()


    # ==========================
    # REINICIAR
    # ==========================

    def reiniciar(self):

        self.destroy()

        from telas import TelaInicial

        tela = TelaInicial(self.master)
        tela.pack(fill="both", expand=True)

    # ==========================
    # LIMPAR CAMPO
    # ==========================

    def limpar_resposta(self):

        if self.idade < 18:
            self.resposta.delete(0, "end")
            self.resposta.focus()

    # ==========================
    # FECHAR
    # ==========================

    def fechar(self):

        self.master.destroy()

    # ==========================
    # MENSAGEM FINAL
    # ==========================

    def finalizar(self):

        tocar_confirmacao()

        self.lbl_pergunta.configure(
            text="🎉 Verificação concluída!"
        )

        self.status.configure(
            text=(
                f"Nome: {self.nome}\n"
                f"Idade: {self.idade} anos\n"
                f"Peso: {self.peso} Kg\n\n"
                "Obrigado por utilizar o\n"
                "JH Maker!"
            )
        )

        self.botao.configure(
            text="FECHAR",
            command=self.fechar
        )

        if self.idade < 18:
            self.resposta.configure(state="disabled")
