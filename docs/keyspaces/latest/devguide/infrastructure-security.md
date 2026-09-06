

# Infrastructure security in Amazon Keyspaces
<a name="infrastructure-security"></a>

As a managed service, Amazon Keyspaces (for Apache Cassandra) is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Amazon Keyspaces through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

Amazon Keyspaces supports two methods of authenticating client requests. The first method uses service-specific credentials, which are password based credentials generated for a specific IAM user. You can create and manage the password using the IAM console, the AWS CLI, or the AWS API. For more information, see [Using IAM with Amazon Keyspaces](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mcs.html).

The second method uses an authentication plugin for the open-source DataStax Java Driver for Cassandra. This plugin enables [IAM users, roles, and federated identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) to add authentication information to Amazon Keyspaces (for Apache Cassandra) API requests using the [AWS Signature Version 4 process (SigV4)](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). For more information, see [Create and configure AWS credentials for Amazon Keyspaces](access.credentials.md). 

You can call these API operations from any network location, but Amazon Keyspaces does support resource-based access policies, which can include restrictions based on the source IP address. You can also use Amazon Keyspaces policies to control access from specific Amazon Virtual Private Cloud (Amazon VPC) endpoints or specific VPCs. Effectively, this isolates network access to a given Amazon Keyspaces resource from only the specific VPC within the AWS network.

You can use an interface VPC endpoint to keep traffic between your Amazon VPC and Amazon Keyspaces from leaving the Amazon network. Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables private communication between AWS services using an elastic network interface with private IPs in your Amazon VPC. For more information, see [Using Amazon Keyspaces with interface VPC endpoints](vpc-endpoints.md). 