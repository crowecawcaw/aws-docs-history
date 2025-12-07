# InstanceRequirements

Specifies the requirements for EC2 instances that will be launched by the capacity provider, including architectures and instance type constraints.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
Architectures: `List`
AllowedTypes: `List`
ExcludedTypes: `List`
```

###### Note

You can choose to specify either `AllowedTypes` or `ExcludedTypes` when defining instance requirements for your capacity provider, but not both.

## Properties

`Architectures`

The instruction set architectures for the capacity provider instances.

_Valid values_: `x86_64` or `arm64`

_Type_: List

_Required_: No

_Default_: `x86_64`

_CloudFormation compatibility_: This property is passed directly to the `Architectures` property of an `AWS::Lambda::CapacityProvider` resource.

`AllowedTypes`

A list of allowed EC2 instance types for the capacity provider instance.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`AllowedInstanceTypes` property of an
`AWS::Lambda::CapacityProvider` resource.

`ExcludedTypes`

A list of EC2 instance types to exclude from the capacity provider.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`ExcludedInstanceTypes` property of an
`AWS::Lambda::CapacityProvider` resource.

## Examples

### Instance requirements configuration

The following example shows instance requirements with specific architecture and instance type constraints.

```
InstanceRequirements:
  Architectures:
    - x86_64
  ExcludedTypes:
    - t2.micro
```
