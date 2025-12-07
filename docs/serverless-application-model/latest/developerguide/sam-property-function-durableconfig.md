# DurableConfig

Configures durable execution settings for AWS Lambda functions. Durable functions can run for up to one year and automatically checkpoint progress, enabling long-running workflows and fault-tolerant applications. For more information about durable functions, see
[Lambda durable functions](../../../lambda/latest/dg/durable-functions.md "../../../lambda/latest/dg/durable-functions.md") in the _AWS Lambda Developer Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  ExecutionTimeout: `Integer`
  RetentionPeriodInDays: `Integer`

```

## Properties

`ExecutionTimeout`

The amount of time (in seconds) that Lambda allows a durable function to run before stopping it. The maximum is one 366-day year or 31,622,400 seconds.

_Type_: Integer

_Required_: Yes

_Minimum_: 1

_Maximum_: 31622400

_CloudFormation compatibility_: This property is passed directly to the `ExecutionTimeout` property of the `AWS::Lambda::Function` `DurableConfig` data type.

`RetentionPeriodInDays`

The number of days after a durable execution is closed that Lambda retains its history, from one to 90 days. The default is 14 days.

_Type_: Integer

_Required_: No

_Default_: 14

_Minimum_: 1

_Maximum_: 90

_CloudFormation compatibility_: This property is passed directly to the `RetentionPeriodInDays` property of the `AWS::Lambda::Function` `DurableConfig` data type.

## Examples

### DurableConfig

Durable configuration example for a function with a 1-hour execution timeout and 7-day retention period.

#### YAML

```
DurableConfig:
  ExecutionTimeout: 3600
  RetentionPeriodInDays: 7

```
