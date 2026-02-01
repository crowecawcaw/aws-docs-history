Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting the JDBC fetch size parameter

By default, the Redshift JDBC driver uses a ring buffer to manage memory efficiently
and prevent out-of-memory errors. The fetch size parameter is only applicable when the
ring buffer is explicitly disabled. For more information, review the [link](../mgmt/jdbc20-configuration-options.md#jdbc20-enablefetchringbuffer-option "../mgmt/jdbc20-configuration-options.md#jdbc20-enablefetchringbuffer-option").
In this configuration, you should set the fetch size to control how many rows are retrieved in each batch.

###### When to Use Fetch Size?

Use the fetch size parameter when:

- You need fine-grained control over row-based batching
- Working with legacy applications that require traditional fetch size behavior

###### Setting Fetch Size

When ring buffer is disabled, the JDBC driver collects all results for a query at one time by default.
Queries that return large result sets can consume excessive memory. To retrieve
result sets in batches instead of all at once, set the JDBC fetch size parameter in your application.

###### Note

Fetch size is not supported for ODBC.

For the best performance, set the fetch size to the highest value that does not lead
to out of memory errors. A lower fetch size value results in more server trips, which
prolong execution times. The server reserves resources, including the WLM query slot and
associated memory, until the client retrieves the entire result set or the query is
canceled. When you tune the fetch size appropriately, those resources are released more
quickly, making them available to other queries.

###### Note

If you need to extract large datasets, we recommend using an
[UNLOAD](r_UNLOAD.md "r_UNLOAD.md")
statement to transfer the data to
Amazon S3. When you use UNLOAD, the compute nodes work in parallel to speed up the
transfer of data.

For more information about setting the JDBC fetch size parameter, go to [Getting results based on a cursor](https://jdbc.postgresql.org/documentation/query/#getting-results-based-on-a-cursor "https://jdbc.postgresql.org/documentation/query/#getting-results-based-on-a-cursor") in the PostgreSQL documentation.
