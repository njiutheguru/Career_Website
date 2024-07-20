from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
# db_connection_string = "mysql+mysqlconnector://sql12721096:8qg19FGj6e@sql12.freesqldatabase.com/sql12721096"
engine = create_engine(db_connection_string)
# connection = engine.connect()
# print(connection)

# print("Connection established successfully...!")


def load_jobs_from_db():
  with engine.connect() as conn:
    jobs = []
    result = conn.execute(text("select * from jobs"))
    result = result.all()

    result_list = [
      {
          'id': item[0],
          'title': item[1],
          'location': item[2],
          'salary': item[3],
          'currency': item[4],
          'responsibilities': item[5],
          'requirements': item[6]
      }
      for item in result]

    jobs.append(result_list)
  
    return jobs[0]

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {'val': id})
    # result = conn.execute(text("select * from jobs where id = :val"), val=id)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      result_list = [
        {
            'id': item[0],
            'title': item[1],
            'location': item[2],
            'salary': item[3],
            'currency': item[4],
            'responsibilities': item[5],
            'requirements': item[6]
        }
        for item in rows]
      return result_list[0]

print(load_jobs_from_db())
print("-----------------")
print(load_job_from_db(1))
