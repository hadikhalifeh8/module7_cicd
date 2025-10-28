-- Create a new user
CREATE ROLE myuser WITH LOGIN PASSWORD 'mypassword';

-- Allow the user to create databases (optional)
ALTER ROLE myuser CREATEDB;

-- Create the app database
CREATE DATABASE myappdb OWNER myuser;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE myappdb TO myuser;

-- Exit
\q