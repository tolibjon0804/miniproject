CREATE TABLE Timetable (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(255),
    day VARCHAR(50),
    time VARCHAR(50),
    room VARCHAR(50),
    level INT
);

INSERT INTO Timetable (course_name, day, time, room, level) VALUES
('Business and Global Issues', 'Tuesday', '2:00 PM', 'Room 405', 3),
('Configuration of ERP Systems', 'Thursday', '4:30 PM', 'Room 230', 4),
('Computer Programming I', 'Monday', '11:30 AM', 'Room 123', 1),
('Chess Beyond the Basics', 'Wednesday', '7:00 PM', 'Room 104', 3),
('Foundations in Education', 'Friday', '11:30 AM', 'Room 305', 2);

CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    level INT
);

INSERT INTO Students (name, level) VALUES
('Tolibjon Olimjonov', 3),
('Tommy Joe', 2),
('Adolf Hitler', 4),
('Joe Biden', 1);
