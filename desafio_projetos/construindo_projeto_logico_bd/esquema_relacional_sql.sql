-- criação do banco de dados para o cenário de E-commerce 

create database ecommerce;
use ecommerce;

-- criar tabela cliente
create table clients(
		IdClient int auto_increment primary key,
        Fname varchar(10),
        Minit char(3),
        Lname varchar(20),
        CPF char(11) not null,
        Address varchar(255),
        Birthday date,
        constraint unique_cpf_client unique (CPF)
);
alter table clients auto_increment=1;

-- criar tabela produto
create table product(
		IdProduct int auto_increment primary key,
        Pname varchar(255) not null,
        ProductDescription varchar(400) not null, 
        Category enum('Eletrônico','Vestimenta','Brinquedos','Alimentos','Móveis') not null,
        Price float not null default 0,        
        Size varchar(10),
        Rating float default 0
);
alter table product auto_increment=1;

-- criar tabela pedido
create table orders(
	IdOrder int auto_increment primary key,
    IdOrderClient int,
    OrderStatus enum('Em andamento', 'Processando', 'Enviado', 'Entregue','Cancelado') default 'Processando',
    OrderDescription varchar(255),
    SendValue float default 10,
    PaymentCash boolean default false, 
    constraint fk_orders_client foreign key (IdOrderClient) references clients(IdClient)
			on update cascade
);
alter table orders auto_increment=1;

-- criar tabela de pagamentos
create table payments(
    IdPayment int auto_increment,
	IdClient int,
    TypePayment enum('Boleto','Cartão','Dois cartões'),
    LimitAvailable float,
    primary key(IdPayment, IdClient),
    constraint fk_payments_client foreign key (IdClient) references clients(IdClient) 
			on update cascade
);
alter table payments auto_increment=1;

-- criar tabela estoque
create table productStorage(
	IdProdStorage int auto_increment primary key,
    StorageLocation varchar(255),
    Quantity int default 0
);
alter table productStorage auto_increment=1;

-- criar tabela fornecedor
create table supplier(
	IdSupplier int auto_increment primary key,
    SocialName varchar(255) not null,
    CNPJ char(15) not null,
    Contact char(11) not null,
    constraint unique_supplier unique (CNPJ)
);
alter table supplier auto_increment=1;

-- criar tabela vendedor
create table seller(
	IdSeller int auto_increment primary key,
    SocialName varchar(255) not null,
    AbstName varchar(255),
    CNPJ char(15),
    CPF char(11) not null,
    SellerLocation varchar(255),
    Contact char(11) not null,
    constraint unique_cnpj_seller unique (CNPJ),
    constraint unique_cpf_seller unique (CPF)
);
alter table seller auto_increment=1;

-- tabelas de relacionamentos M:N
create table productSeller(
	IdPseller int,
    IdPproduct int,
    ProdQuantity int default 1,
    primary key (IdPseller, IdPproduct),
    constraint fk_product_seller foreign key (IdPseller) references seller(IdSeller),
    constraint fk_product_product foreign key (IdPproduct) references product(IdProduct)
);

create table productOrder(
	IdPOproduct int,
    IdPOorder int,
    PoQuantity int default 1,
    PoStatus enum('Disponível', 'Sem estoque') default 'Disponível',
    primary key (IdPOproduct, IdPOorder),
    constraint fk_productorder_product foreign key (IdPOproduct) references product(IdProduct),
    constraint fk_productorder_order foreign key (IdPOorder) references orders(IdOrder)
);

create table storageLocation(
	IdLproduct int,
    IdLstorage int,
    SLocation varchar(255) not null,
    primary key (IdLproduct, IdLstorage),
    constraint fk_storage_location_product foreign key (IdLproduct) references product(IdProduct),
    constraint fk_storage_location_storage foreign key (IdLstorage) references productStorage(IdProdStorage)
);

create table productSupplier(
	IdPsSupplier int,
    IdPsProduct int,
    Quantity int not null,
    primary key (idPsSupplier, idPsProduct),
    constraint fk_product_supplier_supplier foreign key (IdPsSupplier) references supplier(IdSupplier),
    constraint fk_product_supplier_prodcut foreign key (IdPsProduct) references product(IdProduct)
);
