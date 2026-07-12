# VpcConfig

Configures the VPC egress settings for a network connector, including the subnets, security groups, and network protocol for elastic network interface (ENI) provisioning.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
NetworkProtocol: `String`
SecurityGroupIds: `List`
SubnetIds: `List`
```

## Properties

`NetworkProtocol`

The network protocol for the VPC egress connection.

_Valid values_: `IPv4`, `DualStack`

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`NetworkProtocol` property of
`Configuration.VpcEgressConfiguration` of an
`AWS::Lambda::NetworkConnector` resource.

`SecurityGroupIds`

A list of security group IDs to associate with the elastic network interfaces (ENIs).

_Type_: List

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`SecurityGroupIds` property of
`Configuration.VpcEgressConfiguration` of an
`AWS::Lambda::NetworkConnector` resource.

`SubnetIds`

A list of subnet IDs where the service provisions ENIs for VPC egress connectivity.

_Type_: List

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`SubnetIds` property of
`Configuration.VpcEgressConfiguration` of an
`AWS::Lambda::NetworkConnector` resource.

## Examples

### VpcConfig example

```
VpcConfig:
  SubnetIds:
    - subnet-0abc123def4567890
    - subnet-0def456abc7890123
  SecurityGroupIds:
    - sg-0abc1234def567890
  NetworkProtocol: IPv4

```
