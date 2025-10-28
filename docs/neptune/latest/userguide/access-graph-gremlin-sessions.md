# Support for Gremlin script-based sessions

You can use Gremlin sessions with implicit transactions in Amazon Neptune. For information
about Gremlin sessions, see [Considering
Sessions](http://tinkerpop.apache.org/docs/current/reference/#sessions "http://tinkerpop.apache.org/docs/current/reference/#sessions") in the Apache TinkerPop documentation. The sections below describe how
to use Gremlin sessions with Java.

###### Note

This feature is available starting in [Neptune
engine release 1.0.1.0.200463.0](engine-releases-1.0.1.0.200463.md "engine-releases-1.0.1.0.200463.md").

Starting with [Neptune engine release 1.1.1.0](engine-releases-1.1.1.md "engine-releases-1.1.1.md")
and TinkerPop version 3.5.2, you can also use [Gremlin transactions](access-graph-gremlin-transactions.md "access-graph-gremlin-transactions.md").

###### Important

Currently, the longest time Neptune can keep a script-based session open is 10 minutes.
If you don't close a session before that, the session times out and everything in it is
rolled back.

###### Topics

- [Gremlin sessions on the Gremlin console](#access-graph-gremlin-sessions-console "#access-graph-gremlin-sessions-console")
- [Gremlin sessions in the Gremlin Language
  Variant](#access-graph-gremlin-sessions-glv "#access-graph-gremlin-sessions-glv")

## Gremlin sessions on the Gremlin console

If you create a remote connection on the Gremlin Console without the `session`
parameter, the remote connection is created in _sessionless_ mode. In this
mode, each request that is submitted to the server is treated as a complete transaction in
itself, and no state is saved between requests. If a request fails, only that request is
rolled back.

If you create a remote connection that _does_ use the
`session` parameter, you create a script-based session that lasts until you
close the remote connection. Every session is identified by a unique UUID that the console
generates and returns to you.

The following is an example of one console call that creates a session. After queries are
submitted, another call closes the session and commits the queries.

###### Note

The Gremlin client must always be closed to release server side resources.

```
gremlin> :remote connect tinkerpop.server conf/neptune-remote.yaml session
  . . .
  . . .
gremlin> :remote close
```

For more information and examples, see [Sessions](http://tinkerpop.apache.org/docs/current/reference/#console-sessions "http://tinkerpop.apache.org/docs/current/reference/#console-sessions")
in the TinkerPop documentation.

All the queries that you run during a session form a single transaction that isn't
committed until all the queries succeed and you close the remote connection. If a query fails,
or if you don't close the connection within the maximum session lifetime that Neptune
supports, the session transaction is not committed, and all the queries in it are rolled
back.

## Gremlin sessions in the Gremlin Language

Variant

In the Gremlin language variant (GLV), you need to create a `SessionedClient`
object to issue multiple queries in a single transaction, as in the following example.

```
try {                              // line 1
  Cluster cluster = Cluster.open();                    // line 2
  Client client = cluster.connect("sessionName");      // line 3
   ...
   ...
} finally {
  // Always close. If there are no errors, the transaction is committed; otherwise, it's rolled back.
  client.close();
}

```

Line 3 in the preceding example creates the `SessionedClient` object
according to the configuration options set for the cluster in question. The
`sessionName` string that you pass to the connect method
becomes the unique name of the session. To avoid collisions, use a UUID for the name.

The client starts a session transaction when it is initialized. All the queries that you
run during the session form are committed only when you call `client.close( )`.
Again, if a single query fails, or if you don't close the connection within the maximum
session lifetime that Neptune supports, the session transaction fails, and all the queries
in it are rolled back.

###### Note

The Gremlin client must always be closed to release server side resources.

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
