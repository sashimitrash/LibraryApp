CREATE TABLE payment(
	memberid      VARCHAR(256)  NOT NULL,
    paymentDate DATE NOT NULL,
    PRIMARY KEY (memberid, paymentDate),
    FOREIGN KEY (memberID) REFERENCES members(memberid)
);
    
    