

# Access Amazon VPC Lattice using interface endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and Amazon VPC Lattice by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/), a technology that enables you to privately access VPC Lattice APIs without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with VPC Lattice APIs. 

Each interface endpoint is represented by one or more [network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets.

## Considerations for interface VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for VPC Lattice, ensure that you review [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

VPC Lattice supports making calls to all of its API actions from your VPC. 

## Creating an interface VPC endpoint for VPC Lattice
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the VPC Lattice service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

Create a VPC endpoint for VPC Lattice using the following service name: 

`com.amazonaws.{{region}}.vpc-lattice`

If you enable private DNS for the endpoint, you can make API requests to VPC Lattice using its default DNS name for the Region, for example, `vpc-lattice.us-east-1.amazonaws.com`.