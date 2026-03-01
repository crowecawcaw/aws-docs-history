# Getting started: Creating your first GraphQL API in AWS AppSync

You can use the AWS AppSync console to
configure and launch a GraphQL API. GraphQL APIs generally require three components:

1. **GraphQL schema** - Your GraphQL schema is the blueprint of the API. It
   defines the types and fields that you can request when an operation is executed. To populate the schema with
   data, you must connect data sources to the GraphQL API. In this quickstart guide, we'll be creating a schema
   using a predefined model.
2. **Data sources**- These are the resources that contain the data for
   populating your GraphQL API. This can be a DynamoDB table, Lambda function, etc. AWS AppSync supports a
   multitude of data sources to build robust and scalable GraphQL APIs. Data sources are linked to fields in
   the schema. Whenever a request is performed on a field, the data from the source populates the field. This
   mechanism is controlled by the resolver. In this quickstart guide, we'll be creating a data source using a
   predefined model alongside the schema.
3. **Resolvers** - Resolvers are responsible for linking the schema field to
   the data source. They retrieve the data from the source, then return the result based on what was defined by
   the field. AWS AppSync supports both JavaScript and VTL for writing resolvers for your GraphQL APIs. In
   this quickstart guide, the resolvers will be automatically generated based on the schema and the data
   source. We won't be delving into this in this section.
   AWS AppSync supports the creation and configuration of all GraphQL components. When you open the console, you can
   use the following methods to create your API:

4. Designing a customized GraphQL API by generating it through a predefined model and setting up a new DynamoDB
   table (data source) to support it.
5. Designing a GraphQL API with a blank schema and no data sources or resolvers.
6. Using a DynamoDB table to import data and generate your schema's types and fields.
7. Using AWS AppSync's WebSocket capabilities and Pub/Sub architecture to develop real-time APIs.
8. Using existing GraphQL APIs (source APIs) to link to a Merged API.

###### Note

We recommend reviewing the [Designing a schema](designing-your-schema.md#aws-appsync-designing-your-schema "designing-your-schema.md#aws-appsync-designing-your-schema")
section before working with more advanced tools. These guides will explain simpler examples that you can use
conceptually to build more complex applications in AWS AppSync.

AWS AppSync also supports several non-console options to create GraphQL APIs. These include:

1. AWS Amplify
2. AWS SAM
3. CloudFormation
4. The CDK
   The following example will show you how to create the basic components of a GraphQL API using predefined
   models and DynamoDB.

###### Topics

- [Launching a schema](schema-launch-start.md "schema-launch-start.md")
- [Taking a tour of the AWS AppSync console](console-tour.md "console-tour.md")
- [Using GraphQL mutations to add data to a
  DynamoDB table](add-data-with-graphql-mutation.md "add-data-with-graphql-mutation.md")
- [Using GraphQL queries to retrieve data
  from a DynamoDB table](retrieve-data-with-graphql-query.md "retrieve-data-with-graphql-query.md")
- [Supplemental sections](next-steps.md "next-steps.md")
