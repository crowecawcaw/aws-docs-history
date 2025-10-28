# Lambda

Configure an AWS Lambda function as a data source for your GraphQL API
resolver.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
`LogicalId`:
  Description: `String`
  FunctionArn: `String`
  Name: `String`
  ServiceRoleArn: `String`
```

## Properties

`Description`

The description of your data source.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Description` property of an `AWS::AppSync::DataSource`
resource.

`FunctionArn`

The ARN for the Lambda function.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`LambdaFunctionArn` property of an `AWS::AppSync::DataSource
 LambdaConfig` object.

`LogicalId`

The unique name of your data source.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::AppSync::DataSource`
resource.

`Name`

The name of your data source. Specify this property to override the
`LogicalId` value.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::AppSync::DataSource`
resource.

`ServiceRoleArn`

The AWS Identity and Access Management (IAM) service role ARN for the data source. The system assumes this
role when accessing the data source.

###### Note

To revoke access to your data source, remove the Lambda object from your AWS SAM
template.

_Type_: String

_Required_: No. If not specified, AWS SAM will provision
`Write` permissions using [AWS SAM
connectors](managing-permissions-connectors.md "managing-permissions-connectors.md").

_AWS CloudFormation compatibility_: This property is passed directly to the
`ServiceRoleArn` property of an `AWS::AppSync::DataSource`
resource.
