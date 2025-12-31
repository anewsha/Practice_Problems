-- List the names and departments of all instructors whose salary is greater than 70,000.
select name, dept_name from instructor 
where salary > 70000

-- Find the course_id and title of all courses that offer more than 3 credits.
select course_id, title from course where credits >3

--List the student id, student name, and course_id for all students who have taken at least one course.
-- select id, count(*) as cnt from takes
-- group by id
-- having  count(*)=0
select t.id,s.name, t.course_id from takes t left join student s on t.id = s.id

-- Find the names of instructors who teach in the Spring semester of 2023.
select i.name from teaches t left join instructor i on t.id = i.id
where t.semester = 'Spring' and year=2023

