select * from customer --where id = 3

select count(*) from customer

select count(*) from customer where id = 3

select count(*) from customer where country = 'Mexico'

select firstname, lastname /*column selection*/ from customer where firstname like 'G%'

select country, count(*) from customer group by country

select customerid, sum(totalamount) totalsalesvalue/*alias*/, count(*) nooforders 
from orders group by customerid


select * from customer --where id = 3

select count(*) from customer

select count(*) from customer where id = 3

select count(*) from customer where country = 'Mexico'

select firstname "First Name", lastname "Last Name" /*column selection*/ from customer where firstname like 'G%'

select country, count(*) from customer group by country

select customerid, sum(totalamount) totalsalesvalue/*alias*/, count(*) nooforders 
from orders group by customerid

select productid, sum(quantity) from orderitem where quantity > 100 group by productid


select productid, quantity from orderitem where quantity > 500


select fieldname1, fieldname2, fieldname3, fieldname4 from tablename where fieldname1 = 'condn1' and fieldname2 = 'condn2'
 
select fieldname1, operation(fieldname2), operation(fieldname3) from tablename where fieldname1 = 'condn1' and fieldname2 = 'condn2'
group by fieldname1

select productid, sum(quantity) from orderitem group by productid having sum(quantity) > 500

BETWEEN a AND b   ||||||||||     sum(quantity) > 500  AND  sum(quantity) < 1000

select customerid, sum(totalamount) totalsalesvalue/*alias*/, count(*) nooforders 
from orders group by customerid

select * from customer where id = 23

5

select orders.customerid, customer.firstname, orders.totalamount 
from orders, customer where customer.id /*PK*/ = orders.customerid/*FK*/ and orders.customerid = 23

select customerid, firstname, totalamount 
from orders, customer where customer.id /*PK*/ = customerid/*FK*/ and customerid = 23

select productid, quantity from orderitem

------2155
select customer.firstname, customer.lastname, customer.city, customer.country, customer.phone, 
orders.orderdate, orders.ordernumber, product.productname, orderitem.unitprice, orderitem.quantity, orders.totalamount, 
supplier.companyname, supplier.city, supplier.country
from orderitem , orders, product, customer, supplier
where orderitem.orderid = orders.id
and orderitem.productid = product.id
and orders.customerid = customer.id
and product.supplierid = supplier.id

select * from supplier

select count(*) from orders --830
select count(*) from customer --91
select count(*) from product --78
select count(*) from supplier --29
