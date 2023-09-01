-- criação do banco de dados para o cenário de Oficina 

create database oficina;
use oficina;

-- criar tabela carros
create table carros(
		IdCarro int auto_increment primary key,
        Marca varchar(20) not null,
        Modelo varchar(20) not null,
        Ano int not null,
        Placa varchar(20) not null,
        constraint unique_placa_carro unique (Placa)
);
alter table carros auto_increment=1;

-- criar tabela pessoas
create table pessoas(
		IdPessoa int auto_increment primary key,
        NomeCompleto varchar(255) not null,
        CPF char(11) not null,
        Telefone varchar(11) not null,        
        Email varchar(100),
        Endereco varchar(255),
        Cidade varchar(50),
        UF char(2),
        constraint unique_cpf_pessoa unique (CPF)        
);
alter table pessoas auto_increment=1;

-- criar tabela empresas
create table empresas(
		IdEmpresa int auto_increment primary key,
        RazaoSocial varchar(100) not null,
        NomeFantasia varchar(100) not null,
        CNPJ char(15) not null,
        Telefone varchar(11) not null,        
        Email varchar(100) not null,
        Endereco varchar(255) not null,
        Cidade varchar(50) not null,
        UF char(2) not null,
        constraint unique_cnpj_empresa unique (CNPJ)        
);
alter table empresas auto_increment=1;


-- criar tabela de funcionarios
create table funcionarios(
    IdFuncionario int auto_increment primary key,
	Fun_IdPessoa int,
    Cargo varchar(45) not null,
    Especialidade varchar(45),
    constraint fk_funcionarios_pessoa foreign key (Fun_IdPessoa) references pessoas(IdPessoa) 
			on update cascade
);
alter table funcionarios auto_increment=1;

-- criar tabela clientes
create table clientes(
		IdCliente int auto_increment primary key,
        TipoCliente enum('PF','PJ') default 'PF',
        Cli_IdPessoa int,
        Cli_IdEmpresa int,
        Cli_IdCarro int,
        constraint fk_clientes_pessoa foreign key (Cli_IdPessoa) references pessoas(IdPessoa),
        constraint fk_clientes_empresa foreign key (Cli_IdEmpresa) references empresas(IdEmpresa),
        constraint fk_clientes_carro foreign key (Cli_IdCarro) references carros(IdCarro)
);
alter table clientes auto_increment=1;

-- criar tabela orcamentos
create table orcamentos(
		IdOrcamento int auto_increment primary key,
        Solicitante_IdPessoa int,
        Orc_IdCliente int,
        Orc_IdCarro int,
        Valor float not null,
        Desconto float,
        Orc_Data date not null,
        Validade date,
        FormaPagamento enum('PIX', 'DEBITO', 'CREDITO', 'DINHEIRO', 'BOLETO') default 'BOLETO' not null,
        Aprovado enum('SIM', 'NÃO', 'AGUARDANDO') default 'AGUARDANDO',
        constraint fk_orcamentos_pessoa foreign key (Solicitante_IdPessoa) references pessoas(IdPessoa),
        constraint fk_orcamentos_cliente foreign key (Orc_IdCliente) references clientes(IdCliente),
        constraint fk_orcamentos_carro foreign key (Orc_IdCarro) references carros(IdCarro)
);
alter table orcamentos auto_increment=1;

-- criar tabela OS
create table os(
		IdOs int auto_increment primary key,
        Os_IdOrcamento int,
        Os_IdFuncionario int,
        Emissao date not null,
        Conclusao date,
        DescricaoServico varchar(100) not null,
        Obs varchar(255),
        constraint fk_os_orcamento foreign key (Os_IdOrcamento) references orcamentos(IdOrcamento),
        constraint fk_os_funcionario foreign key (Os_IdFuncionario) references funcionarios(IdFuncionario)
);
alter table os auto_increment=1;