from datetime import datetime
from pharmacare import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Item(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    item_name=db.Column(db.String(20),nullable=False)
    pkd_date=db.Column(db.DateTime,nullable=False)
    exp_date=db.Column(db.DateTime,nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    price=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f"addItem('{self.item_name}','{self.pkd_date}','{self.exp_date}','{self.quantity}')"

class Bill(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    itemName=db.Column(db.String(20),nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    price=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return f"billItem('{self.itemName}', '{self.quantity}','{self.price}')"
