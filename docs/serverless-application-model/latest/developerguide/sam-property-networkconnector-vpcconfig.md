

# VpcConfig

Configures the VPC egress settings for a network connector, including the subnets, security groups, and network protocol for elastic network interface (ENI) provisioning.

## Syntax
<a name="sam-property-networkconnector-vpcconfig-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-networkconnector-vpcconfig-syntax.yaml"></a>

```yaml
[ElasticIpConfiguration](#sam-networkconnector-vpcconfig-elasticipconfiguration): {{ElasticIpConfiguration}}
[NetworkProtocol](#sam-networkconnector-vpcconfig-networkprotocol): {{String}}
[SecurityGroupIds](#sam-networkconnector-vpcconfig-securitygroupids): {{List}}
[SubnetIds](#sam-networkconnector-vpcconfig-subnetids): {{List}}
```

## Properties
<a name="sam-property-networkconnector-vpcconfig-properties"></a>

 `ElasticIpConfiguration`   <a name="sam-networkconnector-vpcconfig-elasticipconfiguration"></a>
Specifies whether the service assigns an Elastic IP address to each of the network connector's elastic network interfaces (ENIs). If you don't specify this property, no Elastic IP addresses are assigned.  
If you don't specify an [OperatorRole](sam-resource-networkconnector.md#sam-networkconnector-operatorrole), the role that AWS SAM creates includes the `ec2:AllocateAddress` and `ec2:AssociateAddress` permissions when you specify `ElasticIpConfiguration` with a `Type` other than `None`.  
*Type*: [ElasticIpConfiguration](sam-property-networkconnector-elasticipconfiguration.md)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ElasticIpConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-vpcegressconfiguration.html#cfn-lambda-networkconnector-vpcegressconfiguration-elasticipconfiguration)` property of `Configuration.VpcEgressConfiguration` of an `AWS::Lambda::NetworkConnector` resource. 

 `NetworkProtocol`   <a name="sam-networkconnector-vpcconfig-networkprotocol"></a>
The network protocol for the VPC egress connection.  
*Valid values*: `IPv4`, `DualStack`  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[NetworkProtocol](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-vpcegressconfiguration.html#cfn-lambda-networkconnector-vpcegressconfiguration-networkprotocol)` property of `Configuration.VpcEgressConfiguration` of an `AWS::Lambda::NetworkConnector` resource. 

 `SecurityGroupIds`   <a name="sam-networkconnector-vpcconfig-securitygroupids"></a>
A list of security group IDs to associate with the elastic network interfaces (ENIs).  
*Type*: List  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[SecurityGroupIds](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-vpcegressconfiguration.html#cfn-lambda-networkconnector-vpcegressconfiguration-securitygroupids)` property of `Configuration.VpcEgressConfiguration` of an `AWS::Lambda::NetworkConnector` resource. 

 `SubnetIds`   <a name="sam-networkconnector-vpcconfig-subnetids"></a>
A list of subnet IDs where the service provisions ENIs for VPC egress connectivity.  
*Type*: List  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[SubnetIds](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-vpcegressconfiguration.html#cfn-lambda-networkconnector-vpcegressconfiguration-subnetids)` property of `Configuration.VpcEgressConfiguration` of an `AWS::Lambda::NetworkConnector` resource. 

## Examples
<a name="sam-property-networkconnector-vpcconfig-examples"></a>

### VpcConfig example
<a name="sam-property-networkconnector-vpcconfig-example-basic"></a>

```yaml
VpcConfig:
  SubnetIds:
    - subnet-0abc123def4567890
    - subnet-0def456abc7890123
  SecurityGroupIds:
    - sg-0abc1234def567890
  NetworkProtocol: IPv4
```