from flask import Flask, request, render_template
from flask_restful import Api, Resource
from flask_cors import CORS
from utils import Student

app =Flask(__name__)
api=Api(app)
CORS(app)
students_obj=Student()


@app.route('/')
def renderApp():
    return render_template('index.html')

class AggregateAnalytics(Resource):
    def get(self):
        data=students_obj.AggregateStudentsData()
        return data

class RegisterStudent(Resource):
    def get(self):
        data=students_obj.GetAllStudent()
        return data, 200
    
    def put(self):
        if request.is_json:
            students_obj.UpdateStudents(data=request.json)
        else:
            return False

    def post(self):
        if request.is_json:
            students_obj.StudentsRegistration(data=request.json)
        else:
            return False
    
    def delete(self):
        if request.is_json:
            req_data=request.json
            print(req_data)
            data=students_obj.DeleteStudent(name_student=req_data.get("name"), 
                                            dob=req_data.get("dob"), course=req_data.get("course"))
            return data
        else:
            return False
        

class StudentCourses(Resource):
    def get(self):
        data=students_obj.GetAllCourses()
        return data, 200
    
    def post(self):
        if request.is_json:
            data = students_obj.AddCourse(request.json)
            return data
        else:
            return False
    
    def put(self):
        if request.is_json:
            data = students_obj.UpdateCourse(request.json)
            return data
        else:
            return False
    
    def delete(self):
        if request.is_json:
            data = students_obj.DeleteCourse(request.json)
            return data
        else:
            return False



api.add_resource(RegisterStudent, '/students')
api.add_resource(StudentCourses, '/students/courses')
api.add_resource(AggregateAnalytics, '/students/courses/analytics')

if __name__=="__main__":
    app.run(host="localhost", debug=True, port=8080)