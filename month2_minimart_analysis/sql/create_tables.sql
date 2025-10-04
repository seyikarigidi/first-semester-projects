-- SQL script to create necessary tables
create table customers(
    "customer_id" serial primary key,
    "name" varchar(100) not null,
    "email" varchar(100) unique not null,
    "join_date" date default current_date
);



create table products(
    "product_id" serial primary key,
    "product_name" varchar(100) not null,
    "category" varchar(50) not null,
    "price" numeric(10, 2) not null
);

create table orders(
    "order_id" serial primary key,
    "customer_id" int references customers(customer_id),
    "product_id" int references products(product_id),
    "quantity" int not null,
    "order_date" date default current_date
);


