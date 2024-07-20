from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

# Create an engine instance
engine = create_engine(db_connection_string)


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



# def load_jobs_from_db():
#   with engine.connect() as conn:
#     jobs = []
#     result = conn.execute(text("select * from jobs"))
#     result = result.all()
#     j = {row[0]: row[0:] for row in result}
#     jobs.append(j)
#     # for row in result.all():
#     #   jobs.append(row)
#     return jobs
# SELECT * FROM jobs WHERE id = :val
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {'val': id})
    # result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), val=id)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      # return dict(rows[0])
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
      
    


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("""
        INSERT INTO applications 
        (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) 
        VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
    """)

    # Pass parameters as a dictionary
    conn.execute(query, {
        'job_id': job_id,
        'full_name': data['full_name'],
        'email': data['email'],
        'linkedin_url': data['linkedin_url'],
        'education': data['education'],
        'work_experience': data['work_experience'],
        'resume_url': data['resume_url']
    })




  
  # with engine.connect() as conn:
  #   query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

  #   conn.execute(query,
  #               job_id = job_id,
  #               full_name = data['full_name'],
  #               email= data['email'],
  #               linkedin_url = data['linkedin_url'],
  #               education = data['education'],
  #               work_experience = data['work_experience'],
  #               resume_url= data['resume_url'])



                               
