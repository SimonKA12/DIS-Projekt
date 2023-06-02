
DROP TABLE IF EXISTS Salaries;
CREATE TABLE Salaries (
    id SERIAL PRIMARY KEY,
    work_year INT,
    experience_level VARCHAR(255),
    employment_type VARCHAR(255),
    job_title VARCHAR(255),
    salary FLOAT,
    salary_currency VARCHAR(255),
    salary_in_usd FLOAT,
    employee_residence VARCHAR(255),
    remote_ratio FLOAT,
    company_location VARCHAR(255),
    company_size VARCHAR(255)
);

COPY Salaries(work_year, experience_level, employment_type, job_title, salary, salary_currency, salary_in_usd, employee_residence, remote_ratio, company_location, company_size)
FROM '/Users/simonkroghanderson/Downloads/myapp/ds_salaries.csv'
CSV HEADER;

/* SELECT DISTINCT job_title from Salaries; */
 