-- Average Grade Distribution per Course
SELECT 
    c.CourseID,
    c.CourseName,
    AVG(
        CASE e.Grade
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
        END
    ) AS AvgGPA
FROM courses c
JOIN enrollments e ON c.CourseID = e.CourseID
GROUP BY c.CourseID, c.CourseName
ORDER BY AvgGPA DESC;
