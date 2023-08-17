-- script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- user_0d_1 should have all privileges on your MySQL server
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
