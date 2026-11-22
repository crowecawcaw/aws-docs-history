

# ElasticIpConfiguration

Specifies whether the service assigns an Elastic IP address to each of the network connector's elastic network interfaces (ENIs). With `ServiceManaged`, the service allocates a service-managed Elastic IP address in your account for each ENI and associates it with that ENI. Each address stays the same for the life of its ENI, and the service releases it when it deletes the ENI.

## Syntax
<a name="sam-property-networkconnector-elasticipconfiguration-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-networkconnector-elasticipconfiguration-syntax.yaml"></a>

```yaml
[Type](#sam-networkconnector-elasticipconfiguration-type): {{String}}
```

## Properties
<a name="sam-property-networkconnector-elasticipconfiguration-properties"></a>

 `Type`   <a name="sam-networkconnector-elasticipconfiguration-type"></a>
The Elastic IP address type for the network connector's ENIs:  
+ `None`: No Elastic IP addresses are assigned.
+ `ServiceManaged`: The service allocates a service-managed Elastic IP address for each ENI and associates it with that ENI.
*Valid values*: `None`, `ServiceManaged`  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-networkconnector-elasticipconfiguration.html#cfn-lambda-networkconnector-elasticipconfiguration-type)` property of `Configuration.VpcEgressConfiguration.ElasticIpConfiguration` of an `AWS::Lambda::NetworkConnector` resource. 

## Examples
<a name="sam-property-networkconnector-elasticipconfiguration-examples"></a>

### ElasticIpConfiguration example
<a name="sam-property-networkconnector-elasticipconfiguration-example-basic"></a>

The following example creates a network connector that assigns a service-managed Elastic IP address to each ENI. Because the template doesn't specify an `OperatorRole`, the role that AWS SAM creates includes the `ec2:AllocateAddress` and `ec2:AssociateAddress` permissions.

```yaml
MyNetworkConnector:
  Type: AWS::Serverless::NetworkConnector
  Properties:
    ComputeTypes:
      - MicroVm
    VpcConfig:
      SubnetIds:
        - subnet-1234567890abcdef0
      SecurityGroupIds:
        - sg-abcdef01234567890
      NetworkProtocol: IPv4
      ElasticIpConfiguration:
        Type: ServiceManaged
```