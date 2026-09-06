

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Infrastructure security in AWS Systems Manager
<a name="infrastructure-security"></a>

As a managed service, AWS Systems Manager is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access Systems Manager through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.