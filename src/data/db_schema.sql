DROP TABLE IF EXISTS routes;
DROP TABLE IF EXISTS route_points;
DROP TABLE IF EXISTS route_tags;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS regions;
DROP TABLE IF EXISTS terrain_types;
DROP VIEW IF EXISTS routes_full_view;

CREATE TABLE routes (
    route_uuid VARCHAR(36) PRIMARY KEY,
    name VARCHAR(300) NOT NULL,
    description TEXT,
    difficulty_level INT NOT NULL,
    region_id INT NOT NULL,
    terrain_type_id INT NOT NULL,
    CONSTRAINT chk_difficulty_level CHECK (difficulty_level BETWEEN 1 AND 5),
    FOREIGN KEY (region_id) REFERENCES regions(region_id) ON DELETE SET NULL,
    FOREIGN KEY (terrain_type_id) REFERENCES terrain_type(terrain_type_id) ON DELETE SET NULL
);

CREATE TABLE route_points (
    number_in_order INT NOT NULL,
    route_uuid VARCHAR(36) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    description VARCHAR(300),
    PRIMARY KEY (route_uuid, number_in_order),
    FOREIGN KEY (route_uuid) REFERENCES routes(route_uuid) ON DELETE CASCADE
);

CREATE TABLE route_tags (
    tag_id INT,
    route_uuid VARCHAR(36),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE,
    FOREIGN KEY (route_uuid) REFERENCES routes(route_uuid) ON DELETE CASCADE
);

CREATE TABLE tags (
    tag_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE regions (
    region_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE terrain_types (
    terrain_type_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE VIEW routes_full_view AS
SELECT
    routes.route_uuid,
    routes.name AS route_name,
    routes.description AS route_description,
    routes.difficulty_level,
    regions.name AS region_name,
    terrain_types.name AS terrain_type_name,
    tags.name AS tag_name,
    route_points.number_in_order,
    route_points.latitude,
    route_points.longitude,
    route_points.description AS point_description
FROM routes
LEFT JOIN regions ON routes.region_id = regions.region_id
LEFT JOIN terrain_types ON routes.terrain_type_id = terrain_types.terrain_type_id
LEFT JOIN route_points ON routes.route_uuid = route_points.route_uuid
LEFT JOIN route_tags ON routes.route_uuid = route_tags.route_uuid
LEFT JOIN tags ON route_tags.tag_id = tags.tag_id;

-- Wypełnienie tabel regions
INSERT INTO regions (name) VALUES
    ('Małopolska'),
    ('Mazowsze'),
    ('Podkarpacie'),
    ('Pomorze'),
    ('Śląsk');

-- Wypełnienie tabel terrain_types
INSERT INTO terrain_types (name) VALUES
    ('Góry'),
    ('Las'),
    ('Miasto'),
    ('Wyżyna'),
    ('Nizina');

-- Wypełnienie tabel tags
INSERT INTO tags (name) VALUES
    ('widokowa'),
    ('rodzinna'),
    ('rowerowa'),
    ('piesza'),
    ('historyczna'),
    ('krajobrazowa'),
    ('miejska'),
    ('leśna'),
    ('górska'),
    ('relaks'),
    ('fotograficzna'),
    ('przyrodnicza'),
    ('edukacyjna'),
    ('nocna'),
    ('kulinarna'),
    ('tematyczna'),
    ('długa'),
    ('krótka'),
    ('dla początkujących'),
    ('dla zaawansowanych');

-- Wypełnienie tabel routes
INSERT INTO routes (route_uuid, name, description, difficulty_level, region_id, terrain_type_id) VALUES
    ('11111111-1111-1111-1111-111111111111', 'Szlak Orlich Gniazd', 'Malowniczy szlak przez zamki Jury Krakowsko-Częstochowskiej.', 3, 1, 4),
    ('22222222-2222-2222-2222-222222222222', 'Trasa przez Kampinos', 'Leśna trasa przez Kampinoski Park Narodowy.', 2, 2, 2),
    ('33333333-3333-3333-3333-333333333333', 'Górska Przygoda', 'Wędrówka po Beskidach z pięknymi widokami.', 4, 1, 1),
    ('44444444-4444-4444-4444-444444444444', 'Spacer po Gdańsku', 'Zwiedzanie zabytkowego centrum Gdańska.', 1, 4, 3),
    ('55555555-5555-5555-5555-555555555555', 'Rowerem przez Mazowsze', 'Łatwa trasa rowerowa przez mazowieckie wsie.', 2, 2, 5),
    ('66666666-6666-6666-6666-666666666666', 'Szlak Powstańców', 'Historyczna trasa upamiętniająca powstania śląskie.', 3, 5, 4),
    ('77777777-7777-7777-7777-777777777777', 'Bieszczadzka Wędrówka', 'Długa trasa przez dzikie Bieszczady.', 5, 3, 1),
    ('88888888-8888-8888-8888-888888888888', 'Leśne ścieżki', 'Relaksujący spacer po lasach Pomorza.', 1, 4, 2),
    ('99999999-9999-9999-9999-999999999999', 'Wycieczka po Krakowie', 'Trasa miejska po najważniejszych zabytkach Krakowa.', 1, 1, 3),
    ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 'Szlak nad Wisłą', 'Trasa wzdłuż Wisły z pięknymi krajobrazami.', 2, 2, 5);

-- Wypełnienie tabel route_points (po 3 punkty na trasę)
INSERT INTO route_points (number_in_order, route_uuid, latitude, longitude, description) VALUES
    (1, '11111111-1111-1111-1111-111111111111', 50.615, 19.563, 'Zamek Ogrodzieniec'),
    (2, '11111111-1111-1111-1111-111111111111', 50.452, 19.573, 'Zamek Mirów'),
    (3, '11111111-1111-1111-1111-111111111111', 50.242, 19.132, 'Zamek Olsztyn'),

    (1, '22222222-2222-2222-2222-222222222222', 52.300, 20.700, 'Wjazd do Kampinosu'),
    (2, '22222222-2222-2222-2222-222222222222', 52.350, 20.650, 'Polana Opaleń'),
    (3, '22222222-2222-2222-2222-222222222222', 52.400, 20.600, 'Granica Parku'),

    (1, '33333333-3333-3333-3333-333333333333', 49.700, 19.000, 'Szczyrk Centrum'),
    (2, '33333333-3333-3333-3333-333333333333', 49.720, 19.040, 'Klimczok'),
    (3, '33333333-3333-3333-3333-333333333333', 49.750, 19.060, 'Schronisko na Skrzycznem'),

    (1, '44444444-4444-4444-4444-444444444444', 54.352, 18.646, 'Długi Targ'),
    (2, '44444444-4444-4444-4444-444444444444', 54.350, 18.653, 'Bazylika Mariacka'),
    (3, '44444444-4444-4444-4444-444444444444', 54.355, 18.660, 'Muzeum II Wojny Światowej'),

    (1, '55555555-5555-5555-5555-555555555555', 52.200, 21.000, 'Start w Warszawie'),
    (2, '55555555-5555-5555-5555-555555555555', 52.250, 21.100, 'Wieś Zielona'),
    (3, '55555555-5555-5555-5555-555555555555', 52.300, 21.200, 'Meta w Siedlcach'),

    (1, '66666666-6666-6666-6666-666666666666', 50.300, 18.900, 'Katowice Centrum'),
    (2, '66666666-6666-6666-6666-666666666666', 50.350, 18.950, 'Muzeum Powstań Śląskich'),
    (3, '66666666-6666-6666-6666-666666666666', 50.400, 19.000, 'Pomnik Powstańców'),

    (1, '77777777-7777-7777-7777-777777777777', 49.200, 22.450, 'Ustrzyki Górne'),
    (2, '77777777-7777-7777-7777-777777777777', 49.250, 22.500, 'Połonina Caryńska'),
    (3, '77777777-7777-7777-7777-777777777777', 49.300, 22.550, 'Tarnica'),

    (1, '88888888-8888-8888-8888-888888888888', 54.500, 18.600, 'Wejście do lasu'),
    (2, '88888888-8888-8888-8888-888888888888', 54.520, 18.650, 'Polana leśna'),
    (3, '88888888-8888-8888-8888-888888888888', 54.540, 18.700, 'Jezioro leśne'),

    (1, '99999999-9999-9999-9999-999999999999', 50.061, 19.938, 'Rynek Główny'),
    (2, '99999999-9999-9999-9999-999999999999', 50.064, 19.945, 'Wawel'),
    (3, '99999999-9999-9999-9999-999999999999', 50.067, 19.950, 'Kazimierz'),

    (1, 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 52.250, 21.000, 'Most Gdański'),
    (2, 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 52.300, 21.050, 'Plaża nad Wisłą'),
    (3, 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', 52.350, 21.100, 'Rezerwat przyrody');

-- Wypełnienie tabel route_tags (po 2 tagi na trasę)
INSERT INTO route_tags (tag_id, route_uuid) VALUES
    (1, '11111111-1111-1111-1111-111111111111'),
    (5, '11111111-1111-1111-1111-111111111111'),
    (6, '11111111-1111-1111-1111-111111111111'),
    (11, '11111111-1111-1111-1111-111111111111'),

    (2, '22222222-2222-2222-2222-222222222222'),
    (8, '22222222-2222-2222-2222-222222222222'),
    (10, '22222222-2222-2222-2222-222222222222'),
    (12, '22222222-2222-2222-2222-222222222222'),

    (9, '33333333-3333-3333-3333-333333333333'),
    (1, '33333333-3333-3333-3333-333333333333'),
    (6, '33333333-3333-3333-3333-333333333333'),
    (18, '33333333-3333-3333-3333-333333333333'),

    (7, '44444444-4444-4444-4444-444444444444'),
    (5, '44444444-4444-4444-4444-444444444444'),
    (13, '44444444-4444-4444-4444-444444444444'),
    (16, '44444444-4444-4444-4444-444444444444'),

    (3, '55555555-5555-5555-5555-555555555555'),
    (2, '55555555-5555-5555-5555-555555555555'),
    (17, '55555555-5555-5555-5555-555555555555'),
    (19, '55555555-5555-5555-5555-555555555555'),

    (5, '66666666-6666-6666-6666-666666666666'),
    (4, '66666666-6666-6666-6666-666666666666'),
    (15, '66666666-6666-6666-6666-666666666666'),
    (20, '66666666-6666-6666-6666-666666666666'),

    (9, '77777777-7777-7777-7777-777777777777'),
    (6, '77777777-7777-7777-7777-777777777777'),
    (17, '77777777-7777-7777-7777-777777777777'),
    (18, '77777777-7777-7777-7777-777777777777'),

    (8, '88888888-8888-8888-8888-888888888888'),
    (10, '88888888-8888-8888-8888-888888888888'),
    (12, '88888888-8888-8888-8888-888888888888'),
    (14, '88888888-8888-8888-8888-888888888888'),

    (7, '99999999-9999-9999-9999-999999999999'),
    (5, '99999999-9999-9999-9999-999999999999'),
    (13, '99999999-9999-9999-9999-999999999999'),
    (16, '99999999-9999-9999-9999-999999999999'),

    (6, 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'),
    (1, 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'),
    (11, 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'),
    (15, 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa');
