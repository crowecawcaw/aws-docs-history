Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Merge examples

The following examples perform a merge to update the SALES table. The first example
uses the simpler method of deleting from the target table and then inserting all of the
rows from the staging table. The second example requires updating on select columns in
the target table, so it includes an extra update step.

The Merge examples use a sample dataset for Amazon Redshift, called the TICKIT data set. As a
prerequisite, you can set up the TICKIT tables and data by following the instructions available in the
guide [Getting started with common database tasks](../gsg/database-tasks.md "../gsg/database-tasks.md"). More detailed
information about the sample data set is found at [Sample database](c_sampledb.md "c_sampledb.md").

**Sample merge data source**

The examples in this section need a sample data source that includes both updates and
inserts. For the examples, we will create a sample table named SALES_UPDATE that uses
data from the SALES table. We'll populate the new table with random data that represents
new sales activity for December. We will use the SALES_UPDATE sample table to create the
staging table in the examples that follow.

```
-- Create a sample table as a copy of the SALES table.

create table tickit.sales_update as
select * from tickit.sales;

-- Change every fifth row to have updates.

update tickit.sales_update
set qtysold = qtysold*2,
pricepaid = pricepaid*0.8,
commission = commission*1.1
where saletime > '2008-11-30'
and mod(sellerid, 5) = 0;

-- Add some new rows to have inserts.
-- This example creates a duplicate of every fourth row.

insert into tickit.sales_update
select (salesid + 172456) as salesid, listid, sellerid, buyerid, eventid, dateid, qtysold, pricepaid, commission, getdate() as saletime
from tickit.sales_update
where saletime > '2008-11-30'
and mod(sellerid, 4) = 0;
```

**Example of a merge that replaces existing
rows based on matching keys**

The following script uses the SALES_UPDATE table to perform a merge operation on the
SALES table with new data for December sales activity. This example replaces rows in the
SALES table that have updates. For this example, we will update the qtysold and pricepaid columns,
but leave commission and saletime unchanged.

```
MERGE into tickit.sales
USING tickit.sales_update sales_update
on ( sales.salesid = sales_update.salesid
and sales.listid = sales_update.listid
and sales_update.saletime > '2008-11-30'
and (sales.qtysold != sales_update.qtysold
or sales.pricepaid != sales_update.pricepaid))
WHEN MATCHED THEN
update SET qtysold = sales_update.qtysold,
pricepaid = sales_update.pricepaid
WHEN NOT MATCHED THEN
INSERT (salesid, listid, sellerid, buyerid, eventid, dateid, qtysold , pricepaid, commission, saletime)
values (sales_update.salesid, sales_update.listid, sales_update.sellerid, sales_update.buyerid, sales_update.eventid,
sales_update.dateid, sales_update.qtysold , sales_update.pricepaid, sales_update.commission, sales_update.saletime);

-- Drop the staging table.
drop table tickit.sales_update;

-- Test to see that commission and salestime were not impacted.
SELECT sales.salesid, sales.commission, sales.salestime, sales_update.commission, sales_update.salestime
FROM tickit.sales
INNER JOIN tickit.sales_update sales_update
ON
sales.salesid = sales_update.salesid
AND sales.listid = sales_update.listid
AND sales_update.saletime > '2008-11-30'
AND (sales.commission != sales_update.commission
OR sales.salestime != sales_update.salestime);
```

**Example of a merge that specifies a column list without using MERGE**

The following example performs a merge operation to update SALES with new data for
December sales activity. We need sample data that includes both updates and inserts,
along with rows that have not changed. For this example, we want to update the QTYSOLD
and PRICEPAID columns but leave COMMISSION and SALETIME unchanged. The following script
uses the SALES_UPDATE table to perform a merge operation on the SALES table.

```
-- Create a staging table and populate it with rows from SALES_UPDATE for Dec
create temp table stagesales as select * from sales_update
where saletime > '2008-11-30';

-- Start a new transaction
begin transaction;

-- Update the target table using an inner join with the staging table
-- The join includes a redundant predicate to collocate on the distribution key –- A filter on saletime enables a range-restricted scan on SALES

update sales
set qtysold = stagesales.qtysold,
pricepaid = stagesales.pricepaid
from stagesales
where sales.salesid = stagesales.salesid
and sales.listid = stagesales.listid
and stagesales.saletime > '2008-11-30'
and (sales.qtysold != stagesales.qtysold
or sales.pricepaid != stagesales.pricepaid);

-- Delete matching rows from the staging table
-- using an inner join with the target table

delete from stagesales
using sales
where sales.salesid = stagesales.salesid
and sales.listid = stagesales.listid;

-- Insert the remaining rows from the staging table into the target table
insert into sales
select * from stagesales;

-- End transaction and commit
end transaction;

-- Drop the staging table
drop table stagesales;
```
