create schema Grading_Man_Sys; 
use Grading_Man_Sys; 

DROP TABLE IF EXISTS `student`;
create table student (
	studName varchar(30) not null,
    studID int not null unique,
    sysPwd varchar(30) not null,
    
    primary key(studID)
); 

DROP TABLE IF EXISTS `teacher`;
create table teacher (
	teacName varchar(30) not null,
    teacID int not null unique,
    sysPwd varchar(30) not null,
    
    primary key(teacID)
); 

DROP TABLE IF EXISTS `course`;
create table course (
	courseName varchar(30) not null,
    courseID int not null unique,
	courseCreds int not null,
    
    primary key(courseID)
); 

DROP TABLE IF EXISTS `courseTaken`;
create table courseTaken (
	studID int not null, 
	courseID int not null, 
	
	foreign key(studID) references student(studID) on delete cascade, 
	foreign key(courseID) references course(courseID) on delete cascade, 
	primary key(studID, courseID)
); 

DROP TABLE IF EXISTS `courseTaught`;
create table courseTaught (
	teacID int not null, 
	courseID int not null, 
	
	foreign key(teacID) references teacher(teacID) on delete cascade, 
	foreign key(courseID) references course(courseID) on delete cascade, 
	primary key(teacID, courseID)
); 

DROP TABLE IF EXISTS `grades`;
create table grades (
	studID int not null, 
	courseID int not null, 
    teacID int not null, 
    assig1 char, 
    midsem char,
    assig2 char,
    endsem char,
	finalGrade char,	
	foreign key(studID) references student(studID) on delete cascade,, 
	foreign key(courseID) references course(courseID) on delete cascade, 
    foreign key(teacID) references teacher(teacID) on delete cascade,
	primary key(studID,courseID,teacID)
); 

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `viewSCourses`(IN tstudID int)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID, Output - Courses taken by the student'
BEGIN
	SELECT * FROM course where courseID in (SELECT courseID FROM courseTaken WHERE studID = tstudID);
END$$ 



DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `viewTCourses`(IN tteachID int)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID , Output - Courses taught by the teacher'
BEGIN
	SELECT * FROM course where courseID in (SELECT courseID FROM courseTaught WHERE teacID = tteachID);
END$$



DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `verifySPass`(IN tstudID int, IN pwd varchar(30))
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID and entered password, Output -  Verification of the password'
BEGIN
	IF(tstudID in (select studID from student)) THEN
		DECLARE temppwd varchar(30);
		DECLARE tname varchar(30);
		SELECT sysPwd INTO temppwd FROM student WHERE studID = tstudID;
		SELECT studName INTO tname FROM student WHERE studID = tstudID;
		IF temppwd = pwd THEN
			SELECT 'Welcome ', tname;
		ELSE
			SELECT 'Incorrect Password';
		END IF; 
	ELSE 
		SELECT 'Student ID does not exist';
	END IF;
	
END$$ 



DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `verifyTPass`(IN tteacID int, IN pwd varchar(30))
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID and Course ID, Output - Verification of the password'
BEGIN
	IF(tteachID in (select teachID from teacher)) THEN 
		DECLARE temppwd varchar(30);
		DECLARE tname varchar(30);
		SELECT sysPwd INTO temppwd FROM teacher WHERE teacID = tteacID;
		SELECT teacName INTO tname FROM teacher WHERE teacID = tteacID;
		IF temppwd = pwd THEN
			SELECT 'Welcome ', tname;
		ELSE
			SELECT 'Incorrect Password';
		END IF;
	ELSE 
		SELECT 'Teacher ID does not exist';
	END IF;

END$$ 



DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `viewTGrades`(IN tcourseID int, IN tteachID int)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input -Course ID and Teacher ID, Output - Grades of all students in the particular course taught by the teacher'
BEGIN
	IF((SELECT COUNT(*) FROM courseTaught WHERE courseID = tcourseID AND teacID = tteachID) = 0) THEN
		SELECT 'Teacher is not teaching this course';
	ELSE
		SELECT student.studName as 'Student', grades.assig1 as 'Assignment-1', grades.midsem as 'Midsem', grades.assig2 as 'Assignment-2', grades.endsem as 'Endsem' 
			FROM grades, student 
			WHERE grades.courseID = tcourseID AND grades.teacID = tteachID AND grades.studID = student.studID;
	END IF;
END$$



DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `viewSGrades`(IN tstudID int, IN tcourseID int)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID and Course ID, Output - Grades for the course'
BEGIN

	IF((SELECT COUNT(*) FROM courseTaken WHERE courseID = tcourseID AND studID = tstudID) = 0) THEN
		SELECT 'Student is not taking this course';
	ELSE
		SELECT grades.assig1 as 'Assignment-1', grades.midsem as 'Midsem', grades.assig2 as 'Assignment-2', grades.endsem as 'Endsem'  
			FROM grades 
			WHERE studID = tstudID AND courseID = tcourseID;
	END IF;
END$$ 


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `viewStudPerf`(IN tstudID int)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID, Output - Grades of all courses taken by the student'
BEGIN
	SELECT course.courseName as 'Course Name', grades.assig1 as 'Assignment-1', grades.midsem as 'Midsem', grades.assig2 as 'Assignment-2', grades.endsem as 'Endsem'  
		FROM grades, course 
		WHERE grades.courseID = course.courseID AND grades.studID = tstudID;
END$$ 


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `addGradeAS1`(IN tcourseID int, IN tstudID int, IN tteachID int, IN tgrade char)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID Course ID and Grade of specify component, Output -'
BEGIN
	IF((SELECT COUNT(*) FROM courseTaken WHERE courseID = tcourseID AND studID = tstudID) = 0) THEN
		SELECT 'Student is not taking this course';
	ELSE IF((SELECT COUNT(*) FROM courseTaught WHERE courseID = tcourseID AND teacID = tteachID) = 0) THEN 
		SELECT 'Teacher is not teaching this course';
	ELSE
		UPDATE grades SET assig1 = tgrade WHERE courseID = tcourseID AND studID = tstudID AND teacID = tteachID;
	END IF;
END$$ 


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `addGradeAS2`(IN tcourseID int, IN tstudID int, IN tteachID int, IN tgrade char)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID Course ID and Grade of specify component, Output -'
BEGIN
	IF((SELECT COUNT(*) FROM courseTaken WHERE courseID = tcourseID AND studID = tstudID) = 0) THEN
		SELECT 'Student is not taking this course';
	ELSE IF((SELECT COUNT(*) FROM courseTaught WHERE courseID = tcourseID AND teacID = tteachID) = 0) THEN 
		SELECT 'Teacher is not teaching this course';
	ELSE
		UPDATE grades SET assig2 = tgrade WHERE courseID = tcourseID AND studID = tstudID AND teacID = tteachID;
	END IF;
END$$ 


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `addGradeMS`(IN tcourseID int, IN tstudID int, IN tteachID int, IN tgrade char)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID Course ID and Grade of specify component, Output -'
BEGIN
	IF((SELECT COUNT(*) FROM courseTaken WHERE courseID = tcourseID AND studID = tstudID) = 0) THEN
		SELECT 'Student is not taking this course';
	ELSE IF((SELECT COUNT(*) FROM courseTaught WHERE courseID = tcourseID AND teacID = tteachID) = 0) THEN 
		SELECT 'Teacher is not teaching this course';
	ELSE
		UPDATE grades SET midsem = tgrade WHERE courseID = tcourseID AND studID = tstudID AND teacID = tteachID;
	END IF;
END$$


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `addGradeES`(IN tcourseID int, IN tstudID int, IN tteachID int, IN tgrade char)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID Course ID and Grade of specify component, Output -'
BEGIN
	IF((SELECT COUNT(*) FROM courseTaken WHERE courseID = tcourseID AND studID = tstudID) = 0) THEN
		SELECT 'Student is not taking this course';
	ELSE IF((SELECT COUNT(*) FROM courseTaught WHERE courseID = tcourseID AND teacID = tteachID) = 0) THEN 
		SELECT 'Teacher is not teaching this course';
	ELSE
		UPDATE grades SET endsem = tgrade WHERE courseID = tcourseID AND studID = tstudID AND teacID = tteachID;
	END IF;
END$$


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `addGradeFG`(IN tcourseID int, IN tstudID int, IN tteachID int, IN tgrade char)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID Course ID and Grade of specify component, Output -'
BEGIN
	IF((SELECT COUNT(*) FROM courseTaken WHERE courseID = tcourseID AND studID = tstudID) = 0) THEN
		SELECT 'Student is not taking this course';
	ELSE IF((SELECT COUNT(*) FROM courseTaught WHERE courseID = tcourseID AND teacID = tteachID) = 0) THEN 
		SELECT 'Teacher is not teaching this course';
	ELSE
		UPDATE grades SET finalGrade = tgrade WHERE courseID = tcourseID AND studID = tstudID AND teacID = tteachID;
	END IF;
END$$ 


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `PerformanceRep`(IN tstudID int, IN tcourseID int)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Student ID, Output - Grades of all courses taken by the student'
BEGIN 
	DECLARE tmidsem char; 
	DECLARE final char; 
	SELECT midsem INTO tmidsem FROM grades WHERE studID = tstudID AND courseID = tcourseID;
	SELECT finalGrade INTO final FROM grades WHERE studID = tstudID AND courseID = tcourseID; 

	IF((SELECT COUNT(*) FROM courseTaken WHERE courseID = tcourseID AND studID = tstudID) = 0) THEN
		SELECT 'Student is not taking this course';
	ELSE
		IF (strcmp(tmidsem, endsem) = 1) THEN
			SELECT 'Student is doing well in the course Final grade has improved'; 
		ELSE IF(strcmp(tmidsem, endsem) = 0) THEN 
			SELECT 'Student has not made any progress in the course. Final and Midsem grades are the same'; 
		ELSE 
			SELECT 'Student is not doing well in the course Final grade has decreased'; 
		END IF;
	END IF;
END$$


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `NewStudent`(IN tstudID int, IN tname varchar(30), IN tpwd varchar(30))
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - New Student Details, Output -'
BEGIN
	IF((SELECT COUNT(*) FROM student WHERE studID = tstudID) = 0) THEN
		INSERT INTO student VALUES (tstudID, tname, tpwd);
	ELSE
		SELECT 'Student already exists';
	END IF;
END$$ 


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `NewTeacher`(IN tteacID int, IN tname varchar(30), IN tpwd varchar(30))
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - New Teacher Details, Output -'
BEGIN
	IF((SELECT COUNT(*) FROM teacher WHERE teacID = tteacID) = 0) THEN
		INSERT INTO teacher VALUES (tteacID, tname, tpwd);
	ELSE
		SELECT 'Teacher already exists';
	END IF;
END$$ 


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `NewStudent`(IN tstudID int, IN tname varchar(30), IN tpwd varchar(30))
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - New Student Details, Output -'
BEGIN
	IF((SELECT COUNT(*) FROM student WHERE studID = tstudID) = 0) THEN
		SELECT 'Student doesnt exist';
	ELSE
		UPDATE student SET studName = tname, studPwd = tpwd WHERE studID = tstudID;
	END IF;
END$$ 



DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `RemoveTeac`(IN tteacID int)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input -Teacher ID, Output -'
BEGIN
	IF((SELECT COUNT(*) FROM teacher WHERE teacID = tteacID) = 0) THEN
		SELECT 'Teacher doesnt exist';
	ELSE
		DELETE FROM teacher WHERE teacID = tteacID;
	END IF;
END$$ 



DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `ListStudent`(IN tcourseID int, IN tteachID int, IN tgrade char)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Course ID and Grade , Output - List of Students with a grade better than the input grade'
BEGIN
	IF((SELECT COUNT(*) FROM courseTaught WHERE courseID = tcourseID AND teacID = tteachID) = 0) THEN
		SELECT 'Teacher is not teaching this course';
	ELSE
		SELECT count(studID) 
		FROM grades 
		where courseID = tcourseID AND teacID = tteachID AND (finalGrade < tgrade);
	END IF;
END$$  


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `ListStudent`(IN tcourseID int, IN tteachID int)
READS SQL DATA
NOT DETERMINISTIC
SQL SECURITY INVOKER
COMMENT 'Input - Course ID , Output - Lowest grade of the course'
BEGIN
	IF((SELECT COUNT(*) FROM courseTaught WHERE courseID = tcourseID AND teacID = tteachID) = 0) THEN
		SELECT 'Teacher is not teaching this course';
	ELSE
		SELECT max(finalGrade) 
		FROM grades 
		where courseID = tcourseID AND teacID = tteachID;
	END IF;
END$$
