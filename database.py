from sqlalchemy import create_engine, text
# engine = create_engine("mysql+pymysql://root:password@localhost/flask?charset=utf8mb4")
# print(engine)

DATABASE_URI = 'mysql+pymysql://root:masterguru@localhost:3306/career_website?charset=utf8mb4'
# Create an engine instance
engine = create_engine(DATABASE_URI)


with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())