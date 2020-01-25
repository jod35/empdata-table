from . import app,db
from .models import Employee
from flask import render_template,redirect,request,url_for,flash

@app.route('/')
def hello():
    employees=Employee.query.all()
    context={
        'employees':employees
    }
    return render_template('index.html',**context)

@app.route('/add',methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        args={
            'name':request.form.get('name'),
            'age':request.form.get('age'),
            'gender':request.form.get('gender'),
            'salary':request.form.get('salary'),
            'residence':request.form.get('residence')
        }

        new_employee=Employee(**args)
        db.session.add(new_employee)
        db.session.commit()
        flash("Employee Added Successfully")
        return redirect(url_for('hello'))
        

    return render_template('add.html')

@app.route('/update/<int:id>',methods=['GET', 'POST'])
def update_info(id):
    user=Employee.query.get_or_404(id)
    if request.method == "POST":
        user.name=request.form.get('name')
        user.age=request.form.get('age')
        user.salary=request.form.get('salary')
        user.residence=request.form.get('residence')

        db.session.commit()
        flash("Info Updated Succcessfully")
        return redirect(url_for('hello'))

    context={
        'user':user
    }


    return render_template('update.html',**context)

@app.route('/delete/<int:id>')
def del_employee(id):
    user=Employee.query.get_or_404(id)
    if not user:
        flash("Employee not found")
        return redirect(url_for('hello'))
    db.session.delete(user)
    db.session.commit()
    flash("Record Deleted Successfully")
    return redirect(url_for('hello'))

    
