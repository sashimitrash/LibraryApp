CREATE TABLE Payment(
	memberid      VARCHAR(5)  NOT NULL,
    accession_no  VARCHAR(10) NOT NULL,
    paymentDate DATE NOT NULL,
    PRIMARY KEY (memberid, accession_no, paymentDate),
    FOREIGN KEY (memberID) REFERENCES members(memberid), 
    FOREIGN KEY (accession_no) REFERENCES books(accession_no)
);
    
    