from app import create_app
from app.models import Produto

app = create_app()

with app.app_context():

    produtos = Produto.query.all()

    for produto in produtos:

        print("-" * 35)
        print(f"SKU: {produto.sku}")
        print(f"Nome: {produto.nome}")
        print(f"Quantidade: {produto.quantidade}")
        print(f"Preço de custo: R$ {produto.preco_custo_centavos / 100:.2f}")
        print(f"Preço de venda: R$ {produto.preco_venda_centavos / 100:.2f}")