Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Considerations

This topic describes usage details for cross-database queries in Amazon Redshift.

When you work with the cross-database query feature in Amazon Redshift, consider the
following:

- Amazon Redshift supports cross-database query on all RG and RA3 node types and serverless namespaces.
- Amazon Redshift supports joining data from tables or views across one or more databases in the same Amazon Redshift cluster.
- All queries in a transaction on the connected database read data in the same state of the
  other database as the data was at the beginning of the transaction. This approach
  helps to provide query transactional consistency across databases. Amazon Redshift supports
  transactional consistency for cross-database queries.
- To get metadata across databases, use SVV\_ALL\* and SVV\_REDSHIFT\* metadata views. You can't use the three-part notation or external schemas to query cross-database metadata tables or views under information\_schema and pg\_catalog.
