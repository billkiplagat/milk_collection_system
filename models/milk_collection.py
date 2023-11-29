# from app import db
# from models.base_model import BaseModel, Base
#
#
# class MilkCollection(db.Model, BaseModel, Base):
#     id = db.Column(db.Integer, primary_key=True)
#     farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)
#     collection_date = db.Column(db.Date, nullable=False)
#     quantity = db.Column(db.Float, nullable=False)
#
#     def __repr__(self):
#         return f"<MilkCollection {self.id}>"
