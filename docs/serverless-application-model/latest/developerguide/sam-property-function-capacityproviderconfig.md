# CapacityProviderConfig

Configures the capacity provider to which published versions of the function will be attached. This enables the function to run on customer-owned EC2 instances managed by Lambda.

###### Note

This configuration determines the compute type of a function and needs to be specified
during the first function deployment. It can't be added or removed after the function
resource has been created.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
Arn: `String`
ExecutionEnvironmentMemoryGiBPerVCpu: `Float`
PerExecutionEnvironmentMaxConcurrency: `Integer`

```

## Properties

`Arn`

The ARN of the capacity provider to use for this function.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to SAM.

`ExecutionEnvironmentMemoryGiBPerVCpu`

The ratio of memory (in GiB) to vCPU for each execution environment.

###### Note

The memory ratio per CPU can't exceed function's total memory of 2048MB. The supported memory-to-CPU ratios are 2GB, 4GB, or 8GB per CPU.

_Type_: Float

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `ExecutionEnvironmentMemoryGiBPerVCpu` property of an
`AWS::Lambda::Function` resource.

`PerExecutionEnvironmentMaxConcurrency`

The maximum number of concurrent executions per execution environment (sandbox).

_Type_: Integer

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `PerExecutionEnvironmentMaxConcurrency` property of an
`AWS::Lambda::Function` resource.

## Examples

### Capacity provider configuration

The following example shows a capacity provider configuration that references a capacity provider resource.

```
CapacityProviderConfig:
  Arn: !GetAtt `MyCapacityProvider`.Arn
  ExecutionEnvironmentMemoryGiBPerVCpu: 4.0
  PerExecutionEnvironmentMaxConcurrency: 100

```
