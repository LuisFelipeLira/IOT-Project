create database cadastro;

create table alunos( 
    id INT NOT NULL AUTO_INCREMENT,
    codigo VARCHAR(11),
    matricula VARCHAR(7),
    nome_aluno VARCHAR(50),
    datanascimento VARCHAR(10),
    telefone VARCHAR(38),
    alimentos VARCHAR(500),
    PRIMARY KEY (id)
    );

SELECT codigo
FROM alunos
WHERE codigo LIKE '%%';

UPDATE alunos SET codigo = "3B 57 9D 15", matricula = "5306575", nome_aluno = "Lucas de Souza Barboza", datanascimento = "09/07/1998", telefone = "(21)999694700", alimentos = "NULL" WHERE id = 1;