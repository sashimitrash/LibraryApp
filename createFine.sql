CREATE TABLE Fine(
     memberID     VARCHAR(5)  NOT NULL,
     accessionNo  VARCHAR(10) NOT NULL,
     amount       VARCHAR(10) NOT NULL,
     PRIMARY KEY (memberID, accessionNo),
     FOREIGN KEY (memberID) REFERENCES Member(memberID) ON DELETE RESTRICT);
