class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def pegar_livro(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print(f"{self.nome} pegou o livro '{livro.titulo}'")
        else:
            print("Livro indisponível!")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print(f"{self.nome} devolveu o livro '{livro.titulo}'")


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros(self):
        print("\n📚 Lista de Livros:")
        for livro in self.livros:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"{livro.titulo} - {livro.autor} ({status})")


# ------------------ TESTANDO O SISTEMA ------------------

# Criando biblioteca
biblioteca = Biblioteca()

# Criando livros
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("1984", "George Orwell")

# Criando usuário
usuario1 = Usuario("João")

# Adicionando à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_usuario(usuario1)

# Usando o sistema
biblioteca.listar_livros()
usuario1.pegar_livro(livro1)
biblioteca.listar_livros()
usuario1.devolver_livro(livro1)
biblioteca.listar_livros()