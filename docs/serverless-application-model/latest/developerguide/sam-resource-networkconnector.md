# AWS::Serverless::NetworkConnector

Creates a AWS Lambda Network Connector that defines network connectivity for Lambda
compute resources. A network connector specifies how compute resources connect to
networks — for example, routing egress traffic through a customer VPC using elastic network interfaces (ENIs)
that the service provisions in specified subnets and security groups.

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation
resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Type: AWS::Serverless::NetworkConnector
Properties:
  Name: `String`
  OperatorRole: `String`
  PropagateTags: `Boolean`
  Tags: `Map`
  VpcConfig: `VpcConfig`

```

## Properties

`Name`

The name of the network connector. The name must be unique within your account and Region.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an
`AWS::Lambda::NetworkConnector` resource.

`OperatorRole`

The ARN of the IAM role that the network connector service assumes to create and
manage elastic network interfaces (ENIs).

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is similar to the
`OperatorRole` property of an
`AWS::Lambda::NetworkConnector` resource. This is required in CloudFormation
but not in AWS SAM. If you don't specify a role, AWS SAM creates one with a
logical ID of ``<resource-logical-id>`OperatorRole`.

`PropagateTags`

Specifies whether to pass tags from the `Tags` property to generated
resources, such as the auto-generated operator role.

_Type_: Boolean

_Required_: No

_Default_: `False`

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Tags`

A map of key-value pairs that specifies the tags added to this network connector.

_Type_: Map

_Required_: No

_CloudFormation compatibility_: This property is similar to the
`Tags` property of an
`AWS::Lambda::NetworkConnector` resource. The
`Tags` property in AWS SAM consists of key-value pairs (whereas in CloudFormation this
property consists of a list of `Tag` objects). Also, AWS SAM automatically adds
a `lambda:createdBy:SAM` tag to this network connector, and to the default roles
that are generated for it.

`VpcConfig`

The VPC egress configuration for the network connector. Specifies the subnets, security
groups, and network protocol for routing outbound traffic through your VPC.

_Type_: [VpcConfig](sam-property-networkconnector-vpcconfig.md "sam-property-networkconnector-vpcconfig.md")

_Required_: Yes

_CloudFormation compatibility_: This property is transformed to the
`Configuration.VpcEgressConfiguration` property of an
`AWS::Lambda::NetworkConnector` resource. AWS SAM also injects
`AssociatedComputeResourceTypes: [MicroVm]` automatically.

## Return Values

### Ref

When the logical ID of this resource is provided to the `Ref` intrinsic
function, it returns the ARN of the network connector.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

### Fn::GetAtt

`Fn::GetAtt` returns a value for a specified attribute of this type. The
following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md") in the _AWS CloudFormation User Guide_.

`Arn`

The Amazon Resource Name (ARN) of the network connector.

`State`

The current state of the network connector. Valid values are `PENDING`,
`ACTIVE`, `INACTIVE`, `FAILED`,
`DELETING`, and `DELETE_FAILED`.

## Examples

### Basic network connector with auto-generated role

The following example creates a VPC egress network connector. AWS SAM automatically
generates the operator role.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyVpcConnector:
    Type: AWS::Serverless::NetworkConnector
    Properties:
      Name: my-vpc-connector
      VpcConfig:
        SubnetIds:
          - subnet-0abc123def4567890
          - subnet-0def456abc7890123
        SecurityGroupIds:
          - sg-0abc1234abcde0001
        NetworkProtocol: IPv4
      Tags:
        Environment: Production

```
