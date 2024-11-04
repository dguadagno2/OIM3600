"""
This SQL is meant to find the average danceability and energy of songs produced by Drake
this search utilizes two of the criteria that is used in creating the aura charactistic from spotify 
to tell the aura characteristic of Drake's catalog 
"""
select * 
    from artists
    join avg(danceability) and avg(energy) 
    where name='Drake'
