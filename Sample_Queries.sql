use Grading_Man_Sys; 
select * from grades; 
select * from student;

start transaction;
	CALL viewSCourses(3102); 
commit;    
    
start transaction;
	CALL viewTCourses(101); 
commit;    
    
start transaction;
	CALL viewTGrades(372,102); 
commit;    
    
start transaction;
	CALL viewSGrades(3104,211); 
commit;    
    
start transaction;
	CALL viewStudPerf(3104); 
commit;    
    
start transaction;
	CALL addGradeAS1(342,3110,103,'A'); 
commit;    
    
start transaction;
	CALL addGradeAS2(342,3110,103,'B');
commit;    
    
start transaction;
	CALL addGradeMS(342,3110,103,'A');
commit;    
    
start transaction;
	CALL addGradeES(342,3110,103,'C');
commit;    
    
start transaction;
	CALL addGradeFG(342,3110,103,'B');
commit;    
    
start transaction;
	CALL PerformanceRep(3111,211); 
commit;    
    
start transaction;
	CALL UpdateStud(3102,"Atishi","rahulfan29"); 
commit;    
    
start transaction;
	CALL ListStudent(212,101,'C'); 
commit;    
    
start transaction;
	CALL LowestGrade(372,102); 
commit;    
    
select * from grades; 
select * from student; 
