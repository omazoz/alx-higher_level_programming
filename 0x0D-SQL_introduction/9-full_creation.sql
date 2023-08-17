-- This script created by Oumayma Mazoz
-- creates a table 'second_table' in DB
CREATE TABLE IF NOT EXISTS second_table
(id INT,name VARCHAR(256),score INT);
-- query to insert rows into table
INSERT INTO second_table (id, name, score)
 VALUES (1, 'John', 10);
-- query to insert row into table
INSERT INTO second_table (id, name, score)
 VALUES (2, 'Alex', 3);
-- quert to insert row into table
INSERT INTO second_table (id, name, score)
 VALUES (3, 'Bob', 14);
-- query to insert row into table
INSERT INTO second_table (id, name, score)
 VALUES (4, 'George', 8);
