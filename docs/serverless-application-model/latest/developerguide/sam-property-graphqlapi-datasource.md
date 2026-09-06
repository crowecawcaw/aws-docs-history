

# DataSource
<a name="sam-property-graphqlapi-datasource"></a>

Configure a data source that your GraphQL API resolver can connect to. You can use AWS Serverless Application Model (AWS SAM) templates to configure connections to the following data sources:
+ Amazon DynamoDB
+ AWS Lambda

To learn more about data sources, see [Attaching a data source](https://docs.aws.amazon.com/appsync/latest/devguide/attaching-a-data-source.html) in the *AWS AppSync Developer Guide*.

## Syntax
<a name="sam-property-graphqlapi-datasource-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-graphqlapi-datasource-syntax-yaml"></a>

```
DynamoDb: {{DynamoDb}}
Lambda: {{Lambda}}
```

## Properties
<a name="sam-property-graphqlapi-datasource-properties"></a>

`DynamoDb`  <a name="sam-graphqlapi-datasource-dynamodb"></a>
Configure a DynamoDB table as a data source for your GraphQL API resolver.  
*Type*: [DynamoDb](sam-property-graphqlapi-datasource-dynamodb.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent.

`Lambda`  <a name="sam-graphqlapi-datasource-lambda"></a>
Configure a Lambda function as a data source for your GraphQL API resolver.  
*Type*: [Lambda](sam-property-graphqlapi-datasource-lambda.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent.