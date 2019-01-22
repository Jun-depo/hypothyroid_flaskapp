from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    # 'name,''age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI'
    name = StringField('name: ')
    age = StringField('Age: ')
    tsh = StringField('TSH: ')
    t3 = StringField('T3:   ')
    tt4 = StringField('TT4: ')
    t4u = StringField('T4U: ')
    fti = StringField('FTI: ')
    submit = SubmitField('Submit')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of data to Remove:')
    submit = SubmitField('Remove data')
