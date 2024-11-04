select artists, count(*) as total 
    from songs 
    group by artists 
    order by total desc
    limit 1; 
