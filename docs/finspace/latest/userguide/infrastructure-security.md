

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Infrastructure security in Amazon FinSpace
<a name="infrastructure-security"></a>

As a managed service, Amazon FinSpace is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access FinSpace through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

FinSpace is architected so that your traffic is isolated to the specific AWS Region that your FinSpace environment resides in.

## Connect to FinSpace using an interface VPC endpoint
<a name="connect-vpce"></a>

You can connect to FinSpace APIs using an interface VPC endpoint (AWSPrivateLink) instead of connecting over the internet. When you use an interface VPC endpoint, communication between your VPC and FinSpace is conducted entirely within the AWS network. Each VPC endpoint is represented by one or more [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) (ENIs) with private IP addresses in your VPC subnets.

**Note**  
You can only connect to FinSpace web application over the internet.

To use FinSpace through your VPC, you must connect from an instance that is inside the VPC or connect your private network to your VPC by using an Amazon Virtual Private Network (VPN) or AWS Direct Connect. For information about Amazon VPN, see [VPN connections](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html) in the Amazon Virtual Private Cloud User Guide. For information about AWS Direct Connect, see [Creating a connection](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-connection.html) in the AWS Direct Connect User Guide.

FinSpace supports VPC endpoints in all AWS Regions where both [Amazon VPC](https://docs.aws.amazon.com/general/latest/gr/rande.html#vpc_region) and [FinSpace](regions-ip-ranges.md) are available.

You can create an interface VPC endpoint to connect to FinSpace using the AWS console or AWS Command Line Interface (AWS CLI) commands. For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint).

You will need to create separate endpoints for using FinSpace management APIs and Data APIs:
+ Management APIs – `com.amazonaws.<Region>.finspace` 
+ Data APIs – `com.amazonaws.<Region>.finspace-api` 

After you create an interface VPC endpoint, if you [enable private DNS hostnames](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-private-dns) for the endpoint, the default [FinSpace endpoint](https://finfpace.Region.amazonaws.com) resolves to your VPC endpoint.

For more information, see Interface [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) (AWS PrivateLink) in the Amazon VPC User Guide.

### Create a VPC endpoint policy for FinSpace
<a name="create-a-vpc-endpoint-policy-for-finspace"></a>

You can create a policy for Amazon VPC endpoints for FinSpace to specify the following:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the Amazon VPC User Guide. Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the AWS Identity and Access Management User Guide.