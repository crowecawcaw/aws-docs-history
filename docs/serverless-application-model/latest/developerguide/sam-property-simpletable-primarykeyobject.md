# PrimaryKeyObject

The object describing the properties of a primary key.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  Name: `String`
  Type: `String`

```

## Properties

`Name`

Attribute name of the primary key.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `AttributeName` property of the `AWS::DynamoDB::Table` `AttributeDefinition` data type.

_Additional notes_: This property is also passed to the [AttributeName](../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.md#aws-properties-dynamodb-keyschema-attributename "../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.md#aws-properties-dynamodb-keyschema-attributename") property of an `AWS::DynamoDB::Table KeySchema` data type.

`Type`

The data type for the primary key.

_Valid values_: `String`, `Number`, `Binary`

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `AttributeType` property of the `AWS::DynamoDB::Table` `AttributeDefinition` data type.

## Examples

### PrimaryKey

Primary key example.

#### YAML

```
Properties:
  PrimaryKey:
    Name: MyPrimaryKey
    Type: String

```
