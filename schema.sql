
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username varchar(40) NOT NULL,
    email varchar(255) NOT NULL,
    password varchar(100) NOT NULL
);