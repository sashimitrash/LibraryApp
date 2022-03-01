CREATE TABLE Payment(
	memberID     VARCHAR(5)  NOT NULL,
    accessionNo  VARCHAR(10) NOT NULL,
    paymentDate DATE NOT NULL,
    PRIMARY KEY (memberID, accessionNo, paymentDate),
    FOREIGN KEY (memberID) REFERENCES Member(memberID), 
    FOREIGN KEY (accessionNo) REFERENCES Book(accessionNo)
);
    
    