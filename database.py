from sqlalchemy import Column, Integer, String, TEXT, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import typing
import csv
import logging
import os
from sqlalchemy import select

db_file = "sqlite:///pythonsqlite.db"
engine = create_engine(db_file)
Base = declarative_base()
session = None
path, filename = os.path.split(os.path.realpath(__file__))


class ResumeSubmission(Base):
    """This class represents the resume table"""
    __tablename__ = 'resume_submission'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column('question', String(32))
    description = Column('description', TEXT)
    answer = Column('answer', TEXT)


def insert_data(data: dict) -> None:
    """
    This function will create
    :return: data
    """
    model = ResumeSubmission()
    model.question = data['question']
    model.description = data['description']
    model.answer = data['answer']
    try:
        global session
        session.add(model)
        session.commit()
    except:
        print('fail')
        print(data)


def read_csv() -> typing.List:
    """This function will load the CSV in memory"""
    data_open = []
    with open(path + '/parameters.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            logging.info(row)
            data_open.append({'question': row[0], 'description': row[1], 'answer': row[2]})
            line_count += 1
        logging.info(f'Processed {line_count} lines.')
    return data_open


def query_answer(param: str):
    """
    This function will query the answer in database
    :param param:
    :return:
    """
    stmt = select(ResumeSubmission).where(ResumeSubmission.question == param)
    obj = session.scalars(stmt).first()
    return obj.answer


def create_database() -> None:
    """
    Will create tables and upload tables
    :return:
    """
    engine.execute("DROP TABLE IF EXISTS submission ")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    global session
    session = Session()
    data = read_csv()
    for line in data:
        insert_data(line)


create_database()


