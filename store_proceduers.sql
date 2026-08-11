DELIMITER //
CREATE PROCEDURE get_students()
BEGIN
     SELECT * FROM students;
END //
DELIMITER;

CALL get_students()

DELIMITER //
CREATE PROCEDURE get_students_mark(
      IN minimum_marks INT,
	)
BEGIN
     SELECT * FROM students WHERE marks >= minimum_marks;
END //
DELIMITER ;

CALL get_students_mark(80)

DELIMITER //
CREATE PROCEDURE get_students_mar(
      IN minimum_marks INT,
      IN max_marks INT
	)
BEGIN
     SELECT * FROM students WHERE marks between minimum_marks AND max_marks;
END //
DELIMITER ;

CALL get_students_between_mar(80,90)



