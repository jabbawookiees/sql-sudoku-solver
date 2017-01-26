/*

This is for initializing postgresql with a user and a database for people who don't know how. :)
You will want to run `sudo -u postgres psql` after installing postgresql to access the SQL interface.
Then you can run the following lines:
*/

/* Create a user named 'somebody' that is able to login, with access to a database named 'something' */
CREATE USER somebody WITH LOGIN PASSWORD 'password';
CREATE DATABASE something;
GRANT ALL PRIVILEGES ON DATABASE something2 TO somebody2;

/* Switch to database 'something' */
\connect something

/* Create the database table 'digits' filled up with the 9 digits */
CREATE TABLE digits (value int);
INSERT INTO digits VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9);

/* Create all the other tables for the other solver as well! */

CREATE TABLE a0 (value int);
CREATE TABLE a1 (value int);
CREATE TABLE a2 (value int);
CREATE TABLE a3 (value int);
CREATE TABLE a4 (value int);
CREATE TABLE a5 (value int);
CREATE TABLE a6 (value int);
CREATE TABLE a7 (value int);
CREATE TABLE a8 (value int);

CREATE TABLE b0 (value int);
CREATE TABLE b1 (value int);
CREATE TABLE b2 (value int);
CREATE TABLE b3 (value int);
CREATE TABLE b4 (value int);
CREATE TABLE b5 (value int);
CREATE TABLE b6 (value int);
CREATE TABLE b7 (value int);
CREATE TABLE b8 (value int);

CREATE TABLE c0 (value int);
CREATE TABLE c1 (value int);
CREATE TABLE c2 (value int);
CREATE TABLE c3 (value int);
CREATE TABLE c4 (value int);
CREATE TABLE c5 (value int);
CREATE TABLE c6 (value int);
CREATE TABLE c7 (value int);
CREATE TABLE c8 (value int);

CREATE TABLE d0 (value int);
CREATE TABLE d1 (value int);
CREATE TABLE d2 (value int);
CREATE TABLE d3 (value int);
CREATE TABLE d4 (value int);
CREATE TABLE d5 (value int);
CREATE TABLE d6 (value int);
CREATE TABLE d7 (value int);
CREATE TABLE d8 (value int);

CREATE TABLE e0 (value int);
CREATE TABLE e1 (value int);
CREATE TABLE e2 (value int);
CREATE TABLE e3 (value int);
CREATE TABLE e4 (value int);
CREATE TABLE e5 (value int);
CREATE TABLE e6 (value int);
CREATE TABLE e7 (value int);
CREATE TABLE e8 (value int);

CREATE TABLE f0 (value int);
CREATE TABLE f1 (value int);
CREATE TABLE f2 (value int);
CREATE TABLE f3 (value int);
CREATE TABLE f4 (value int);
CREATE TABLE f5 (value int);
CREATE TABLE f6 (value int);
CREATE TABLE f7 (value int);
CREATE TABLE f8 (value int);

CREATE TABLE g0 (value int);
CREATE TABLE g1 (value int);
CREATE TABLE g2 (value int);
CREATE TABLE g3 (value int);
CREATE TABLE g4 (value int);
CREATE TABLE g5 (value int);
CREATE TABLE g6 (value int);
CREATE TABLE g7 (value int);
CREATE TABLE g8 (value int);

CREATE TABLE h0 (value int);
CREATE TABLE h1 (value int);
CREATE TABLE h2 (value int);
CREATE TABLE h3 (value int);
CREATE TABLE h4 (value int);
CREATE TABLE h5 (value int);
CREATE TABLE h6 (value int);
CREATE TABLE h7 (value int);
CREATE TABLE h8 (value int);

CREATE TABLE i0 (value int);
CREATE TABLE i1 (value int);
CREATE TABLE i2 (value int);
CREATE TABLE i3 (value int);
CREATE TABLE i4 (value int);
CREATE TABLE i5 (value int);
CREATE TABLE i6 (value int);
CREATE TABLE i7 (value int);
CREATE TABLE i8 (value int);

/* Since the tables were created by user postgres, we want to give somebody access to all of them */
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO somebody;
