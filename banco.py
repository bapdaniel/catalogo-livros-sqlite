import sqlite3
from pathlib import Path


def conectar(caminho: str | Path = "catalogo.db") -> sqlite3.Connection:
    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    conexao.execute(
        """
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER CHECK (ano BETWEEN 0 AND 2100)
        )
        """
    )
    return conexao


def adicionar_livro(conexao: sqlite3.Connection, titulo: str, autor: str, ano: int) -> int:
    if not titulo.strip() or not autor.strip():
        raise ValueError("Título e autor são obrigatórios.")
    cursor = conexao.execute(
        "INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)",
        (titulo.strip(), autor.strip(), ano),
    )
    conexao.commit()
    return cursor.lastrowid


def listar_livros(conexao: sqlite3.Connection) -> list[sqlite3.Row]:
    return conexao.execute("SELECT * FROM livros ORDER BY titulo").fetchall()


def buscar_livros(conexao: sqlite3.Connection, termo: str) -> list[sqlite3.Row]:
    termo_busca = f"%{termo.strip()}%"
    return conexao.execute(
        "SELECT * FROM livros WHERE titulo LIKE ? OR autor LIKE ? ORDER BY titulo",
        (termo_busca, termo_busca),
    ).fetchall()
