# FunctionScalingConfig

Configures the scaling behavior for Lambda function versions, controlling the number of execution environments (sandboxes) that can be created. This configuration applies to both $LATEST.PUBLISHED and numeric function versions.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
MinExecutionEnvironments: `Integer`
MaxExecutionEnvironments: `Integer`
```

## Properties

`MinExecutionEnvironments`

The minimum number of execution environments to maintain for the function version.

_Type_: Integer

_Required_: No

_Default_: `3`

_Minimum_: `0`

_CloudFormation compatibility_: This property is passed directly to the `MinExecutionEnvironments` property of an `AWS::Lambda::Function` resource.

`MaxExecutionEnvironments`

The maximum number of execution environments that can be created for the function version.

_Type_: Integer

_Required_: No

_Default_: `3`

_Minimum_: `0`

_CloudFormation compatibility_: This property is passed directly to the `MaxExecutionEnvironments` property of an `AWS::Lambda::Function` resource.

## Examples

### Function scaling configuration

The following example shows a function scaling configuration with minimum and maximum execution environments.

```
FunctionScalingConfig:
  MinExecutionEnvironments: 5
  MaxExecutionEnvironments: 100
```
