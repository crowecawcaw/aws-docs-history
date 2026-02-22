# SQL server graph features for T-SQL

This topic provides reference information about graph database capabilities in Microsoft SQL Server 2019 and their potential migration to Amazon Aurora PostgreSQL. You can understand the fundamental concepts of graph databases, including nodes, edges, and their unique features for modeling complex relationships. The topic explores how SQL Server implements graph functionality, offering examples of creating graph tables and performing queries.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                           |
| ------------------------------ | ---------------------------------- | ------------------------- | --------------------------------------------------------- |
| Two star feature compatibility | No automation                      | N/A                       | No native support. Rewriting the application is required. |

## SQL Server Usage

SQL Server offers graph database capabilities to model many-to-many relationships. The graph relationships are integrated into Transact-SQL and receive the benefits of using SQL Server as the foundational database management system.

A graph database is a collection of nodes or vertices and edges or relationships. A node represents an entity. For example, a person or an organization. An edge represents a relationship between the two nodes that it connects. For example, this can be likes or friends. Both nodes and edges may have properties associated with them. Here are some features that make a graph database unique:

- Edges or relationships are first class entities in a Graph Database and can have attributes or properties associated with them.
- A single edge can flexibly connect multiple nodes in a Graph Database.
- You can express pattern matching and multi-hop navigation queries easily.
- You can express transitive closure and polymorphic queries easily.

A relational database can achieve anything a graph database can. However, a graph database makes it easier to express certain kinds of queries. Also, with specific optimizations, certain queries may perform better. Your decision to choose either a relational or graph database is based on following factors:

- Your application has hierarchical data. You can use the `HierarchyID` data type to implement hierarchies, but it has some limitations. For example, it doesn’t allow you to store multiple parents for a node.
- Your application has complex many-to-many relationships. As application evolves, new relationships are added.
- You need to analyze interconnected data and relationships.

SQL Server 2017 adds new graph database capabilities for modeling graph many-to-many relationships. They include the new `CREATE TABLE` syntax for creating node and edge tables, and the keyword `MATCH` for queries. For more information, see [Graph processing with SQL Server and Azure SQL Database](https://docs.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/graphs/sql-graph-overview?view=sql-server-ver15").

The following example creates SQL Server graph tables.

```
CREATE TABLE Person (ID INTEGER PRIMARY KEY, Name VARCHAR(100), Age INT) AS NODE;
CREATE TABLE friends (StartDate date) AS EDGE;
```

A new `MATCH` clause is introduced to support pattern matching and multi-hop navigation through the graph. The `MATCH` function uses ASCII-art style syntax for pattern matching. The following example uses the `MATCH` function.

```
-- Find friends of John
SELECT Person2.Name
FROM Person Person1, Friends, Person Person2
WHERE MATCH(Person1-(Friends)->Person2)
AND Person1.Name = 'John';
```

SQL Server 2019 adds ability to define cascaded delete actions on an edge constraint in a graph database. Edge constraints enable users to add constraints to their edge tables, thereby enforcing specific semantics and also maintaining data integrity. For more information, see [Edge constraints](https://docs.microsoft.com/en-us/sql/relational-databases/tables/graph-edge-constraints?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/tables/graph-edge-constraints?view=sql-server-ver15") in the _SQL Server documentation_.

In SQL Server 2019, graph tables now have support for table and index partitioning. For more information, see [Partitioned Tables and Indexes](https://docs.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Currently, PostgreSQL doesn’t provide native Graph Database feature, but it is possible to implement some of them using recursive CTE queries or serializing graphs to regular relations.
