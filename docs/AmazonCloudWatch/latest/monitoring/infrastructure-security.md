# Infrastructure security in Amazon CloudWatch

As a managed service, Amazon CloudWatch is protected by AWS global network security. For
 information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
 environment using the best practices for infrastructure security, see [Infrastructure
 Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html "https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html") in *Security Pillar AWS Well‐Architected
 Framework*.

You use AWS published API calls to access CloudWatch through the network. Clients must
 support the following:


* Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
* Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
 Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
 such as Java 7 and later support these modes.

## Network isolation


A virtual private cloud (VPC) is a virtual network in your own logically isolated area
 in the Amazon Web Services Cloud. A subnet is a range of IP addresses in a VPC. You can deploy a variety of 
 AWS resources in the subnets of your VPCs. For example, you can deploy Amazon EC2 instances, 
 EMR clusters, and DynamoDB tables in subnets. For more information, see the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/ "https://docs.aws.amazon.com/vpc/latest/userguide/").


To enable CloudWatch to communicate with resources in a VPC without going through the public 
 internet, use AWS PrivateLink. For more information, see [Using CloudWatch, CloudWatch Synthetics, and CloudWatch Network
 Monitoring with interface VPC endpoints](cloudwatch-and-interface-VPC.md "cloudwatch-and-interface-VPC.md").


A private subnet is a subnet with no default route to the public internet. Deploying an 
 AWS resource in a private subnet does not prevent Amazon CloudWatch from collecting built-in metrics 
 from the resource.


If you need to publish custom metrics from an AWS resource in a private subnet, you can
 do so using a proxy server. The proxy server forwards those HTTPS requests to the public 
 API endpoints for CloudWatch.
