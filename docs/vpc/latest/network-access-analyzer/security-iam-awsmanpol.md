# AWS managed policies for Network Access Analyzer

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AmazonVPCNetworkAccessAnalyzerFullAccessPolicy

Provides permissions to create, analyze, and delete Network Access Scopes, and to describe network path resources,
such as firewalls, internet gateways, load balancers, NAT gateways, network interfaces, transit gateway attachments,
VPC endpoints, VPC peering connections, and virtual private gateways.

To view the permissions for this policy, see [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](../../../aws-managed-policy/latest/reference/AmazonVPCNetworkAccessAnalyzerFullAccessPolicy.md "../../../aws-managed-policy/latest/reference/AmazonVPCNetworkAccessAnalyzerFullAccessPolicy.md") in the _AWS Managed Policy Reference_.

Network Access Analyzer does not support resources from Direct Connect (service prefix:
`directconnect`) or AWS Global Accelerator (service prefix:
`globalaccelerator`). If you use this policy as a model for your own policies,
you can omit these actions.

## Network Access Analyzer updates to AWS managed

policies

View details about updates to AWS managed policies for Network Access Analyzer since this service began
tracking these changes.

| Change                                                                                                                                                                             | Description                                                                                                                                     | Date             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy "#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy") – Update to an existing policy | Added the action `elasticloadbalancing:DescribeTargetGroupAttributes`,<br>which grants permission to describe the attributes of a target group. | May 15, 2024     |
| [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy "#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy") – Update to an existing policy | Removed resource ID prefixes from the resource ARNs used to allow tagging<br>Network Access Analyzer resources on create.                       | November 3, 2023 |
| [AmazonVPCNetworkAccessAnalyzerFullAccessPolicy](#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy "#AmazonVPCNetworkAccessAnalyzerFullAccessPolicy") – New policy                   | Added a policy that provides full access to Network Access Analyzer.                                                                            | June 15, 2023    |
| Network Access Analyzer started tracking changes                                                                                                                                   | Network Access Analyzer started tracking changes for its AWS managed policies.                                                                  | December 1, 2021 |
