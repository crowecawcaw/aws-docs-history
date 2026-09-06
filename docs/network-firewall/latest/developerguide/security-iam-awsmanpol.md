

# AWS managed policies for AWS Network Firewall
<a name="security-iam-awsmanpol"></a>







To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.













## Network Firewall updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Network Firewall since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Network Firewall Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
| `AWSNetworkFirewallServiceRolePolicy` – Update to the existing policy | Updated the `AWSNetworkFirewallServiceRolePolicy` to support monitoring container lifecycle events for container associations.<br />For policy details, see [AWSNetworkFirewallServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSNetworkFirewallServiceRolePolicy$serviceLevelSummary).  | June 30, 2026 | 
| `AWSNetworkFirewallReadOnlyAccess` – Update to the existing policy | Updated the `AWSNetworkFirewallReadOnlyAccess` to support describing and listing ProxyRules, ProxyRuleGroups, ProxyConfigurations, Proxies, VpcEndpointAssociation, and describing FirewallMetadata.<br />For policy details, see [AWSNetworkFirewallReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSNetworkFirewallReadOnlyAccess$serviceLevelSummary).  | January 16, 2026 | 
| `AWSNetworkFirewallServiceRolePolicy` – Update to the existing policy | Updated the `AWSNetworkFirewallServiceRolePolicy` to support describing ACM certificates for use with TLS inspection configurations.<br />For policy details, see [AWSNetworkFirewallServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSNetworkFirewallServiceRolePolicy$serviceLevelSummary).  | March 31, 2023 | 
| `AWSNetworkFirewallServiceRolePolicy` – Update to the existing policy | AWS Network Firewall expanded availability of the policy to the AWS GovCloud (US) Regions, AWS GovCloud (US-East) and AWS GovCloud (US-West). <br />`AWSNetworkFirewallServiceRolePolicy` is an access policy that allows Network Firewall to manage Network Firewall related resources on behalf of your AWS account. Network Firewall uses this policy to create, describe, and delete VPC endpoints in support of your firewall management activities. <br />For policy details, see [AWSNetworkFirewallServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSNetworkFirewallServiceRolePolicy$serviceLevelSummary). <br />This policy uses the service-linked role `AWSServiceRoleForNetworkFirewall`. For more information, see [Using service-linked roles for Network Firewall](using-service-linked-roles.md). | June 24, 2021 | 
| Network Firewall started tracking changes | Network Firewall started tracking changes for its AWS managed policies. | June 24, 2021 | 