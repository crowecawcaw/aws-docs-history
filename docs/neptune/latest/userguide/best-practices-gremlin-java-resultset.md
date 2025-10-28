# Always completely consume the

ResultSet or Iterator returned by a query

The client object should always completely consume the `ResultSet` (in
the case of string-based submission), or the iterator returned by `GraphTraversal`.
If the query results are not completely consumed, the server holds onto them, waiting
for the client to finish consuming them.

If your application only needs a partial set of results, you can use a `limit(X)`
step with your query to restrict the number of results that the server generates.
