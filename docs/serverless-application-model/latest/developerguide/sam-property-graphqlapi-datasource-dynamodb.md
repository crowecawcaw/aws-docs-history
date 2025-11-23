# DynamoDb

Configure an Amazon DynamoDB table as a data source for your GraphQL API
resolver.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
`LogicalId`:
  DeltaSync: `DeltaSyncConfig`
  Description: `String`
  Name: `String`
  Permissions: `List`
  Region: `String`
  ServiceRoleArn: `String`
  TableArn: `String`
  TableName: `String`
  UseCallerCredentials: `Boolean`
  Versioned: `Boolean`
```

## Properties

`DeltaSync`

Describes a Delta Sync configuration.

_Type_: [DeltaSyncConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-appsync-datasource-deltasyncconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`DeltaSyncConfig` property of an `AWS::AppSync::DataSource
 DynamoDBConfig` object.

`Description`

The description of your data source.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Description` property of an `AWS::AppSync::DataSource`
resource.

`LogicalId`

The unique name of your data source.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::AppSync::DataSource`
resource.

`Name`

The name of your data source. Specify this property to override the
`LogicalId` value.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::AppSync::DataSource`
resource.

`Permissions`

Provision permissions to your data source using [AWS SAM
connectors](managing-permissions-connectors.md "managing-permissions-connectors.md"). You can provide any of the
following values in a list:

- `Read` – Allow your resolver to read your data source.
- `Write` – Allow your resolver to write to your data
  source.

AWS SAM uses an `AWS::Serverless::Connector` resource which is transformed
at deployment to provision your permissions. To learn about generated resources, see
[CloudFormation resources generated when
you specify AWS::Serverless::Connector](sam-specification-generated-resources-connector.md "sam-specification-generated-resources-connector.md").

###### Note

You can specify `Permissions` or `ServiceRoleArn`, but not
both. If neither are specified, AWS SAM will generate default values of
`Read` and `Write`. To revoke access to your data source,
remove the DynamoDB object from your AWS SAM template.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent. It is similar to the `Permissions` property of an
`AWS::Serverless::Connector` resource.

`Region`

The AWS Region of your DynamoDB table. If you don’t specify it, AWS SAM uses
`AWS::Region`.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`AwsRegion` property of an `AWS::AppSync::DataSource
 DynamoDBConfig` object.

`ServiceRoleArn`

The AWS Identity and Access Management (IAM) service role ARN for the data source. The system assumes this
role when accessing the data source.

You can specify `Permissions` or `ServiceRoleArn`, but not
both.

_Type_: String

_Required_: No. If not specified, AWS SAM applies the default value
for `Permissions`.

_CloudFormation compatibility_: This property is passed directly to the
`ServiceRoleArn` property of an `AWS::AppSync::DataSource`
resource.

`TableArn`

The ARN for the DynamoDB table.

_Type_: String

_Required_: Conditional. If you don’t specify
`ServiceRoleArn`, `TableArn` is required.

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn’t have an CloudFormation equivalent.

`TableName`

The table name.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`TableName` property of an `AWS::AppSync::DataSource
 DynamoDBConfig` object.

`UseCallerCredentials`

Set to `true` to use IAM with this data source.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`UseCallerCredentials` property of an `AWS::AppSync::DataSource
 DynamoDBConfig` object.

`Versioned`

Set to `true` to use [Conflict Detection,
Conflict Resolution, and Sync](../../../appsync/latest/devguide/conflict-detection-and-sync.md "../../../appsync/latest/devguide/conflict-detection-and-sync.md") with this data source.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Versioned` property of an `AWS::AppSync::DataSource
 DynamoDBConfig` object.
