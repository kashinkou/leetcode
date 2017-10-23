select x.Name as Employee
from Employee x
join Employee y on (x.ManagerId = y.Id)
where x.Salary > y.Salary
;
