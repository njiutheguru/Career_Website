from flask import Flask, render_template
# create a constant list of JOBS
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'ksh 220,000',
  },
  {
    'id': 2,
    'title': 'Data Engineer',
    'location': 'Nairobi,Kenya',
    'salary': 'ksh 230000',
  },
  {
    'id': 3,
    'title': 'Data Manager',
    'location': 'Kampala, Uganda',
    'salary': 'ksh 120,000',
  },
  {
    'id': 4,
    'title': 'IOT developer',
    'location': 'Mombase Kenya',
    'salary': 'ksh 320,000',
  },
]

app = Flask(__name__)
@app.route("/")
def hello_world():
  return render_template("bootstrap.html",
                        jobs=JOBS,
                        company_name="CML")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

    

