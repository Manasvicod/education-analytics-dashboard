--  Most Popular Courses (Highest Enrollments)
SELECT 
    c.CourseID,
    c.CourseName,
    c.Department,
    COUNT(e.EnrollmentID) AS TotalEnrollments
FROM courses c
JOIN enrollments e ON c.CourseID = e.CourseID
GROUP BY c.CourseID, c.CourseName, c.Department
ORDER BY TotalEnrollments DESC
LIMIT 10;
