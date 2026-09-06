

# Synchronous Data Mesh for GraphQL Queries
<a name="synchronous-data-mesh-graphql"></a>

Publication date: **April 25, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to use an API composition pattern to build a modern, distributed, and decentralized data architecture. It enables clients to query data where it lives, without first transporting it to a data lake or data warehouse. It also allows domain-specific teams to own and serve data as a product.

## Synchronous Data Mesh for GraphQL Queries
<a name="diagram1"></a>

![Architecture diagram showing a synchronous data mesh for GraphQL queries using Amazon AppSync, Lambda, Athena, and DynamoDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/synchronous-data-mesh-graphql/images/synchronous-data-mesh-graphql.png)


The following steps describe the architecture:

1. Expose your domain's schema through an HTTPS API with [Amazon AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html), allowing users to dynamically query a domain's data with GraphQL syntax.

1. Compose the returning query results with a combination of resolvers built with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions.

1. For data partially available in a data lake, retrieve the data by running SQL queries supported by [Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html). Run the Athena jobs asynchronously with the [athena-express](https://aws.amazon.com/blogs/apn/using-athena-express-to-simplify-sql-queries-on-amazon-athena/) library.

1. For data partially available in databases, retrieve the data either directly from Amazon AppSync, or by using Lambda functions as proxy resolvers to your databases.

1. For data partially available in external sources, use Lambda resolvers to fetch the data by invoking remote HTTP APIs.

1. To improve your API's performance, enable server-side caching on Amazon AppSync.

1. Other parties using AWS can replicate this architecture in their domains, also allowing clients to query their APIs using GraphQL, and composing the results with internal and external resolvers.

1. Parties that do not use AWS can also expose their domains with GraphQL APIs built with other technologies, providing a seamless experience to clients.

1. To retrieve large datasets, clients can subscribe to AWS Data Exchange instead.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | April 25, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.