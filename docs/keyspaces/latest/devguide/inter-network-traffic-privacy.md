

# Internetwork traffic privacy in Amazon Keyspaces
<a name="inter-network-traffic-privacy"></a>

This topic describes how Amazon Keyspaces (for Apache Cassandra) secures connections from on-premises applications to Amazon Keyspaces and between Amazon Keyspaces and other AWS resources within the same AWS Region.

## Traffic between service and on-premises clients and applications
<a name="inter-network-traffic-privacy-on-prem"></a>

You have two connectivity options between your private network and AWS: 
+ An AWS Site-to-Site VPN connection. For more information, see [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the *AWS Site-to-Site VPN User Guide*.
+ An Direct Connect connection. For more information, see [What is Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) in the *Direct Connect User Guide*.

As a managed service, Amazon Keyspaces (for Apache Cassandra) is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Amazon Keyspaces through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Amazon Keyspaces supports two methods of authenticating client requests. The first method uses service-specific credentials, which are password based credentials generated for a specific IAM user. You can create and manage the password using the IAM console, the AWS CLI, or the AWS API. For more information, see [Using IAM with Amazon Keyspaces](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mcs.html).

The second method uses an authentication plugin for the open-source DataStax Java Driver for Cassandra. This plugin enables [IAM users, roles, and federated identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) to add authentication information to Amazon Keyspaces (for Apache Cassandra) API requests using the [AWS Signature Version 4 process (SigV4)](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). For more information, see [Create and configure AWS credentials for Amazon Keyspaces](access.credentials.md). 

## Traffic between AWS resources in the same Region
<a name="inter-network-traffic-privacy-within-region"></a>

Interface VPC endpoints enable private communication between your virtual private cloud (VPC) running in Amazon VPC and Amazon Keyspaces. Interface VPC endpoints are powered by AWS PrivateLink, which is an AWS service that enables private communication between VPCs and AWS services. AWS PrivateLink enables this by using an elastic network interface with private IPs in your VPC so that network traffic does not leave the Amazon network. Interface VPC endpoints don't require an internet gateway, NAT device, VPN connection, or Direct Connect connection. For more information, see [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/) and [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html). For example policies, see [Using interface VPC endpoints for Amazon Keyspaces](vpc-endpoints.md#using-interface-vpc-endpoints).