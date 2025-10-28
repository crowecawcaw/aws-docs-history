# Security Lake queries

You can query the data that Security Lake stores in AWS Lake Formation databases and tables. You can also create third-party subscribers in the Security Lake console, API, or
AWS CLI. Third-party subscribers can also query Lake Formation data from the sources that you specify.

The Lake Formation data lake administrator must grant `SELECT` permissions on the relevant databases and
tables to the IAM identity that queries the data. A subscriber must also be created in Security Lake before it can query
data. For more information about how to create a subscriber with query access, see [Managing query access for Security Lake
subscribers](subscriber-query-access.md "subscriber-query-access.md").

**Querying data with retention settings**

The [Amazon S3 Lifecycle settings](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") affect how long data is kept,
which in turn affects how far back in time you can query.
If you have retention settings configured in Security Lake, you must include a time-based filter in your queries
to ensure your result sets are scoped to the data files that have not expired. For more information about data retention
in Security Lake, see [Lifecycle management](lifecycle-management.md "lifecycle-management.md").

The query examples in the following sections include time-based filters, such as `eventDay` or `time_dt`,
to demonstrate this best practice.

###### Topics

- [Security Lake queries for AWS source version 1 (OCSF 1.0.0-rc.2)](subscriber-query-examples1.md "subscriber-query-examples1.md")
- [Security Lake queries for AWS source version 2 (OCSF 1.1.0)](subscriber-query-examples2.md "subscriber-query-examples2.md")
