# Querying tables in DynamoDB

You can use the `Query` API operation in Amazon DynamoDB to find items based on
primary key values.

You must provide the name of the partition key attribute and a single value for that
attribute. `Query` returns all items with that partition key value. Optionally,
you can provide a sort key attribute and use a comparison operator to refine the search
results.

For more information on how to use `Query`, such as the request syntax,
response parameters, and additional examples, see [Query](../APIReference/API_Query.md "../APIReference/API_Query.md") in the
_Amazon DynamoDB API Reference_.

###### Topics

- [Key condition expressions for the Query
  operation in DynamoDB](Query.md "Query.md")
- [Filter expressions for the Query operation in
  DynamoDB](Query.md "Query.md")
- [Paginating table query results in DynamoDB](Query.md "Query.md")
- [Other aspects of working with the Query operation in
  DynamoDB](Query.md "Query.md")
