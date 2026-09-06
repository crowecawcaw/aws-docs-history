

# Gremlin transactions in Neptune
<a name="access-graph-gremlin-transactions"></a>

There are several contexts within which Gremlin [transactions](transactions.md) are executed. When working with Gremlin it is important to understand the context you are working within and what its implications are:
+ **`Script-based`**   –   Requests are made using text-based Gremlin strings, like this:
  + Using the Java driver and `Client.submit({{string}})`.
  + Using the Gremlin console and `:remote connect`.
  + Using the HTTP API.
+ **`Bytecode-based`**   –   Requests are made using serialized Gremlin bytecode typical of [Gremlin Language Variants](https://tinkerpop.apache.org/docs/current/reference/#gremlin-drivers-variants)(GLV).

  For example, using the Java driver, `g = traversal().withRemote({{...}})`.

For either of the above contexts, there is the additional context of the request being sent as sessionless or as bound to a session.

**Note**  
 Gremlin transactions must always either be committed or rolled back, so that server-side resources can be released. In the event of an error during the transaction, it is important to retry the entire transaction and not just the particular request that failed. 

## Sessionless requests
<a name="access-graph-gremlin-transactions-sessionless"></a>

 When sessionless, a request is equivalent to a single transaction.

For scripts, the implication is that one or more Gremlin statements sent in a single request will commit or rollback as a single transaction. For example:

```
Cluster cluster = Cluster.open();
Client client = cluster.connect(); // sessionless
// 3 vertex additions in one request/transaction:
client.submit("g.addV();g.addV();g.addV()").all().get();
```

For bytecode, a sessionless request is made for each traversal spawned and executed from `g`:

```
GraphTraversalSource g = traversal().withRemote({{...}});

// 3 vertex additions in three individual requests/transactions:
g.addV().iterate();
g.addV().iterate();
g.addV().iterate();

// 3 vertex additions in one single request/transaction:
g.addV().addV().addV().iterate();
```

## Requests bound to a session
<a name="access-graph-gremlin-transactions-session-bound"></a>

When bound to a session, multiple requests can be applied within the context of a single transaction.

For scripts, the implication is that there is no need to concatenate together all of the graph operations into a single embedded string value:

```
Cluster cluster = Cluster.open();
Client client = cluster.connect(sessionName); // session
try {
    // 3 vertex additions in one request/transaction:
    client.submit("g.addV();g.addV();g.addV()").all().get();
} finally {
    client.close();
}

try {
    // 3 vertex additions in three requests, but one transaction:
    client.submit("g.addV()").all().get(); // starts a new transaction with the same sessionName
    client.submit("g.addV()").all().get();
    client.submit("g.addV()").all().get();
} finally {
    client.close();
}
```

For script-based sessions, closing the client with `client.close()` commits the transaction. There is no explicit rollback command available in script-based sessions. To force a rollback, you can cause the transaction to fail by issuing a query such as `g.inject(0).fail('rollback')` before closing the client.

**Note**  
A query like `g.inject(0).fail('rollback')`, used to intentionally throw an error to force a rollback, produces an exception on the client. Catch and discard the resulting exception before closing the client.

For bytecode, the transaction can be explicitly controlled and the session managed transparently. Gremlin Language Variants (GLV) support Gremlin's `tx()` syntax to `commit()` or `rollback()` a transaction as follows:

```
GraphTraversalSource g = traversal().withRemote(conn);

Transaction tx = g.tx();

// Spawn a GraphTraversalSource from the Transaction.
// Traversals spawned from gtx are executed within a single transaction.
GraphTraversalSource gtx = tx.begin();
try {
    gtx.addV('person').iterate();
    gtx.addV('software').iterate();

    tx.commit();
} finally {
    if (tx.isOpen()) {
        tx.rollback();
    }
}
```

Although the example above is written in Java, you can also use this `tx()` syntax in other languages. For language-specific transaction syntax, see the Transactions section of the Apache TinkerPop documentation for [Java](https://tinkerpop.apache.org/docs/current/reference/#gremlin-java-transactions), [Python](https://tinkerpop.apache.org/docs/current/reference/#gremlin-python-transactions), [Javascript](https://tinkerpop.apache.org/docs/current/reference/#gremlin-javascript-transactions), [.NET](https://tinkerpop.apache.org/docs/current/reference/#gremlin-dotnet-transactions), and [Go](https://tinkerpop.apache.org/docs/current/reference/#gremlin-go-transactions).

**Warning**  
Sessionless read-only queries are executed under [SNAPSHOT](transactions-isolation-levels.md) isolation, but read-only queries run within an explicit transaction are executed under [SERIALIZABLE](transactions-isolation-levels.md) isolation. The read-only queries executed under `SERIALIZABLE` isolation incur higher overhead and can block or get blocked by concurrent writes, unlike those run under `SNAPSHOT` isolation.

## Timeout behavior for bytecode commit and rollback
<a name="access-graph-gremlin-transactions-commit-rollback-timeout"></a>

When you use bytecode-based transactions with the `tx()` syntax, the `commit()` and `rollback()` operations are not subject to query timeout settings. Neither the global `neptune_query_timeout` parameter nor per-query timeout values set through `evaluationTimeout` apply to these operations. On the server, `commit()` and `rollback()` run without a time limit until they complete or encounter an error.

On the client side, the Gremlin driver's `tx.commit()` and `tx.rollback()` calls will not complete until the server responds. Depending on the language, this might manifest as a blocking call or an unresolved async operation. No driver provides a built-in timeout setting that bounds these calls. Consult the API documentation for your specific Gremlin Language Variant for details on concurrency behavior around these transaction features.

**Important**  
If a `commit()` or `rollback()` call takes longer than expected, it might be blocked by lock contention from a concurrent transaction. For more information about lock conflicts, see [Conflict Resolution Using Lock-Wait Timeouts](transactions-neptune.md#transactions-neptune-conflicts).

If you need to bound the time your application waits for a `commit()` or `rollback()`, you can use your language's concurrency features to apply a client-side timeout. If the client-side timeout fires, the server continues processing the operation. The server-side operation holds a worker thread until it completes. After a client-side timeout, close the connection and create a new one rather than reusing the existing connection, because the transaction state is indeterminate.

### Server-side transaction cleanup
<a name="access-graph-gremlin-transactions-server-side-cleanup"></a>

If a client disconnects or abandons a transaction without committing or rolling back, Neptune has server-side mechanisms that eventually clean up the orphaned transaction:
+ **Session timeout**   –   Bytecode-based sessions that remain idle for longer than the maximum session lifetime (10 minutes) are closed, and any open transaction is rolled back.
+ **Connection idle timeout**   –   Neptune closes WebSocket connections that are idle for approximately 20 minutes. When the connection closes, the server rolls back any open transaction associated with that connection.

These cleanup mechanisms are safety nets. We recommend that you always explicitly commit or roll back transactions when you are finished with them.