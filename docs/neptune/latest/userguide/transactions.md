# Transaction Semantics in Neptune

Amazon Neptune is designed to support highly concurrent online transactional processing
(OLTP) workloads over data graphs. The [W3C
SPARQL Query Language for RDF](https://www.w3.org/TR/rdf-sparql-query/ "https://www.w3.org/TR/rdf-sparql-query/") specification and the [Apache TinkerPop Gremlin Graph Traversal
Language](http://tinkerpop.apache.org/gremlin.html "http://tinkerpop.apache.org/gremlin.html") documentation do not define transaction semantics for concurrent query
processing. Because ACID support and well-defined transaction guarantees can be very
important, we enforce strict semantics to help avoid data anomalies.

This section defines these semantics and illustrates how they apply to some common use
cases in Neptune.

###### Topics

- [Definition of Isolation Levels](transactions-isolation-levels.md "transactions-isolation-levels.md")
- [Transaction Isolation Levels in Neptune](transactions-neptune.md "transactions-neptune.md")
- [Examples of Neptune transaction semantics](transactions-examples.md "transactions-examples.md")
