# Infrastructure security in AWS TNB

As a managed service, AWS Telco Network Builder is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access AWS TNB through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.
  Here are some examples of shared responsibilities:

- AWS is responsible for securing components that support AWS TNB,
  including:
  - Compute instances (also known as _workers_)
  - Internal databases
  - Network communications between internal components
  - The AWS TNB application programming interface (API)
  - AWS Software Development Kits (SDK)

- You are responsible for securing your access to your AWS resources and your
  workload components, including (but not limited to):
  - IAM users, groups, roles, and policies
  - S3 buckets that you use to store your data for AWS TNB
  - Other AWS services and resources that you use to support the network service
    that you provisioned through AWS TNB
  - Your application code
  - Connections between the network service that you provisioned through AWS TNB
    and its clients

###### Important

You are responsible for implementing a disaster recovery plan that can effectively
recover a network service that you provisioned through AWS TNB.

## Network connectivity security

model

The network services that you provision through AWS TNB, run on compute instances
within a virtual private cloud (VPC) located in an AWS Region that you select. A VPC is a
virtual network in the AWS Cloud, which isolates infrastructure by workload or
organizational entity. Communication between compute instances within VPCs stay within the
AWS network and don't travel over the internet. Some internal service communication
crosses the internet, and is encrypted. Network services provisioned through AWS TNB for
all customers running in the same Region share the same VPC. Network services provisioned
through AWS TNB for different customers use separate compute instances within the same
VPC.

Communications between your network service clients and your network service in
AWS TNB traverse the internet. AWS TNB does not manage these connections. It is your
responsibility to secure your client connections.

Your connections to AWS TNB through the AWS Management Console, AWS Command Line Interface (AWS CLI), and AWS SDKs
are encrypted.
