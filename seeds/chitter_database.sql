DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS peeps_id_seq;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text NOT NULL,
  email text NOT NULL,
  password text NOT NULL
);

CREATE TABLE peeps (
  id SERIAL PRIMARY KEY,
  content text NOT NULL,
  post_time TIMESTAMP ,
  user_id INTEGER REFERENCES users (id)
);


-- Inserting data into the users table
INSERT INTO users (username, email, password)
VALUES ('JohnDoe', 'johndoe@example.com', 'password123');

INSERT INTO users (username, email, password)
VALUES ('JaneSmith', 'janesmith@example.com', 'abc123');

-- Inserting data into the peeps table
INSERT INTO peeps (content, post_time, user_id)
VALUES ('Hello, world!', '2023-05-19 09:00:00', 1);

INSERT INTO peeps (content, post_time, user_id)
VALUES ('This is my first peep!', '2023-05-19 10:30:00', 2);


