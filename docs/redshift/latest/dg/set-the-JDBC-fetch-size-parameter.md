Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting the JDBC fetch size parameter

By default, the JDBC driver collects all the results for a query at one time. As a
result, when you attempt to retrieve a large result set over a JDBC connection, you
might encounter a client-side out-of-memory error. To enable your client to retrieve
result sets in batches instead of in a single all-or-nothing fetch, set the JDBC fetch
size parameter in your client application.

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
