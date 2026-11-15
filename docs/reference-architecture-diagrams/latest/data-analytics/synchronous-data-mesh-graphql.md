

# Synchronous data mesh for GraphQL queries
<a name="synchronous-data-mesh-graphql"></a>

Publication date: **April 25, 2022 ([Diagram history](diagram-history.md))**

This architecture shows how to use an API composition pattern to build a modern, distributed, and decentralized data architecture. It enables clients to query data where it lives, without first transporting it to a data lake or data warehouse. It also allows domain-specific teams to own and serve data as a product.

## Synchronous data mesh for GraphQL queries diagram
<a name="synchronous-data-mesh-graphql-diagram1"></a>

![Diagram of AWS AppSync receiving GraphQL queries and Lambda resolvers fetching data from Athena and DynamoDB.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/synchronous-data-mesh-graphql.png)


The following steps describe the architecture:

1. Expose your domain's schema through an HTTPS API with [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/), allowing users to dynamically query a domain's data with GraphQL syntax.

1. Compose the returning query results with a combination of resolvers built with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions.

1. For data partially available in a data lake, retrieve the data by running SQL queries supported by [Athena](https://docs.aws.amazon.com/athena/latest/ug/). Run the Athena jobs asynchronously with the [athena-express](https://aws.amazon.com/blogs/apn/using-athena-express-to-simplify-sql-queries-on-amazon-athena/) library.

1. For data partially available in databases, retrieve the data either directly from AWS AppSync, or by using Lambda functions as proxy resolvers to your databases.

1. For data partially available in external sources, use Lambda resolvers to fetch the data by invoking remote HTTP APIs.

1. To improve your API's performance, enable server-side caching on AWS AppSync.

1. Other parties using AWS can replicate this architecture in their domains, also allowing clients to query their APIs using GraphQL, and composing the results with internal and external resolvers.

1. Parties that do not use AWS can also expose their domains with GraphQL APIs built with other technologies, providing a seamless experience to clients.

1. To retrieve large datasets, clients can subscribe to [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/) instead.

## Further reading
<a name="synchronous-data-mesh-graphql-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)