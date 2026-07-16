import customtkinter as ctk

from telas import TelaInicial, TelaPergunta
from sucesso import TelaSucesso
from perguntas import perguntas, verificar_resposta
from utils import centralizar_janela, calcular_porcentagem
import config


class JHMakerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(config.NOME_APP)
        centralizar_janela(
            self,
            config.LARGURA,
            config.ALTURA
        )

        self.resizable(False, False)

        self.tela_atual = None

        self.pergunta_atual = 0
        self.acertos = 0

        self.mostrar_tela_inicial()


    def trocar_tela(self, nova_tela):

        if self.tela_atual:
            self.tela_atual.destroy()

        self.tela_atual = nova_tela
        self.tela_atual.pack(
            fill="both",
            expand=True
        )


    def mostrar_tela_inicial(self):

        tela = TelaInicial(
            self,
            self.iniciar_teste
        )

        self.trocar_tela(tela)


    def iniciar_teste(self):

        self.pergunta_atual = 0
        self.acertos = 0

        self.mostrar_pergunta()


    def mostrar_pergunta(self):

        if self.pergunta_atual < len(perguntas):

            tela = TelaPergunta(self)

            dados = perguntas[self.pergunta_atual]

            tela.titulo.configure(
                text=f"Pergunta {self.pergunta_atual + 1}"
            )

            tela.pergunta.configure(
                text=dados["pergunta"]
            )

            tela.botao.configure(
                command=lambda: self.verificar(
                    tela
                )
            )

            self.trocar_tela(tela)

        else:
            self.finalizar()


    def verificar(self, tela):

        resposta = tela.resposta.get()

        if verificar_resposta(
            self.pergunta_atual,
            resposta
        ):
            self.acertos += 1


        self.pergunta_atual += 1

        self.mostrar_pergunta()


    def finalizar(self):

        porcentagem = calcular_porcentagem(
            self.acertos,
            len(perguntas)
        )

        tela = TelaSucesso(
            self,
            self.acertos,
            porcentagem
        )

        self.trocar_tela(tela)



if __name__ == "__main__":

    app = JHMakerApp()
    app.mainloop()
