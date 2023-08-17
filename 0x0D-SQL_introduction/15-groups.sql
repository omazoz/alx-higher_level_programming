-- script to count number of records  with same score
SELECT score,COUNT(*) AS 'number' FROM second_table
 GROUP BY score
 ORDER BY score DESC;
