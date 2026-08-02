# Infrastructure security in AWS Security Agent

As a managed service, AWS Security Agent is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS environment using the best practices for infrastructure security, see [Security](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/") in the _AWS Well-Architected Framework_.

## Network isolation

AWS Security Agent is a fully managed service accessed through the AWS Console and AWS Security Agent web application. Access to the service is controlled through AWS Identity and Access Management (IAM) or AWS IAM Identity Center, which can integrate with your identity provider.

AWS Security Agent supports interface VPC endpoints powered by AWS PrivateLink, enabling you to privately access the service APIs from your VPC without traversing the public internet. For more information, see [AWS Security Agent and interface VPC endpoints (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

AWS Security Agent requires internet access to perform penetration testing on target applications and for control plane operations. The service uses AWS-managed infrastructure for testing and does not provision EC2 instances or other compute resources in your account. If you configure VPC access for penetration testing, Security Agent creates an ENI in your subnet, but this ENI does not have a public IP address. For more information, see [Connect agent to private VPC resources](connect-agent-vpc.md "connect-agent-vpc.md").

## Multi-tenancy and resource isolation

AWS Security Agent is a multi-tenant service. Security reviews, findings, and customer data are isolated to individual AWS accounts and encrypted at rest. AWS applies standard infrastructure isolation controls to ensure that one customer’s security testing activities do not impact another customer’s performance or confidentiality.
