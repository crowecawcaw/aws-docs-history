

# VTL resolver tutorials for AWS AppSync
<a name="tutorials"></a>

**Note**  
We now primarily support the APPSYNC\_JS runtime and its documentation. Please consider using the APPSYNC\_JS runtime and its guides [here](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials-js.html).

Data sources and resolvers are used by AWS AppSync to translate GraphQL requests and fetch information from your AWS resources. AWS AppSync supports automatic provisioning and connections with certain data source types. AWS AppSync also supports AWS Lambda, Amazon DynamoDB, relational databases (Amazon Aurora Serverless), Amazon OpenSearch Service, and HTTP endpoints as data sources. You can use a GraphQL API with your existing AWS resources or build data sources and resolvers from scratch. The following sections are meant to elucidate some of the more common GraphQL use cases in the form of tutorials.

AWS AppSync uses *mapping templates* written in Apache Velocity Template Language (VTL) for resolvers. For more information about using mapping templates, see the [Resolver mapping template reference](resolver-mapping-template-reference.md#aws-appsync-resolver-mapping-template-reference). More information about working with VTL is available in the [Resolver mapping template programming guide](resolver-mapping-template-reference-programming-guide.md#aws-appsync-resolver-mapping-template-reference-programming-guide).

AWS AppSync supports the automatic provisioning of DynamoDB tables from a GraphQL schema as described in Provision from schema (optional) and Launch a sample schema. You can also import from an existing DynamoDB table which will create schema and connect resolvers. This is outlined in Import from Amazon DynamoDB (optional).

**Topics**
+ [Creating a simple post application using DynamoDB resolvers](tutorial-dynamodb-resolvers.md)
+ [Using AWS Lambda resolvers](tutorial-lambda-resolvers.md)
+ [Using OpenSearch Service resolvers](tutorial-elasticsearch-resolvers.md)
+ [Using local resolvers](tutorial-local-resolvers.md)
+ [Combining GraphQL resolvers](tutorial-combining-graphql-resolvers.md)
+ [Using DynamoDB batch operations](tutorial-dynamodb-batch.md)
+ [Performing DynamoDB transactions](tutorial-dynamodb-transact.md)
+ [Using HTTP resolvers](tutorial-http-resolvers.md)
+ [Using Aurora Serverless v2 resolvers](tutorial-rds-resolvers.md)
+ [Using pipeline resolvers](tutorial-pipeline-resolvers.md)
+ [Using Delta Sync operations on versioned data sources](tutorial-delta-sync.md)