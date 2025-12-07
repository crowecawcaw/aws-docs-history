# VpcConfig

Configures the VPC settings for a capacity provider, including the subnets and security groups where EC2 instances will be launched.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
SubnetIds: `List`
SecurityGroupIds: `List`
```

## Properties

`SubnetIds`

A list of subnet IDs where EC2 instances will be launched. At least one subnet must be specified.

_Type_: List

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the `SubnetIds` property of an `AWS::Lambda::CapacityProvider` resource.

`SecurityGroupIds`

A list of security group IDs to associate with the EC2 instances. If not specified, the default security group for the VPC will be used.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `SecurityGroupIds` property of an `AWS::Lambda::CapacityProvider` resource.

## Examples

### VPC configuration

The following example shows a VPC configuration with multiple subnets and security groups.

```
VpcConfig:
  SubnetIds:
    - `subnet-12345678`
    - `subnet-87654321`
  SecurityGroupIds:
    - `sg-12345678`
    - `sg-87654321`
```
