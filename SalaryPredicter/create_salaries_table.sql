DROP TABLE IF EXISTS Salaries;
DROP TABLE IF EXISTS employment_type_description;

CREATE TABLE Salaries (
    id SERIAL PRIMARY KEY,
    work_year INT,
    experience_level VARCHAR(255),
    employment_type CHAR(2),
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
FROM '/Users/simonkroghanderson/Downloads/SalaryPredicter/ds_salaries.csv'
CSV HEADER;

CREATE TABLE employment_type_description (
    employment_type CHAR(2) PRIMARY KEY,
    description TEXT NOT NULL
);
INSERT INTO employment_type_description (employment_type, description)
VALUES ('FT', 'Full Time'), ('PT', 'Part Time'), ('CT', 'Contract Time'),('FL', 'Freelance');

ALTER TABLE Salaries
ADD FOREIGN KEY (employment_type) 
REFERENCES employment_type_description (employment_type);


 