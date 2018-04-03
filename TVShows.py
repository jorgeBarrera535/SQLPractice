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
