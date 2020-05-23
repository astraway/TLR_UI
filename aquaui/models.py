from aquaui import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


# allows for user auth
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __table__name = "users"

    id = db.Column(db.Integer, primary_key=True)

    profile_image = db.Column(db.String(20), nullable=False, default='default_profile.png')

    username = db.Column(db.String(64), unique=True, index=True)

    email = db.Column(db.String(64), unique=True, index=True)

    password_hash = db.Column(db.String(128))

    quotes = db.relationship('QuoteCreation', backref='requester', lazy = True )


    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def __check_password__(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"



class QuoteCreation(db.Model):
    users = db.relationship(User)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False )
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    BEGEOID = db.Column(db.String(128))
    CAMPAIGN_DUE_DATE = db.Column(db.String(128))
    CAMPAIGN_TYPE = db.Column(db.String(128))
    CCOID = db.Column(db.String(128))
    DATA_SOURCE_TYPE = db.Column(db.String(128))
    DEFAULT_DAYS_FUTURE = db.Column(db.String(128))


    def __init__(self, user_id, BEGEOID, CAMPAIGN_DUE_DATE, CAMPAIGN_TYPE,CCOID, DATA_SOURCE_TYPE, DEFAULT_DAYS_FUTURE):
        self.user_id = user_id
        self.BEGEOID = BEGEOID
        self.CAMPAIGN_DUE_DATE = CAMPAIGN_DUE_DATE
        self.CAMPAIGN_TYPE = CAMPAIGN_TYPE
        self.CCOID = CCOID
        self.DATA_SOURCE_TYPE = DATA_SOURCE_TYPE
        self.DEFAULT_DAYS_FUTURE = DEFAULT_DAYS_FUTURE

    def __repr__(self):
        return f"CCOID: {self.CCOID} -- Campaign Due Date: {self.CAMPAIGN_TYPE}"
