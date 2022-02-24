CREATE TABLE books(
	accession_no VARCHAR(256) PRIMARY KEY,
    title VARCHAR(256) NOT NULL,
    isbn VARCHAR(256) NOT NULL,
    publisher VARCHAR(256) NOT NULL,
    pulbication_year YEAR NOT NULL 
);
