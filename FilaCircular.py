import tkinter as tk

class Aluno:
    def __init__(self, nome, tel, idade):
        self.nome = nome
        self.tel = tel
        self.idade = idade

class Node:
    def __init__(self, aluno):
        self.aluno = aluno
        self.proximo = None

class Fila:
    def __init__(self):
        self.frente = self.atras = None

    def vazia(self):
        return self.frente is None

    def inserir(self, aluno):
        novoNode = Node(aluno)
        if self.vazia():
            self.frente = self.atras = novoNode
            self.atras.proximo = self.frente
        else:
            self.atras.proximo = novoNode
            self.atras = novoNode
            self.atras.proximo = self.frente

    def excluir(self):
        if self.vazia():
            return 'Fila vazia!'
        elif self.frente == self.atras:
            self.frente = self.atras = None
            return 'Aluno removido e fila agora está vazia!'
        else:
            self.frente = self.frente.proximo
            self.atras.proximo = self.frente
            return 'Aluno removido!'

    def alterar(self, nome, novoNome, novoTel, novoIdade):
        atual = self.frente
        if self.vazia():
            return 'Fila vazia!'

        while True:
            if atual.aluno.nome == nome:
                atual.aluno.nome = novoNome
                atual.aluno.tel = novoTel
                atual.aluno.idade = novoIdade
                return f'Aluno {nome} alterado com sucesso para Nome: {novoNome}, Tel: {novoTel}, Idade: {novoIdade}.'
            atual = atual.proximo
            if atual == self.frente:
                return f'Aluno {nome} não encontrado!'

    def listar(self):
        if self.vazia():
            return 'Fila vazia!'

        alunos = []
        atual = self.frente
        while True:
            alunos.append(f'Nome: {atual.aluno.nome}, Tel: {atual.aluno.tel}, Idade: {atual.aluno.idade}')
            atual = atual.proximo
            if atual == self.frente:
                break
        return '\n'.join(alunos)    

    def localizar(self, nome):
        if self.vazia():
            print('Fila vazia!')
            return

        atual = self.frente
        encontrados = []
        while True:
            if atual.aluno.nome == nome:
                encontrados.append(atual.aluno)
            atual = atual.proximo
            if atual == self.frente:
                break

        if encontrados:
            for aluno in encontrados:
                print(f'Nome: {aluno.nome}, Telefone: {aluno.tel}, Idade: {aluno.idade}')
        else:
            print('Nenhum aluno encontrado!')

    def inverter(self):
        if self.vazia() or self.frente == self.atras:
            return 'Fila não precisa ser invertida!'

        antes = self.atras
        atual = self.frente
        inicio = self.frente

        while True:
            proximo_node = atual.proximo
            atual.proximo = antes
            antes = atual
            atual = proximo_node

            if atual == inicio:
                break

        self.frente, self.atras = self.atras, self.frente
        self.atras.proximo = self.frente
        return 'Fila invertida com sucesso!'

fila = Fila()

#Começo
root = tk.Tk()
root.title('Fila Circular')
root.geometry('460x380')

tk.Label(root, text='Nome').grid(row=1, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text='Telefone').grid(row=2, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text='Idade').grid(row=3, column=0, padx=10, pady=5, sticky='e')

inNome = tk.Entry(root, width=50)
inTel = tk.Entry(root, width=50)
inIdade = tk.Entry(root, width=50)

inNome.grid(row=1, column=1, padx=10, pady=5, sticky='w')
inTel.grid(row=2, column=1, padx=10, pady=5, sticky='w')
inIdade.grid(row=3, column=1, padx=10, pady=5, sticky='w')

btnDiv = tk.Frame(root)
btnDiv.grid(row=4, column=0, columnspan=2, pady=10)

def adicionar():
    nome = inNome.get()
    tel = inTel.get()
    idade = inIdade.get()

    fila.inserir(Aluno(nome, tel, idade))
    text.insert(tk.END, f'Aluno adicionado:\nNome: {nome},\nTel: {tel},\nIdade: {idade}\n')

def listar():
    text.insert(tk.END, f'Listando alunos: \n')
    text.insert(tk.END, fila.listar() + '\n')

def editar():
    nome = inNome.get()
    novoTel = inTel.get()
    novaIdade = inIdade.get()

    mensagem = fila.alterar(nome, novoTel=novoTel, novoIdade=novaIdade)
    text.insert(tk.END, mensagem + '\n')

def excluir():
    text.insert(tk.END, fila.excluir() + '\n')
    listar()

def inverter():
    fila.inverter()
    print('Fila invertida!')

btnTamanho = 10

tk.Button(btnDiv, text='Adicionar', command=adicionar, width=btnTamanho).grid(row=5, column=0, padx=5, pady=10)
tk.Button(btnDiv, text='Excluir', command=excluir, width=btnTamanho).grid(row=5, column=1, padx=5, pady=10)
tk.Button(btnDiv, text='Listar', command=listar, width=btnTamanho).grid(row=5, column=2, padx=5, pady=10)
tk.Button(btnDiv, text='Editar', command=editar, width=btnTamanho).grid(row=5, column=3, padx=5, pady=10)
tk.Button(btnDiv, text='Inverter fila', command=inverter, width=btnTamanho).grid(row=5, column=4, padx=5, pady=10)

text = tk.Text(root, height=10, width=50)
text.grid(row=6, column=0, padx=10, pady=10, columnspan=5)

#Final
root.mainloop()

# Inserindo
fila.inserir(Aluno('Pedro', '3333-3333', 21))
fila.inserir(Aluno('João Silva', '4444-4444', 23))