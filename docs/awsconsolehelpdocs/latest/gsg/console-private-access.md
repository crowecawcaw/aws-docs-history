

# AWS Management Console Private Access
<a name="console-private-access"></a>

AWS Management Console Private Access is an advanced security feature that combines network isolation and access controls for the AWS Management Console. With AWS Management Console Private Access, you can limit the use of the AWS Management Console to a specified set of known AWS accounts when the traffic originates from within your Amazon Virtual Private Cloud (VPC). You can also use AWS Management Console Private Access to route console traffic through AWS PrivateLink, establish private connectivity to the AWS Management Console through VPC endpoints, and avoid need for public internet access.

AWS Management Console Private Access addresses the following security requirements:
+ **Trusted identities** – Only explicitly authorized identities can access the AWS Management Console from within your network. You cannot sign in with personal accounts or with AWS accounts outside your organization.
+ **Trusted resources** – Authorized IAM identities can access only resources belonging to expected AWS accounts and organizations.
+ **Expected networks** – Authorized IAM identities can use the AWS Management Console and access AWS resources only from inside expected networks. You can prevent access from unauthorized network locations.
+ **Network isolation** – The AWS Management Console can operate in VPCs without access to the public internet. AWS Management Console Private Access controls 100% of the browser traffic through VPC endpoints.

You implement AWS Management Console Private Access by creating VPC endpoints for the AWS Management Console, AWS Management Console-only APIs, AWS Sign-In, and service APIs. Once configured with appropriate DNS resolution, console traffic from your VPC flows through these private endpoints. You then layer VPC endpoint policies and IAM controls to enforce your security objectives. AWS Management Console Private Access supports traffic from any network that can route to your VPC endpoints, including on-premises networks connected through Direct Connect or AWS Site-to-Site VPN.

You pay only for the AWS PrivateLink VPC endpoint usage and data processing associated with AWS Management Console Private Access. For more information, see [Amazon Virtual Private Cloud pricing](https://aws.amazon.com/vpc/pricing/).

**Topics**
+ [Supported AWS Regions, service consoles, and features in Private Access](supported-regions-consoles.md)
+ [Configuring VPC endpoints for accessing AWS Management Console](required-endpoints-dns-configuration.md)
+ [Configuring DNS for accessing AWS Management Console](dns-configuration-console-signin.md)
+ [Implementing access controls](implementing-access-controls.md)
+ [Getting started with a test environment](try-out-private-access.md)
+ [Reference architecture](console-private-access-reference-architectures.md)