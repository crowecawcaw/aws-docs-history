

# AWS managed policies for Network Access Analyzer
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AmazonVPCNetworkAccessAnalyzerFullAccessPolicy
<a name="AmazonVPCNetworkAccessAnalyzerFullAccessPolicy"></a>

Provides permissions to create, analyze, and delete Network Access Scopes, and to describe network path resources, such as firewalls, internet gateways, load balancers, NAT gateways, network interfaces, transit gateway attachments, VPC endpoints, VPC peering connections, and virtual private gateways.

To view the permissions for this policy, see [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonVPCNetworkAccessAnalyzerFullAccessPolicy.html) in the *AWS Managed Policy Reference*.

Network Access Analyzer does not support resources from Direct Connect (service prefix: `directconnect`) or AWS Global Accelerator (service prefix: `globalaccelerator`). If you use this policy as a model for your own policies, you can omit these actions.

## Network Access Analyzer updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Network Access Analyzer since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy) – Update to an existing policy | Added `ec2:DescribeAddresses`, `ec2:DescribeTransitGatewayPolicyTables`, `ec2:GetTransitGatewayPolicyTableEntries`, `ec2:GetTransitGatewayPolicyTableAssociations`, and `network-firewall:DescribeFirewallMetadata`. These read-only actions grant permission to retrieve Elastic IP address information and AWS Network Firewall metadata. They also grant permission to retrieve transit gateway policy tables, including entries and associations. Network Access Analyzer does not yet support analysis of transit gateway policy tables. | August 14, 2026 | 
| [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy) – Update to an existing policy | Added the action elasticloadbalancing:DescribeTargetGroupAttributes, which grants permission to describe the attributes of a target group. | May 15, 2024 | 
| [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy) – Update to an existing policy | Removed resource ID prefixes from the resource ARNs used to allow tagging Network Access Analyzer resources on create. | November 3, 2023 | 
| [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy) – New policy | Added a policy that provides full access to Network Access Analyzer. | June 15, 2023 | 
| Network Access Analyzer started tracking changes | Network Access Analyzer started tracking changes for its AWS managed policies. | December 1, 2021 | 