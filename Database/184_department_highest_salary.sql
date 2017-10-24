/*
The Employee table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
The Department table holds all departments of the company.

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, Max has the highest salary in the IT department and Henry has the highest salary in the Sales department.

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
*/

select d.Name as Department, t.Name as Employee, t.Salary
from
(select e1.Id, e1.Name, e1.Salary, e1.DepartmentId, count(distinct e2.Salary) as Rank
from Employee e1 join Employee e2 on (e1.Salary <= e2.Salary and e1.DepartmentId = e2.DepartmentId)
group by e1.Id) t
join Department d on (t.DepartmentId = d.Id)
where t.Rank = 1
;


--------
--faster
select d.Name as Department,
       e.Name as Employee,
       e.Salary
from Employee e join Department d on (e.DepartmentId = d.Id)
where (d.Id, e.Salary) in
    (select DepartmentId, max(Salary)
     from Employee
     group by DepartmentId)
;