from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreatePostForm(FlaskForm):
    title = StringField(
        label="Title",
        name="title",
        validators=[
            DataRequired(),
            Length(min=3, max=25),
        ],
    )
    body = TextAreaField(
        label="Body",
        name="body",
        validators=[
            DataRequired(),
        ],
    )
