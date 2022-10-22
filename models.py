

import email
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class User(UserMixin):

    __table__name='pildoras_user'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(256), unique=True, nullable=False)
    name=db.Column(db.String(128), nullable=False)
    is_admin=db.Column(db.Boolean, default=False)

    def set_password(self, password):

        self.password=generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(self.password, password)
        
    def save(self):

        if not self.id:
            db.session.add(self)

        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(id):
        return User.query.filter_by_email(email=email).first()