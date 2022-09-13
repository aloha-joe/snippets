-- part1
CREATE TABLE users (
id serial,
login varchar(64),
pass varchar(64),
active bool DEFAULT true,
CONSTRAINT login_unique UNIQUE (login)
);

-- part2
INSERT INTO users (
login, pass, active)
VALUES ('test_user_1', 'test_pass_1', True);
INSERT INTO users (
login, pass, active)
VALUES ('test_user_2', 'test_pass_2', True);

-- part3
UPDATE users SET active = FALSE
WHERE login = 'test_user_2';

-- part4
ALTER TABLE users ADD COLUMN blocked bool;

-- part5
INSERT INTO users (
login, pass, active)
VALUES ('test_user_3', 'test_pass_3', True);

-- part6
DELETE FROM users
WHERE login = 'test_user_2';

-- part7
DELETE FROM users;