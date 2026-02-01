Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift and PostgreSQL JDBC and

ODBC

Because Amazon Redshift is based on PostgreSQL, we previously recommended using JDBC4
Postgresql driver version 8.4.703 and psqlODBC version 9.x drivers. If you are
currently using those drivers, we recommend moving to the new Amazon Redshift–specific
drivers going forward. For more information about drivers and configuring
connections, see [JDBC and ODBC
Drivers for Amazon Redshift](../mgmt/configuring-connections.md#connecting-drivers "../mgmt/configuring-connections.md#connecting-drivers") in the _Amazon Redshift Management Guide_.

To avoid client-side out-of-memory errors when retrieving large data sets using
JDBC, you can enable your client to fetch data in batches by setting the JDBC fetch
size parameter. For more information, see [Setting the JDBC fetch size parameter](set-the-JDBC-fetch-size-parameter.md "set-the-JDBC-fetch-size-parameter.md").

Amazon Redshift does not recognize the JDBC maxRows parameter. Instead, specify a [LIMIT](r_ORDER_BY_clause.md#order-by-clause-limit "r_ORDER_BY_clause.md#order-by-clause-limit") clause to restrict the result set. You can also
use an [OFFSET](r_ORDER_BY_clause.md#order-by-clause-offset "r_ORDER_BY_clause.md#order-by-clause-offset") clause to skip to a specific starting
point in the result set.
