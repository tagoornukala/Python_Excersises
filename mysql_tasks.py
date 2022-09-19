# 1.Find the employee whose job code is 669.


mysql> SELECT * from employee where Jcode=669;
+-------+----------+-------+-------+------------+---------+------------+-------+
| EmpNo | EName    | Jcode | MgrNo | HireDate   | Salary  | Commission | DepNo |
+-------+----------+-------+-------+------------+---------+------------+-------+
|     3 | Pradeep  |   669 |     1 | 2005-10-10 | 1000000 |       NULL |    40 |
|     4 | Srinivas |   669 |     1 | 2005-05-08 | 1000000 |       NULL |    30 |
+-------+----------+-------+-------+------------+---------+------------+-------+
2 rows in set (0.00 sec)

# 2.Find the employee joining before 2007.
mysql> select * from employee where HireDate<'2007-01-01';
+-------+----------+-------+-------+------------+---------+------------+-------+
| EmpNo | EName    | Jcode | MgrNo | HireDate   | Salary  | Commission | DepNo |
+-------+----------+-------+-------+------------+---------+------------+-------+
|     1 | Venkat   |   672 |  NULL | 2006-02-01 | 1200000 |   10000.00 |    40 |
|     3 | Pradeep  |   669 |     1 | 2005-10-10 | 1000000 |       NULL |    40 |
|     4 | Srinivas |   669 |     1 | 2005-05-08 | 1000000 |       NULL |    30 |
|     5 | Krishna  |   668 |     2 | 2005-10-09 |  500000 |   20000.00 |    22 |
|     7 | Keerthi  |   668 |     4 | 2006-06-05 |  600000 |       NULL |    24 |
+-------+----------+-------+-------+------------+---------+------------+-------+
5 rows in set (0.00 sec)


# 3.Find the details of employee whose name contain john.
mysql> select * from employee where EName='john';
Empty set (0.00 sec)


# 4.Find the details of employee whose commision is more than their salary.
mysql> select * from employee where Commission>Salary;
Empty set (0.00 sec)

# 5.Find the list of employee who do not have manager.
mysql> select Ename from employee where MgrNo is NULL;
+--------+
| Ename  |
+--------+
| Venkat |
+--------+
1 row in set (0.00 sec)


# 6.Find the employee having more than 1year experience and still a trainee.

mysql> select ename from employee where experience>=1;
+----------+
| ename    |
+----------+
| Venkat   |
| Pradeep  |
| Srinivas |
| Deepa    |
| Keerthi  |
+----------+


#7.display the employee name and job name of all the employee;
mysql> select ename,jname from employee,job where employee.jcode = job.jcode;
+----------+-------------+
| ename    | jname       |
+----------+-------------+
| Nirmala  | President   |
| Pradeep  | SalesPerson |
| Srinivas | SalesPerson |
| Krishna  | Analyst     |
| Deepa    | Analyst     |
| Keerthi  | Analyst     |
+----------+-------------+
6 rows in set (0.00 sec)


# 8.display department name and its loaction name for all departments

mysql> select dname,lname from department d,location l where d.lcode = l.lcode;
+-------------+---------+
| dname       | lname   |
+-------------+---------+
| Accounting  | Chicago |
| Research    | NewYark |
| Finance     | Chicago |
| Sales       | Chicago |
| HR          | Chicago |
| Sales       | Atlanta |
| Operataions | Paris   |
+-------------+---------+
7 rows in set (0.00 s


               
# 9.display employee name and job name of all the employee in department no 30.


mysql> select ename,jname from employee e,job j where e.depno=30 and j.deptno=30;
+----------+---------+
| ename    | jname   |
+----------+---------+
| Srinivas | Manager |
+----------+---------+
1 row in set (0.00 sec)


# 10.display employee name and department name for all analyst.

mysql> select ename,dname from employee,department,job where employee.depno=department.deptno and employee.jcode=job.jcode and jname='Analyst';
+---------+---------+
| ename   | dname   |
+---------+---------+
| Krishna | Finance |
| Deepa   | Sales   |
| Keerthi | HR      |
+---------+---------+
3 rows in set (0.00 sec)
               
# 11.write a query to display all the department names amd their location names.


mysql> select dname,lname from department d,location l where d.lcode = l.lcode;
+-------------+---------+
| dname       | lname   |
+-------------+---------+
| Accounting  | Chicago |
| Research    | NewYark |
| Finance     | Chicago |
| Sales       | Chicago |
| HR          | Chicago |
| Sales       | Atlanta |
| Operataions | Paris   |
+-------------+---------+
7 rows in set (0.00 sec)


# 12.write a query to display the name jobname department name and location of every employee.


mysql> select ename,jname,dname,lname from employee e,job j,department d,location l where e.jcode = j.jcode and d.lcode=l.lcode and d.deptno=e.depno;
+----------+-------------+-------------+---------+
| ename    | jname       | dname       | lname   |
+----------+-------------+-------------+---------+
| Nirmala  | President   | Research    | NewYark |
| Pradeep  | SalesPerson | Operataions | Paris   |
| Srinivas | SalesPerson | Sales       | Atlanta |
| Krishna  | Analyst     | Finance     | Chicago |
| Deepa    | Analyst     | Sales       | Chicago |
| Keerthi  | Analyst     | HR          | Chicago |
+----------+-------------+-------------+---------+
6 rows in set (0.00 sec)


# 13.write a query to display the list of department with at least one analyst along with their location name.


mysql> select dname,lname from department,location where department.lcode=location.lcode;
+-------------+---------+
| dname       | lname   |
+-------------+---------+
| Accounting  | Chicago |
| Research    | NewYark |
| Finance     | Chicago |
| Sales       | Chicago |
| HR          | Chicago |
| Sales       | Atlanta |
| Operataions | Paris   |
+-------------+---------+
7 rows in set (0.00 sec)

               
               
