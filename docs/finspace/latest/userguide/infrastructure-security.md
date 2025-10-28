After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Infrastructure security in Amazon FinSpace

As a managed service, Amazon FinSpace is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access FinSpace through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  FinSpace is architected so that your traffic is isolated to the specific AWS Region that
  your FinSpace environment resides in.

## Connect to FinSpace using an interface VPC endpoint

You can connect to FinSpace APIs using an interface VPC endpoint (AWSPrivateLink)
instead of connecting over the internet. When you use an interface VPC endpoint,
communication between your VPC and FinSpace is conducted entirely within the AWS network.
Each VPC endpoint is represented by one or more [Elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md")
(ENIs) with private IP addresses in your VPC subnets.

###### Note

You can only connect to FinSpace web application over the internet.

To use FinSpace through your VPC, you must connect from an instance that is inside the
VPC or connect your private network to your VPC by using an Amazon Virtual Private
Network (VPN) or AWS Direct Connect. For information about Amazon VPN, see [VPN
connections](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the Amazon Virtual Private Cloud User Guide. For information about AWS Direct
Connect, see [Creating a
connection](../../../directconnect/latest/UserGuide/create-connection.md "../../../directconnect/latest/UserGuide/create-connection.md") in the AWS Direct Connect User Guide.

FinSpace supports VPC endpoints in all AWS Regions where both [Amazon VPC](../../../general/latest/gr/rande.md#vpc_region "../../../general/latest/gr/rande.md#vpc_region") and
[FinSpace](regions-ip-ranges.md "regions-ip-ranges.md") are available.

You can create an interface VPC endpoint to connect to FinSpace using the AWS console
or AWS Command Line Interface (AWS CLI) commands. For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint").

You will need to create separate endpoints for using FinSpace management APIs and Data
APIs:

- Management APIs – `com.amazonaws.<Region>.finspace`
- Data APIs – `com.amazonaws.<Region>.finspace-api`

After you create an interface VPC endpoint, if you [enable private DNS
hostnames](../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns "../../../vpc/latest/userguide/vpce-interface.md#vpce-private-dns") for the endpoint, the default [FinSpace endpoint](https://finfpace.Region.amazonaws.com "https://finfpace.Region.amazonaws.com") resolves to your
VPC endpoint.

For more information, see Interface [VPC endpoints](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") (AWS
PrivateLink) in the Amazon VPC User Guide.

### Create a VPC endpoint

policy for FinSpace

You can create a policy for Amazon VPC endpoints for FinSpace to specify the
following:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to
services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the Amazon VPC User Guide. Whenever you use IAM
policies, make sure that you follow IAM best practices. For more information, see
[Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the AWS Identity and Access Management User Guide.
