SET SEARCH_PATH TO 'star';

CREATE TYPE TRANSMISSION_TYPE AS ENUM('viral', 'bacterial');
CREATE TYPE EXAM_TYPE AS ENUM('viral', 'bacterial');
CREATE TYPE DIAGNOSTIC_TYPE AS ENUM('blood_analysis', 'fluid', 'feces', 'petechiae');

CREATE TYPE CASE_STATUS AS ENUM('open', 'closed', 'pending');
CREATE TYPE EXAM_STATUS AS ENUM('requested', 'in_analysis', 'completed');

-- HealthProfessional table
CREATE TABLE HealthProfessional (
  id INT PRIMARY KEY,
  name TEXT
);

-- Pacient table
CREATE TABLE Pacient (
  id INT PRIMARY KEY,
  healh_professional_id INT,
  name TEXT,

  FOREIGN KEY (healh_professional_id) REFERENCES HealthProfessional(id)
);

-- Case table
CREATE TABLE SuspicionCase (
  id INT PRIMARY KEY,
  pacient_id INT,

  create_date TIMESTAMP,
  updated_date TIMESTAMP,

  case_status CASE_STATUS,

  FOREIGN KEY (pacient_id) REFERENCES Pacient(id)
);

-- Transmissions table
CREATE TABLE Transmissions (
  source_id INT,
  target_id INT,

  create_date TIMESTAMP,

  transmission_type TRANSMISSION_TYPE,

  PRIMARY KEY (source_id, target_id),
  FOREIGN KEY (source_id) REFERENCES Pacient(id),
  FOREIGN KEY (target_id) REFERENCES Pacient(id)
);

-- Laboratory table
CREATE TABLE Laboratory (
    name TEXT,
    id INTEGER PRIMARY KEY
);

-- Exam table
CREATE TABLE Exam (
  id INT PRIMARY KEY,
  laboratory_id INTEGER,

  create_date TIMESTAMP,
  updated_date TIMESTAMP,

  exam_status EXAM_STATUS,
  pacient_id INT,
  diagnostic DIAGNOSTIC_TYPE,
  transmission_type TRANSMISSION_TYPE,
  report TEXT,
  result BOOLEAN,

  FOREIGN KEY (pacient_id) REFERENCES Pacient(id),
  FOREIGN KEY (laboratory_id) REFERENCES Laboratory(id)
);
