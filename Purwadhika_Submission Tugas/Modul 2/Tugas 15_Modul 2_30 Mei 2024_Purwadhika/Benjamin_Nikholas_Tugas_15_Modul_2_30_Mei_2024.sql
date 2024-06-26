use sakila;

show tables;

select 
	title, 
    category, 
    length
from film_list
where category = 'Comedy'
order by length 
asc limit 10;

select 
	category as kategori,
    count(title) as jumlahMovie,
    sum(price)/count(title) as rataHargaSewa
from film_list
group by category
order by jumlahMovie desc;

select 
	rating,
    CASE 
        WHEN rating = 'G' THEN 'General Audiences'
        WHEN rating = 'PG' THEN 'Parental Guidance Suggested'
        WHEN rating = 'PG-13' THEN 'Parental Guidance for Children Under 13'
        WHEN rating = 'R' THEN 'Restricted'
        WHEN rating = 'NC-17' THEN 'No Children Under 17 Admitted'
        ELSE 'Unknown'
    END AS keterangan,
    count(title) as jumlahMovie
from film_list
group by rating
order by rating;

select
	a.actor_id,
    a.first_name,
    a.last_name,
    count(film_id) as jumlah_Movie
from actor as a
left join film_actor as fa
on a.actor_id = fa.actor_id
group by a.actor_id
order by 
	jumlah_Movie desc,
    first_name desc
limit 10;

select
	fl.category,
    count(fl.title) as jumlah_Movie
from actor as a
left join  film_actor as fa
on a.actor_id = fa.actor_id
left join film_list as fl
on fa.film_id = fl.FID
where 
	(a.first_name = 'GINA') &
    (a.last_name  = 'DEGENERES')
group by fl.category;

select
	fl.title,
    fl.category
from actor as a
left join  film_actor as fa
on a.actor_id = fa.actor_id
left join film_list as fl
on fa.film_id = fl.FID
where 
	(a.first_name = 'GINA') &
    (a.last_name  = 'DEGENERES') &
    (fl.category = 'Sci-Fi');

select
	a.actor_id,
    a.first_name,
    a.last_name,
    count(fl.title) as jumlah_Movie
from actor as a
left join  film_actor as fa
on a.actor_id = fa.actor_id
left join film_list as fl
on fa.film_id = fl.FID
where category = 'Horror'
group by a.actor_id
order by 
	jumlah_Movie desc,
    a.first_name asc
limit 10;

select
	fl.title,
    fl.category
from actor as a
left join  film_actor as fa
on a.actor_id = fa.actor_id
left join film_list as fl
on fa.film_id = fl.FID
where 
	(a.first_name = 'JULIA') &
    (a.last_name = 'MCQUEEN') &
    (fl.category = 'Horror');