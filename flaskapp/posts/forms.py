from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import data_required, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Length(min=5, max=150)])
    content = TextAreaField('Content', validators=[
                            data_required(), Length(min=5)])
    submit = SubmitField('Post')
