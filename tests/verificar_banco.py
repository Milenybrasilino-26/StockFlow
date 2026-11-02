from app import create_app, db
from sqlalchemy import inspect

app = create_app()

with app.app_context():

    inspector = inspect(db.engine)

    tabelas = inspector.get_table_names()

    print("\nTABELAS ENCONTRADAS NO BANCO:\n")

    for tabela in tabelas:
        print(f"- {tabela}")

    print("\nVerificação concluída!")