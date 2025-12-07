# Infrastructure security in AWS Security Agent

As a managed service, AWS Security Agent is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS environment using the best practices for infrastructure security, see [Security](https://aws.amazon.com/architecture/security-identity-compliance/ "https://aws.amazon.com/architecture/security-identity-compliance/") in the _AWS Well-Architected Framework_.

## Network isolation

AWS Security Agent is a fully managed service accessed through the AWS Console and AWS Security Agent Web Application. Access to the service is controlled through AWS Identity and Access Management (IAM) or AWS IAM Identity Center, which can integrate with your identity provider.

The service does not support VPC endpoints or deployment within customer VPCs, and cannot be restricted to specific subnets through IAM or SCP policies.

AWS Security Agent requires internet access to perform penetration testing on target applications and for control plane operations. The service does not create customer-owned resources with public IP addresses.

## Multi-tenancy and resource isolation

AWS Security Agent is a multi-tenant service. Security reviews, findings, and customer data are isolated to individual AWS accounts and encrypted at rest. AWS applies standard infrastructure isolation controls to ensure that one customer’s security testing activities do not impact another customer’s performance or confidentiality.
