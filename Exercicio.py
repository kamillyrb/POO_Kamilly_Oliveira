# Exceções
class LimiteEmprestimosExcedido(Exception):
    pass

class LivroIndisponivel(Exception):
    pass


# Classe Livro
class Livro:
    def __init__(self, isbn, titulo, autor, disponivel=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True


# Classe Usuario
class Usuario:
    def __init__(self, matricula, nome, limite):
        self.matricula = matricula
        self.nome = nome
        self.livros_emprestados = []
        self.limite = limite

    def pegar_emprestado(self, livro):
        if len(self.livros_emprestados) >= self.limite:
            raise LimiteEmprestimosExcedido("Limite de livros atingido")

        if not livro.disponivel:
            raise LivroIndisponivel("Livro não está disponível")

        livro.emprestar()
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)


# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.acervo = []
        self.usuarios = []

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def registrar_emprestimo(self, matricula, isbn):
        usuario = None
        livro = None

        for u in self.usuarios:
            if u.matricula == matricula:
                usuario = u

        for l in self.acervo:
            if l.isbn == isbn:
                livro = l

        if usuario and livro:
            usuario.pegar_emprestado(livro)

    def consultar_livros_emprestados(self):
        for usuario in self.usuarios:
            print("Usuário:", usuario.nome)
            if len(usuario.livros_emprestados) == 0:
                print("Nenhum livro emprestado")
            else:
                for livro in usuario.livros_emprestados:
                    print("-", livro.titulo)
            print()


# --------------------------
# Testando o sistema
# --------------------------

biblioteca = Biblioteca()

# Livros com nomes aleatórios
biblioteca.acervo.append(Livro("LIV001", "Redes e Café", "Marcos Silva"))
biblioteca.acervo.append(Livro("LIV002", "Algoritmos do Dia a Dia", "Carla Souza"))
biblioteca.acervo.append(Livro("LIV003", "Programando sem Stress", "Rafael Lima"))
biblioteca.acervo.append(Livro("LIV004", "Histórias da Tecnologia", "Bruna Alves"))
biblioteca.acervo.append(Livro("LIV005", "Python para Curiosos", "Daniel Rocha"))

# Usuários
babs = Usuario("ALUNO01", "Babs", 3)
kams = Usuario("ALUNO02", "Kams", 3)
gabs = Usuario("PROF01", "Gabs", 5)

biblioteca.cadastrar_usuario(babs)
biblioteca.cadastrar_usuario(kams)
biblioteca.cadastrar_usuario(gabs)

# Empréstimos
biblioteca.registrar_emprestimo("ALUNO01", "LIV001")
biblioteca.registrar_emprestimo("ALUNO02", "LIV003")
biblioteca.registrar_emprestimo("PROF01", "LIV004")

# Mostrar resultado
biblioteca.consultar_livros_emprestados()