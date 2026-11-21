-- =====================================================
-- PROJETO INTEGRADOR: HelpDesk Pro
-- Etapa 2 - Script DDL e DML do Banco de Dados
-- =====================================================

-- Parâmetros de Conexão (Exemplo PostgreSQL / Remoto)
-- Host: localhost (ou IP do servidor remoto)
-- Porta: 5432 | Banco: helpdesk_db | User: postgres

CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    tipo_perfil VARCHAR(20) CHECK (tipo_perfil IN ('Cliente', 'Tecnico', 'Administrador')) NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chamados (
    id_chamado SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT NOT NULL,
    prioridade VARCHAR(20) CHECK (prioridade IN ('Baixa', 'Média', 'Alta', 'Urgente')) DEFAULT 'Média',
    status VARCHAR(30) CHECK (status IN ('Aberto', 'Em Andamento', 'Concluído', 'Cancelado')) DEFAULT 'Aberto',
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

CREATE TABLE comentarios (
    id_comentario SERIAL PRIMARY KEY,
    texto TEXT NOT NULL,
    data_comentario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_chamado INT REFERENCES chamados(id_chamado) ON DELETE CASCADE,
    id_usuario INT REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Inserção de dados iniciais (DML - Seeds)
INSERT INTO usuarios (nome, email, senha, tipo_perfil) VALUES 
('Kevin Josué', 'kevin@email.com', 'senha123', 'Administrador'),
('Felipe Fontana', 'felipe@email.com', 'senha123', 'Tecnico'),
('Maria Souza', 'maria@email.com', 'senha123', 'Cliente');

INSERT INTO chamados (titulo, descricao, prioridade, status, id_usuario) VALUES 
('Erro na impressora do setor fiscal', 'A impressora principal não está puxando papel nem respondendo aos comandos da rede.', 'Alta', 'Aberto', 3),
('Lentidão no sistema ERP', 'O sistema está travando ao tentar gerar os relatórios mensais.', 'Média', 'Em Andamento', 3);

INSERT INTO comentarios (texto, id_chamado, id_usuario) VALUES 
('Chamado recebido pela equipe de suporte. Vamos verificar o driver da impressora.', 1, 2);
