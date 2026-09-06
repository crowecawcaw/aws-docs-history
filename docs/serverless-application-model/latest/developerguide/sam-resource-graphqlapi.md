

# AWS::Serverless::GraphQLApi
<a name="sam-resource-graphqlapi"></a>

Use the AWS Serverless Application Model (AWS SAM) `AWS::Serverless::GraphQLApi` resource type to create and configure an AWS AppSync GraphQL API for your serverless application.

To learn more about AWS AppSync, see [What is AWS AppSync?](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) in the *AWS AppSync Developer Guide*.

## Syntax
<a name="sam-resource-graphqlapi-syntax"></a>

### YAML
<a name="sam-resource-graphqlapi-syntax-yaml"></a>

```
{{LogicalId}}:
  Type: AWS::Serverless::GraphQLApi
  Properties:
    ApiKeys: {{ApiKeys}}
    Auth: {{Auth}}
    Cache: {{[AWS::AppSync::ApiCache](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html)}}
    DataSources: {{DataSource}}
    DomainName: {{[AWS::AppSync::DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html)}}
    Functions: {{Function}}
    Logging: {{[LogConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html)}}
    Name: {{String}}
    Resolvers: {{Resolver}}
    SchemaInline: {{String}}
    SchemaUri: {{String}}
    Tags:
    {{- [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html)}}
    XrayEnabled: {{Boolean}}
```

## Properties
<a name="sam-resource-graphqlapi-properties"></a>

`ApiKeys`  <a name="sam-graphqlapi-apikeys"></a>
Create a unique key that can be used to perform GraphQL operations requiring an API key.  
*Type*: [ApiKeys](sam-property-graphqlapi-apikeys.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent.

`Auth`  <a name="sam-graphqlapi-auth"></a>
Configure authentication for your GraphQL API.  
*Type*: [Auth](sam-property-graphqlapi-auth.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent.

`Cache`  <a name="sam-graphqlapi-cache"></a>
The input of a `CreateApiCache` operation.  
*Type*: [AWS::AppSync::ApiCache](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the [AWS::AppSync::ApiCache](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html) resource.

`DataSources`  <a name="sam-graphqlapi-datasources"></a>
Create data sources for functions in AWS AppSync to connect to. AWS SAM supports Amazon DynamoDB and AWS Lambda data sources.  
*Type*: [DataSource](sam-property-graphqlapi-datasource.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent.

`DomainName`  <a name="sam-graphqlapi-domainname"></a>
Custom domain name for your GraphQL API.  
*Type*: [AWS::AppSync::DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the [AWS::AppSync::DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.html) resource. AWS SAM automatically generates the [AWS::AppSync::DomainNameApiAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.html) resource.

`Functions`  <a name="sam-graphqlapi-functions"></a>
Configure functions in GraphQL APIs to perform certain operations.  
*Type*: [Function](sam-property-graphqlapi-function.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent.

`Logging`  <a name="sam-graphqlapi-logging"></a>
Configures Amazon CloudWatch logging for your GraphQL API.  
If you don’t specify this property, AWS SAM will generate `CloudWatchLogsRoleArn` and set the following values:  
+ `ExcludeVerboseContent: true`
+ `FieldLogLevel: ALL`
To opt out of logging, specify the following:  

```
Logging: false
```
*Type*: [LogConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[LogConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-logconfig)` property of an `AWS::AppSync::GraphQLApi` resource.

`LogicalId`  <a name="sam-graphqlapi-logicalid"></a>
The unique name of your GraphQL API.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name)` property of an `AWS::AppSync::GraphQLApi` resource.

`Name`  <a name="sam-graphqlapi-name"></a>
The name of your GraphQL API. Specify this property to override the `LogicalId` value.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-name)` property of an `AWS::AppSync::GraphQLApi` resource.

`Resolvers`  <a name="sam-graphqlapi-resolvers"></a>
Configure resolvers for the fields of your GraphQL API. AWS SAM supports [JavaScript pipeline resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-overview-js.html#anatomy-of-a-pipeline-resolver-js).  
*Type*: [Resolver](sam-property-graphqlapi-resolver.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn’t have an CloudFormation equivalent.

`SchemaInline`  <a name="sam-graphqlapi-schemainline"></a>
The text representation of a GraphQL schema in SDL format.  
*Type*: String  
*Required*: Conditional. You must specify `SchemaInline` or `SchemaUri`.  
*CloudFormation compatibility*: This property is passed directly to the `[Definition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definition)` property of an `AWS::AppSync::GraphQLSchema` resource.

`SchemaUri`  <a name="sam-graphqlapi-schemauri"></a>
The schema’s Amazon Simple Storage Service (Amazon S3) bucket URI or path to a local folder.  
If you specify a path to a local folder, CloudFormation requires that the file is first uploaded to Amazon S3 before deployment. You can use the AWS SAM CLI to facilitate this process. For more information, see [How AWS SAM uploads local files at deployment](deploy-upload-local-files.md).  
*Type*: String  
*Required*: Conditional. You must specify `SchemaInline` or `SchemaUri`.  
*CloudFormation compatibility*: This property is passed directly to the `[DefinitionS3Location](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html#cfn-appsync-graphqlschema-definitions3location)` property of an `AWS::AppSync::GraphQLSchema` resource.

`Tags`  <a name="sam-graphqlapi-tags"></a>
Tags (key-value pairs) for this GraphQL API. Use tags to identify and categorize resources.  
*Type*: List of [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-tags)` property of an `AWS::AppSync::GraphQLApi` resource.

`XrayEnabled`  <a name="sam-graphqlapi-xrayenabled"></a>
Indicate whether to use [AWS X-Ray tracing](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) for this resource.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[XrayEnabled](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#cfn-appsync-graphqlapi-xrayenabled)` property of an `AWS::AppSync::GraphQLApi` resource.

## Return Values
<a name="sam-resource-graphqlapi-return-values"></a>

For a list of return values, refer to [AWS::Serverless::GraphQLApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html#aws-resource-appsync-graphqlapi-return-values.html) in the [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

## Examples
<a name="sam-resource-graphqlapi-examples"></a>

### GraphQL API with DynamoDB data source
<a name="sam-resource-graphqlapi-examples-example1"></a>

In this example, we create a GraphQL API that uses a DynamoDB table as a data source.

**schema.graphql**

```
schema {
  query: Query
  mutation: Mutation
}

type Query {
  getPost(id: String!): Post
}

type Mutation {
  addPost(author: String!, title: String!, content: String!): Post!
}

type Post {
  id: String!
  author: String
  title: String
  content: String
  ups: Int!
  downs: Int!
  version: Int!
}
```

**template.yaml**

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  DynamoDBPostsTable:
    Type: AWS::Serverless::SimpleTable

  MyGraphQLAPI:
    Type: AWS::Serverless::GraphQLApi
    Properties:
      SchemaUri: ./sam_graphql_api/schema.graphql
      Auth:
        Type: AWS_IAM
      DataSources:
        DynamoDb:
          PostsDataSource:
            TableName: !Ref DynamoDBPostsTable
            TableArn: !GetAtt DynamoDBPostsTable.Arn
      Functions:
        preprocessPostItem:
          Runtime:
            Name: APPSYNC_JS
            Version: 1.0.0
          DataSource: NONE
          CodeUri: ./sam_graphql_api/preprocessPostItem.js
        createPostItem:
          Runtime:
            Name: APPSYNC_JS
            Version: "1.0.0"
          DataSource: PostsDataSource
          CodeUri: ./sam_graphql_api/createPostItem.js
        getPostFromTable:
          Runtime:
            Name: APPSYNC_JS
            Version: "1.0.0"
          DataSource: PostsDataSource
          CodeUri: ./sam_graphql_api/getPostFromTable.js
      Resolvers:
        Mutation:
          addPost:
            Runtime:
              Name: APPSYNC_JS
              Version: "1.0.0"
            Pipeline:
            - preprocessPostItem
            - createPostItem
        Query:
          getPost:
            CodeUri: ./sam_graphql_api/getPost.js
            Runtime:
              Name: APPSYNC_JS
              Version: "1.0.0"
            Pipeline:
            - getPostFromTable
```

**createPostItem.js**

```
import { util } from "@aws-appsync/utils";

export function request(ctx) {
  const { key, values } = ctx.prev.result;
  return {
    operation: "PutItem",
    key: util.dynamodb.toMapValues(key),
    attributeValues: util.dynamodb.toMapValues(values),
  };
}

export function response(ctx) {
  return ctx.result;
}
```

**getPostFromTable.js**

```
import { util } from "@aws-appsync/utils";

export function request(ctx) {
  return dynamoDBGetItemRequest({ id: ctx.args.id });
}

export function response(ctx) {
  return ctx.result;
}

/**
 * A helper function to get a DynamoDB item
 */
function dynamoDBGetItemRequest(key) {
  return {
    operation: "GetItem",
    key: util.dynamodb.toMapValues(key),
  };
}
```

**preprocessPostItem.js**

```
import { util } from "@aws-appsync/utils";

export function request(ctx) {
  const id = util.autoId();
  const { ...values } = ctx.args;
  values.ups = 1;
  values.downs = 0;
  values.version = 1;
  return { payload: { key: { id }, values: values } };
}

export function response(ctx) {
  return ctx.result;
}
```

Here is our resolver code:

**getPost.js**

```
export function request(ctx) {
  return {};
}

export function response(ctx) {
  return ctx.prev.result;
}
```

### GraphQL API with a Lambda function as a data source
<a name="sam-resource-graphqlapi-examples-example2"></a>

In this example, we create a GraphQL API that uses a Lambda function as a data source.

**template.yaml**

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyLambdaFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      Runtime: nodejs20.x
      CodeUri: ./lambda

  MyGraphQLAPI:
    Type: AWS::Serverless::GraphQLApi
    Properties:
      Name: MyApi
      SchemaUri: ./gql/schema.gql
      Auth:
        Type: API_KEY
      ApiKeys:
        MyApiKey:
          Description: my api key
      DataSources:
        Lambda:
          MyLambdaDataSource:
            FunctionArn: !GetAtt MyLambdaFunction.Arn
      Functions:
        lambdaInvoker:
          Runtime:
            Name: APPSYNC_JS
            Version: 1.0.0
          DataSource: MyLambdaDataSource
          CodeUri: ./gql/invoker.js
      Resolvers:
        Mutation:
          addPost:
            Runtime:
              Name: APPSYNC_JS
              Version: 1.0.0
            Pipeline:
            - lambdaInvoker
        Query:
          getPost:
            Runtime:
              Name: APPSYNC_JS
              Version: 1.0.0
            Pipeline:
            - lambdaInvoker

Outputs:
  MyGraphQLAPI:
    Description: AppSync API
    Value: !GetAtt MyGraphQLAPI.GraphQLUrl
  MyGraphQLAPIMyApiKey:
    Description: API Key for authentication
    Value: !GetAtt MyGraphQLAPIMyApiKey.ApiKey
```

**schema.graphql**

```
schema {
  query: Query
  mutation: Mutation
}
type Query {
  getPost(id: ID!): Post
}
type Mutation {
  addPost(id: ID!, author: String!, title: String, content: String): Post!
}
type Post {
  id: ID!
  author: String!
  title: String
  content: String
  ups: Int
  downs: Int
}
```

Here are our functions:

**lambda/index.js**

```
exports.handler = async (event) => {
  console.log("Received event {}", JSON.stringify(event, 3));

  const posts = {
    1: {
      id: "1",
      title: "First book",
      author: "Author1",
      content: "Book 1 has this content",
      ups: "100",
      downs: "10",
    },
  };

  console.log("Got an Invoke Request.");
  let result;
  switch (event.field) {
    case "getPost":
      return posts[event.arguments.id];
    case "addPost":
      // return the arguments back
      return event.arguments;
    default:
      throw new Error("Unknown field, unable to resolve " + event.field);
  }
};
```

**invoker.js**

```
import { util } from "@aws-appsync/utils";

export function request(ctx) {
  const { source, args } = ctx;
  return {
    operation: "Invoke",
    payload: { field: ctx.info.fieldName, arguments: args, source },
  };
}

export function response(ctx) {
  return ctx.result;
}
```