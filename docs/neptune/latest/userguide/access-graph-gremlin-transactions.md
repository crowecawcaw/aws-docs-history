# Gremlin transactions in Neptune

There are several contexts within which Gremlin [transactions](transactions.md "transactions.md")
are executed. When working with Gremlin it is important to understand the context you are working
within and what its implications are:

- **`Script-based`**   –  
  Requests are made using text-based Gremlin strings, like this:
  - Using the Java driver and `Client.submit(`string`)`.
  - Using the Gremlin console and `:remote connect`.
  - Using the HTTP API.

- **`Bytecode-based`**   –  
  Requests are made using serialized Gremlin bytecode typical of [Gremlin
  Language Variants](https://tinkerpop.apache.org/docs/current/reference/#gremlin-drivers-variants "https://tinkerpop.apache.org/docs/current/reference/#gremlin-drivers-variants")(GLV).

For example, using the Java driver,
`g = traversal().withRemote(`...`)`.
For either of the above contexts, there is the additional context of the request
being sent as sessionless or as bound to a session.

###### Note

Gremlin transactions must always either be committed or rolled back, so that server-side resources can be released. In the
event of an error during the transaction, it is important to retry the entire transaction and not just the particular
request that failed.

## Sessionless requests

When sessionless, a request is equivalent to a single transaction.

For scripts, the implication is that one or more Gremlin statements sent in a single
request will commit or rollback as a single transaction. For example:

```
Cluster cluster = Cluster.open();
Client client = cluster.connect(); // sessionless
// 3 vertex additions in one request/transaction:
client.submit("g.addV();g.addV();g.addV()").all().get();
```

For bytecode, a sessionless request is made for each traversal spawned and executed
from `g`:

```
GraphTraversalSource g = traversal().withRemote(`...`);

// 3 vertex additions in three individual requests/transactions:
g.addV().iterate();
g.addV().iterate();
g.addV().iterate();

// 3 vertex additions in one single request/transaction:
g.addV().addV().addV().iterate();
```

## Requests bound to a session

When bound to a session, multiple requests can be applied within the context of
a single transaction.

For scripts, the implication is that there is no need to concatenate together all
of the graph operations into a single embedded string value:

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

For bytecode, after TinkerPop `3.5.x`, the transaction can be explicitly controlled
and the session managed transparently. Gremlin Language Variants (GLV) support Gremlin's
`tx()` syntax to `commit()` or `rollback()` a transaction
as follows:

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

Although the example above is written in Java, you can also use this `tx()`
syntax in Python, Javascript and .NET.

###### Warning

Sessionless read-only queries are executed under [SNAPSHOT](transactions-isolation-levels.md "transactions-isolation-levels.md") isolation,
but read-only queries run within an explicit transaction are executed under
[SERIALIZABLE](transactions-isolation-levels.md "transactions-isolation-levels.md") isolation.
The read-only queries executed under `SERIALIZABLE` isolation
incur higher overhead and can block or get blocked by concurrent writes,
unlike those run under `SNAPSHOT` isolation.
