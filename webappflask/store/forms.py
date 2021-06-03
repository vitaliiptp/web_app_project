from flask_wtf import FlaskForm
from wtforms import SubmitField


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')
