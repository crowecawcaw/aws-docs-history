# Test Gremlin code in the context where you will deploy it

In Gremlin, there are multiple ways for clients to submit queries to the
server: using WebSocket, or Bytecode GLV, or through the Gremlin console using
string-based scripts.

It is important to recognize that Gremlin query execution can differ depending
on how you submit the query. A query that returns an empty result might be treated
as having succeeded if submitted in Bytecode mode, but be treated as having
failed if submitted in script mode. For example, if you include `next()`
in a script-mode query, the `next()` is sent to the server, but using
ByteCode the client usually processes the `next()` itself. In the first case, the query
fails if no results are found, but in the second, the query succeeds whether or not
the result set is empty.

If you develop and test your code in one context (for example, the Gremlin console
which generally submits queries in text form), but then deploy your code in a different
context (for example through the Java driver using Bytecode) you can run into problems
where your code behaves differently in production than it did in your development
environment.

###### Important

Be sure to test Gremlin code in the GLV context where it will
be deployed, to avoid unexpected results.
