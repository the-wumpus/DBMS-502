/*
find the names of students who have taken a course taught by instructor WU
*/
select s.name
from instructor i, teaches t, student s, takes tk
where i.name = "Wu" and i.ID = t.ID and s.ID = tk.ID and t.course_id = tk.course_id;

/*
find the number  of students who have taken a course taught by instructor WU
*/
select count(*)
from instructor i, teaches t,  takes tk
where i.name = "Wu" and i.ID = t.ID and  t.course_id = tk.course_id;

/*
find the unique departments who have a course listed in the university
*/
select distinct dept_name 
from course;

/* find all instructors with two letters in name */
select *
from instructor i
where i.name like "__";

/* find all instructors with 4 or more letters in name */
select *
from instructor i
where i.name like "____%";

select *
from student;

select *
from student
where name like "sh%";

/* find dept where average of tot_cred is greater than 50 */
select s.dept_name, avg(s.tot_cred) as avgCred
from student s
group by s.dept_name
having avgCred > 50;

/* Which studio spent the most in the year 2014 (i.e. the sum of the budgets of the movies that the studio produced was the highest)? */
/* using view */

create view V2 as
select m.StudioName, sum(m.Budget) as totalBudget
from movie m
where m.Year = "2014" 
group by m.StudioName;
select *
from V2
where totalBudget = (select max(totalBudget) from V2);

/*Which movie stars have the highest net worth?*/
select *
from moviestar 
where NetWorth = (select max(NetWorth) from moviestar);

/* Which movies have the average netWorth of the movie stars greater than the average networth of all movie stars? */
/* using view */

create view v4 as
select avg(networth) as avgNet
from moviestar;

select s.movietitle, avg(m.NetWorth) as avgNW
from starsin s, moviestar m
where s.starName = m.Name
group by s.movieTitle
having avgNW > (select avgNet from V4);

/* without view */

select s.movietitle, avg(m.NetWorth) as avgNW
from starsin s, moviestar m
where s.starName = m.Name
group by s.movieTitle
having avgNW > (select avg(NetWorth) from moviestar);


/* Find the movies whose title starts with B and were released in 2014 */
select m.title
from movie m
where m.Title like "B%";

/* What is the runtime and title of the movie that has the maximum number of stars? Hint: Count the number of stars in each movie. 
 Then, find the movie name that has the maximum number
of stars, and then find the runtime and title of this movie. */

create view v3 as
select s.movieTitle, m.Length, count(s.starname) as numstars
from starsin s, movie m
where s.movieTitle = m.Title
group by s.movieTitle;

select *
from v3
where numstars = (select max(numstars) from v3);







