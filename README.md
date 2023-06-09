# Student_Record_Management_System_Shyftlabs

## Student Record Management System

Live version of the app is available at: http://vardhanseepala.pythonanywhere.com/
### Description

This is a simple student record management system. It is a console based application. It is written in Django and Python. It uses SQLite3 as database. It has the following features:

- Add Student
- Delete Student
- View Students
- Add Course
- Delete Course
- Add Results
- View Results

### Installation

1. Clone the repository: `git clone https://github.com/seepala98/Student_Record_Management_System_Shyftlabs.git`
2. Move to the directory: `cd Student_Record_Management_System_Shyftlabs`
3. Create a virtual environment: `python -m venv venv` 
4. Activate the virtual environment: `venv\Scripts\activate`
5. Install the requirements: `pip install -r requirements.txt`
6. Migrate the database: `python manage.py makemigrations` then `python manage.py migrate`
7. Create super user: `python manage.py createsuperuser`
8. Run the server: `python manage.py runserver`
9. Open the browser and go to `http://127.0.0.1:8000/`

### Common errors: 
1. no such table exists - `python manage.py makemigrations <appname>` then `python manage.py migrate <appname>`

### Screenshots
<p float="left">
<img src="images\1_welcome.png" width=25% height=25%>
<img src="images\2_student_list.png" width=25% height=25%>
<img src="images\3_add_course.png" width=25% height=25%>
<img src="images\4_course_list.png" width=25% height=25%>
<img src="images\5_add_result.png" width=25% height=25%>
<img src="images\6_show_result.png" width=25% height=25%>
<img src="images\7_add_student_warning.png" width=25% height=25%>
<img src="images\8_add_same_course_warning.png" width=25% height=25%>
</p>

### Future Scope 
- Add more features
- Improve UI
- Add more validations
- Dockerize the app
- Scale the app/ deploy it on cloud preferabely serverless
