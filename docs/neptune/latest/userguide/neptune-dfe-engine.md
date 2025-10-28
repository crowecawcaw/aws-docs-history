# The Amazon Neptune alternative query engine (DFE)

Amazon Neptune has an alternative query engine known as the DFE that uses
DB instance resources such as CPU cores, memory, and I/O more efficiently than
the original Neptune engine.

###### Note

With large data sets, the DFE engine may not run well on t3 instances.

The DFE engine runs SPARQL, Gremlin and openCypher queries, and supports a wide
variety of plan types, including left-deep, bushy, and hybrid ones. Plan operators
can invoke both compute operations, which run on a reserved set of compute cores,
and I/O operations, each of which runs on its own thread in an I/O thread pool.

The DFE uses pre-generated statistics about your Neptune graph data to make informed
decisions about how to structure queries. See [DFE statistics](neptune-dfe-statistics.md "neptune-dfe-statistics.md") for information about how these statistics
are generated.

The choice of plan type and the number of compute threads used is made automatically
based on pre-generated statistics and on the resources that are available in the Neptune
head node. The order of results is not predetermined for plans that have internal compute
parallelism.
