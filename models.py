from app import db


class PipeLine1(db.Model):
    __tablename__ = "deployment_data"

    id = db.Column(db.Integer, primary_key=True)
    batch_title = db.Column(db.String())
    batch_size = db.Column(db.Integer)

    def __init__(self, batch_title, batch_size):
        self.batch_title = batch_title
        self.batch_size = batch_size

    def __repr__(self):
        return "<id {}>".format(self.id)

