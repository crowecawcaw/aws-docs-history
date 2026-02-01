Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Designating distribution

styles

The considerations and recommendations for designating distribution styles in
this section use a star schema as an example. Your database design might be based on
a star schema, some variant of a star schema, or an entirely different schema.
Amazon Redshift is designed to work effectively with whatever schema design you choose. The
principles in this section can be applied to any design schema.

1. **Specify the primary key and foreign keys for all your
   tables.**

Amazon Redshift does not enforce primary key and foreign key constraints, but the
query optimizer uses them when it generates query plans. If you set primary
keys and foreign keys, your application must maintain the validity of the
keys. 2. **Distribute the fact table and its largest dimension
table on their common columns.**

Choose the largest dimension based on the size of dataset that
participates in the most common join, not only the size of the table. If a
table is commonly filtered, using a WHERE clause, only a portion of its rows
participate in the join. Such a table has less impact on redistribution than
a smaller table that contributes more data. Designate both the dimension
table's primary key and the fact table's corresponding foreign key
as DISTKEY. If multiple tables use the same distribution key, they are also
collocated with the fact table. Your fact table can have only one
distribution key. Any tables that join on another key isn't collocated
with the fact table. 3. **Designate distribution keys for the other dimension
tables.**

Distribute the tables on their primary keys or their foreign keys,
depending on how they most commonly join with other tables. 4. **Evaluate whether to change some of the dimension
tables to use ALL distribution.**

If a dimension table cannot be collocated with the fact table or other
important joining tables, you can improve query performance significantly by
distributing the entire table to all of the nodes. Using ALL distribution
multiplies storage space requirements and increases load times and
maintenance operations, so you should weigh all factors before choosing ALL
distribution. The following section explains how to identify candidates for
ALL distribution by evaluating the EXPLAIN plan. 5. **Use AUTO distribution for the remaining
tables.**

If a table is largely denormalized and does not participate in joins, or
if you don't have a clear choice for another distribution style, use AUTO
distribution.
To let Amazon Redshift choose the appropriate distribution style, don't explicitly specify a
distribution style.
