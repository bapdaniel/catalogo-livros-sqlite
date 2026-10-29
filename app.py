from banco import adicionar_livro, buscar_livros, conectar, listar_livros


def mostrar(livros) -> None:
    if not livros:
        print("Nenhum livro encontrado.")
        return
    for livro in livros:
        print(f'{livro["id"]}: {livro["titulo"]} — {livro["autor"]} ({livro["ano"]})')


def main() -> None:
    conexao = conectar()
    try:
        while True:
            print("\n1. Adicionar livro\n2. Listar livros\n3. Buscar\n0. Sair")
            opcao = input("Opção: ").strip()
            if opcao == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                try:
                    ano = int(input("Ano: "))
                    adicionar_livro(conexao, titulo, autor, ano)
                    print("Livro adicionado.")
                except (ValueError, TypeError) as erro:
                    print(f"Não foi possível cadastrar: {erro}")
            elif opcao == "2":
                mostrar(listar_livros(conexao))
            elif opcao == "3":
                mostrar(buscar_livros(conexao, input("Título ou autor: ")))
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")
    finally:
        conexao.close()


if __name__ == "__main__":
    main()
