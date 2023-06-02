from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def get_db():
    conn = psycopg2.connect(
        dbname="projekt",
        user="postgres",
        password="simonkrogh",
        host="localhost"
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        work_year = request.form.get('work_year')
        employment_type = request.form.get('employment_type')
        job_title = request.form.get('job_title')

        work_year = None if work_year == '' else work_year
        employment_type = None if employment_type == '' else employment_type
        job_title = None if job_title == '' else job_title


        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT AVG(salary_in_usd) 
            FROM Salaries 
            WHERE work_year = COALESCE(%s,work_year) AND
            employment_type = COALESCE(%s,employment_type) AND
            job_title = COALESCE (%s,job_title)
            """, (work_year, employment_type, job_title))

        

        result = cur.fetchone()
        avg_salary = result[0] if result else  'No data found.'
        # Convert to string with 2 decimals
        # avg_salary = "{:.2f}".format(avg_salary)

        if avg_salary == None:
            cur.execute(
            """
            SELECT AVG(salary_in_usd) 
            FROM Salaries 
            WHERE work_year = COALESCE(%s,work_year) AND
            job_title = COALESCE (%s,job_title)
            """, (work_year, job_title))

            result = cur.fetchone()
            avg_salary1 = result[0] if result else  'No data found.'
            return render_template('results.html', avg_salary=avg_salary1)

        cur.close()
        conn.close()

        return render_template('results.html', avg_salary=avg_salary)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
