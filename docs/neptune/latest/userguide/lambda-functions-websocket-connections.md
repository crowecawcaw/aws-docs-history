# Managing Gremlin WebSocket connections in AWS Lambda functions

If you use a Gremlin language variant to query Neptune, the driver connects to
the database using a WebSocket connection. WebSockets are designed to support
long-lived client-server connection scenarios. AWS Lambda, on the other hand, is
designed to support relatively short-lived and stateless executions. This mismatch
in design philosophy can lead to some unexpected issues when using Lambda to query
Neptune.

An AWS Lambda function runs in an [execution
context](../../../lambda/latest/dg/runtimes-context.md "../../../lambda/latest/dg/runtimes-context.md") which isolates the function from other functions. The execution context is
created the first time the function is invoked and may be reused for subsequent invocations
of the same function.

Any one execution context is never used to handle multiple concurrent invocations
of the function, however. If your function is invoked simultaneously by multiple clients,
Lambda [spins up an additional execution
context](../../../lambda/latest/dg/configuration-concurrency.md "../../../lambda/latest/dg/configuration-concurrency.md") for each instance of the function. All these new execution contexts may in
turn be reused for subsequent invocations of the function.

At some point, Lambda recycles execution contexts, particularly if they have been
inactive for some time. AWS Lambda exposes the execution context lifecycle, including
the `Init`, `Invoke` and `Shutdown` phases, through
[Lambda extensions](../../../lambda/latest/dg/using-extensions.md "../../../lambda/latest/dg/using-extensions.md"). Using
these extensions, you can write code that cleans up external resources such as database
connections when the execution context is recycled.

A common best practice is to [open
the database connection outside the Lambda handler function](../../../lambda/latest/dg/best-practices.md "../../../lambda/latest/dg/best-practices.md") so that it can be
reused with each handler call. If the database connection drops at some point, you
can reconnect from inside the handler. However, there is a danger of connection leaks
with this approach. If an idle connection stays open long after an execution context
is destroyed, intermittent or bursty Lambda invocation scenarios can gradually leak
connections and exhaust database resources.

Neptune connection limits and connection timeouts have changed with newer
engine releases. Previously, every instance supported up to 60,000 WebSocket
connections. Now, the maximum number of concurrent WebSocket connections per
Neptune instance [varies with the instance
type](limits.md "limits.md").

Also, starting with engine release 1.0.3.0, Neptune reduced the
idle timeout for connections from one hour down to approximately 20 minutes.
If a client doesn't close a connection, the connection is closed automatically
after a 20- to 25-minute idle timeout. AWS Lambda doesn't document execution
context lifetimes, but experiments show that the new Neptune connection
timeout aligns well with inactive Lambda execution context timeouts. By the
time an inactive execution context is recycled, there's a good chance its
connection has already been closed by Neptune, or will be closed soon
afterwards.
