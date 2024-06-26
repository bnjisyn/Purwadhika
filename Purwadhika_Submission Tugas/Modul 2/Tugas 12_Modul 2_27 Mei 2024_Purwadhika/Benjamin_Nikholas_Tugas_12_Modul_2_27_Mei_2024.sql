use world;

select c.Name as Negara, c.GNP
from country as c
left join countrylanguage as cl
on c.Code = cl.CountryCode
where (cl.Language = 'English') 
	& (cl.Percentage > 50.0)
order by c.GNP desc limit 5;

select c.Name
from country as c
left join countrylanguage as cl
on c.Code = cl.CountryCode
where (cl.Language = 'English') 
	& (cl.Percentage > 50.0)
order by cl.Percentage desc limit 7;

select 
	city.Name as nama_kota, 
	c.Name as negara, city.Population
from country as c
left join city
on c.Code = city.CountryCode
order by city.Population 
desc limit 10;

select 
	city.Name as nama_kota, 
	city.District as Provinsi, 
	c.Name as Negara, 
	city.Population as Populasi
from country as c
left join city
on c.Code = city.CountryCode
where c.Name = 'Indonesia'
order by city.Population 
desc limit 10;

select 
	Name as Nama,
	Continent as Benua,
    LifeExpectancy as AngkaHarapanHidup,
    GNP
from country
where
	(Continent = 'Asia') & 
    (LifeExpectancy > (
		select avg(LifeExpectancy) 
        from country
    ))
order by AngkaHarapanHidup desc;

select
	c.Name as Negara,
    c.Population as Populasi_Negara,
    c.GNP,
    city.Name as Ibu_Kota,
    city.Population as Populasi_Ibukota
from country as c
left join city
on c.Capital = city.ID
where c.Region = 'Southeast Asia'
order by c.Name;