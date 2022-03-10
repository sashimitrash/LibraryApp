CREATE TABLE fine(
     memberid     VARCHAR(256)  NOT NULL,
     amount       INT NOT NULL CHECK (amount > 0),
     PRIMARY KEY (memberid, amount),
     FOREIGN KEY (memberid) REFERENCES members(memberid) ON DELETE RESTRICT
);
