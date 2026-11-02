from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    DecimalField,
    SelectField,
    SubmitField
)

#StringField: recebe textos.
#IntegerField: recebe números inteiros.
#DecimalField: recebe valores decimais, como preços.
#SelectField: cria uma lista de opções.
#DataRequired: exige o preenchimento.
#NumberRange: limita os valores permitidos.

from wtforms.validators import (
    DataRequired,
    NumberRange,
    Length,
    Optional
)


class ProdutoForm(FlaskForm):

    sku = StringField(
        "SKU",
        validators=[
            DataRequired(),
            Length(max=50)
        ]
    )

    nome = StringField(
        "Nome do produto",
        validators=[
            DataRequired(),
            Length(max=150)
        ]
    )

    categoria_id = SelectField(
        "Categoria",
        coerce=int,
        validators=[DataRequired()]
    )

    fornecedor_id = SelectField(
        "Fornecedor",
        coerce=int,
        validators=[Optional()]
    )

    estoque_minimo = IntegerField(
        "Estoque mínimo",
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ]
    )

    preco_custo = DecimalField(
        "Preço de custo",
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ],
        places=2
    )

    preco_venda = DecimalField(
        "Preço de venda",
        validators=[
            DataRequired(),
            NumberRange(min=0)
        ],
        places=2
    )

    submit = SubmitField("Cadastrar produto")


from app.models import Categoria, Fornecedor


def carregar_opcoes(form):

    categorias = Categoria.query.order_by(
        Categoria.nome.asc()
    ).all()

    fornecedores = Fornecedor.query.order_by(
        Fornecedor.nome.asc()
    ).all()

    form.categoria_id.choices = [
        (categoria.id, categoria.nome)
        for categoria in categorias
    ]

    form.fornecedor_id.choices = [
        (0, "Sem fornecedor")
    ] + [
        (fornecedor.id, fornecedor.nome)
        for fornecedor in fornecedores
    ]