from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


def Convert_to_float(string):
    try:
        float(string)
        return float(string)
    except ValueError:
        return "Please enter a number"


def get_db():
    conn = psycopg2.connect(
        dbname="XXXX",
        user="XXXX",
        password="XXXX",
        host="localhost"
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def FrontPage():
    return render_template('frontpage.html')
    
@app.route('/iGotJob', methods=['GET', 'POST'])
def iGotJob():
    # initialize options for dropdowns
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT work_year FROM Salaries ORDER BY work_year")
    work_years = [item[0] for item in cur.fetchall()]
    cur.execute("SELECT employment_type, description FROM employment_type_description ORDER BY employment_type")
    employment_types = cur.fetchall()
    cur.execute("SELECT DISTINCT job_title FROM Salaries ORDER BY job_title")
    job_titles = [item[0] for item in cur.fetchall()]
    cur.close()
    conn.close()

    # calculates average salary based on user input
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
            if avg_salary1 == None: avg_salary1 = 'not found so expect a random amount of'
            return render_template('iGotJobResult.html',  answer="We don't know, you are the only one with that job combination\n Try with fewer variables")
        else: 
            avg_salary = "{:.2f}".format(avg_salary)

        cur.close()
        conn.close()

        user_salary = request.form.get('user_salary')
        print(avg_salary, "avg_salary")
        print(user_salary, "user_salary")
        
        if Convert_to_float(user_salary) == "Please enter a number":
            answer = "Please enter a number"
        elif  Convert_to_float(user_salary) <  Convert_to_float(avg_salary):
            answer = "You're underpaid! You should ask for a raise!"
        else:
            answer = "You're overpaid! Still, ask for a raise!"

        return render_template('iGotJobResult.html', answer=answer)

    return render_template('iGotJob.html', work_years=work_years, employment_types=employment_types, job_titles=job_titles)



@app.route('/index', methods=['GET', 'POST'])
def index():
    # initialize options for dropdowns
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT work_year FROM Salaries ORDER BY work_year")
    work_years = [item[0] for item in cur.fetchall()]
    cur.execute("SELECT employment_type, description FROM employment_type_description ORDER BY employment_type")
    employment_types = cur.fetchall()
    cur.execute("SELECT DISTINCT job_title FROM Salaries ORDER BY job_title")
    job_titles = [item[0] for item in cur.fetchall()]
    cur.close()
    conn.close()

    # calculates average salary based on user input
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
            if avg_salary1 == None: avg_salary1 = 'not found so expect a random amount of'
            return render_template('results.html', avg_salary=avg_salary1)
        else: 
            avg_salary = "{:.2f}".format(avg_salary)

        cur.close()
        conn.close()

        return render_template('results.html', avg_salary=avg_salary)

    return render_template('index.html', work_years=work_years, employment_types=employment_types, job_titles=job_titles)

if __name__ == "__main__":
    app.run(debug=True)
