create table if not exists clients (
    client_id int primary key,
    client_name nvarchar(128) not null
);
delete from clients;
insert into clients(client_id, client_name)
values (1, 'Иван'),
    (2, 'Константин'),
    (3, 'Дмитрий'),
    (4, 'Александр');
create table if not exists products (
    product_id int primary key,
    product_name nvarchar(128) not null,
    price decimal not null
);
delete from products;
insert into products(product_id, product_name, price)
values (1, 'Мяч', 299.99),
    (2, 'Ручка', 18),
    (3, 'Кружка', 159.87),
    (4, 'Монитор', 18000),
    (5, 'Телефон', 9999.9),
    (6, 'Кофе', 159);
create table if not exists orders (
    order_id int primary key,
    client_id int,
    product_id int,
    order_name nvarchar(128) not null,
    constraint fk_orders_clients foreign key (client_id) references clients(client_id),
    constraint fk_orders_products foreign key (product_id) references products(product_id)
);
delete from orders;
insert into orders(order_id, client_id, product_id, order_name)
values (1, 2, 2, 'Закупка 1'),
    (2, 2, 5, 'Закупка 2'),
    (3, 2, 1, 'Закупка 3'),
    (4, 1, 1, 'Закупка 4'),
    (5, 1, 3, 'Закупка 5'),
    (6, 1, 6, 'Закупка 6'),
    (7, 1, 2, 'Закупка 7'),
    (8, 4, 5, 'Закупка 8'),
    (9, 3, 6, 'Закупка 9'),
    (10, 3, 3, 'Закупка 10'),
    (11, 1, 5, 'Закупка 11');