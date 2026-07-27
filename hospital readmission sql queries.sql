USE de_project;

select * from hospital_readmissions_cleaned;

-- Average Hospital Stay by Specialty:
SELECT medical_specialty, AVG(time_in_hospital) AS avg_stay
FROM hospital_readmissions_cleaned
GROUP BY medical_specialty
ORDER BY avg_stay DESC;


-- Total Number of Readmitted Patients-- 
SELECT COUNT(*) AS total_readmitted
FROM hospital_readmissions_cleaned
WHERE readmitted = 1;

-- Medication Load by Diagnosis
SELECT diag_1, AVG(n_medications) AS avg_meds
FROM hospital_readmissions_cleaned
GROUP BY diag_1
ORDER BY avg_meds DESC
LIMIT 10;

-- Outpatient Visits vs. Readmission Risk
SELECT n_outpatient, AVG(readmitted) AS readmission_rate
FROM hospital_readmissions_cleaned
GROUP BY n_outpatient
ORDER BY n_outpatient;

-- Readmission Rate by Age Bucket
SELECT age, AVG(readmitted) AS readmission_rate
FROM hospital_readmissions_cleaned
GROUP BY age
ORDER BY age;
