Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Multidimensional data layout sorting

A multidimensional data layout sort key is a type of AUTO sort key that is based
on repetitive predicates found in a workload. If your workload has repetitive
predicates, then Amazon Redshift can improve table scan performance by colocating data rows
that satisfy the repetitive predicates. Instead of storing data of a table in strict
column order, a multidimensional data layout sort key stores data by analyzing
repetitive predicates that appear in a workload. More than one repetitive predicate
can be found in a workload. Depending on your workload, this kind of sort key can
improve performance of many predicates. Amazon Redshift automatically determines if this sort
key method should be used for tables that are defined with an `AUTO` sort
key.

For example, suppose you have a table that has data sorted in column order.
Many data blocks might need to be examined to determine if they satisfy the predicates in your workload.
But, if the data is stored on disk in a predicate order, then fewer blocks need to be scanned to satisfy the query.
Using a multidimensional data layout sort key is beneficial in this case.

To view whether a query is using a multidimensional data layout key, see the
`step_attribute` column of the [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md") view. When the value is
`multi-dimensional` then multidimensional data layout was used for
the query.

To prevent Amazon Redshift from using a multidimensional data layout sort key, choose a different table sort key option other than `SORTKEY AUTO`.
For more information on SORTKEY options, see
[CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md").
