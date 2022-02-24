CREATE TABLE fines(
	memberid VARCHAR(256) NOT NULL,
    accession_no VARCHAR(256) NOT NULL,
	amount INT,
    PRIMARY KEY(memberid, accession_no, amount),
    FOREIGN KEY(memberid) REFERENCES members(memberid),
    FOREIGN KEY(accession_no) REFERENCES books(accession_no)
);