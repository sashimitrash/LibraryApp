CREATE TABLE payments(
	memberid VARCHAR(256) NOT NULL,
    accession_no VARCHAR(256) NOT NULL,
	PaymentDate DATE NOT NULL,
    PRIMARY KEY(memberid, accession_no, PaymentDate),
    FOREIGN KEY(memberid) REFERENCES members(memberid),
    FOREIGN KEY(accession_no) REFERENCES books(accession_no)
);