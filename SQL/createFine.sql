CREATE TABLE Fine(
     memberid     VARCHAR(256)  NOT NULL,
     accession_no  VARCHAR(256) NOT NULL,
     amount       INT NOT NULL CHECK (amount > 0),
     PRIMARY KEY (memberid, accession_no, amount),
     FOREIGN KEY (accession_no) REFERENCES books(accession_no) ON DELETE RESTRICT,
     FOREIGN KEY (memberid) REFERENCES members(memberid) ON DELETE RESTRICT
);
