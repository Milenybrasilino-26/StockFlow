from app import create_app
from app.services.estoque_service import listar_produtos_estoque_baixo

app = create_app()

with app.app_context():

    produtos = listar_produtos_estoque_baixo()

    print("\nPRODUTOS COM ESTOQUE BAIXO\n")

    if not produtos:
        print("Nenhum produto precisa de reposição.")

    else:
        for produto in produtos:

            print(f"Produto: {produto.nome}")
            print(f"SKU: {produto.sku}")
            print(f"Estoque atual: {produto.quantidade}")
            print(f"Estoque mínimo: {produto.estoque_minimo}")

            print("-" * 35)