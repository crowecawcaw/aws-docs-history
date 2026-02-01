Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Query hangs

Your query can hang, or stop responding, for the following reasons. We suggest the
following troubleshooting approaches.

###### Connection to the database is dropped

Reduce the size of maximum transmission unit (MTU). The MTU size determines the
maximum size, in bytes, of a packet that can be transferred in one Ethernet frame
over your network connection. For more information, go to [The connection to the database is
dropped](../mgmt/connecting-drop-issues.md "../mgmt/connecting-drop-issues.md") in the _Amazon Redshift Management Guide._

###### Connection to the database times out

Your client connection to the database appears to hang or time out when running
long queries, such as a COPY command. In this case, you might observe that the
Amazon Redshift console displays that the query has completed, but the client tool itself
still appears to be running the query. The results of the query might be missing or
incomplete depending on when the connection stopped. This effect happens when idle
connections are terminated by an intermediate network component. For more
information, go to [Firewall Timeout Issue](../mgmt/connecting-firewall-guidance.md "../mgmt/connecting-firewall-guidance.md") in the _Amazon Redshift Management Guide._

###### Client-side out-of-memory error occurs with ODBC

If your client application uses an ODBC connection and your query creates a result
set that is too large to fit in memory, you can stream the result set to your client
application by using a cursor. For more information, see [DECLARE](declare.md "declare.md") and [Performance considerations when using
cursors](declare.md#declare-performance "declare.md#declare-performance").

###### Client-side out-of-memory error occurs with JDBC

When you attempt to retrieve large result sets over a JDBC connection, you might
encounter client-side out-of-memory errors. For more information, see [Setting the JDBC fetch size parameter](set-the-JDBC-fetch-size-parameter.md "set-the-JDBC-fetch-size-parameter.md").

###### There is a potential deadlock

If there is a potential deadlock, try the following:

- View the [STV_LOCKS](r_STV_LOCKS.md "r_STV_LOCKS.md") and [STL_TR_CONFLICT](r_STL_TR_CONFLICT.md "r_STL_TR_CONFLICT.md") system tables
  to find conflicts involving updates to more than one table.
- Use the [PG_CANCEL_BACKEND](PG_CANCEL_BACKEND.md "PG_CANCEL_BACKEND.md")
  function to cancel one or more conflicting queries.
- Use the [PG_TERMINATE_BACKEND](PG_TERMINATE_BACKEND.md "PG_TERMINATE_BACKEND.md") function to terminate a session, which
  forces any currently running transactions in the terminated session to release all
  locks and roll back the transaction.
- Schedule concurrent write operations carefully. For more information, see [Managing concurrent write operations](c_Concurrent_writes.md "c_Concurrent_writes.md").
