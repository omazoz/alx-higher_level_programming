-- This script created by Oumayma Mazoz
-- script for listing average temp per city
SELECT city, AVG(value) AS avg_temp
 FROM temperatures
 GROUP BY city
 ORDER BY AVG(value) DESC;
