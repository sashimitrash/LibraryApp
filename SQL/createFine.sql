CREATE TABLE Fine(
     memberID     VARCHAR(5)  NOT NULL,
     accessionNo  VARCHAR(10) NOT NULL,
     amount       INT NOT NULL CHECK (amount > 0),
     PRIMARY KEY (memberID, accessionNo),
     FOREIGN KEY (accessionNo) REFERENCES Book(accessionNo) ON DELETE RESTRICT,
     FOREIGN KEY (memberID) REFERENCES Member(memberID) ON DELETE RESTRICT
);
