from tkinter import *

from tkinter import ttk

from aluno import Aluno


class AlunoAppLista:

    # Titulo padrão da interface
    titulo = 'Lista de Alunos'

    # Fonte padrão dos elementos da interface
    font = ('Verdana', 12)

    width = 10

    anchor = W

    def __init__(self, master=None):

        # Armazenando em um atributo o container principal
        self.master = master

        self.master.title(AlunoAppLista.titulo)

        # Criação do frame central para apresentar em 
        # tela os componentes dentro do container principal
        # frame_master espaço vazio
        self.frame_master = Frame(self.master)
        self.frame_master.pack()

        # Apresentando o titulo da interface
        # Segmentando as areas da interfca utiziando o container
        # frame do titulo
        self.frame_titulo = Frame(
            self.frame_master
        )

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=AlunoAppLista.titulo,
            font=('Verdana', 20, 'bold')
        )

        self.label_titulo.pack()

        self.frame_lista = Frame(
            self.frame_master
        )

        self.frame_lista.pack()

        self.lista = ttk.Treeview(self.frame_lista, selectmode = "browse", columns = (
            "matricula", "nome", "cpf", "telefone", "email"), show = "headings")
        
        # Declarando as colunas
        # Criando o cabeçalho da lista
        # Stretch = arrastar o cabeçalho da tabela

        self.lista.column(
            "matricula",
            anchor = CENTER,
            width = 75,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#1",
            text = "Matricula"
        )

        self.lista.column(
            "nome",
            anchor = CENTER,
            width = 150,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#2",
            text = "Nome"
        )

        self.lista.column(
            "cpf",
            anchor = CENTER,
            width = 150,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#3",
            text = "CPF"
        )

        self.lista.column(
            "telefone",
            anchor = CENTER,
            width = 150,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#4",
            text = "telefone"
        )

        self.lista.column(
            "email",
            anchor = CENTER,
            width = 200,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#5",
            text = "E-mail"
        )


        # Apresentando a tabela
        self.lista.pack()

        self.listar()

    def listar (self):

        lista_alunos = Aluno.listar()

        for aluno in lista_alunos:

            # Fazendo o loop das linhas da tabela, 
            # com os dados vindos do banco de dados

            self.lista.insert(
                "",
                END,
                values = (
                    aluno[0],
                    aluno[1],
                    aluno[2],
                    aluno[3],
                    aluno[4]
                )
            )

if __name__ == '__main__':

    root = Tk()

    AlunoAppLista(root)

    root.mainloop()

    # print(Aluno.listar())