from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    class Meta:
        csrf = False
    title = StringField('name', validators=[DataRequired()])
    author = StringField('description', validators=[DataRequired()])
    