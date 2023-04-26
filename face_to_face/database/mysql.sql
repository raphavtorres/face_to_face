CREATE database face_to_face;

USE face_to_face;

CREATE TABLE people (
    id INT AUTO_INCREAMENT PRIMARY KEY,
    person VARCHAR(50),
    tip1 VARCHAR(50),
    tip2 VARCHAR(50),
    tip3 VARCHAR(50),
    tip4 VARCHAR(50),
    tip5 VARCHAR(50),
);


INSERT INTO user (id, person, tip1, tip2, tip3, tip4, tip5)
VALUES ('')