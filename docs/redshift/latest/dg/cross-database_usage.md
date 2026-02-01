Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations

This topic describes usage details for cross-database queries in Amazon Redshift.

When you work with the cross-database query feature in Amazon Redshift, consider the
following:

- Amazon Redshift supports cross-database query on all ra3 node types and serverless namespaces.
- Amazon Redshift supports joining data from tables or views across one or more databases in the same Amazon Redshift cluster.
- All queries in a transaction on the connected database read data in the same state of the
  other database as the data was at the beginning of the transaction. This approach
  helps to provide query transactional consistency across databases. Amazon Redshift supports
  transactional consistency for cross-database queries.
- To get metadata across databases, use SVV_ALL\* and SVV_REDSHIFT\* metadata views. You can't use the three-part notation or external schemas to query cross-database metadata tables or views under information_schema and pg_catalog.
