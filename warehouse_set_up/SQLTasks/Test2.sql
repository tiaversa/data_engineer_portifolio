-- Write SQL statements to retrieve the following information: 
-- 1. For the customer with email address ‘fancygirl83@hotmail.com’ show all product_skus the customer has an active subscription for. 
select p.product_sku
from sql_test.customer c
join sql_test.subscription s
on c.id_customer = s.fk_customer
left join sql_test.product p
on s.fk_product_subscribed_to = p.id_product
where c.email = 'fancygirls83@hotmail.com'
and s.status = 'active';
-- 2. Get all the customers that have an active subscription to a product that corresponds to a product family with product_family_handle = ‘classic-box’ 
select c.id_customer
from sql_test.customer c
join sql_test.subscription s
on c.id_customer = s.fk_customer
join sql_test.product p
on s.fk_product_subscribed_to = p.id_product
left join sql_test.product_family pf
on p.fk_product_family = pf.id_product_family
where s.status = 'active'
and pf.product_family_handle = 'classic-box';
-- 3. Get all the paused subscriptions that have only received one box. 
select s.id_subscription
from (
    select count(fk_subscription) as count_subscription, fk_subscription 
    from sql_test.order 
    group by fk_subscription
    ) o 
join sql_test.subscription s
on s.id_subscription = o.fk_subscription
where s.status = 'paused'
and o.count_subscription = 1;
-- 4. How many subscriptions do our customers have on average? 
select avg(subscription_count) 
from (
    select count(fk_customer) as subscription_count, fk_customer from sql_test.subscription
    group by fk_customer
) x ;
-- 5. How many customers have ordered more than one product? 
select count(customer)
from (
    select s.fk_customer as customer, 
        s.id_subscription as subscription, 
        o.fk_product as product
    from sql_test.order o
    join sql_test.subscription s
    on o.fk_subscription = s.id_subscription
) x
group by customer
having count(distinct product) > 1;

-- 6. How many customers have ordered more that one product with the same subscription? 
select count(customer)
from (
    select s.fk_customer as customer, 
        s.id_subscription as subscription, 
        o.fk_product as product
    from sql_test.order o
    join sql_test.subscription s
    on o.fk_subscription = s.id_subscription
    group by s.id_subscription, o.fk_product, s.fk_customer
) x
group by customer
having count(subscription) > 1;
    
-- 7. Get a list of all customers which got a box delivered to them two weeks ago, and the count of boxes that had been delivered to them up to that week (loyalty) 
select customer, sum(weekly_amount_delivered) as weekly_amount_delivered
from (
    select s.fk_customer as customer,
        count(o.id_order) as weekly_amount_delivered
    from sql_test.subscription s
    join sql_test.order o
    on o.fk_subscription = s.id_subscription
    where o.delivery_date between '2023-11-07' and '2023-11-14'
    group by s.fk_customer
) x 
group by customer
order by customer;

-- 8. For all our customers, get the date of the latest order delivered to them and include associated product_sku, delivery_date and purchase price. If there were two orders delivered to the same customer on the same date, they should both appear.
with latest_list as (
    select s.fk_customer as customer,
        max(o.delivery_date) as latest_delivery_date
    from sql_test.subscription s
    join sql_test.order o
    on o.fk_subscription = s.id_subscription
    group by customer
) 
select s.fk_customer as customer, 
    o.delivery_date, 
    p.product_sku, 
    o.purchase_price
from sql_test.subscription s
join latest_list ll
on ll.customer = s.fk_customer
join sql_test.order o
on o.fk_subscription = s.id_subscription
and o.delivery_date = ll.latest_delivery_date
join sql_test.product p
on p.id_product = o.fk_product
order by s.fk_customer;