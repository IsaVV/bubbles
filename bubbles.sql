-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 02-Dez-2020 às 18:55
-- Versão do servidor: 10.4.14-MariaDB
-- versão do PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bubbles`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `Calendário`
--

CREATE TABLE `Calendário` (
  `Id` int(11) NOT NULL,
  `Pessoa` varchar(255) DEFAULT NULL,
  `Tarefa` varchar(255) DEFAULT NULL,
  `Hora_Inicio` smallint(6) DEFAULT NULL,
  `Dia` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `Calendário`
--

INSERT INTO `Calendário` (`Id`, `Pessoa`, `Tarefa`, `Hora_Inicio`, `Dia`) VALUES
(10, 'Pedro', 'Tirar lixo', 1630, 17),
(11, 'Pedro', 'Limpar o chão', 1500, 24),
(16, 'Pedro', 'Lavar louça', 2000, 24),
(18, 'Isa', 'Lavar roupas', 1600, 21),
(19, 'João', 'Lavar roupas', 1200, 23);

-- --------------------------------------------------------

--
-- Estrutura da tabela `Horarios_Livres`
--

CREATE TABLE `Horarios_Livres` (
  `Nome` varchar(255) DEFAULT NULL,
  `Hora1` smallint(6) DEFAULT NULL,
  `Hora2` smallint(6) DEFAULT NULL,
  `Hora3` smallint(6) DEFAULT NULL,
  `Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `Horarios_Livres`
--

INSERT INTO `Horarios_Livres` (`Nome`, `Hora1`, `Hora2`, `Hora3`, `Id`) VALUES
('p', 1000, 2000, 2100, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `Lista_de_Tarefas`
--

CREATE TABLE `Lista_de_Tarefas` (
  `Nome` varchar(255) DEFAULT NULL,
  `Id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `Lista_de_Tarefas`
--

INSERT INTO `Lista_de_Tarefas` (`Nome`, `Id`) VALUES
('Lavar louça', 1),
('Limpar o chão', 2),
('Lavar roupas', 3),
('Tirar lixo', 4);

-- --------------------------------------------------------

--
-- Estrutura da tabela `Lista_de_Usuarios`
--

CREATE TABLE `Lista_de_Usuarios` (
  `Nome` varchar(255) DEFAULT NULL,
  `Usuario` varchar(255) DEFAULT NULL,
  `Senha` varchar(255) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `Data_Nascimento` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `Lista_de_Usuarios`
--

INSERT INTO `Lista_de_Usuarios` (`Nome`, `Usuario`, `Senha`, `id`, `Data_Nascimento`, `Email`) VALUES
('Pedro', 'p', 'abc', 5, '09/04/1999', 'pmama@cesar.school'),
('João', 'jf', 'j123', 8, '01/06/2002', 'jfpm@cesar.school'),
('Gustavo', 'guga', 'g', 11, '25/05/2002', 'glvm@cesar.school'),
('Isa', 'isa', 'abc', 12, '01/01/2002', 'ivv@cesar.school');

-- --------------------------------------------------------

--
-- Estrutura da tabela `Reclamacoes`
--

CREATE TABLE `Reclamacoes` (
  `id` int(11) NOT NULL,
  `Reclamacao` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `Reclamacoes`
--

INSERT INTO `Reclamacoes` (`id`, `Reclamacao`) VALUES
(3, 'Estou com problemas no calendário!');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `Calendário`
--
ALTER TABLE `Calendário`
  ADD PRIMARY KEY (`Id`);

--
-- Índices para tabela `Horarios_Livres`
--
ALTER TABLE `Horarios_Livres`
  ADD PRIMARY KEY (`Id`);

--
-- Índices para tabela `Lista_de_Tarefas`
--
ALTER TABLE `Lista_de_Tarefas`
  ADD PRIMARY KEY (`Id`);

--
-- Índices para tabela `Lista_de_Usuarios`
--
ALTER TABLE `Lista_de_Usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `Reclamacoes`
--
ALTER TABLE `Reclamacoes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `Calendário`
--
ALTER TABLE `Calendário`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de tabela `Horarios_Livres`
--
ALTER TABLE `Horarios_Livres`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `Lista_de_Tarefas`
--
ALTER TABLE `Lista_de_Tarefas`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `Lista_de_Usuarios`
--
ALTER TABLE `Lista_de_Usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de tabela `Reclamacoes`
--
ALTER TABLE `Reclamacoes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
