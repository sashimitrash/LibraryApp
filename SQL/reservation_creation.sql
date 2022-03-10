CREATE TABLE Reservation(
	ReserverID VARCHAR(256) NOT NULL,
    ReservedBookAccession VARCHAR(256) NOT NULL,
    ReservedDate DATE NOT NULL,
	PRIMARY KEY(ReserverID, ReservedBookAccession, ReservedDate),
	FOREIGN KEY(ReserverID) REFERENCES members(memberid) ON DELETE CASCADE,
	FOREIGN KEY(ReservedBookAccession) REFERENCES books(accession_no) ON DELETE CASCADE                                                                                                       
);
