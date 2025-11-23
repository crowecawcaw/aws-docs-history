# Resolver

Configure resolvers for the fields of your GraphQL API. AWS Serverless Application Model (AWS SAM)
supports [JavaScript pipeline
resolvers](../../../appsync/latest/devguide/resolver-reference-overview-js.md "../../../appsync/latest/devguide/resolver-reference-overview-js.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
`OperationType`:
  `LogicalId`:
    Caching: `CachingConfig`
    CodeUri: `String`
    FieldName: `String`
    InlineCode: `String`
    MaxBatchSize: `Integer`
    Pipeline: `List`
    Runtime: `Runtime`
    Sync: `SyncConfig`
```

## Properties

`Caching`

The caching configuration for the resolver that has caching activated.

_Type_: [CachingConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-cachingconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`CachingConfig` property of an `AWS::AppSync::Resolver`
resource.

`CodeUri`

The resolver function code’s Amazon Simple Storage Service (Amazon S3) URI or path to a local folder.

If you specify a path to a local folder, CloudFormation requires that the file is first
uploaded to Amazon S3 before deployment. You can use the AWS SAM CLI to facilitate this
process. For more information, see [How AWS SAM uploads local files at deployment](deploy-upload-local-files.md "deploy-upload-local-files.md").

If neither `CodeUri` or `InlineCode` are provided, AWS SAM will
generate `InlineCode` that redirects the request to the first pipeline
function and receives the response from the last pipeline function.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`CodeS3Location` property of an `AWS::AppSync::Resolver`
resource.

`FieldName`

The name of your resolver. Specify this property to override the
`LogicalId` value.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`FieldName` property of an `AWS::AppSync::Resolver`
resource.

`InlineCode`

The resolver code that contains the request and response functions.

If neither `CodeUri` or `InlineCode` are provided, AWS SAM will
generate `InlineCode` that redirects the request to the first pipeline
function and receives the response from the last pipeline function.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Code` property of an `AWS::AppSync::Resolver`
resource.

`LogicalId`

The unique name for your resolver. In a GraphQL schema, your resolver
name should match the field name that its used for. Use that same field name for
`LogicalId`.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.

`MaxBatchSize`

The maximum number of resolver request inputs that will be sent to a single
AWS Lambda function in a `BatchInvoke` operation.

_Type_: Integer

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`MaxBatchSize` property of an `AWS::AppSync::Resolver`
resource.

`OperationType`

The GraphQL operation type that is associated with your resolver. For
example, `Query`, `Mutation`, or `Subscription`. You
can nest multiple resolvers by `LogicalId` within a single
`OperationType`.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`TypeName` property of an `AWS::AppSync::Resolver`
resource.

`Pipeline`

Functions linked with the pipeline resolver. Specify functions by logical ID in a
list.

_Type_: List

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent. It is similar to the `PipelineConfig` property of an `AWS::AppSync::Resolver`
resource.

`Runtime`

The runtime of your pipeline resolver or function. Specifies the name and version to
use.

_Type_: [Runtime](sam-property-graphqlapi-resolver-runtime.md "sam-property-graphqlapi-resolver-runtime.md")

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent. It is similar to the `Runtime` property of an `AWS::AppSync::Resolver`
resource.

`Sync`

Describes a Sync configuration for a resolver.

Specifies which Conflict Detection strategy and Resolution strategy to use when the
resolver is invoked.

_Type_: [SyncConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-resolver-syncconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`SyncConfig` property of an `AWS::AppSync::Resolver`
resource.

## Examples

### Use the AWS SAM generated

resolver function code and save fields as variables

Here is the GraphQL schema for our example:

```
schema {
  query: Query
  mutation: Mutation
}

type Query {
  getPost(id: ID!): Post
}

type Mutation {
  addPost(author: String!, title: String!, content: String!): Post!
}

type Post {
  id: ID!
  author: String
  title: String
  content: String
}
```

Here is a snippet of our AWS SAM template:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyGraphQLApi:
    Type: AWS::Serverless::GraphQLApi
    Properties:
      ...
      Functions:
        preprocessPostItem:
          ...
        createPostItem:
          ...
      Resolvers:
        Mutation:
          addPost:
            Runtime:
              Name: APPSYNC_JS
              Version: 1.0.0
            Pipeline:
            - preprocessPostItem
            - createPostItem
```

In our AWS SAM template, we don’t specify `CodeUri` or `InlineCode`.
At deployment, AWS SAM automatically generates the following inline code for our
resolver:

```
export function request(ctx) {
  return {};
}

export function response(ctx) {
  return ctx.prev.result;
}
```

This default resolver code redirects the request to the first pipeline function and
receives the response from the last pipeline function.

In our first pipeline function, we can use the provided `args` field to parse
the request object and create our variables. We can then use these variables within our
function. Here is an example of our `preprocessPostItem` function:

```
import { util } from "@aws-appsync/utils";

export function request(ctx) {
  const author = ctx.args.author;
  const title = ctx.args.title;
  const content = ctx.args.content;

  // Use variables to process data

}

export function response(ctx) {
  return ctx.result;
}
```
