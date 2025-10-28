# AWS::Serverless::SimpleTable

Creates a DynamoDB table with a single attribute primary key. It is useful when data only
needs to be accessed via a primary key.

For more advanced features, use an [AWS::DynamoDB::Table](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md") resource in AWS CloudFormation. These resouces can be used in AWS SAM. They are comprehensive and provide further customization, including
[key schema](../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-keyschema.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-keyschema.md") and
[resource policy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-resourcepolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-resourcepolicy.md") customization.

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into AWS CloudFormation resources.
For more information, see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Type: AWS::Serverless::SimpleTable
Properties:
  PointInTimeRecoverySpecification: `PointInTimeRecoverySpecification`
  PrimaryKey: `PrimaryKeyObject`
  ProvisionedThroughput: `ProvisionedThroughputObject`
  SSESpecification: `SSESpecification`
  TableName: `String`
  Tags: `Map`

```

## Properties

`PointInTimeRecoverySpecification`

The settings used to enable point in time recovery.

_Type_: [PointInTimeRecoverySpecification](../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `PointInTimeRecoverySpecification` property of an `AWS::DynamoDB::Table` resource.

`PrimaryKey`

Attribute name and type to be used as the table's primary key. If not provided, the
primary key will be a `String` with a value of `id`.

###### Note

The value of this property cannot be modified after this resource is
created.

_Type_: [PrimaryKeyObject](sam-property-simpletable-primarykeyobject.md "sam-property-simpletable-primarykeyobject.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`ProvisionedThroughput`

Read and write throughput provisioning information.

If `ProvisionedThroughput` is not specified `BillingMode` will
be specified as `PAY_PER_REQUEST`.

_Type_: [ProvisionedThroughputObject](sam-property-simpletable-provisionedthroughputobject.md "sam-property-simpletable-provisionedthroughputobject.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`ProvisionedThroughput` property of an
`AWS::DynamoDB::Table` resource.

`SSESpecification`

Specifies the settings to enable server-side encryption.

_Type_: [SSESpecification](../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`SSESpecification` property of an `AWS::DynamoDB::Table`
resource.

`TableName`

Name for the DynamoDB Table.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`TableName` property of an `AWS::DynamoDB::Table`
resource.

`Tags`

A map (string to string) that specifies the tags to be added to this SimpleTable.
For details about valid keys and values for tags, see [Resource tag](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md") in the
_AWS CloudFormation User Guide_.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`Tags` property of an `AWS::DynamoDB::Table` resource. The
Tags property in SAM consists of Key:Value pairs; in CloudFormation it consists of a
list of Tag objects.

## Return Values

### Ref

When the logical ID of this resource is provided to the Ref intrinsic function, it
returns the resource name of the underlying DynamoDB table.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

## Examples

### SimpleTableExample

Example of a SimpleTable

#### YAML

```
Properties:
  TableName: my-table
  PrimaryKey:
    Name: MyPrimaryKey
    Type: String
  ProvisionedThroughput:
    ReadCapacityUnits: `5`
    WriteCapacityUnits: `5`
  Tags:
    Department: Engineering
    AppType: Serverless

```
