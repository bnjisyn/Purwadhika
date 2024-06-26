use world;

select
	city.Name as nama_kota,
	c.Name as Negara,
    city.Population
from country as c
left join city
on c.Code = city.CountryCode
order by city.Population 
desc limit 10;

select
	c.Name as Negara,
    c.GNP,
    city.Name as Capital,
    city.Population
from country as c
left join city
on c.Capital = city.ID
where
	(c.Name = 'Netherlands');

select
	c.Name as Negara,
    cl.percentage as Persentase
from country as c
left join countrylanguage as cl
on c.Code = cl.CountryCode
where cl.Language = 'Spanish'
order by cl.Percentage 
desc limit 10;

select
	c.Name as Negara,
    c.GNP,
    city.Name as Capital,
    city.Population
from country as c
left join city
on c.Capital = city.ID
where
	(c.Name = 'Indonesia');

select
	c.Name as Negara,
    c.GNP,
    city.Name as ibu_kota,
    city.Population as Populasi,
    cl.Language as Bahasa
from country as c
left join city
on c.Capital = city.ID
left join countrylanguage as cl
on c.Code = cl.CountryCode
where
	(c.Name = 'Indonesia') &
    (cl.isOfficial = 'T');
    
select 
	Continent, 
	count(Name) as jumlah_negara
from country
group by Continent
having 
	jumlah_negara > (
		select count(*) 
        from country 
        where Continent = 'North America'
    );

select name, GNP
from country
where
	(GNP > (
		select avg(GNP) 
        from country 
        where Continent = 'Europe'
    )) &
    (Continent = 'Asia')
order by GNP desc;

select 
	count(distinct Region) as jumlah_region, 
    Continent
from country
where
	Continent like '%a'
group by Continent
having
	count(distinct Region) > (
		select count(distinct Region) 
        from country 
        where Continent = 'Asia'
    );
