use college;

select * from student1;

alter table student1 add email_id VARCHAR(100);

alter table student1 add number INT;

alter table student1 modify number BIGINT;

alter table student_data modify age TINYINT;

alter table student1 rename column email_id to email;

alter table student1 rename column course to branch;

DESCRIBE student1;

rename table student1 to student_data;

select * from student_data;


INSERT INTO student_data
(id, name, branch, marks, city, age, email)
VALUES
(1, 'Rahul', 'CSE', 88, 'Bangalore', 20, 'rahul@gmail.com'),
(2, 'Priya', 'ECE', 91, 'Hyderabad', 21, 'priya@gmail.com'),
(3, 'Arjun', 'ISE', 79, 'Mysore', 20, 'arjun@gmail.com'),
(4, 'Sneha', 'EEE', 95, 'Chennai', 22, 'sneha@gmail.com'),
(5, 'Kiran', 'ME', 84, 'Pune', 21, 'kiran@gmail.com'),
(6, 'Anjali', 'CSE', 90, 'Delhi', 20, 'anjali@gmail.com');

desc student_data;

alter table student_data drop column number;


alter table student_data drop PRIMARY KEY;

desc student_data;

SET SQL_SAFE_UPDATES = 0;
delete from student_data where id = 6;





