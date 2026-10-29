import unittest

from banco import adicionar_livro, buscar_livros, conectar, listar_livros


class BancoTest(unittest.TestCase):
    def setUp(self):
        self.conexao = conectar(":memory:")

    def tearDown(self):
        self.conexao.close()

    def test_adiciona_e_lista(self):
        adicionar_livro(self.conexao, "Dom Casmurro", "Machado de Assis", 1899)
        livros = listar_livros(self.conexao)
        self.assertEqual(len(livros), 1)
        self.assertEqual(livros[0]["autor"], "Machado de Assis")

    def test_busca_por_autor(self):
        adicionar_livro(self.conexao, "O Alienista", "Machado de Assis", 1882)
        self.assertEqual(len(buscar_livros(self.conexao, "Machado")), 1)


if __name__ == "__main__":
    unittest.main()
