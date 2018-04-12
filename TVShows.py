CREATE TABLE tv_shows (
  id INT,
  name TEXT,
  rating INT
);
INSERT INTO tv_shows (id, name, rating)
VALUES (1, "Naruto", 3),
(2, "Pokemon", 5),
(3, "One Piece", 2);

SELECT * FROM tv_shows;

CREATE TABLE dogs (
  name TEXT,
  breed TEXT,
  contact_number INT,
  date_lost TEXT,
  last_location TEXT,
  picture_URL TEXT,
  Reward INT,
  Owners_name TEXT,
  Address TEXT,
  dog_description TEXT,
  Found Bool
);

INSERT INTO dogs (name, breed, contact_number, date_lost, last_location, picture_URL, Reward, Owners_name, Address, dog_description, Found)
VALUES ("Sr.Fluffy Boots", "Blood Hound", "(555)555-5555", "3/10/2018", "jasmine court", "", "$500", "Jeffrey", "1234 Hackberry Drv.", "Small Yorkie, with bright blue colar on and a silver/black coat", false);
("cujo", "Pitbull", 25),
("Bubbles", "Yorkie", 5);


