-- Roll Up SQL
SELECT  C.continent, C.name, AVG(H.numberofdeathinfant),
FROM fact_table as F, month as M, country as C, helth as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = H.healthKey 
GROUP BY M.year, ROLLUP(  C.continent, C.name)
ORDER BY C.continent

-- Drill down SQL
SELECT  M.year, M.quater, M.month, C.name, AVG(H.numberofdeathinfant)
FROM fact_table as F, month as M, country as C, helth as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = H.healthKey 
GROUP BY M.year, M.quater, M.month, C.name;

-- Slicing
SELECT   M.month, C.name, AVG(H.numberofdeathinfant)
FROM fact_table as F, month as M, country as C, helth as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = H.healthKey 
and C.name='Canada'
GROUP BY M.year, M.quater, M.month, C.name;

-- Dicing
SELECT COUNT(*) M.year, C.name, E.name, 
FROM fact_table as F, month as M, country as C, event as E
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.eventKey = E.eventKey
and C.continent='Africa' and E.name in ('Epidemic', 'Flood', 'Armed conflict', 'Civil war') and M.year > 2005
GROUP BY (C.name, E.name , M.year);

SELECT  M.quater, C.name, AVG(E.primarySchoolEnrollment)
FROM fact_table as F, month as M, country as C, education as E
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.educationKey = E.educationKey
and C.continent='Africa' and M.quater='1'
GROUP BY (C.name, M.quater);

-- Combining OLAP operations

--  roll up and slice
SELECT  C.continent, C.name, AVG(H.numberofdeathinfant), M.quater,
FROM fact_table as F, month as M, country as C, helth as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = H.healthKey 
and C.continent='North America' and M.quater = '1'
GROUP BY M.year, ROLLUP(  C.continent, C.name)
ORDER BY C.continent

-- dice and slice
SELECT COUNT(*) M.year, C.name, E.name, AVG(E.economic_damage)
FROM fact_table as F, month as M, country as C, event as E
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.eventKey = E.eventKey
and C.continent='Africa' and E.name in ('Epidemic', 'Flood', 'Armed conflict', 'Civil war') and M.year > 2005 and M.year < 2010
GROUP BY (C.name, E.name , M.year);


-- drill down and slice
SELECT  M.year, M.quater, M.month, C.name, AVG(H.numberofdeathinfant)
FROM fact_table as F, month as M, country as C, helth as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = H.healthKey 
and M.month='January' and C.name in ('Epidemic', 'Flood', 'Armed conflict', 'Civil war') and M.year > 2005 and M.year < 2010
GROUP BY M.year, M.quater, M.month, C.name;

-- roll up and slice
SELECT C.name, H.adultsWithHIV, M.month, M.year
FROM fact_table as F, month as M, country as C, helth as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = E.healthKey
and C.continent='Africa' and M.year='2020'
GROUP BY M.year, ROLLUP(  C.continent, C.name)
ORDER BY H.adultsWithHIV DESC

-- Iceberg queries
SELECT C.name, H.adultsWithHIV, M.month, M.year
FROM fact_table as F, month as M, country as C, health as H
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.healthKey = E.healthKey
and C.continent='Africa' and M.year='2020'
ORDER BY H.adultsWithHIV DESC
OPTIMIZE FOR 10 ROWS 

-- Windowing queries
SELECT e.country, e.name, e.casualties, AVG(e.casualties),
OVER (PARTITION BY e.country)
FROM fact_table as F, month as M, country as C, event as E;  
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.eventKey = E.eventKey
and C.continent='North America' and M.year > 2015 and e.name in ('Hurricane', 'Wildfire', 'Flood', 'Winter storm', 'Earthquake', 'Heat wave')

-- Using the Window clause 

SELECT e.country, M.month, e.name, AVG(e.casualties) OVER W AS movavg
FROM fact_table as F, month as M, country as C, event as E;  
WHERE F.monthKey = M.monthKey and F.countryKey = C.countryKey and F.eventKey = E.eventKey
WINDOW W AS (PARTITION BY e.country ORDER BY M.Month
        RANGE BETWEEN INTERVAL `1´ MONTH PERCEEDING AND INTERVAL `1´ MONTH FOLLOWING) 





