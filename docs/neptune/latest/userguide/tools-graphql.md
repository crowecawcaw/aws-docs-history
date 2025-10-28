# Amazon Neptune utility for GraphQL

The Amazon Neptune utility for [GraphQL](https://graphql.org/ "https://graphql.org/") is
an open-source Node.js command-line tool that can help you create and maintain a GraphQL
API for a Neptune property-graph database (it does not yet work with RDF data). It is a
no-code way to create a GraphQL resolver for GraphQL queries that have a variable
number of input parameters and return a variable number of nested fields.

It has been released as an open-source project located at [https://github.com/aws/amazon-neptune-for-graphql](https://github.com/aws/amazon-neptune-for-graphql "https://github.com/aws/amazon-neptune-for-graphql").

You can install the utility using NPM like this (see [Installation and Setup](tools-graphql-setup.md "tools-graphql-setup.md") for details):

```
npm i @aws/neptune-for-graphql -g
```

The utility can discover the graph schema of an existing Neptune property graph,
including nodes, edges, properties, and edge cardinality. It then generates a GraphQL
schema with the directives needed to map the GraphQL types to the nodes and edges
the database, and auto-generates resolver code. The resolver code is designed to
minimize latency by returning only the data requested by the GraphQL query.

You can also start with an existing GraphQL schema and an empty Neptune
database, and let the utility infer the directives needed to map that GraphQL schema
to the nodes and edges of data to be loaded into the database. Or, you can
start with a GraphQL schema and directives that you've already created or modified.

The utility is capable of creating all the AWS resources it needs for its
pipeline, including the AWS AppSync API, the IAM roles, the data source, schema,
and resolver, and the AWS Lambda function that queries Neptune.

###### Note

Command-line examples here assume a Linux console. If you are using
Windows, replace the backslashes ('\') at the end of lines with carets ('^').

###### Topics

- [Installing and setting up the Amazon Neptune utility for GraphQL](tools-graphql-setup.md "tools-graphql-setup.md")
- [Scanning data in an existing Neptune database](tools-graphql-scan-existing.md "tools-graphql-scan-existing.md")
- [Starting from a GraphQL schema with no directives](tools-graphql-start-from-schema.md "tools-graphql-start-from-schema.md")
- [Working with directives for a GraphQL schema](tools-graphql-schema-with-directives.md "tools-graphql-schema-with-directives.md")
- [Command-line arguments for the GraphQL utility](tools-graphql-cmd-line-args.md "tools-graphql-cmd-line-args.md")
