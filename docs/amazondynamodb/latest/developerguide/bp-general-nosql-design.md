# NoSQL design for DynamoDB

NoSQL database systems like Amazon DynamoDB use alternative models for data management, such as
key-value pairs or document storage. When you switch from a relational database management
system to a NoSQL database system like DynamoDB, it's important to understand the key differences
and specific design approaches.

###### Topics

- [Differences between relational data design and NoSQL](#bp-general-nosql-design-vs-relational "#bp-general-nosql-design-vs-relational")
- [Two key concepts for NoSQL design](#bp-general-nosql-design-concepts "#bp-general-nosql-design-concepts")
- [Approaching NoSQL design](#bp-general-nosql-design-approach "#bp-general-nosql-design-approach")
- [NoSQL Workbench for DynamoDB](#bp-general-nosql-workbench "#bp-general-nosql-workbench")

## Differences between relational data design and NoSQL

Relational database systems (RDBMS) and NoSQL databases have different strengths and
weaknesses:

- In RDBMS, data can be queried flexibly, but queries are relatively expensive and
  don't scale well in high-traffic situations (see [First steps for modeling relational data in DynamoDB](bp-modeling-nosql.md "bp-modeling-nosql.md")).
- In a NoSQL database such as DynamoDB, data can be queried efficiently in a limited
  number of ways, outside of which queries can be expensive and slow.

These differences make database design different between the two systems:

- In RDBMS, you design for flexibility without worrying about implementation details
  or performance. Query optimization generally doesn't affect schema design, but
  normalization is important.
- In DynamoDB, you design your schema specifically to make the most common and important
  queries as fast and as inexpensive as possible. Your data structures are tailored to the
  specific requirements of your business use cases.

## Two key concepts for NoSQL design

NoSQL design requires a different mindset than RDBMS design. For an RDBMS, you can go
ahead and create a normalized data model without thinking about access patterns. You can
then extend it later when new questions and query requirements arise. You can organize each
type of data into its own table.

###### How NoSQL design is different

- By contrast, you shouldn't start designing your schema for DynamoDB until you know the
  questions it will need to answer. Understanding the business problems and the
  application use cases up front is essential.
- You should maintain as few tables as possible in a DynamoDB application. Having fewer
  tables keeps things more scalable, requires less permissions management, and reduces
  overhead for your DynamoDB application. It can also help keep backup costs lower
  overall.

## Approaching NoSQL design

_The first step in designing your DynamoDB application is to identify the specific
query patterns that the system must satisfy._

In particular, it is important to understand three fundamental properties of your
application's access patterns before you begin:

- **Data size**: Knowing how much data will be stored and
  requested at one time will help determine the most effective way to partition the
  data.
- **Data shape**: Instead of reshaping data when a query
  is processed (as an RDBMS system does), a NoSQL database organizes data so that its
  shape in the database corresponds with what will be queried. This is a key factor in
  increasing speed and scalability.
- **Data velocity**: DynamoDB scales by increasing the
  number of physical partitions that are available to process queries, and by efficiently
  distributing data across those partitions. Knowing in advance what the peak query loads
  will be might help determine how to partition data to best use I/O capacity.

After you identify specific query requirements, you can organize data according to
general principles that govern performance:

- **Keep related data together.**   Research
  has shown that the principle of 'locality of reference', keeping related data together
  in one place, is a key factor in improving performance and response times in NoSQL systems,
  just as it was found to be important for optimizing routing tables many years ago.

As a general rule, you should maintain as few tables as possible in a DynamoDB
application.

Exceptions are cases where high-volume time series data are involved, or datasets
that have very different access patterns. A single table with inverted indexes can
usually enable simple queries to create and retrieve the complex hierarchical data
structures required by your application.

- **Use sort order.**   Related items can be
  grouped together and queried efficiently if their key design causes them to sort
  together. This is an important NoSQL design strategy.
- **Distribute queries.**   It's also
  important that a high volume of queries not be focused on one part of the database,
  where they can exceed I/O capacity. Instead, you should design data keys to distribute
  traffic evenly across partitions as much as possible, avoiding hot spots.
- **Use global secondary indexes.**   By
  creating specific global secondary indexes, you can enable different queries than your
  main table can support, and that are still fast and relatively inexpensive.

These general principles translate into some common design patterns that you can use to
model data efficiently in DynamoDB.

## NoSQL Workbench for DynamoDB

[NoSQL Workbench for DynamoDB](workbench.md "workbench.md") is a cross-platform, client-side GUI
application that you can use for modern database development and operations. It's available
for Windows, macOS, and Linux. NoSQL Workbench is a visual development tool that provides
data modeling, data visualization, sample data generation, and query development features to
help you design, create, query, and manage DynamoDB tables. With NoSQL Workbench for DynamoDB, you
can build new data models from, or design models based on, existing data models that satisfy
your application's data access patterns. You can also import and export the designed data
model at the end of the process. For more information, see [Building data models with NoSQL Workbench](workbench.md "workbench.md").
