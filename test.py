from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date


# engine=create_engine("sqlite:///student.db")
engine = create_engine("mysql+pymysql://root:1234@localhost:3306/student_db")

Base = declarative_base()


class Students(Base):
    __tablename__="students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    dob = Column(Date)
    address = Column(String(255))
    course = Column(String(255))
    course_start = Column(Date)
    course_end = Column(Date)
    fee=Column(Integer)
    paid_fees=Column(Integer, default=0)
    pending = Column(Integer, default=0)



class Courses(Base):
    __tablename__="courses"
    course_name = Column(String(255), primary_key=True)
    fee=Column(Integer)
    course_start = Column(Date)
    course_end = Column(Date)

# Students.__table__.drop(engine)
Base.metadata.create_all(engine)



# Session=sessionmaker(engine)
# session=Session()

# from sqlalchemy import func
# from models import Students  # Assuming your ORM model is called 'Students'

# SQLAlchemy query
# result = (
#     session.query(
#         Students.course,
#         func.count(Students.name).label('student_count'),
#         func.sum(Students.paid_fees).label('total_fee')
#     )
#     .group_by(Students.course)
#     .all()
# )

# # Process the result
# for row in result:
#     print(f"Course: {row.course}, Student Count: {row.student_count}, Total Fee: {row.total_fee}")



# from datetime import date

# data=[{"course_name":"Physics", "fee":200000, "course_start":date(2024, 8, 26), "course_end":date(2024, 9, 26)},
#       {"course_name":"Chemistry", "fee":300000, "course_start":date(2024, 6, 29), "course_end":date(2024, 7, 29)},
#         {"course_name":"Bio-Technology", "fee":700000, "course_start":date(2024, 9, 29), "course_end":date(2024, 11, 12)}]


# for i in data:
#     f=Courses(course_name=i.get("course_name"), fee=i.get("fee"),
#               course_start=i.get("course_start"), course_end=i.get("course_end"))
#     session.add(f)
#     session.commit()

# data=Students(name ="Allen Turing", first_name="Allen", last_name="Turing",
#                dob=date(1908, 8, 23), address="Hyderabad", course="Computer Science",
#                course_start=date(2004, 8, 12), course_end=date(2004, 8, 26), fee=1500000)


# session.add(data)
# session.commit()



