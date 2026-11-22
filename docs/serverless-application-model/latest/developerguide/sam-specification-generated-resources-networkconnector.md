

# CloudFormation resources generated when AWS::Serverless::NetworkConnector is specified

When you specify an `AWS::Serverless::NetworkConnector`, AWS Serverless Application Model (AWS SAM) generates an `AWS::Lambda::NetworkConnector` base CloudFormation resource.

**`AWS::Lambda::NetworkConnector`**  
*`LogicalId`: *`{{<networkconnector‑LogicalId>}}`  
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

In addition to this CloudFormation resource, when `AWS::Serverless::NetworkConnector` is specified, AWS SAM also generates CloudFormation resources for the following scenarios:

**Topics**
+ [OperatorRole property is not specified](#sam-specification-generated-resources-networkconnector-iam-role)

## OperatorRole property is not specified
<a name="sam-specification-generated-resources-networkconnector-iam-role"></a>

When you don't specify the `OperatorRole` property of an `AWS::Serverless::NetworkConnector`, AWS SAM generates an `AWS::IAM::Role` CloudFormation resource with the `AWSLambdaNetworkConnectorOperatorPolicy` AWS managed policy attached.

The role trust policy allows the `lambda.amazonaws.com` service principal to assume the role.

If `VpcConfig` specifies an [ElasticIpConfiguration](sam-property-networkconnector-vpcconfig.md#sam-networkconnector-vpcconfig-elasticipconfiguration) whose `Type` isn't `None`, the role also gets an inline policy that allows `ec2:AllocateAddress` and `ec2:AssociateAddress`, which the service needs to assign Elastic IP addresses. The policy limits `ec2:AssociateAddress` on Elastic IP addresses to addresses tagged for a network connector, and limits both actions on network interfaces to the connector's own network interfaces. If the `Type` value is an intrinsic function, AWS SAM can't resolve it during the transform and adds the policy.

**`AWS::IAM::Role`**  
*`LogicalId`: *`{{<networkconnector‑LogicalId>}}OperatorRole`