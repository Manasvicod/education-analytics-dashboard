-- Top-Performing Students (Highest Average Grade → GPA)
SELECT 
    s.StudentID,
    s.Name,
    ROUND(AVG(
        CASE e.Grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            ELSE 0
        END
    ),2) AS GPA
FROM students s
JOIN enrollments e ON s.StudentID = e.StudentID
GROUP BY s.StudentID, s.Name
ORDER BY GPA DESC
LIMIT 10;
