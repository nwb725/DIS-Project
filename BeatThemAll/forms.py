from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

class SportStatsForm(FlaskForm):
    sport_name = StringField('Sport Name', validators=[DataRequired()], render_kw={"placeholder": "Enter sport name"})
    strength = FloatField('Strength',
                         validators=[DataRequired(), NumberRange(min=0, max=100)])
    peed = FloatField('Speed',
                         validators=[DataRequired(), NumberRange(min=0, max=100)])
    durability = FloatField('Durability',
                         validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Get Stats')
