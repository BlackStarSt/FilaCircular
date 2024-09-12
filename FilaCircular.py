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
            print("Fila vazia!")
        elif self.frente == self.atras:
            self.frente = self.atras = None
        else:
            self.frente = self.frente.proximo
            self.atras.proximo = self.frente

    def alterar(self, nome, novoNome, novoTel, novoIdade):
        atual = self.frente
        if self.vazia():
            print("Fila vazia!")
            return

        while True:
            if atual.aluno.nome == nome:
                atual.aluno.nome = novoNome
                atual.aluno.tel = novoTel
                atual.aluno.idade = novoIdade
                break
            atual = atual.proximo
            if atual == self.frente:
                print("Aluno não encontrado!")
                break

    def listar(self):
        if self.vazia():
            print("Fila vazia!")
            return

        atual = self.frente
        while True:
            print(f"Nome: {atual.aluno.nome}, Telefone: {atual.aluno.tel}, Idade: {atual.aluno.idade}")
            atual = atual.proximo
            if atual == self.frente:
                break

    def localizar(self, nome):
        if self.vazia():
            print("Fila vazia!")
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
                print(f"Nome: {aluno.nome}, Telefone: {aluno.tel}, Idade: {aluno.idade}")
        else:
            print("Nenhum aluno encontrado!")

    def inverter(self):
        if self.vazia() or self.frente == self.atras:
            print("Fila não precisa ser invertida!")
            return

        prev = self.atras
        current = self.frente
        start = self.frente

        while True:
            proximo_node = current.proximo
            current.proximo = prev
            prev = current
            current = proximo_node

            if current == start:
                break

        self.frente, self.atras = self.atras, self.frente
        self.atras.proximo = self.frente

# Teste da Fila Circular
fila = Fila()

# Inserindo alunos
fila.inserir(Aluno("João", "1111-1111", 20))
fila.inserir(Aluno("Maria", "2222-2222", 22))
fila.inserir(Aluno("Pedro", "3333-3333", 21))

# Listando alunos
print("Lista inicial de alunos:")
fila.listar()

# Localizando aluno pelo nome
print("\nLocalizando 'Maria':")
fila.localizar("Maria")

# Alterando aluno
print("\nAlterando 'João':")
fila.alterar("João", "João Silva", "4444-4444", 23)
fila.listar()

# Excluindo aluno
print("\nExcluindo primeiro aluno:")
fila.excluir()
fila.listar()

# Invertendo a fila
print("\nInvertendo a fila:")
fila.inverter()
fila.listar()