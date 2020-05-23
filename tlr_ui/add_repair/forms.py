from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileAllowed, FileField

from flask_login import current_user
from tlr_ui.models import User


class CreateQuoteForm(FlaskForm):
    BEGEOID = StringField('BEGEOID', validators=[DataRequired()])
    CAMPAIGN_DUE_DATE = StringField('CAMPAIGN DUE DATE', validators=[DataRequired()])
    CAMPAIGN_TYPE = StringField('CAMPAIGN TYPE', validators=[DataRequired()])
    CCOID = StringField('CCOID', validators=[DataRequired()])
    DATA_SOURCE_TYPE = StringField('DATA SOURCE TYPE', validators=[DataRequired()])
    DEFAULT_DAYS_FUTURE = StringField('DEFAULT DAYS FUTURE', validators=[DataRequired()])
    submit = SubmitField('Request Quote')