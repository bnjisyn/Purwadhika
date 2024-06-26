use world;

select distinct continent as Benua 
from country
order by Benua asc;

select distinct Region
from country
where Region like "%Africa";

select Name, GNP 
from country
order by GNP desc limit 10;

select Language
from countrylanguage
where countrycode = 'IDN'
order by percentage desc limit 7;

select 
	Continent as Benua, 
	count(Name) as Jumlah_Negara
from country
group by Continent;

select 
	Continent as Benua, 
	sum(Population) as Populasi
from country
where 
	Continent not in ('Oceania', 'Antarctica')
group by Continent;

select 
	Continent, 
	sum(Population) as Populasi
from country
group by Continent
having sum(Population) > 700000000;

select Region, avg(GNP) as GNP
from country
group by Region
order by GNP desc limit 5;