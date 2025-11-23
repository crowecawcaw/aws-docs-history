# Function

Configure functions in GraphQL APIs to perform certain operations.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
`LogicalId`:
  CodeUri: `String`
  DataSource: `String`
  Description: `String`
  Id: `String`
  InlineCode: `String`
  MaxBatchSize: `Integer`
  Name: `String`
  Runtime: `Runtime`
  Sync: `SyncConfig`
```

## Properties

`CodeUri`

The function code’s Amazon Simple Storage Service (Amazon S3) URI or path to local folder.

If you specify a path to a local folder, CloudFormation requires that the file is first
uploaded to Amazon S3 before deployment. You can use the AWS SAM CLI to facilitate this
process. For more information, see [How AWS SAM uploads local files at deployment](deploy-upload-local-files.md "deploy-upload-local-files.md").

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`CodeS3Location` property of an
`AWS::AppSync::FunctionConfiguration` resource.

`DataSource`

The name of the data source that this function will attach to.

- To reference a data source within the `AWS::Serverless::GraphQLApi`
  resource, specify its logical ID.
- To reference a data source outside of the
  `AWS::Serverless::GraphQLApi` resource, provide its `Name`
  attribute using the `Fn::GetAtt` intrinsic function. For example,
  `!GetAtt MyLambdaDataSource.Name`.
- To reference a data source from a different stack, use `Fn::ImportValue`.

If a variation of `[NONE | None | none]` is specified, AWS SAM will
generate a `None` value for the `AWS::AppSync::DataSource`
`Type` object.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`DataSourceName` property of an
`AWS::AppSync::FunctionConfiguration` resource.

`Description`

The description of your function.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Description` property of an
`AWS::AppSync::FunctionConfiguration` resource.

`Id`

The Function ID for a function located outside of the
`AWS::Serverless::GraphQLApi` resource.

- To reference a function within the same AWS SAM template, use the
  `Fn::GetAtt` intrinsic function. For example `Id: !GetAtt
createPostItemFunc.FunctionId`.
- To reference a function from a different stack, use `Fn::ImportValue`.

When using `Id`, all other properties are not allowed. AWS SAM will
automatically pass the Function ID of your referenced function.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.

`InlineCode`

The function code that contains the request and response functions.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Code` property of an `AWS::AppSync::FunctionConfiguration`
resource.

`LogicalId`

The unique name of your function.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::AppSync::FunctionConfiguration`
resource.

`MaxBatchSize`

The maximum number of resolver request inputs that will be sent to a single
AWS Lambda function in a `BatchInvoke` operation.

_Type_: Integer

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
[MaxBatchSize](../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.md#cfn-appsync-functionconfiguration-maxbatchsize "../../../AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.md#cfn-appsync-functionconfiguration-maxbatchsize") property of an `AWS::AppSync::FunctionConfiguration`
resource.

`Name`

The name of the function. Specify to override the `LogicalId`
value.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::AppSync::FunctionConfiguration`
resource.

`Runtime`

Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function.
Specifies the name and version of the runtime to use.

_Type_: [Runtime](sam-property-graphqlapi-function-runtime.md "sam-property-graphqlapi-function-runtime.md")

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent. It is similar to the `Runtime` property of an
`AWS::AppSync::FunctionConfiguration` resource.

`Sync`

Describes a Sync configuration for a function.

Specifies which Conflict Detection strategy and Resolution strategy to use when the
function is invoked.

_Type_: [SyncConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-functionconfiguration-syncconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`SyncConfig` property of an
`AWS::AppSync::FunctionConfiguration` resource.
