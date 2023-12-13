# Milk Collection Management System
1. Introduction

Welcome to the Milk Collection Management System! This system is designed to streamline the process of collecting milk from farmers in rural areas, replacing traditional pen-and-paper methods with a digital solution. The goal is to enhance efficiency, accuracy, and transparency in the milk collection process.

2. Team Members
* Billy Kiplagat: Developer
* 
# Project Inspiration
The inspiration for this project stems from the challenges associated with manual record-keeping in rural milk collection. The need for a digital solution became apparent to address issues related to data accuracy, time consumption, and lack of transparency in the current process.

# Technologies Used
# Backend
1. Flask (Chosen):
* Lightweight Python web framework for quick development.
* Highly customizable and scalable, suitable for small to large-scale projects.
* Flexibility in integrating with databases and authentication systems.

2. CORS (Cross-Origin Resource Sharing):
* Essential for secure handling of cross-origin requests from the front end.

# Frontend
1. HTML, CSS, JavaScript (Chosen):
* HTML for page structure.
* CSS for styling and layout.
* JavaScript for dynamic interactivity and data manipulation.

# Alternate Technology Considerations
# Backend
1. Alternate Option: Django (Considered):
* Powerful and feature-rich Python web framework.
* Robust ORM and authentication system.
* Flask was chosen for its lightweight nature and simplicity, aligning with the project's requirements.
 
# Frontend
1. Alternate Option: React (Considered):
* Popular JavaScript library for building user interfaces.
* Component-based architecture for modular and maintainable code.
* Plain HTML, CSS, and JavaScript were chosen for simplicity; React may be considered for future expansion.

# Core Functionality
The system addresses the following key functionalities:

1. Admin (Milk Collector):

* Registering new farmers.
* Recording daily milk collections.
* Calculating payments based on quantity and quality.
* Viewing reports and analytics.
2. Farmer:
* Registering in the system.
* Viewing personal information and contact details.
* Accessing milk collection history.
* Viewing payment history.
# How to start the backend
`MYSQL_USER=root MYSQL_PWD=root MYSQL_HOST=localhost MYSQL_DB=milk_collection_system TYPE_STORAGE=db API_HOST=0.0.0.0 API_PORT=5000 python3 -m app.app`

# Acknowledgments
Special thanks to all contributors and supporters who have helped make this project a reality. Your contributions are highly appreciated!