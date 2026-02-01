Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Loading tables with DML commands

Amazon Redshift supports standard data manipulation language (DML) commands (INSERT, UPDATE,
and DELETE) that you can use to modify rows in tables. You can also use the TRUNCATE
command to do fast bulk deletes.

###### Note

We strongly encourage you to use the [COPY](r_COPY.md "r_COPY.md")
command to load large amounts of data. Using individual INSERT statements to populate a
table might be prohibitively slow. Alternatively, if your data already exists in other
Amazon Redshift database tables, use INSERT INTO ... SELECT FROM or CREATE TABLE AS to improve
performance. For information, see [INSERT](r_INSERT_30.md "r_INSERT_30.md") or [CREATE TABLE AS](r_CREATE_TABLE_AS.md "r_CREATE_TABLE_AS.md").

If you insert, update, or delete a significant number of rows in a table, relative to
the number of rows before the changes, run the ANALYZE and VACUUM commands against the
table when you are done. If a number of small changes accumulate over time in your
application, you might want to schedule the ANALYZE and VACUUM commands to run at regular
intervals. For more information, see [Analyzing tables](t_Analyzing_tables.md "t_Analyzing_tables.md") and [Vacuuming tables](t_Reclaiming_storage_space202.md "t_Reclaiming_storage_space202.md").

###### Topics

- [Updating and inserting new
  data](t_updating-inserting-using-staging-tables-.md "t_updating-inserting-using-staging-tables-.md")
