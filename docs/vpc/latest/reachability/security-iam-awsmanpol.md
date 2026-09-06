

# AWS managed policies for Reachability Analyzer
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AmazonVPCReachabilityAnalyzerFullAccessPolicy
<a name="AmazonVPCReachabilityAnalyzerFullAccessPolicy"></a>

Provides permissions to create, analyze, and delete paths, and to describe path resources, such as EC2 instances, firewalls, internet gateways, load balancers, NAT gateways, network interfaces, transit gateways, VPC endpoint services, VPC endpoints, VPC peering connections, and virtual private gateways.

To view the permissions for this policy, see [AmazonVPCReachabilityAnalyzerFullAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonVPCReachabilityAnalyzerFullAccessPolicy.html) in the *AWS Managed Policy Reference*.

Reachability Analyzer does not support resources from Direct Connect (service prefix: `directconnect`) or AWS Global Accelerator (service prefix: `globalaccelerator`). If you use this policy as a model for your own policies, you can omit these actions.

## AWS managed policy: AmazonVPCReachabilityAnalyzerPathComponentReadPolicy
<a name="AmazonVPCReachabilityAnalyzerPathComponentReadPolicy"></a>

This policy is attached to the role [IAMRoleForReachabilityAnalyzerCrossAccountResourceAccess](cross-account-access-roles.md#IAMRoleForReachabilityAnalyzerCrossAccountResourceAccess). This role is deployed to the member accounts in an organization when the management account enables trusted access for Reachability Analyzer using the console. It provides permissions to view resources from across your organization using the Reachability Analyzer console. For more information, see [Cross-account access roles](cross-account-access-roles.md).

To view the permissions for this policy, see [AmazonVPCReachabilityAnalyzerPathComponentReadPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonVPCReachabilityAnalyzerPathComponentReadPolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSReachabilityAnalyzerServiceRolePolicy
<a name="AWSReachabilityAnalyzerServiceRolePolicy"></a>

This policy is attached to a service-linked role that allows Reachability Analyzer to perform actions on your behalf. For more information, see [Use service-linked roles](using-service-linked-roles.md).

To view the permissions for this policy, see [AWSReachabilityAnalyzerServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSReachabilityAnalyzerServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Reachability Analyzer updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Reachability Analyzer since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| [AmazonVPCReachabilityAnalyzerFullAccessPolicy](#AmazonVPCReachabilityAnalyzerFullAccessPolicy) – Update to an existing policy | Added `ec2:DescribeAddresses`, `ec2:DescribeTransitGatewayPolicyTables`, `ec2:GetTransitGatewayPolicyTableEntries`, `ec2:GetTransitGatewayPolicyTableAssociations`, and `network-firewall:DescribeFirewallMetadata`. These read-only actions grant permission to retrieve Elastic IP address information and AWS Network Firewall metadata. They also grant permission to retrieve transit gateway policy tables, including entries and associations. Reachability Analyzer does not yet support analysis of transit gateway policy tables. | August 14, 2026 | 
| [AWSReachabilityAnalyzerServiceRolePolicy](using-service-linked-roles.md#slr-permissions) – Update to an existing policy | Added `ec2:DescribeAddresses`, `ec2:DescribeTransitGatewayPolicyTables`, `ec2:GetTransitGatewayPolicyTableEntries`, `ec2:GetTransitGatewayPolicyTableAssociations`, and `network-firewall:DescribeFirewallMetadata`. These read-only actions grant permission to retrieve Elastic IP address information and AWS Network Firewall metadata. They also grant permission to retrieve transit gateway policy tables, including entries and associations. Reachability Analyzer does not yet support analysis of transit gateway policy tables. | August 14, 2026 | 
| [AWSReachabilityAnalyzerServiceRolePolicy](#AWSReachabilityAnalyzerServiceRolePolicy) – Update to an existing policy | Removed actions related to AWS Global Accelerator (service prefix: `globalaccelerator`). | September 10, 2024 | 
| [AmazonVPCReachabilityAnalyzerFullAccessPolicy](#AmazonVPCReachabilityAnalyzerFullAccessPolicy) – Update to an existing policy | Added the action elasticloadbalancing:DescribeTargetGroupAttributes, which grants permission to describe the attributes of a target group. | May 15, 2024 | 
| [AWSReachabilityAnalyzerServiceRolePolicy](#AWSReachabilityAnalyzerServiceRolePolicy) – Update to an existing policy | Added the action elasticloadbalancing:DescribeTargetGroupAttributes, which grants permission to describe the attributes of a target group. | May 15, 2024 | 
| [AmazonVPCReachabilityAnalyzerFullAccessPolicy](#AmazonVPCReachabilityAnalyzerFullAccessPolicy) – Update to an existing policy | Removed resource ID prefixes from the resource ARNs used to allow tagging Reachability Analyzer resources on create. | November 3, 2023 | 
| [AmazonVPCReachabilityAnalyzerFullAccessPolicy](#AmazonVPCReachabilityAnalyzerFullAccessPolicy) – New policy | Added a policy that provides full access to Reachability Analyzer for single account use. | June 14, 2023 | 
| [AmazonVPCReachabilityAnalyzerPathComponentReadPolicy](#AmazonVPCReachabilityAnalyzerPathComponentReadPolicy) – New policy | Added a policy that grants member accounts permission to view resources from across your organization. The policy is attached to a role that is deployed to member accounts when the management account enables trusted access for Reachability Analyzer using the console. | May 1, 2023 | 
| [AWSReachabilityAnalyzerServiceRolePolicy](#AWSReachabilityAnalyzerServiceRolePolicy) – New policy | Added a policy that is attached to a service-linked role that allows it to access AWS resources and integrate with AWS Organizations on your behalf. | November, 23, 2022 | 
| Reachability Analyzer started tracking changes | Reachability Analyzer started tracking changes for its AWS managed policies. | March 1, 2021 | 