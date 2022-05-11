from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 

class SearchForm(FlaskForm):
    
    # title = StringField('Review title',validators=[Required()])
    # review = TextAreaField('Movie review', validators=[Required()])
    # submit = SubmitField('Submit')
    
    text = StringField("enter text to searc")
    submit = SubmitField('Submit')