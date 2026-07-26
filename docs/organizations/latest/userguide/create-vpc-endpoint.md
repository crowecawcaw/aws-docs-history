# Creating a VPC endpoint for AWS Organizations

You can create an AWS Organizations endpoint in your VPC using the Amazon VPC Console,
the AWS Command Line Interface (AWS CLI) or CloudFormation.

For information about creating and configuring an endpoint using the Amazon VPC
console or the AWS CLI, see [Create a VPC
endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _Amazon VPC User Guide_. For information about
creating and configuring an endpoint using CloudFormation, see the [AWS::EC2::VPCEndpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.md") resource in the _AWS CloudFormation User Guide_.

AWS Organizations is a global service with its control plane located in US East (N. Virginia)
(us-east-1) for commercial AWS Regions. You can create an interface VPC endpoint for
AWS Organizations only in us-east-1. Use the following service name:

```
com.amazonaws.us-east-1.organizations
```

If you require FIPS 140-2 validated cryptographic modules when accessing AWS Organizations,
use the following AWS Organizations FIPS service name:

```
com.amazonaws.us-east-1.organizations-fips
```

If your VPC is in a different Region, you must use AWS Transit Gateway to access
the endpoint from that Region. For the AWS China and AWS GovCloud partitions, use
the service name that corresponds to the AWS Organizations control plane Region in that
partition.
