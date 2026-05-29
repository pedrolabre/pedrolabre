CREATE DATABASE IF NOT EXISTS CADASTRO_ALUNOS;

USE CADASTRO_ALUNOS;

CREATE TABLE ALUNOS (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(150) NOT NULL,
    Idade INT,
    Matricula VARCHAR(15) UNIQUE NOT NULL,
    Curso VARCHAR(50) NOT NULL,
    Periodo VARCHAR(20) NOT NULL,
    Hobby VARCHAR(60) NOT NULL
);

DELIMITER //
CREATE PROCEDURE sp_AddAluno (
    IN p_Nome VARCHAR(150),
    IN p_Idade INT,
    IN p_Matricula VARCHAR(15),
    IN p_Curso VARCHAR(50),
    IN p_Periodo VARCHAR(20),
    IN p_Hobby VARCHAR(60)
)
BEGIN
    INSERT INTO ALUNOS (Nome, Idade, Matricula, Curso, Periodo, Hobby)
    VALUES (p_Nome, p_Idade, p_Matricula, p_Curso, p_Periodo, p_Hobby);
END 
// DELIMITER ;

CALL sp_AddAluno('Pedro quase Pontes', 30, '202410630002', 'Sistemas de Informação', 'Noturno', 'Beber');
CALL sp_AddAluno('Fiat Bruno', 22, '202410630001', 'Sistemas de Informação', 'Noturno', 'Jogar Volei');
CALL sp_AddAluno('Jovem Dex', 20, '202410630003', 'Sistemas de Informação', 'Nortuno', 'Trollar');

SELECT * FROM ALUNOS;