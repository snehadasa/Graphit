-- script that prepares a MySQL server for Graphit project
-- database graphit_db
CREATE DATABASE IF NOT EXISTS graphit_db;
CREATE USER IF NOT EXISTS graphit_user@localhost IDENTIFIED BY "graphit_pwd";
GRANT ALL PRIVILEGES ON graphit_db.* TO graphit_user@localhost;
GRANT SELECT ON performance_schema.* TO graphit_user@localhost;
