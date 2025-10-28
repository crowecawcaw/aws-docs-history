Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Use a bulk insert

Use a bulk insert operation with a SELECT clause for high-performance data
insertion.

Use the [INSERT](r_INSERT_30.md "r_INSERT_30.md") and [CREATE TABLE AS](r_CREATE_TABLE_AS.md "r_CREATE_TABLE_AS.md") commands when you
need to move data or a subset of data from one table into another.

For example, the following INSERT statement selects all of the rows from the CATEGORY
table and inserts them into the CATEGORY_STAGE table.

```
insert into category_stage
(select * from category);
```

The following example creates CATEGORY_STAGE as a copy of CATEGORY and inserts all of
the rows in CATEGORY into CATEGORY_STAGE.

```
create table category_stage as
select * from category;
```
