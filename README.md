# StockFlow — Sistema de Gerenciamento de Estoque

O **StockFlow** é uma aplicação web desenvolvida para auxiliar pequenas e médias empresas no gerenciamento de seus estoques, permitindo organizar produtos, acompanhar movimentações e consultar informações importantes para o controle operacional.

O projeto está sendo desenvolvido como parte da minha evolução prática em programação e Ciência de Dados, aplicando conceitos de desenvolvimento web, banco de dados, organização de código e regras de negócio.

## Objetivo do projeto

Desenvolver um sistema que facilite o controle de estoque, reduza processos manuais e centralize informações sobre produtos e movimentações.

## Tecnologias utilizadas

- **Python:** linguagem principal.
- **Flask:** desenvolvimento da aplicação web.
- **Flask-SQLAlchemy:** integração com o banco de dados.
- **SQLite:** armazenamento dos dados.
- **Flask-Migrate:** gerenciamento das migrações do banco.
- **Flask-WTF e WTForms:** criação e validação de formulários.
- **HTML:** estrutura das páginas.
- **CSS:** estilização da interface.
- **Pandas e OpenPyXL:** ferramentas previstas para relatórios e exportações.
- **Pytest:** ferramenta prevista para testes automatizados.
- **Git e GitHub:** controle de versão e hospedagem do código.

## Funcionalidades

### Implementadas

- [x] Estrutura inicial da aplicação Flask.
- [x] Modelagem e criação do banco de dados.
- [x] Cadastro de categorias e fornecedores para testes.
- [x] Cadastro de produtos pela interface web.
- [x] Listagem de produtos cadastrados.
- [x] Relacionamento entre produtos, categorias e fornecedores.
- [x] Registro de entradas e saídas de estoque por serviço.
- [x] Validação para impedir saídas superiores ao estoque disponível.
- [x] Consulta de movimentações.
- [x] Identificação de produtos com estoque baixo.
- [x] Indicadores de estoque no dashboard.

### Em desenvolvimento

- [ ] Edição de produtos.
- [ ] Inativação de produtos.
- [ ] Pesquisa e filtros de produtos.
- [ ] Registro de entradas e saídas pela interface.
- [ ] Histórico de movimentações pela interface.
- [ ] Indicadores completos no dashboard.
- [ ] Relatórios gerenciais.
- [ ] Exportação de relatórios para Excel.
- [ ] Cadastro e autenticação de usuários.
- [ ] Controle de acesso e permissões.
- [ ] Testes automatizados.
- [ ] Publicação da aplicação.

## Estrutura do projeto

```text
StockFlow/
│
├── app/
│   ├── forms/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── templates/
│   └── static/
│       ├── css/
│       ├── js/
│       └── img/
│
├── instance/
├── migrations/
├── tests/
├── docs/
│
├── config.py
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta

```bash
cd StockFlow
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 6. Criar a pasta do banco de dados

```bash
mkdir instance
```

Se a pasta já existir, não é necessário executar novamente.

### 7. Aplicar as migrações

```bash
flask --app run.py db upgrade
```

### 8. Executar a aplicação

```bash
python run.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

## Regras de negócio

- Cada produto possui um SKU único.
- A quantidade em estoque não pode ser negativa.
- Toda entrada ou saída deve gerar uma movimentação.
- Produtos com histórico de movimentação devem ser inativados, em vez de excluídos.
- Produtos com quantidade igual ou inferior ao estoque mínimo devem ser identificados como estoque baixo.
- O cadastro de um produto inicia com quantidade zero.
- Os valores monetários são armazenados em centavos no banco de dados.

## Status do desenvolvimento

O StockFlow está em desenvolvimento. Novas funcionalidades estão sendo implementadas e testadas gradualmente.

## Autor

Desenvolvido por **[Seu nome]**.

Projeto pessoal de aprendizado e desenvolvimento prático na área de Tecnologia e Ciência de Dados.