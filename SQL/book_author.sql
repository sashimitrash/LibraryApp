CREATE TABLE book_author(
	author_name VARCHAR(256) NOT NULL,
    book_accession VARCHAR(256) NOT NULL,
	PRIMARY KEY(book_accession, author_name),
	FOREIGN KEY(book_accession) REFERENCES books(accession_no) ON DELETE CASCADE,
    FOREIGN KEY(author_name) REFERENCES authors(name) ON DELETE CASCADE
);