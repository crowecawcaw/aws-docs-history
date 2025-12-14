**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS Shield network security director (preview)

###### Note

AWS Shield network security director is in public preview release and is subject to change.

AWS Shield network security director helps secure your AWS environment by discovering your compute, networking, and network security resources across your account.
network security director evaluates each resource's security configuration by analyzing network topology and security configurations against AWS best practices and threat intelligence.
To help you strengthen your security, network security director rates its findings from low to critical severity and shares specific remediation steps, which you can explore using natural language queries through Amazon Q Developer.

## AWS Shield network security director pricing

AWS currently does not charge for use of network security director. However, you are responsible for fees incurred for the underlying services you use, such as AWS WAF.
When network security director becomes generally available, pricing will differ from the preview release.

## AWS Shield network security director quotas

AWS accounts have default quotas, formerly referred to as limits, for each AWS service. The following table describes the quota for network security director. For information about quotas that can be changed, see [Service Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

| Resource                                                       | Default Quota |
| -------------------------------------------------------------- | ------------- |
| Maximum resources processed per scan                           | 300,000       |
| Maximum number of edges per resource                           | 200           |
| Maximum number of accounts enabled per region per organization | 15,000        |
| Maximum Q prompts per organization per month                   | 200           |

When network security director reaches the maximum number of resources that it can process in a network analysis or the maximum number of edges per resource, the network analysis fails. You are not charged for the failed network analysis.
