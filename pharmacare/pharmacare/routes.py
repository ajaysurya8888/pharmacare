from flask import Flask,render_template,url_for, flash, redirect,request
from datetime import date
import datetime
from sqlalchemy import text,update
from pharmacare.forms import LoginForm,RegistrationForm,addItemForm,billItemForm
from pharmacare import app, db, bcrypt
from pharmacare.models import User,Item,Bill
from flask_login import login_user, current_user, logout_user, login_required
flag=0
@app.route('/login',methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if request.method=='POST':
        return redirect(url_for('about'))

    return render_template('login.html', title='login',form=form)
@app.route('/',methods=['GET','POST'])
@app.route("/register",methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method=="POST":
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',title='register',form=form)

@app.route("/bill",methods=['GET', 'POST'])
def bill():
    form=billItemForm()
    bill=Bill.query.all()
    if 'enter' in request.form:
        bill= Bill(itemName=form.itemName.data,quantity=form.quantity.data,price=form.price.data)
        db.session.add(bill)
        stmt = update(Item).where(Item.item_name == bill.itemName).values(quantity = Item.quantity-bill.quantity)
        db.session.execute(stmt)
        db.session.commit()
        return redirect(url_for('bill'))
    # if 'clear' in request.form:
    #     db.session.query(Bill).delete()
    #     db.session.commit()
    #     return redirect(url_for('bill'))


    return render_template('bill.html',title='home',form=form,bill=bill)

@app.route("/about")
def about():
    return render_template('about.html',title='about')
@app.route("/addItem",methods=['GET', 'POST'])
def addItem():
    form=addItemForm()
    items=Item.query.filter(Item.quantity!=0)
    itemupd=Item.query.all()

    if request.method=="POST":

        name=request.form['itemName']
        q=request.form['quantity']
        for i in itemupd:
            if i.item_name ==name:
                stmt = update(Item).where(Item.item_name == name).values(quantity = q+Item.quantity)
                db.session.execute(stmt)
                db.session.commit()
                global flag
                flag=1

        if flag==0:
            items=Item.query.filter(Item.quantity!=0)()
            addd= Item(item_name=form.itemName.data,pkd_date=form.pkdDate.data, exp_date=form.expDate.data,quantity=form.quantity.data,price=form.price.data)
            db.session.add(addd)
            db.session.commit()
        return redirect(url_for('addItem'))

    return render_template('addItem.html',title='addItem',form=form,items=items)
@app.route("/expired")
def expired():
    items=Item.query.filter(text(":val")>Item.exp_date).params(val=datetime.datetime.now())
    return render_template('expired.html',title='expired',items=items)
@app.route("/outOfStock")
def outOfStock():
    items=Item.query.filter(Item.quantity==0)
    return render_template('outOfStock.html',title='outOfStock',items=items)

if __name__ == '__main__':
   app.run()
