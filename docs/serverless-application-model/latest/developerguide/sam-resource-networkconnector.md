

# AWS::Serverless::NetworkConnector
<a name="sam-resource-networkconnector"></a>

 Creates a AWS Lambda Network Connector that defines network connectivity for Lambda compute resources. A network connector specifies how compute resources connect to networks — for example, routing egress traffic through a customer VPC using elastic network interfaces (ENIs) that the service provisions in specified subnets and security groups. 

**Note**  
When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md). 

## Syntax
<a name="sam-resource-networkconnector-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-resource-networkconnector-syntax.yaml"></a>

```
Type: AWS::Serverless::NetworkConnector
Properties:
  [Name](#sam-networkconnector-name): {{String}}
  [OperatorRole](#sam-networkconnector-operatorrole): {{String}}
  [PropagateTags](#sam-networkconnector-propagatetags): {{Boolean}}
  [Tags](#sam-networkconnector-tags): {{Map}}
  [VpcConfig](#sam-networkconnector-vpcconfig): {{VpcConfig}}
```

## Properties
<a name="sam-resource-networkconnector-properties"></a>

 `Name`   <a name="sam-networkconnector-name"></a>
The name of the network connector. The name must be unique within your account and Region.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-networkconnector.html#cfn-lambda-networkconnector-name)` property of an `AWS::Lambda::NetworkConnector` resource. 

 `OperatorRole`   <a name="sam-networkconnector-operatorrole"></a>
The ARN of the IAM role that the network connector service assumes to create and manage elastic network interfaces (ENIs).  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[OperatorRole](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-networkconnector.html#cfn-lambda-networkconnector-operatorrole)` property of an `AWS::Lambda::NetworkConnector` resource. This is required in CloudFormation but not in AWS SAM. If you don't specify a role, AWS SAM creates one with a logical ID of `{{<resource-logical-id>}}OperatorRole`. 

 `PropagateTags`   <a name="sam-networkconnector-propagatetags"></a>
Specifies whether to pass tags from the `Tags` property to generated resources, such as the auto-generated operator role.  
*Type*: Boolean  
*Required*: No  
*Default*: `False`  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Tags`   <a name="sam-networkconnector-tags"></a>
A map of key-value pairs that specifies the tags added to this network connector.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[Tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-networkconnector.html#cfn-lambda-networkconnector-tags)` property of an `AWS::Lambda::NetworkConnector` resource. The `Tags` property in AWS SAM consists of key-value pairs (whereas in CloudFormation this property consists of a list of `Tag` objects). Also, AWS SAM automatically adds a `lambda:createdBy:SAM` tag to this network connector, and to the default roles that are generated for it. 

 `VpcConfig`   <a name="sam-networkconnector-vpcconfig"></a>
The VPC egress configuration for the network connector. Specifies the subnets, security groups, and network protocol for routing outbound traffic through your VPC.  
*Type*: [VpcConfig](sam-property-networkconnector-vpcconfig.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is transformed to the `[Configuration.VpcEgressConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-vpcegressconfiguration.html)` property of an `AWS::Lambda::NetworkConnector` resource. AWS SAM also injects `AssociatedComputeResourceTypes: [MicroVm]` automatically. 

## Return Values
<a name="sam-resource-networkconnector-return-values"></a>

### Ref
<a name="sam-resource-networkconnector-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, it returns the ARN of the network connector.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html) in the *AWS CloudFormation User Guide*.

### Fn::GetAtt
<a name="sam-resource-networkconnector-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html) in the *AWS CloudFormation User Guide*.

`Arn`  <a name="sam-networkconnector-getatt-arn"></a>
The Amazon Resource Name (ARN) of the network connector.

`State`  <a name="sam-networkconnector-getatt-state"></a>
The current state of the network connector. Valid values are `PENDING`, `ACTIVE`, `INACTIVE`, `FAILED`, `DELETING`, and `DELETE_FAILED`.

## Examples
<a name="sam-resource-networkconnector-examples"></a>

### Basic network connector with auto-generated role
<a name="sam-resource-networkconnector-example-basic"></a>

The following example creates a VPC egress network connector. AWS SAM automatically generates the operator role.

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