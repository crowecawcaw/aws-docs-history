# ProvisionedThroughputObject

The object describing the properties of a provisioned throughput.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  ReadCapacityUnits: `Integer`
  WriteCapacityUnits: `Integer`

```

## Properties

`ReadCapacityUnits`

The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`.

_Type_: Integer

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `ReadCapacityUnits` property of the `AWS::DynamoDB::Table` `ProvisionedThroughput` data type.

`WriteCapacityUnits`

The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException`.

_Type_: Integer

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the `WriteCapacityUnits` property of the `AWS::DynamoDB::Table` `ProvisionedThroughput` data type.

## Examples

### ProvisionedThroughput

Provisioned throughput example.

#### YAML

```
Properties:
   ProvisionedThroughput:
     ReadCapacityUnits: `5`
     WriteCapacityUnits: `5`

```
