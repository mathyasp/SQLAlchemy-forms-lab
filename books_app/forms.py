from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre
import re

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', 
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    publish_date = DateField('Date Published', validators=[DataRequired()])
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')

    def validate_title(form, field):
        if 'banana' in field.data:
            raise ValidationError('Title cannot contain the word banana')


class AuthorForm(FlaskForm):
    """Form to create an author."""

    # TODO: Fill out the fields in this class for:
    # - the author's name
    # - the author's biography (hint: use a TextAreaField)
    # - a submit button
    name = StringField('Author Name',
        validators=[
            DataRequired(),
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    birth_date = DateField('Birth Date', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    submit = SubmitField('Submit')

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.
    def validate_name(form, field):
        if not re.match(r'^[A-Za-z\s]+$', field.data):
            raise ValidationError('Name can only contain letters and spaces')

    def validate_biography(form, field):
        if not re.match(r'^[A-Za-z0-9\s\.,!?]+$', field.data):
            raise ValidationError('Biography can only contain letters, numbers, spaces, and punctuation')

    def validate_birth_date(form, field):
        if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', field.data):
            raise ValidationError('Birth date must be in the format YYYY-MM-DD')

    def validate_country(form, field):
        if not re.match(r'^[A-Za-z\s]+$', field.data):
            raise ValidationError('Name can only contain letters and spaces')

class GenreForm(FlaskForm):
    """Form to create a genre."""

    # TODO: Fill out the fields in this class for:
    # - the genre's name (e.g. fiction, non-fiction, etc)
    # - a submit button
    name = StringField('Genre Name',
        validators=[
            DataRequired(),
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    submit = SubmitField('Submit')

    def validate_name(form, field):
        if not re.match(r'^[A-Za-z\s]+$', field.data):
            raise ValidationError('Name can only contain letters and spaces')
