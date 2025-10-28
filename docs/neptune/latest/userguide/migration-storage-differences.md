# Data storage differences between Neptune and Neo4j

Neptune uses a [graph data model](feature-overview-data-model.md "feature-overview-data-model.md")
based on a native quad model. When migrating your data to Neptune, there are
several differences in the architecture of the data model and storage layer that you
should be aware of to make optimal use of the distributed and scalable shared storage
that Neptune provides:

- Neptune doesn't use any explicitly defined schema or constraints. It lets
  you add nodes, edges, and properties dynamically without having to define the schema ahead
  of time. Neptune doesn't limit the values and types of data stored, except as noted in
  [Neptune limits](limits.md#limits-properties "limits.md#limits-properties"). As part of Neptune's storage
  architecture, data is also [automatically
  indexed](feature-overview-storage-indexing.md "feature-overview-storage-indexing.md") in a way that handles many of the most common access patterns. This storage
  architecture removes the operational overhead of creation and management of database schema
  and index optimization.
- Neptune provides a unique distributed and shared storage architecture that
  automatically scales in 10 GB chunks as the storage needs of your database grow, up to 128
  tebibytes (TiB). This storage layer is reliable, durable, and fault-tolerant, with data
  copied 6 times, twice in each of 3 Availability Zones. It provides all Neptune clusters
  with a highly available and fault-tolerant data storage layer by default. Neptune's
  storage architecture reduces costs and removes the need to provision or over-provision
  storage to handle future data growth.
  Before migrating your data to Neptune, it's good to familiarize yourself with Neptune's
  [property graph data model](feature-overview-storage-indexing.md#feature-overview-storage-indexing-gremlin "feature-overview-storage-indexing.md#feature-overview-storage-indexing-gremlin")
  and [transaction semantics](transactions.md "transactions.md").
