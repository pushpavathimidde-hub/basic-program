create database colleges1;
use colleges1;
 create table student2(
       student2id INT,
       student2name VARCHAR(30),
       age  INT,
       branch VARCHAR(5),
       email VARCHAR(20)
);

INSERT INTO student2 VALUES

(2,"Naveen",22,'AI','naveen@gmail.com'),
(2,"Rahul",21,'CSE','rahul@gmail.com'),
(2,"Priya",20,'BCE','priya@gmail.com'),
(2,"Anitha",23,'IT','Anitha@gmail.com'),
(2,"Kiran",22,'MECH','kiran@gmail.com');

select * from student2;

alter table student2 add phone_number INT;
select * from student2;
select student2name,branch from student2;
select * from student2 where age < 21;
select * from student2;
select * from student2 where branch = 'AI';


SELECT * FROM student2
ORDER BY age DESC;

UPDATE student2
SET age=25
WHERE student2id=2;