

# Test Gremlin code in the context where you will deploy it
<a name="best-practices-gremlin-console-glv-differences"></a>

Gremlin provides multiple ways for clients to submit queries to the server. These submission modes differ in how queries are evaluated and how transactions behave. These differences can lead to unexpected results if you develop in one mode and deploy in another.

**Script mode (string-based submission)**  
In script mode, the client sends the entire query as a text string to the server. The server evaluates the complete string, including any *terminal steps*, and streams the results back to the client. The following tools and methods use script mode:
+ [Gremlin Console](access-graph-gremlin-console.md) – when using the `:remote` command
+ [Neptune graph notebook](graph-notebooks.md)
+ [HTTP with AWS SDK or AWS CLI](access-graph-gremlin-rest.md)
+ Submitting query strings through TinkerPop drivers (for example, using `client.submit("g.V().count()")` in Java)

In script mode, the client sends a query like the following to the server as a complete string:

```
// Script mode – the entire string, including .next(), is sent to the server
// V('non-existing-id') yields nothing because no vertex with that ID exists
Cluster cluster = Cluster.build().addContactPoint("your-neptune-endpoint")
                         .port(8182).enableSsl(true).create();
Client client = cluster.connect();
client.submit("g.V('existing-id').addV('person').V('non-existing-id').next()");
```

The server evaluates the full query including `.next()`. If `.next()` finds no results, the server raises a `NoSuchElementException` and the transaction *rolls back*.

**Bytecode mode (GLV traversal objects)**  
In bytecode mode, the client builds a traversal object locally using a Gremlin Language Variant (GLV). The driver serializes the traversal steps as bytecode and sends them to the server. Terminal steps such as `.toList()` or `.next()` execute on the *client side* to iterate over the results returned by the server. You can use bytecode mode with [Java](access-graph-gremlin-java.md), [Python](access-graph-gremlin-python.md), [Go](access-graph-gremlin-go.md), [.NET](access-graph-gremlin-dotnet.md), [JavaScript](access-graph-gremlin-node-js.md), and other third-party TinkerPop-compliant drivers suitable to the Neptune engine version used.

In bytecode mode, the same query looks like this:

```
// Bytecode mode – the driver sends the traversal steps as bytecode
// .next() executes on the client to iterate results
Cluster cluster = Cluster.build().addContactPoint("your-neptune-endpoint")
                         .port(8182).enableSsl(true).create();
GraphTraversalSource g = traversal().withRemote(
    DriverRemoteConnection.using(cluster));
g.V("existing-id").addV("person").V("non-existing-id").next();
```

The driver sends only the traversal steps (`g.V().addV().V()`) as bytecode. The server successfully evaluates the traversal, commits the transaction, and returns the result set. The client then calls `.next()` locally to read from the result set. If the result set is empty, the client raises a `NoSuchElementException`, but the transaction has *already committed* on the server.

**Transaction behavior differences**  
The critical difference between these modes is how terminal steps affect transactions:
+ **Script mode** – The server evaluates terminal steps. If a terminal step like `.next()` fails because the result set is empty, the server treats the query as failed and *rolls back* the transaction. The server does not persist any mutations in the same traversal (such as `addV()`).
+ **Bytecode mode** – The client evaluates terminal steps. The server evaluates only the traversal steps, successfully commits the transaction, and returns results. If the client then calls `.next()` on an empty result set, the resulting `NoSuchElementException` is a client-side error only. The transaction has already committed, so the server *persists* any mutations.

**Terminal steps**  
In Gremlin, [terminal steps](https://tinkerpop.apache.org/docs/current/reference/#terminal-steps) are the steps that cause a traversal to be submitted to Neptune for evaluation. In bytecode mode, the terminal step triggers the driver to serialize and send the traversal. In script mode, the terminal step is part of the query string evaluated on the server. The terminal steps are:
+ `hasNext()` – Returns `true` if results are available, `false` otherwise.
+ `next()` – Returns the next result. Throws `NoSuchElementException` if no results exist.
+ `next(n)` – Returns the next {{n}} results as a list.
+ `toList()` – Returns all results as a list. Returns an empty list if no results exist.
+ `toSet()` – Returns all results as a set. Returns an empty set if no results exist.
+ `iterate()` – Iterates all results without returning them. Use this for mutations where you do not need the return value.

**Note**  
Individual language GLVs may provide additional terminal steps specific to their implementation. See the language-specific pages for details.

If you develop and test your code in one context, you can run into problems. For example, the Gremlin console submits queries as scripts. Your code might behave differently in production if you deploy it in a different context, such as through the Java driver using bytecode.

**Important**  
Be sure to test Gremlin code using the same submission mode in which it will be deployed, to avoid unexpected transaction behavior.