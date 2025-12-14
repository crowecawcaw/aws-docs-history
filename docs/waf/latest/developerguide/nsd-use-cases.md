**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS Shield network security director use cases

###### Note

AWS Shield network security director is in public preview release and is subject to change.

AWS Shield network security director helps secure your AWS environment by discovering your compute, networking, and network security resources across your account.
network security director evaluates each resource's security configuration by analyzing network topology and security configurations against AWS best practices and threat intelligence.
To help you strengthen your security, network security director rates its findings from low to critical severity and shares specific remediation steps, which you can explore using natural language queries through Amazon Q Developer.

Network security director and Amazon Q Developer help you identify security issues in your network security configuration and provide mitigation options:

- **Overly permissive access to your EC2 instances** – Identify security groups and network ACLs (NACLs) that are associated with your VPCs and Amazon Elastic Compute Cloud instances that allow unrestricted access to high-risk ports, such as ports 22 and 3389. Follow step-by-step instructions for implementing the right rules for security groups or NACLs to restrict access for these high-risk ports.
- **Compute and networking resources that are open to the internet** – Identify resources that are reachable from the internet via connectivity with an internet gateway.
- **Internet-facing resources that aren't fully protected by AWS WAF** – Identify resources that are reachable from the internet and understand the status of their AWS WAF protections. Follow step-by-step instructions for configuring and deploying AWS WAF, including recommendations for using rules such as rate-limiting rules and AWS Managed Rules rule groups.
- **Resources that are exposed to known threats** – Identify resources that are exposed to known threats, such as distributed denial of service (DDoS) attacks, SQL injection attacks, and cross-site scripting (XSS) attacks. Follow step-by-step instructions for implementing custom rules or AWS WAF AWS Managed Rules rule groups to defend against these threats.
- **Network security services that are enabled but aren't attached to any compute or networking resources** –
  Identify AWS WAF web ACLs and VPC security groups and NACLs that are currently not protecting any of your compute or networking resources. Follow instructions for removing them or for adding recommended rules to improve protections in case you decide to associate them with compute or networking resources in the future.
