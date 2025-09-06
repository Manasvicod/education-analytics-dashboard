-- 1. Count students by Department, Gender, Admission Year 
SELECT 
    Department,
    Gender,
    AdmissionYear,
    COUNT(*) AS StudentCount
FROM students
GROUP BY Department, Gender, AdmissionYear
ORDER BY Department, AdmissionYear;


