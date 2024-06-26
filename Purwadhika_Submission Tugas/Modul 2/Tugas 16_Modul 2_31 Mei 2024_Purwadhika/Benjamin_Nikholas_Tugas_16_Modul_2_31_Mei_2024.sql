use world;

show tables;

select 
	c.Name as Country_Name, 
	count(cl.Language) as Total_Language
from country as c
left join countrylanguage as cl
on c.Code = cl.CountryCode
group by c.Name
having count(cl.Language) > (
	select avg(len_lang) as avg_lang
    from (
		select count(language) as len_lang
        from countrylanguage
        group by CountryCode
    ) as lang_len_data)
order by 
	Total_Language desc,
    Country_Name desc
limit 10;

select 
    Name as Country_Name,
    GovernmentForm,
    tb_wp.World_Population,
    (Population / (
		select sum(Population) from country
    ) * 100) AS Pop_Percentage,
    @row_num := @row_num + 1 as row_index
from 
    country,
    (select sum(population) as World_Population from country) as tb_wp,
    (select @row_num := 0) as r
order by
    Pop_Percentage desc
limit 10;

select
	c.Continent,
    c.Region,
    count(city.Name) as Number_of_City,
    row_number() over (
		partition by c.Continent 
    ) as row_group
from country as c
left join city
on c.Code = city.CountryCode
where 
	c.Continent = ('Asia') or 
    c.Continent = ('Europe')
group by c.Region, c.Continent;

select 
	c.Continent,
    sum(city.Population) as Total_Capital_Population,
    avg(c.GNP) as Average_GNP,
    rank() over (
		order by sum(city.Population) desc
    ) as Rank_Population,
    rank() over (
		order by avg(c.GNP) desc
    ) as Rank_GNP
from country as c
left join city
on c.Capital = city.ID
group by c.Continent
having
	sum(city.Population) is not null
order by Total_Capital_Population desc;


select *
from country as c
left join city
on c.Capital = city.ID;

select * from city;
select * from country;

select 
    Name,
    GNP_Percentage,
    Cumulative_GNP,
    GNP_Rank,
    ceil((GNP_Rank - 0.01) / 4) AS Market_Priority_1234
from (
    select 
        Name,
        GNP_Percentage,
        Cumulative_GNP,
        GNP_Rank
    from (
        select 
            Name,
            GNP_Percentage,
            sum(GNP_Percentage) over (
				order by GNP_Percentage desc
            ) as Cumulative_GNP,
            row_number() over (
				order by GNP_Percentage desc
            ) as GNP_Rank
        from (
            select 
                Name,
                round((GNP / (
					select sum(GNP) 
                    from country
                )) * 100, 2) as GNP_Percentage
            from country
        ) as subquery
    ) as ranked_countries
) as final
order by GNP_Percentage desc;