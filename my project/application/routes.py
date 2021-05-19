from application import app, db
from application.models import Games

@app.route('/')
def index():
    _todos= todos.query.all()
    #todos_1= ""
    #for c in all_todos:
     #   todos_1+="<br>"+str(c.id)+" " +c.Task+" "+str(c.Completed)
    return  render_template("index.html", all_todos=_todos)
    
 
@app.route('/add',methods=['GET','POST'])
def to_do1():
    form = TodoForm()
    if form.validate_on_submit():
        Task_3 = todos(Task = form.task.data)
        db.session.add(Task_3)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", form=form)

@app.route('/complete/<int:n>')
def is_complete(n):
    task_4= todos.query.get(n)
    task_4.Completed = True
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/incomplete/<int:n>')
def is_incomplete(n):
    task_5= todos.query.get(n)
    task_5.Completed = False
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:n>')
def is_delete(n):
    task_6 = todos.query.get(n)
    db.session.delete(task_6)
    db.session.commit()
    #return 'deleted'
    return  redirect (url_for("index"))
@app.route('/update/<int:n>',methods = ['GET','POST'])
def update(n):
    form = TodoForm()
    todo_update= todos.query.get(n)
    if form.validate_on_submit():
        todo_update.Task = form.task.data
        db.session.commit()
        return redirect(url_for("index"))
    if request.method == "GET":
        form.task.data= todo_update.Task
    return render_template("update.html",form=form)