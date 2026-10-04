

# Infrastructure security in AWS Startups
<a name="infrastructure-security"></a>

As a managed service, AWS Startups is protected by the AWS global network security procedures that are described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf) whitepaper.

You use AWS published API calls to access AWS Startups through the network. Clients must support Transport Layer Security (TLS) 1.2 or later. Clients must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed using an access key ID and a secret access key that is associated with an IAM principal. Or you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) (AWS STS) to generate temporary security credentials to sign requests.

 AWS Startups is available in the US East (N. Virginia) (`us-east-1`) Region only.

 AWS Startups supports interface VPC endpoints powered by AWS PrivateLink. An interface VPC endpoint lets you create a private connection between your VPC and AWS Startups without traversing the public internet. This connection lets AWS Startups communicate with the resources in your VPC using private IP addresses, and traffic between your VPC and the service does not leave the Amazon network. To create an interface VPC endpoint, use the endpoint service name `aws.api.global.startups`. For more information about AWS PrivateLink and interface VPC endpoints, see [What is AWS PrivateLink?](https://docs.aws.amazon.com/vpc/latest/privatelink/) in the AWS PrivateLink Guide. For steps to create an interface VPC endpoint for AWS Startups, see [AWS Startups and interface VPC endpoints (AWS PrivateLink)](vpc-interface-endpoints.md).