# Creating a VPC endpoint for AWS Organizations

You can create an AWS Organizations endpoint in your VPC using the Amazon VPC Console,
the AWS Command Line Interface (AWS CLI) or AWS CloudFormation.

For information about creating and configuring an endpoint using the Amazon VPC
console or the AWS CLI, see [Create a VPC
endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _Amazon VPC User Guide_. For information about
creating and configuring an endpoint using AWS CloudFormation, see the [AWS::EC2::VPCEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md") resource in the _AWS CloudFormation User Guide_.

When you create an AWS Organizations endpoint, use the following as the service
name:

```
com.amazonaws.us-east-1.organizations
```

If you require FIPS 140-2 validated cryptographic modules when accessing AWS,
use the following AWS Organizations FIPS service name:

```
com.amazonaws.us-east-1.organizations-fips
```
