
-- Roll Up SQL
SELECT  C.continent, C.name, AVG(H.numberofdeathinfant),
FROM fact_table as F, month as M, country as C, helth as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = H.healthKey 
and C.continent='North America'
GROUP BY M.year, ROLLUP(  C.continent, C.name)
ORDER BY C.continent

-- Drill down SQL

SELECT  M.year, M.quater, M.month, C.name, AVG(H.numberofdeathinfant)
FROM fact_table as F, month as M, country as C, helth as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = H.healthKey 
and C.continent='North America'
GROUP BY M.year, M.quater, M.month, C.name;

-- Slicing
SELECT   M.month, C.name, AVG(H.numberofdeathinfant)
FROM fact_table as F, month as M, country as C, helth as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = H.healthKey 
and C.name='Canada'
GROUP BY M.year, M.quater, M.month, C.name;

-- Dicing
SELECT COUNT(*) M.year, C.name, E.name, 
FROM fact_table as F, month as M, country as C, event as e
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.eventKey = E.eventKey
and C.continent='Africa' and E.name in ('Epidemic', 'Flood', 'Armed conflict', 'Civil war')
GROUP BY (C.name, E.name , M.year);




 




-- Combining OLAP operations


-- Iceberg queries

-- Windowing queries

-- Using the Window clause




    

