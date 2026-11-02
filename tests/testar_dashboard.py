from app import create_app
from app.services.dashboard_service import obter_indicadores_estoque

app = create_app()

with app.app_context():

    indicadores = obter_indicadores_estoque()

    print("\nINDICADORES DO STOCKFLOW")
    print("-" * 35)

    print(
        f"Produtos ativos: "
        f"{indicadores['total_produtos']}"
    )

    print(
        f"Unidades disponíveis: "
        f"{indicadores['total_unidades']}"
    )

    print(
        f"Produtos com estoque baixo: "
        f"{indicadores['produtos_estoque_baixo']}"
    )

    valor = indicadores["valor_estoque_centavos"] / 100

    print(
        f"Valor estimado do estoque: "
        f"R$ {valor:,.2f}".replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )