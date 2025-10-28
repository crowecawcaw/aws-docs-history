# Best practices: getting the most out of Neptune

The following are some general recommendations for working with Amazon Neptune. Use this
information as a reference to quickly find recommendations for using Amazon Neptune and
maximizing performance.

###### Contents

- [Amazon Neptune basic operational guidelines](best-practices-general-basic.md "best-practices-general-basic.md")
  - [Amazon Neptune security best practices](best-practices-general-security.md "best-practices-general-security.md")
  - [Avoid different instance classes in a cluster](best-practices-general-basic.md#best-practices-loader-heterogeneous-instances "best-practices-general-basic.md#best-practices-loader-heterogeneous-instances")
  - [Avoid repeated restarts during bulk loading](best-practices-general-basic.md#best-practices-loader-repeated-restarts "best-practices-general-basic.md#best-practices-loader-repeated-restarts")
  - [Enable the OSGP Index if you have a large number of predicates](best-practices-general-basic.md#best-practices-general-predicates "best-practices-general-basic.md#best-practices-general-predicates")
  - [Avoid long-running transactions where possible](best-practices-general-basic.md#best-practices-general-long-running-transactions "best-practices-general-basic.md#best-practices-general-long-running-transactions")
  - [Best practices for using Neptune metrics](best-practices-general-metrics.md "best-practices-general-metrics.md")
  - [Best practices for tuning Neptune queries](best-practices-general-basic.md#best-practices-general-tuning "best-practices-general-basic.md#best-practices-general-tuning")
  - [Load balancing across read replicas](best-practices-general-basic.md#best-practices-general-loadbalance "best-practices-general-basic.md#best-practices-general-loadbalance")
  - [Loading faster using a temporary larger
    instance](best-practices-general-basic.md#best-practices-loader-tempinstance "best-practices-general-basic.md#best-practices-loader-tempinstance")
  - [Resize your writer instance by failing over to a read-replica](best-practices-general-basic.md#best-practices-resize-instance "best-practices-general-basic.md#best-practices-resize-instance")
  - [Retry upload after data prefetch task interrupted error](best-practices-general-basic.md#load-api-reference-status-interrupted "best-practices-general-basic.md#load-api-reference-status-interrupted")

- [General Best Practices for Using Gremlin with Neptune](best-practices-gremlin.md "best-practices-gremlin.md")
  - [Structure upsert queries to take advantage of the DFE engine](best-practices-gremlin.md#best-practices-gremlin-upserts "best-practices-gremlin.md#best-practices-gremlin-upserts")
  - [Test Gremlin code in the context where you will deploy it](best-practices-gremlin-console-glv-differences.md "best-practices-gremlin-console-glv-differences.md")
  - [Creating Efficient Multithreaded
    Gremlin Writes](best-practices-gremlin-multithreaded-writes.md "best-practices-gremlin-multithreaded-writes.md")
  - [Pruning Records with the Creation Time
    Property](best-practices-gremlin-prune.md "best-practices-gremlin-prune.md")
  - [Using the datetime( ) Method
    for Groovy Time Data](best-practices-gremlin-datetime.md "best-practices-gremlin-datetime.md")
  - [Using Native Date and Time for GLV
    Time Data](best-practices-gremlin-datetime-glv.md "best-practices-gremlin-datetime-glv.md")

- [Best practices using the Gremlin Java client with Neptune](best-practices-gremlin-java-client.md "best-practices-gremlin-java-client.md")
  - [Use the latest compatible version of the Apache TinkerPop Java client](best-practices-gremlin-java-client.md#best-practices-tinkerpop-java-client-latest "best-practices-gremlin-java-client.md#best-practices-tinkerpop-java-client-latest")
  - [Re-use the client object across multiple threads](best-practices-gremlin-java-reuse.md "best-practices-gremlin-java-reuse.md")
  - [Create separate Gremlin Java client
    objects for read and write endpoints](best-practices-gremlin-java-separate.md "best-practices-gremlin-java-separate.md")
  - [Add multiple read replica endpoints to a
    Gremlin Java connection pool](best-practices-gremlin-java-multiple.md "best-practices-gremlin-java-multiple.md")
  - [Close the client to avoid the connections limit](best-practices-gremlin-java-close-connections.md "best-practices-gremlin-java-close-connections.md")
  - [Create a new connection after
    failover](best-practices-gremlin-java-new-connection.md "best-practices-gremlin-java-new-connection.md")
  - [Set maxInProcessPerConnection
    and maxSimultaneousUsagePerConnection to the same value](best-practices-gremlin-java-maxes.md "best-practices-gremlin-java-maxes.md")
  - [Send queries to the server as bytecode rather than as strings](best-practices-gremlin-java-bytecode.md "best-practices-gremlin-java-bytecode.md")
  - [Always completely consume the
    ResultSet or Iterator returned by a query](best-practices-gremlin-java-resultset.md "best-practices-gremlin-java-resultset.md")
  - [Bulk add vertices and edges in batches](best-practices-gremlin-java-batch-add.md "best-practices-gremlin-java-batch-add.md")
  - [Disable DNS caching in the Java Virtual Machine](best-practices-gremlin-java-disable-dns-caching.md "best-practices-gremlin-java-disable-dns-caching.md")
  - [Optionally, set timeouts at a per-query level](best-practices-gremlin-java-per-query-timeout.md "best-practices-gremlin-java-per-query-timeout.md")
  - [Troubleshooting
    java.util.concurrent.TimeoutException](best-practices-gremlin-java-exceptions-TimeoutException.md "best-practices-gremlin-java-exceptions-TimeoutException.md")

- [Neptune Best Practices Using openCypher and Bolt](best-practices-opencypher.md "best-practices-opencypher.md")
  - [Create a new connection after failover](best-practices-opencypher.md#best-practices-opencypher-renew-connection "best-practices-opencypher.md#best-practices-opencypher-renew-connection")
  - [Connection handling for
    long-lived applications](best-practices-opencypher.md#best-practices-opencypher-long-connections "best-practices-opencypher.md#best-practices-opencypher-long-connections")
  - [Connection handling for AWS Lambda](best-practices-opencypher.md#best-practices-opencypher-lambda-connections "best-practices-opencypher.md#best-practices-opencypher-lambda-connections")
  - [Prefer directed to bi-directional edges in queries](best-practices-opencypher-directed-edges.md "best-practices-opencypher-directed-edges.md")
  - [Neptune does not support
    multiple concurrent queries in a transaction](best-practices-opencypher-multiple-queries.md "best-practices-opencypher-multiple-queries.md")
  - [Close driver objects when you're done](best-practices-opencypher-close-driver.md "best-practices-opencypher-close-driver.md")
  - [Use explicit transaction modes for reading and writing](best-practices-opencypher-use-explicit-txs.md "best-practices-opencypher-use-explicit-txs.md")
    - [Read-only transactions](best-practices-opencypher-use-explicit-txs.md#best-practices-opencypher-read-txs "best-practices-opencypher-use-explicit-txs.md#best-practices-opencypher-read-txs")
    - [Mutation transactions](best-practices-opencypher-use-explicit-txs.md#best-practices-opencypher-mutation-txs "best-practices-opencypher-use-explicit-txs.md#best-practices-opencypher-mutation-txs")

  - [Retry logic for exceptions](best-practices-opencypher-retry-logic.md "best-practices-opencypher-retry-logic.md")
  - [Set multiple properties at once using a single SET clause](best-practices-content-0.md "best-practices-content-0.md")
    - [Use the SET clause to remove multiple properties at once](best-practices-content-0.md#best-practices-content-1 "best-practices-content-0.md#best-practices-content-1")

  - [Use parameterized queries](best-practices-content-2.md "best-practices-content-2.md")
  - [Use flattened maps instead of nested maps in UNWIND clause](best-practices-content-3.md "best-practices-content-3.md")
  - [Place more restrictive nodes on the left side in
    Variable-Length Path (VLP) expressions](best-practices-content-4.md "best-practices-content-4.md")
  - [Avoid redundant node label checks by using granular relationship names](best-practices-content-5.md "best-practices-content-5.md")
  - [Specify edge labels where possible](best-practices-content-6.md "best-practices-content-6.md")
  - [Avoid using the WITH clause when possible](best-practices-content-7.md "best-practices-content-7.md")
  - [Place restrictive filters as early in the query as possible](best-practices-content-8.md "best-practices-content-8.md")
  - [Explicitly check whether properties exist](best-practices-content-9.md "best-practices-content-9.md")
  - [Do not use named path (unless it is required)](best-practices-content-10.md "best-practices-content-10.md")
  - [Avoid COLLECT(DISTINCT())](best-practices-content-11.md "best-practices-content-11.md")
  - [Prefer the properties function over individual property lookup when
    retrieving all property values](best-practices-content-12.md "best-practices-content-12.md")
  - [Perform static computations outside of the query](best-practices-content-13.md "best-practices-content-13.md")
  - [Batch inputs using UNWIND instead of individual statements](best-practices-content-14.md "best-practices-content-14.md")
  - [Prefer using custom IDs for node/relationship](best-practices-content-15.md "best-practices-content-15.md")
  - [Avoid doing ~id computations in the query](best-practices-content-16.md "best-practices-content-16.md")
  - [Updating/Merging multiple nodes](best-practices-merge-multiple-nodes.md "best-practices-merge-multiple-nodes.md")

- [Neptune Best Practices Using SPARQL](best-practices-sparql.md "best-practices-sparql.md")
  - [Querying All Named Graphs by Default](best-practices-sparql-query.md "best-practices-sparql-query.md")
  - [Specifying a Named Graph for Load](best-practices-sparql-graph.md "best-practices-sparql-graph.md")
  - [Choosing Between FILTER, FILTER...IN, and VALUES in Your Queries](best-practices-sparql-batch.md "best-practices-sparql-batch.md")
