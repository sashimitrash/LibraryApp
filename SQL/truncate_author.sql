ALTER TABLE book_author
DROP CONSTRAINT `book_author_ibfk_2`;

TRUNCATE authors;

ALTER TABLE book_author
ADD FOREIGN KEY (`author_name`) REFERENCES authors(name) ON DELETE CASCADE;