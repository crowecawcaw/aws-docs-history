Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SUPER data type and materialized views

With Amazon Redshift, you can use materialized views to enhance the performance and flexibility of
queries run against the SUPER data type. The SUPER data type lets you store a superset of columns from the
base tables in a materialized view, letting you query the materialized view directly
without joining the base tables. The following sections show you how to create and use
materialized views with the SUPER data type in Amazon Redshift.

Amazon Redshift supports materialized views that incorporate SUPER data type columns and
PartiQL queries. Materialized views can incrementally refresh, whereas Amazon Redshift only
updates data that has changed in the base tables since the last refresh operation.
This selective update approach makes the refresh process more efficient than full
recalculations. For more information about materialized views, see [Materialized views in Amazon Redshift](materialized-view-overview.md "materialized-view-overview.md").

## Accelerating PartiQL queries

You can use materialized views to accelerate PartiQL queries that navigate and/or
unnest hierarchical data in SUPER columns. By creating one or more materialized views to
shred the SUPER values into multiple columns and utilize the columnar organization of
Amazon Redshift analytical queries, you can essentially extract and normalize nested data.
The level of normalization depends on how much effort you put into turning the
SUPER data into conventional columnar data.

The following topics showcase examples of breaking down, or shredding, complex data into smaller columns,
as well as creating scalar columns out of shredded data to improve performance.

###### Topics

- [Shredding semi-structured data into SUPER columns with materialized views](r_shred_super.md "r_shred_super.md")
- [Creating Amazon Redshift scalar columns out of shredded
  data](r_create_scalar.md "r_create_scalar.md")
