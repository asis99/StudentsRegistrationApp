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

Base.metadata.create_all(engine)



