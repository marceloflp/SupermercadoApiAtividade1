CREATE TABLE usuarios(
    id int primary key AUTOINCREMENT,
    nome
);

CREATE TABLE produtos(
    id int primary key AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE setores(
    id int primary key AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE categorias(
    id int primary key AUTOINCREMENT,
    nome TEXT NOT NULL
);