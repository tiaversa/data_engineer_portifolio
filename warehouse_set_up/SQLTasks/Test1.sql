-- Assume the sample data is available in card_transactions table. 
-- Write the PostgreSQL query to list Client Id, Transaction Date, 
-- Amount EUR and a comparison column for each transaction that shows 
-- if the amount is increased or decreased compared to the previous 
-- transaction of the same client for all Approved transactions.

-- Analysing the question
--  Data for the result that I already have:
--  ClientId, Transaction Date, Amount EUR
-- What still need, comparison on the previous amount
-- necessary to consider to not get transactions where the response is not approved


-- To get this first I need to order the orders for this client
-- by date and then check how the present compares to the previous one
-- my first idea would be to do it based on a row count match like I have previously done.
with base_table as (
                    select Row_number() over(order by t."Client Id", t."Transaction Date") as row_number, 
                            t."Client Id" as client_id, 
                            t."Transaction Date" as transaction_date, 
                            t."Amount EUR" as amount_eur
                    from "Test1" t
                    where t."Response Description" Like ('Approved')
                    )
select bt1.client_id, 
    bt1.transaction_date, 
    bt1.amount_eur, 
    case
        when bt1.amount_eur > bt2.amount_eur then 'increased'
        when bt1.amount_eur < bt2.amount_eur then 'decreased'
        when bt2.amount_eur is null then null
        else 'same'
    end as comparison
from base_table bt1 
left join base_table bt2
    on bt1.row_number - 1 = bt2.row_number and bt1.client_id = bt2.client_id;
