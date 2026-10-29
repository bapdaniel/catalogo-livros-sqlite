import unittest

from banco import (
    adicionar_livro,
    atualizar_livro,
    buscar_livros,
    conectar,
    listar_livros,
    remover_livro,
)


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

    def test_atualiza_livro(self):
        livro_id = adicionar_livro(self.conexao, "Titulo antigo", "Autor", 2000)
        self.assertTrue(atualizar_livro(self.conexao, livro_id, "Título novo", "Autor", 2001))
        self.assertEqual(listar_livros(self.conexao)[0]["titulo"], "Título novo")

    def test_remove_livro(self):
        livro_id = adicionar_livro(self.conexao, "Livro", "Autor", 2020)
        self.assertTrue(remover_livro(self.conexao, livro_id))
        self.assertEqual(listar_livros(self.conexao), [])


if __name__ == "__main__":
    unittest.main()

