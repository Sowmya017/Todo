from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db =SQLAlchemy(app)

class todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime, default=lambda: datetime.now())
   
   
   
   
    def __repr__(self):  #used for returing the output 
        return f"{self.sno} - {self.title}"
@app.route('/',methods=['GET','POST'])
def index():

    if request.method=="POST":
      title= request.form['title']
      desc=request.form['desc']
      Todo=todo(title=title ,desc=desc)
      db.session.add(Todo)
      db.session.commit()
    allTodo=todo.query.all()

    return render_template('index.html',allTodo=allTodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    allTodo=todo.query.filter_by(sno=sno).first()
    db.session.delete(allTodo)
    db.session.commit()
    return redirect('/')
@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method == "POST":
        title=request.form['title']
        desc=request.form['desc']
        Todo=todo.query.filter_by(sno=sno).first()
        Todo.title=title
        Todo.desc=desc
        db.session.add(Todo)
        db.session.commit()
        return redirect('/')
    Todo=todo.query.filter_by(sno=sno).first()
    return render_template('update.html',Todo=Todo)

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug=True,port=8000)