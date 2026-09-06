

# Components of a GraphQL API
<a name="api-components"></a>

A standard GraphQL API is composed of a single schema that handles the shape of the data that will be queried. Your schema is linked to one or more of your data sources like a database or Lambda function. In between the two sits one or more resolvers that handle the business logic for your requests. Each component plays an important role in your GraphQL implementation. The following sections will introduce these three components and the role they play in the GraphQL service.

![GraphQL API architecture showing schema, resolvers, and data sources connected by arrows.](http://docs.aws.amazon.com/appsync/latest/devguide/images/appsync-architecture-graphql-api.png)


**Topics**
+ [GraphQL schemas](schema-components.md)
+ [Data sources](data-source-components.md)
+ [Resolvers](resolver-components.md)