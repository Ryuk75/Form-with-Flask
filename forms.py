from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField,TextAreaField

class FormContactanos(FlaskForm):
    nombre = StringField('Nombre',validators=[validators.required(),validators.length(max=100)])
    correo = StringField('Correo',validators=[validators.required(),validators.length(max=150)])
    mensaje = TextAreaField('Mensaje',validators=[validators.required(),validators.length(max=500)])
    enviar = SubmitField('Enviar mensaje')
