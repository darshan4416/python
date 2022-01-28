from flask import Flask
from flask import Flask, render_template, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    dept = db.Column(db.String(40))
    dept_name = db.Column(db.String(40))
    manager_name = db.Column(db.String(40))

class Department(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    dept = db.Column(db.String(40),db.ForeignKey(Employee.dept))
    dept_name = db.Column(db.String(40))
    manager_name = db.Column(db.String(40))

@app.route('/', methods=['POST','GET'])
def index():
    employees = Employee.query.order_by(Employee.id).all()
    department = Department.query.order_by(Department.dept).distinct()

    return render_template('index.html',employees=employees, department=department)

@app.route('/add-emp/',methods=['POST'])
def add():
    name = request.form["name"]
    dept = request.form["dept"]
    dept_name = request.form["dept_name"]
    manager_name = request.form["manager_name"]
    new_Emp = Employee(name=name, dept=dept, dept_name=dept_name, manager_name=manager_name)
    new_Dept = Department(dept=dept, dept_name=dept_name, manager_name=manager_name)

    db.session.add(new_Emp)
    db.session.add(new_Dept)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>/',methods=['POST','GET'])
def delete(id):
    
    emp_to_del = Employee.query.get_or_404(id)
    print(emp_to_del)
    temp = len(Employee.query.filter(Employee.dept == emp_to_del.dept).all())

    if temp == 1:
        dept_del = Department.query.get_or_404(emp_to_del.dept)

    try:
        if temp > 1:
            db.session.delete(emp_to_del)
            db.session.commit()
            return redirect("/")
        else:
            db.session.delete(emp_to_del)
            db.session.delete(dept_del)
            db.session.commit()
            return redirect("/")

    except:
        return "Something Went Wrong"





    



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

