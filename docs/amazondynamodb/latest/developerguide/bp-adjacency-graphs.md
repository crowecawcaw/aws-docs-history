

# Best practices for managing many-to-many relationships in DynamoDB tables
<a name="bp-adjacency-graphs"></a>

Adjacency lists are a design pattern that is useful for modeling many-to-many relationships in Amazon DynamoDB. More generally, they provide a way to represent graph data (nodes and edges) in DynamoDB.

## Adjacency list design pattern
<a name="bp-adjacency-lists"></a>

When different entities of an application have a many-to-many relationship between them, the relationship can be modeled as an adjacency list. In this pattern, all top-level entities (synonymous to nodes in the graph model) are represented using the partition key. Any relationships with other entities (edges in a graph) are represented as an item within the partition by setting the value of the sort key to the target entity ID (target node).

The advantages of this pattern include minimal data duplication and simplified query patterns to find all entities (nodes) related to a target entity (having an edge to a target node).

A real-world example where this pattern has been useful is an invoicing system where invoices contain multiple bills. One bill can belong in multiple invoices. The partition key in this example is either an `InvoiceID` or a `BillID`. `BillID` partitions have all attributes specific to bills. `InvoiceID` partitions have an item storing invoice-specific attributes, and an item for each `BillID` that rolls up to the invoice.

The schema looks like the following.

![Table schema for billing adjacency-list example.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/AdjacencyLists_01.png)


Using the preceding schema, you can see that all bills for an invoice can be queried using the primary key on the table. To look up all invoices that contain a part of a bill, create a global secondary index on the table's sort key. 

The projections for the global secondary index look like the following.

![GSI projection for billing adjacency-list example.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/AdjacencyLists_02.png)


## Materialized graph pattern
<a name="bp-graph-pattern"></a>

Many applications need to understand rankings across peers, relationships between entities, and neighbor entity state. If your application uses these types of graph style workflows, consider the following schema design pattern.

As a real-world example, consider a social networking application. In this application, people have relationships with other people, possess skills, live in places, and have associated dates (such as birthdates). Each person is a *node* in the graph. The connections between people, such as friendships, are *edges*. The associations between people and their attributes (skills, places, dates) are also edges.

With the materialized graph pattern, you can store both nodes and edges in a single DynamoDB table and efficiently traverse relationships. The following diagrams show how to model this social networking graph. The first diagram shows the primary table structure. The subsequent diagrams show the global secondary index projections.

![Primary table schema for the materialized graph pattern in DynamoDB, showing people as partition keys with their edges as items within each partition.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/1513869910203-418.png)


![First global secondary index projection in DynamoDB, built on the overloaded Data attribute for queries by dates, names, places, and skills.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/1513852802235-256.png)


![Second global secondary index projection in DynamoDB, built on the TypeTarget composite key for reverse lookups.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/1513852905360-671.png)


The table uses the following key structure:
+ **Partition key** – The entity ID (for example, `Person-1`, `Person-2`). Each partition contains one node item and multiple edge items.
+ **Sort key** – For node items, the entity's own ID. For edge items, a composite of the edge type and target (for example, `Friend-Person-2` or `Skill-DynamoDB`).

Edge items contain a `Target` and a `Type` attribute. These form the composite key "TypeTarget" that identifies items in the primary table and in the second global secondary index. For example, "Person-1 is friends with Person-2" produces `Type=Friend`, `Target=Person-2`, and `TypeTarget=Friend-Person-2`.

The first global secondary index is built on the `Data` attribute. This attribute uses global secondary index overloading to index several attribute types within the same index:
+ `Dates` – birthdates, join dates (for example, `1971-12-21`)
+ `Names` – display names (for example, `Ana Carolina Silva`)
+ `Places` – locations (for example, `Seattle`)
+ `Skills` – competencies (for example, `DynamoDB`)

You can use this single global secondary index to query for all people born on a specific date, all people in a location, or all people with a specific skill.

The second global secondary index uses `TypeTarget` as its partition key for reverse lookups. For example, you can find all people who list `Person-2` as a friend by querying for `TypeTarget=Friend-Person-2`.

As you insert items into the table, you can use an intelligent sharding strategy to distribute item sets with large aggregations (birthdate, skill) across as many logical partitions on the global secondary indexes as are needed to avoid hot read/write problems.

With this combination of design patterns, you get a solid datastore for highly efficient real-time graph workflows. You can use it to build high-performance neighbor entity state and edge aggregation queries for recommendation engines, social-networking applications, node rankings, subtree aggregations, and other common graph use cases.

If your use case isn't sensitive to real-time data consistency, you can use a scheduled Amazon EMR process to populate edges with relevant graph summary aggregations for your workflows. If your application doesn't need to know immediately when an edge is added to the graph, you can use a scheduled process to aggregate results.

To maintain some level of consistency, the design could include Amazon DynamoDB Streams and AWS Lambda to process edge updates. It could also use an Amazon EMR job to validate results on a regular interval. This approach is illustrated by the following diagram. It is commonly used in social networking applications, where the cost of a real-time query is high and the need to immediately know individual user updates is low.

![Diagram illustrating graph workflow.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/1513856345673-336.png)


IT service-management (ITSM) and security applications generally need to respond in real time to entity state changes composed of complex edge aggregations. Such applications need a system that can support real-time multiple node aggregations of second- and third-level relationships, or complex edge traversals. If your use case requires these types of real-time graph query workflows, we recommend that you consider using [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/) to manage these workflows.

**Note**  
If you need to query highly connected datasets or traverse multiple nodes (multi-hop queries) with millisecond latency, consider using [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/). Amazon Neptune is a purpose-built, high-performance graph database engine. It is optimized for storing billions of relationships and querying the graph with millisecond latency.