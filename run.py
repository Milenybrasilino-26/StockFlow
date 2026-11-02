from app import create_app

# Instanciamos a aplicação chamando a função Factory
app = create_app()

if __name__ == "__main__":
    # O modo debug=True recarrega o servidor automaticamente a cada alteração no código
    app.run(debug=True)