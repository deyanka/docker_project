CREATE DATABASE IF NOT EXISTS winx_club_db;
USE winx_club_db;

CREATE TABLE IF NOT EXISTS winx_fairies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fairy_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    zodiac_sign VARCHAR(20) NOT NULL,
    boyfriend_name VARCHAR(50),
    wing_color VARCHAR(30) NOT NULL,
    magic_power VARCHAR(50),
    UNIQUE KEY (fairy_name)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO winx_fairies (fairy_name, age, zodiac_sign, boyfriend_name, wing_color, magic_power)
VALUES
    ('Bloom', 17, 'Dragon', 'Sky', 'Blue with pink', 'Fire magic'),
    ('Stella', 17, 'Gemini', 'Brandon', 'Yellow-orange', 'Sun and moon magic'),
    ('Flora', 16, 'Virgo', 'Helia', 'Green', 'Nature magic'),
    ('Musa', 17, 'Scorpio', 'Riven', 'Purple', 'Music magic'),
    ('Tecna', 17, 'Capricorn', 'Timmy', 'Blue', 'Technology magic'),
    ('Layla', 18, 'Pisces', 'Nabu', 'Turquoise', 'Wave magic');
