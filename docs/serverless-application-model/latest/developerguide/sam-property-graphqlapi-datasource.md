# DataSource

Configure a data source that your GraphQL API resolver can connect to. You
can use AWS Serverless Application Model (AWS SAM) templates to configure connections to the following data
sources:

- Amazon DynamoDB
- AWS Lambda
  To learn more about data sources, see [Attaching a data source](../../../appsync/latest/devguide/attaching-a-data-source.md "../../../appsync/latest/devguide/attaching-a-data-source.md") in
  the _AWS AppSync Developer Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
DynamoDb: `DynamoDb`
Lambda: `Lambda`
```

## Properties

`DynamoDb`

Configure a DynamoDB table as a data source for your GraphQL API
resolver.

_Type_: [DynamoDb](sam-property-graphqlapi-datasource-dynamodb.md "sam-property-graphqlapi-datasource-dynamodb.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.

`Lambda`

Configure a Lambda function as a data source for your GraphQL API
resolver.

_Type_: [Lambda](sam-property-graphqlapi-datasource-lambda.md "sam-property-graphqlapi-datasource-lambda.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.
