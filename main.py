from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'My ultra super duper secret key'

class addTodoForm(FlaskForm):
  name = StringField('To do', validators=[DataRequired()])
  submit = SubmitField('Register')

todos = ['Read a book', 'Sing a song', 'write a letter']

@app.route('/', methods=['GET', 'POST'])
def index():
  form = addTodoForm(request.form, csrf_enabled=False)
  if request.method == 'POST' and form.validate():
    todos.append(form.name.data)
  return render_template('index.html', todos=todos, template_form=form)


app.run(debug=True, host='0.0.0.0')