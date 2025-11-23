# AWS::Serverless::GraphQLApi

Use the AWS Serverless Application Model (AWS SAM) `AWS::Serverless::GraphQLApi` resource type to create
and configure an AWS AppSync GraphQL API for your serverless application.

To learn more about AWS AppSync, see [What is AWS AppSync?](../../../appsync/latest/devguide/what-is-appsync.md "../../../appsync/latest/devguide/what-is-appsync.md") in the
_AWS AppSync Developer Guide_.

## Syntax

### YAML

```
`LogicalId`:
  Type: AWS::Serverless::GraphQLApi
  Properties:
    ApiKeys: `ApiKeys`
    Auth: `Auth`
    Cache: `AWS::AppSync::ApiCache`
    DataSources: `DataSource`
    DomainName: `AWS::AppSync::DomainName`
    Functions: `Function`
    Logging: `LogConfig`
    Name: `String`
    Resolvers: `Resolver`
    SchemaInline: `String`
    SchemaUri: `String`
    Tags:
    `- Tag`
    XrayEnabled: `Boolean`
```

## Properties

`ApiKeys`

Create a unique key that can be used to perform GraphQL operations
requiring an API key.

_Type_: [ApiKeys](sam-property-graphqlapi-apikeys.md "sam-property-graphqlapi-apikeys.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.

`Auth`

Configure authentication for your GraphQL API.

_Type_: [Auth](sam-property-graphqlapi-auth.md "sam-property-graphqlapi-auth.md")

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.

`Cache`

The input of a `CreateApiCache` operation.

_Type_: [AWS::AppSync::ApiCache](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
[AWS::AppSync::ApiCache](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.md") resource.

`DataSources`

Create data sources for functions in AWS AppSync to connect to. AWS SAM supports Amazon DynamoDB
and AWS Lambda data sources.

_Type_: [DataSource](sam-property-graphqlapi-datasource.md "sam-property-graphqlapi-datasource.md")

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.

`DomainName`

Custom domain name for your GraphQL API.

_Type_: [AWS::AppSync::DomainName](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
[AWS::AppSync::DomainName](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainname.md") resource. AWS SAM automatically generates the [AWS::AppSync::DomainNameApiAssociation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-domainnameapiassociation.md") resource.

`Functions`

Configure functions in GraphQL APIs to perform certain
operations.

_Type_: [Function](sam-property-graphqlapi-function.md "sam-property-graphqlapi-function.md")

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.

`Logging`

Configures Amazon CloudWatch logging for your GraphQL API.

If you don’t specify this property, AWS SAM will generate
`CloudWatchLogsRoleArn` and set the following values:

- `ExcludeVerboseContent: true`
- `FieldLogLevel: ALL`

To opt out of logging, specify the following:

```
Logging: false
```

_Type_: [LogConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-logconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`LogConfig` property of an `AWS::AppSync::GraphQLApi`
resource.

`LogicalId`

The unique name of your GraphQL API.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::AppSync::GraphQLApi`
resource.

`Name`

The name of your GraphQL API. Specify this property to override the
`LogicalId` value.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::AppSync::GraphQLApi`
resource.

`Resolvers`

Configure resolvers for the fields of your GraphQL API. AWS SAM
supports [JavaScript pipeline resolvers](../../../appsync/latest/devguide/resolver-reference-overview-js.md#anatomy-of-a-pipeline-resolver-js "../../../appsync/latest/devguide/resolver-reference-overview-js.md#anatomy-of-a-pipeline-resolver-js").

_Type_: [Resolver](sam-property-graphqlapi-resolver.md "sam-property-graphqlapi-resolver.md")

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.

`SchemaInline`

The text representation of a GraphQL schema in SDL
format.

_Type_: String

_Required_: Conditional. You must specify
`SchemaInline` or `SchemaUri`.

_CloudFormation compatibility_: This property is passed directly to the
`Definition` property of an `AWS::AppSync::GraphQLSchema`
resource.

`SchemaUri`

The schema’s Amazon Simple Storage Service (Amazon S3) bucket URI or path to a local folder.

If you specify a path to a local folder, CloudFormation requires that the file is first
uploaded to Amazon S3 before deployment. You can use the AWS SAM CLI to facilitate this
process. For more information, see [How AWS SAM uploads local files at deployment](deploy-upload-local-files.md "deploy-upload-local-files.md").

_Type_: String

_Required_: Conditional. You must specify
`SchemaInline` or `SchemaUri`.

_CloudFormation compatibility_: This property is passed directly to the
`DefinitionS3Location` property of an
`AWS::AppSync::GraphQLSchema` resource.

`Tags`

Tags (key-value pairs) for this GraphQL API. Use tags to identify and
categorize resources.

_Type_: List of [Tag](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Tag` property of an `AWS::AppSync::GraphQLApi`
resource.

`XrayEnabled`

Indicate whether to use [AWS X-Ray tracing](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") for this
resource.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`XrayEnabled` property of an `AWS::AppSync::GraphQLApi`
resource.

## Return Values

For a list of return values, refer to
[AWS::Serverless::GraphQLApi](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#aws-resource-appsync-graphqlapi-return-values.html "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.md#aws-resource-appsync-graphqlapi-return-values.html")
in the [CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md").

## Examples

### GraphQL API with

DynamoDB data source

In this example, we create a GraphQL API that uses a DynamoDB table as a
data source.

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

### GraphQL API with

a Lambda function as a data source

In this example, we create a GraphQL API that uses a Lambda function as a
data source.

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
