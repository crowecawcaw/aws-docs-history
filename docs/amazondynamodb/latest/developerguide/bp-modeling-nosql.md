# First steps for modeling relational data in DynamoDB

###### Note

NoSQL design requires a different mindset than RDBMS design. For an RDBMS, you can create
a normalized data model without thinking about access patterns. You can then extend it later
when new questions and query requirements arise. By contrast, in Amazon DynamoDB, you shouldn't
start designing your schema until you know the questions that it needs to answer.
Understanding the business problems and the application use cases up front is absolutely
essential.

To start designing a DynamoDB table that will scale efficiently, you must take several steps
first to identify the access patterns that are required by the operations and business support
systems (OSS/BSS) that it needs to support:

- For new applications, review user stories about activities and objectives. Document the
  various use cases you identify, and analyze the access patterns that they require.
- For existing applications, analyze query
  logs to find out how people are currently using the system
  and what the key access patterns are.
  After completing this process, you should end up with a list that might look something like
  the following.

| Access Patterns for Order Entry Application | Pattern #                                     | Access Pattern Description |
| ------------------------------------------- | --------------------------------------------- | -------------------------- |
| 1                                           | Look up Employee Details by Employee ID       |
| 2                                           | Query Employee Details by Employee Name       |
| 3                                           | Find an Employee's Phone Number(s)            |
| 4                                           | Find a Customer's Phone Number(s)             |
| 5                                           | Get Orders for Customer within Date Range     |
| 6                                           | Show all Open Orders within Date Range        |
| 7                                           | See all Employees hired recently              |
| 8                                           | Find all Employees in Warehouse               |
| 9                                           | Get all Items on Order for Product            |
| 10                                          | Get Inventories for Product at all Warehouses |
| 11                                          | Get Customers by Account Rep                  |
| 12                                          | Get Orders by Account Rep                     |
| 13                                          | Get Employees with Job Title                  |
| 14                                          | Get Inventory by Product and Warehouse        |
| 15                                          | Get Total Product Inventory                   |

In a real application, your list might be much longer. But this collection represents the
range of query pattern complexity that you might find in a production environment.

A modern approach to DynamoDB schema design uses aggregate-oriented principles, grouping data based on access patterns rather than rigid entity boundaries. This approach considers multiple design patterns:

- _Single Table Design_ - Using composite sort keys, overloaded global secondary indexes, and adjacency list patterns to store multiple entity types in one table
- _Multi-Table Design_ - Using separate tables for entities with independent operational characteristics and low access correlation, with strategic GSIs for cross-entity queries
- _Aggregate Design_ - Embedding related data when always accessed together (Order + OrderItems) or using item collections for identifying relationships (Product + Inventory)
  The choice between these approaches depends on your specific access patterns, data characteristics, and operational requirements. You can use these elements to structure the data so that an application can retrieve whatever it needs for a given access pattern using a single query on a table or index.

###### Note

The choice between single-table and multi-table design depends on your specific requirements. Single-table design works well when entities have high access correlation and similar operational characteristics. Multi-table design is preferred when entities have independent operational requirements, different access patterns, or when you need clear operational boundaries. The example in this guide demonstrates a multi-table approach with strategic aggregation and denormalization.

To use NoSQL Workbench for DynamoDB to help visualize your partition key design, see
[Building data models with NoSQL Workbench](workbench.md "workbench.md").
