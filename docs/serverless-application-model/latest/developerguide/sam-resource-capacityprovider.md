# AWS::Serverless::CapacityProvider

Creates a capacity provider for AWS Lambda functions that enables running Lambda Managed
Instances on customer-owned Amazon Elastic Compute Cloud instances.
This resource is part of the Lambda Managed Instances feature, which provides cost
optimization for large-scale Lambda workloads by utilizing Amazon EC2 pricing models.

The capacity provider manages the lifecycle of Amazon EC2 instances and provides the necessary
infrastructure for Lambda functions to execute on customer-owned compute resources while
maintaining the serverless programming model.

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation
resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Type: AWS::Serverless::CapacityProvider
Properties:
  CapacityProviderName: `String`
  VpcConfig: `VpcConfig`
  OperatorRole: `String`
  Tags: `Map`
  PropagateTags: `Boolean`
  InstanceRequirements: `InstanceRequirements`
  ScalingConfig: `ScalingConfig`
  KmsKeyArn: `String`

```

## Properties

`CapacityProviderName`

The name of the capacity provider. This name must be unique within your AWS account and region.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`CapacityProviderName` property of an
`AWS::Lambda::CapacityProvider` resource.

`VpcConfig`

The VPC configuration for the capacity provider. Specifies the VPC subnets and security groups where Amazon EC2 instances will be launched.

_Type_: [VpcConfig](sam-property-capacityprovider-vpcconfig.md "sam-property-capacityprovider-vpcconfig.md")

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`VpcConfig` property of an
`AWS::Lambda::CapacityProvider` resource.

`OperatorRole`

The ARN of the operator role for Lambda with permissions to create and
manage Amazon EC2 instances and related resources in the customer account. If not
provided, AWS SAM automatically generates a role with the necessary
permissions.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`CapacityProviderOperatorRoleArn` property of
`PermissionsConfig` of an
`AWS::Lambda::CapacityProvider` resource.

`Tags`

A map of key-value pairs to apply to the capacity provider and its associated resources.

_Type_: Map

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Tags` property of an
`AWS::Lambda::CapacityProvider` resource. The `Tags` property in AWS SAM consists of key-value pairs (whereas in CloudFormation this property consists of a list of Tag objects).
Also, AWS SAM automatically adds a `lambda:createdBy:SAM` tag to this Lambda function, and to the default roles generated for this function.

`PropagateTags`

Indicates whether or not to pass tags from the Tags property to your `AWS::Serverless::CapacityProvider` generated resources.
Set this to `True` to propagate tags in your generated resources.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`InstanceRequirements`

Specifications for the types of compute instances that the capacity
provider can use. This includes architecture requirements and `allowed`
or `excluded` instance types.

_Type_: [InstanceRequirements](sam-property-capacityprovider-instancerequirements.md "sam-property-capacityprovider-instancerequirements.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`InstanceRequirements` property of an
`AWS::Lambda::CapacityProvider` resource.

`ScalingConfig`

The scaling configuration for the capacity provider. Defines how the
capacity provider scales Amazon EC2 instances based on demand.

_Type_: [ScalingConfig](sam-property-capacityprovider-scalingconfig.md "sam-property-capacityprovider-scalingconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`CapacityProviderScalingConfig` property of an
`AWS::Lambda::CapacityProvider` resource.

`KmsKeyArn`

The ARN of the AWS KMS key used to encrypt data at rest and in transit for the capacity provider.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`KmsKeyArn` property of an
`AWS::Lambda::CapacityProvider` resource.

## Return Values

### Ref

When the logical ID of this resource is provided to the `Ref` intrinsic
function, it returns the name of the capacity provider.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

### Fn::GetAtt

`Fn::GetAtt` returns a value for a specified attribute of this type.
The following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md") in the _AWS CloudFormation User Guide_.

`Arn`

The ARN of the capacity provider.

## Examples

### Basic capacity provider

The following example creates a basic capacity provider with VPC configuration.

```
MyCapacityProvider:
  Type: AWS::Serverless::CapacityProvider
  Properties:
    CapacityProviderName: `my-capacity-provider`
    VpcConfig:
      SubnetIds:
        - `subnet-12345678`
        - `subnet-87654321`
      SecurityGroupIds:
        - `sg-12345678`
    Tags:
      Environment: Production
      Team: ServerlessTeam
```

### Advanced capacity provider with scaling

The following example creates a capacity provider with custom instance requirements and scaling configuration.

```
AdvancedCapacityProvider:
  Type: AWS::Serverless::CapacityProvider
  Properties:
    CapacityProviderName: `advanced-capacity-provider`
    VpcConfig:
      SubnetIds:
        - `subnet-12345678`
        - `subnet-87654321`
      SecurityGroupIds:
        - `sg-12345678`
    OperatorRole: arn:aws:iam::`123456789012`:role/`MyCapacityProviderRole`
    PropagateTags: true
    InstanceRequirements:
      Architectures:
        - x86_64
      ExcludedTypes:
        - t2.micro
    ScalingConfig:
      MaxInstanceCount: 10
      ManualScalingPolicies:
        AverageCPUUtilization: 70.0
    KmsKeyArn: arn:aws:kms:`us-east-1`:`123456789012`:key/`12345678-1234-1234-1234-123456789012`
    Tags:
      Environment: Production
      CostCenter: Engineering
```
