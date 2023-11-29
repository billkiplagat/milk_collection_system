# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from routes import admin, farmer, milk_collection, reports
# from models import admin as admin_model, farmer as farmer_model, milk_collection as milk_collection_model
#
# # Initialize the Flask app
# app = Flask(__name__)
#
#
# # Initialize the SQLAlchemy database
# db = SQLAlchemy(app)
#
# # Register blueprints
# app.register_blueprint(admin.admin_bp)
# app.register_blueprint(farmer.farmer_bp)
# app.register_blueprint(milk_collection.milk_collection_bp)
# app.register_blueprint(reports.reports_bp)
#
# # Create database tables
# with app.app_context():
#     db.create_all()
#
# if __name__ == '__main__':
#     app.run()
