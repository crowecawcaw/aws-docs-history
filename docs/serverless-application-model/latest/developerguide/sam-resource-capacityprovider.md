

# AWS::Serverless::CapacityProvider
<a name="sam-resource-capacityprovider"></a>

 Creates a capacity provider for AWS Lambda functions that enables running Lambda Managed Instances on customer-owned Amazon Elastic Compute Cloud instances. This resource is part of the Lambda Managed Instances feature, which provides cost optimization for large-scale Lambda workloads by utilizing Amazon EC2 pricing models. 

 The capacity provider manages the lifecycle of Amazon EC2 instances and provides the necessary infrastructure for Lambda functions to execute on customer-owned compute resources while maintaining the serverless programming model. 

**Note**  
When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md). 

## Syntax
<a name="sam-resource-capacityprovider-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-resource-capacityprovider-syntax.yaml"></a>

```
Type: AWS::Serverless::CapacityProvider
Properties:
  [CapacityProviderName](#sam-capacityprovider-capacityprovidername): {{String}}
  [VpcConfig](#sam-capacityprovider-vpcconfig): {{VpcConfig}}
  [OperatorRole](#sam-capacityprovider-operatorrole): {{String}}
  [Tags](#sam-capacityprovider-tags): {{Map}}
  [PropagateTags](#sam-capacityprovider-propagatetags): {{Boolean}}
  [InstanceRequirements](#sam-capacityprovider-instancerequirements): {{InstanceRequirements}}
  [ScalingConfig](#sam-capacityprovider-scalingconfig): {{ScalingConfig}}
  [LoggingConfig](#sam-capacityprovider-loggingconfig): {{[CapacityProviderLoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-capacityproviderloggingconfig.html)}}
  [KmsKeyArn](#sam-capacityprovider-kmskeyarn): {{String}}
  [ManagedResourceTags](#sam-capacityprovider-managedresourcetags): {{ManagedResourceTags}}
```

## Properties
<a name="sam-resource-capacityprovider-properties"></a>

 `CapacityProviderName`   <a name="sam-capacityprovider-capacityprovidername"></a>
The name of the capacity provider. This name must be unique within your AWS account and region.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[CapacityProviderName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-capacityprovidername)` property of an `AWS::Lambda::CapacityProvider` resource. 

 `VpcConfig`   <a name="sam-capacityprovider-vpcconfig"></a>
The VPC configuration for the capacity provider. Specifies the VPC subnets and security groups where Amazon EC2 instances will be launched.  
*Type*: [VpcConfig](sam-property-capacityprovider-vpcconfig.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[VpcConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-vpcconfig)` property of an `AWS::Lambda::CapacityProvider` resource. 

 `OperatorRole`   <a name="sam-capacityprovider-operatorrole"></a>
 The ARN of the operator role for Lambda with permissions to create and manage Amazon EC2 instances and related resources in the customer account. If not provided, AWS SAM automatically generates a role with the necessary permissions.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[CapacityProviderOperatorRoleArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-capacityproviderpermissionsconfig.html#cfn-lambda-capacityprovider-capacityproviderpermissionsconfig-capacityprovideroperatorrolearn)` property of `[PermissionsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-permissionsconfig)` of an `AWS::Lambda::CapacityProvider` resource. 

 `Tags`   <a name="sam-capacityprovider-tags"></a>
A map of key-value pairs to apply to the capacity provider and its associated resources.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-tags)` property of an `AWS::Lambda::CapacityProvider` resource. The `Tags` property in AWS SAM consists of key-value pairs (whereas in CloudFormation this property consists of a list of Tag objects). Also, AWS SAM automatically adds a `lambda:createdBy:SAM` tag to this Lambda function, and to the default roles generated for this function. 

 `PropagateTags`   <a name="sam-capacityprovider-propagatetags"></a>
 Indicates whether or not to pass tags from the Tags property to your `AWS::Serverless::CapacityProvider` generated resources. Set this to `True` to propagate tags in your generated resources.   
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `InstanceRequirements`   <a name="sam-capacityprovider-instancerequirements"></a>
 Specifications for the types of compute instances that the capacity provider can use. This includes architecture requirements and `allowed` or `excluded` instance types.  
*Type*: [InstanceRequirements](sam-property-capacityprovider-instancerequirements.md)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[InstanceRequirements](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-instancerequirements)` property of an `AWS::Lambda::CapacityProvider` resource. 

 `ScalingConfig`   <a name="sam-capacityprovider-scalingconfig"></a>
 The scaling configuration for the capacity provider. Defines how the capacity provider scales Amazon EC2 instances based on demand.  
*Type*: [ScalingConfig](sam-property-capacityprovider-scalingconfig.md)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[CapacityProviderScalingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-capacityproviderscalingconfig)` property of an `AWS::Lambda::CapacityProvider` resource. 

 `LoggingConfig`   <a name="sam-capacityprovider-loggingconfig"></a>
 Use `LoggingConfig` to configure system logging for the capacity provider. System logs capture scaling activity and operational events and send them to a Amazon CloudWatch log group at a configurable log level.  
*Type*: [CapacityProviderLoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-capacityproviderloggingconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[LoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-capacityprovidertelemetryconfig.html#cfn-lambda-capacityprovider-capacityprovidertelemetryconfig-loggingconfig)` property of `[TelemetryConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-telemetryconfig)` of an `AWS::Lambda::CapacityProvider` resource. 

 `KmsKeyArn`   <a name="sam-capacityprovider-kmskeyarn"></a>
The ARN of the AWS KMS key used to encrypt data at rest and in transit for the capacity provider.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[KmsKeyArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-kmskeyarn)` property of an `AWS::Lambda::CapacityProvider` resource. 

 `ManagedResourceTags`   <a name="sam-capacityprovider-managedresourcetags"></a>
 Applies explicit tags to the Amazon Elastic Compute Cloud instances and other managed resources that the capacity provider provisions on your behalf.  
*Type*: [ManagedResourceTags](sam-property-capacityprovider-managedresourcetags.md)  
*Required*: No  
*CloudFormation compatibility*: AWS SAM uses this property to construct the `[PropagateTags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-propagatetags)` property of an `AWS::Lambda::CapacityProvider` resource. 

## Return Values
<a name="sam-resource-capacityprovider-return-values"></a>

### Ref
<a name="sam-resource-capacityprovider-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, it returns the name of the capacity provider.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html) in the *AWS CloudFormation User Guide*. 

### Fn::GetAtt
<a name="sam-resource-capacityprovider-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html) in the *AWS CloudFormation User Guide*. 

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the capacity provider.

## Examples
<a name="sam-resource-capacityprovider-examples"></a>

### Basic capacity provider
<a name="sam-resource-capacityprovider-examples-basic"></a>

The following example creates a basic capacity provider with VPC configuration.

```
MyCapacityProvider:
  Type: AWS::Serverless::CapacityProvider
  Properties:
    CapacityProviderName: {{my-capacity-provider}}
    VpcConfig:
      SubnetIds:
        - {{subnet-12345678}}
        - {{subnet-87654321}}
      SecurityGroupIds:
        - {{sg-12345678}}
    Tags:
      Environment: Production
      Team: ServerlessTeam
```

### Advanced capacity provider with scaling
<a name="sam-resource-capacityprovider-examples-advanced"></a>

The following example creates a capacity provider with custom instance requirements and scaling configuration.

```
AdvancedCapacityProvider:
  Type: AWS::Serverless::CapacityProvider
  Properties:
    CapacityProviderName: {{advanced-capacity-provider}}
    VpcConfig:
      SubnetIds:
        - {{subnet-12345678}}
        - {{subnet-87654321}}
      SecurityGroupIds:
        - {{sg-12345678}}
    OperatorRole: arn:aws:iam::{{123456789012}}:role/{{MyCapacityProviderRole}}
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
    KmsKeyArn: arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{12345678-1234-1234-1234-123456789012}}
    LoggingConfig:
      LogGroup: /aws/lambda/capacity-provider/{{advanced-capacity-provider}}
      SystemLogLevel: INFO
    ManagedResourceTags:
      Tags:
        CostCenter: {{cc-1234}}
        Environment: {{Production}}
    Tags:
      Environment: Production
      CostCenter: Engineering
```