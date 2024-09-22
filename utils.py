from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orms import Students, Courses
from sqlalchemy import func

# engine=create_engine("sqlite:///student.db")
engine = create_engine("mysql+pymysql://root:1234@localhost:3306/student_db")
Session=sessionmaker(bind=engine)
session=Session()




def convert_date(date_string, n=True):
    from datetime import datetime
    # Convert the string to a datetime object
    if n:
        date_object = datetime.strptime(date_string, "%Y-%m-%d").date()
        return date_object
    else:
        date_object = datetime.strptime(str(date_string), "%Y-%m-%d").strftime("%Y-%m-%d")
        return date_object


def findTotalCourseDuration(days):
    from datetime import timedelta
    delta = timedelta(days=314)
    days = delta.days
    years = days // 365
    remaining_days = days % 365
    months = remaining_days // 30
    remaining_days = remaining_days % 30
    return f"{years} year-{months}-months-{remaining_days}-days"


class Student:
    def AggregateStudentsData(self):
        result = (
            session.query(
                Students.course,
                func.count(Students.name).label('student_count'),
                func.sum(Students.paid_fees).label('total_fee')
            )
            .group_by(Students.course)
            .all()
        )
        aggregatedData=[{"course":row.course, "student_count":row.student_count, "total_fee": int(row.total_fee)} for row in result]
        # print(aggregatedData)
        return aggregatedData

    def GetAllStudent(self):
       with Session() as session:
        data = session.query(Students).all()
        allData = [
            {
                "name": s.name,
                "duration": findTotalCourseDuration((s.course_end - s.course_start).days) if s.course_start and s.course_end else None,
                "fee": s.fee,
                "address":s.address,
                "dob":convert_date(s.dob, n=False),
                "paid_fees":s.paid_fees,
                "pending":s.pending
            }
            for s in data
        ]
        return allData
    
    def StudentsRegistration(self, data):
        newStudent=Students(name=data.get("first_name")+" "+data.get("last_name"), 
                            first_name=data.get("first_name"), last_name=data.get("last_name"), 
                            dob=convert_date(data.get("dob")), address=data.get("address"), 
                            course=data.get("course"))
        
        course_data=session.query(Courses).filter_by(course_name=data.get("course")).first()
        if course_data:
            newStudent.fee=course_data.fee
            newStudent.course_start=course_data.course_start
            newStudent.course_end = course_data.course_end

        session.add(newStudent)
        session.commit()
        return True
    
    def UpdateStudents(self, data):
        print(data)
        if data.get("name"):
            sessiondata=session.query(Students).filter_by(name=data.get("name"), course=data.get("course")).first()
            coursedata =session.query(Courses).filter_by(course_name=data.get("course")).first()
            if sessiondata:
                if data.get("address"):
                    sessiondata.address=data.get("address")
        
                if data.get("dob"):
                    sessiondata.course_end=convert_date(data.get("dob"))
                    session.commit()
                if data.get("paid_fees"):
                    sessiondata.paid_fees=sessiondata.paid_fees + int(data.get("paid_fees")) if sessiondata.paid_fees != sessiondata.fee else sessiondata.fee
                    session.commit()
                    if coursedata:
                        sessiondata.pending = coursedata.fee - sessiondata.paid_fees
                        session.commit()
            else:
                return "No course found", 404
        else:
            return False
    
    def DeleteStudent(self, name_student, dob, course):
        data=session.query(Students).filter_by(name=name_student, dob=convert_date(dob), course=course).all()
        if data:
            for i in data:
                session.delete(i)
                session.commit()
            return True
        else:
            return False

    def GetAllCourses(self):
        with Session() as session:
            data = session.query(Courses).all()
            getAll=[{"course_name":i.course_name, "fee":i.fee, 
                    "course_start":str(i.course_start.year)+"-"+str(i.course_start.month)+"-"+ str(i.course_start.day), 
                    "course_end":str(i.course_end.year)+"-"+str(i.course_end.month)+"-"+ str(i.course_end.day), 
                    } 
                    for i in data]
            session.close()
            return getAll
    
    def AddCourse(self, data):
          newStudent=Courses(course_name=data.get("course_name"), 
                            fee=data.get("fee"), 
                            course_start=convert_date(data.get("course_start")), 
                            course_end=convert_date(data.get("course_end")))
          session.add(newStudent)
          session.commit()
          return True
    
    def UpdateCourse(self, data):
        if data.get("course_name"):
            sessiondata=session.query(Courses).filter_by(course_name=data.get("course_name")).first()
            if sessiondata:
                if data.get("fee"):
                    sessiondata.fee=data.get("fee")
                    session.commit()
                if data.get("course_start"):
                    sessiondata.course_start=convert_date(data.get("course_start"))
                    session.commit()
                if data.get("course_end"):
                    sessiondata.course_end=convert_date(data.get("course_end"))
                    session.commit()
            else:
                return "No course found", 404
        else:
            return False
    
    def DeleteCourse(self, data):
        data=session.query(Courses).filter_by(course_name=data.get("course_name")).first()
        if data:
            session.delete(data)
            session.commit()
            return True
        else:
            return False



# Instantiate and query
# f = Student()
# d = f.GetAllStudent()
# print(d)
# from datetime import date
# f.DeleteStudent(name_student="Nilam Pandey", dob=date(1908, 8, 23))
# f.StudentsRegistration(first_name="Nilam", last_name="Pandey",
#                         dob=date(1908, 8, 23), address="Chennai", 
#                         course="Chemistry")








