# Recommendations for using AWS Lambda with Amazon Neptune Gremlin

We now recommend using a single connection and graph traversal source
for the entire lifetime of a Lambda execution context, rather than one for each
function invocation (every function invocation handles only one client request).
Because concurrent client requests are handled by different function instances
running in separate execution contexts, there's no need to maintain a pool
of connections to handle concurrent requests inside a function instance.
If the Gremlin driver you’re using has a connection pool, configure it to use
just one connection.

To handle connection failures, use retry logic around each query. Even though
the goal is to maintain a single connection for the lifetime of an execution context,
unexpected network events can cause that connection to be terminated abruptly.
Such connection failures manifest as different errors depending on which driver you
are using. You should code your Lambda function to handle these connection issues
and attempt a reconnection if necessary.

Some Gremlin drivers automatically handle reconnections. The Java driver, for
example, automatically attempts to reestablish connectivity to Neptune on behalf of
your client code. With this driver, your function code only needs to back off and
retry the query. The JavaScript and Python drivers, by contrast, do not implement
any automatic reconnection logic, so with these drivers your function code must
try to reconnect after backing off, and only retry the query once the connection
has been re-established.

Code examples here do include reconnection logic rather than assume that the
client is taking care of it.
