

AWS Well-Architected Agent is in preview release and is subject to change.

# AWS managed policies for AWS Well-Architected

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: WellArchitectedConsoleFullAccess
<a name="security-iam-awsmanpol-WellArchitectedConsoleFullAccess"></a>

You can attach the `WellArchitectedConsoleFullAccess` policy to your IAM identities.

This policy grants full access to AWS Well-Architected, including the Well-Architected Tool for workload reviews and lens management, and AWS Well-Architected Agent for automated architecture analysis. It includes permissions for AWS Organizations delegated administrator management, AWS Trusted Advisor data access, service-linked role management for Well-Architected service principals, IAM role and policy creation scoped to `service-role/*` for console-guided execution role setup, and `iam:PassRole` conditioned to Well-Architected and Agent service principals.

For more details about this policy, including the full JSON policy document, see [WellArchitectedConsoleFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedConsoleFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: WellArchitectedConsoleReadOnlyAccess
<a name="security-iam-awsmanpol-WellArchitectedConsoleReadOnlyAccess"></a>

You can attach the `WellArchitectedConsoleReadOnlyAccess` policy to your IAM identities.

This policy grants read-only access to AWS Well-Architected, including the Well-Architected Tool for viewing workloads and lenses, and AWS Well-Architected Agent for viewing architecture analysis results. It includes read-only permissions for AWS Organizations organization structure visibility and AWS Trusted Advisor data access.

For more details about this policy, including the full JSON policy document, see [WellArchitectedConsoleReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedConsoleReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: WellArchitectedAgentResourceScanning
<a name="security-iam-awsmanpol-WellArchitectedAgentResourceScanning"></a>

You can attach the `WellArchitectedAgentResourceScanning` policy to the access roles in your workload accounts that AWS Well-Architected Agent analyzes.

This policy grants AWS WA Agent read-only access to AWS resource configurations, security settings, and operational data across your accounts to generate optimization recommendations. The policy provides broad read-only access because AWS WA Agent must evaluate cross-service configurations holistically. All actions are read-only (`Get*`, `Describe*`, `List*`, `BatchGet*`). No create, update, delete, or invoke actions are included.

For more details about this policy, including the full JSON policy document, see [WellArchitectedAgentResourceScanning](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedAgentResourceScanning.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSWellArchitectedOrganizationsServiceRolePolicy
<a name="security-iam-awsmanpol-AWSWellArchitectedOrganizationsServiceRolePolicy"></a>

This policy is attached to the AWS WA Tool service-linked role (`AWSServiceRoleForWellArchitected`) and cannot be attached to your users, groups, or roles.

This policy grants administrative permissions in AWS Organizations that are required to support AWS Well-Architected Tool integration with Organizations. These permissions allow the organization management account to enable resource sharing with AWS WA Tool. It grants read access to the organization's accounts, organizational units, roots, and service-access status needed to enable and operate resource sharing.

For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedOrganizationsServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedOrganizationsServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSWellArchitectedDiscoveryServiceRolePolicy
<a name="security-iam-awsmanpol-AWSWellArchitectedDiscoveryServiceRolePolicy"></a>

This policy is attached to the AWS WA Tool service-linked role (`AWSServiceRoleForWellArchitected`) and cannot be attached to your users, groups, or roles.

This policy supports AWS Well-Architected Tool resource discovery by granting read access to Trusted Advisor checks, AppRegistry applications and their associated resources, CloudFormation stacks and their resources, and resource groups (including resource tagging), and by letting the AWS WA Tool manage the service-managed AppRegistry attribute groups for those applications. These permissions let the AWS WA Tool discover and associate the AWS resources related to your Well-Architected workloads.

For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedDiscoveryServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedDiscoveryServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSWellArchitectedAgentResourceScanningServiceRolePolicy
<a name="security-iam-awsmanpol-AWSWellArchitectedAgentResourceScanningServiceRolePolicy"></a>

This policy is attached to the `` service-linked role in each account of your organization. AWS Well-Architected Agent uses this role to analyze accounts for organizational profiles. When you enable AWS Organizations integration, AWS Organizations creates this role in your member accounts, and AWS WA Agent creates it in your management account.

This policy grants AWS WA Agent read-only access to AWS resource configurations, security settings, and operational data to generate optimization recommendations. The policy provides broad read-only access beecause AWS WA Agent must evaluate cross-service configurations holistically. All actions are read-only, such as `Get*`, `Describe*`, `List*`, and `BatchGet*`. No create, update, delete, or invoke actions are included. Each permission is limited to resources in the account that contains the service-linked role.

For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedAgentResourceScanningServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedAgentResourceScanningServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSWellArchitectedAgentOrganizationsServiceRolePolicy
<a name="security-iam-awsmanpol-AWSWellArchitectedAgentOrganizationsServiceRolePolicy"></a>

This policy is attached to the `` service-linked role in your organization's management account. AWS Well-Architected Agent creates this role when you enable AWS Organizations integration.

This policy grants AWS WA Agent read-only access to your organization structure and delegated administrator information in AWS Organizations. AWS WA Agent uses this access to determine which accounts and organizational units are in scope for organizational profiles and reports. All actions are read-only (`Describe*`, `List*`).

For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedAgentOrganizationsServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedAgentOrganizationsServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS Well-Architected policy updates
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Well-Architected since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed in [Release notes](release-notes.md).


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSWellArchitectedAgentOrganizationsServiceRolePolicy](#security-iam-awsmanpol-AWSWellArchitectedAgentOrganizationsServiceRolePolicy) – New policy | AWS Well-Architected Agent added a new service-linked role policy that grants read-only access to your organization structure for organizational profiles and reports.  | November 16, 2026 | 
| [AWSWellArchitectedAgentResourceScanningServiceRolePolicy](#security-iam-awsmanpol-AWSWellArchitectedAgentResourceScanningServiceRolePolicy) – New policy | AWS Well-Architected Agent added a new service-linked role policy that grants read-only access to your organization structure for organizational profiles and reports.  | November 16, 2026 | 
| [WellArchitectedAgentResourceScanning](#security-iam-awsmanpol-WellArchitectedAgentResourceScanning) – New policy | AWS Well-Architected Agent added a new service-linked role policy that grants read-only access to resource configurations in each account of your organization for recommendation generation. | October 1, 2026 | 
| [WellArchitectedConsoleFullAccess](#security-iam-awsmanpol-WellArchitectedConsoleFullAccess) – Updated policy | Updated to include permissions for AWS Well-Architected Agent, including AWS Organizations delegated administrator management, IAM role and policy creation for execution role setup, and `iam:PassRole` for Well-Architected and Agent service principals. | October 1, 2026 | 
| [WellArchitectedConsoleReadOnlyAccess](#security-iam-awsmanpol-WellArchitectedConsoleReadOnlyAccess) – Updated policy | Updated to include read-only permissions for AWS Well-Architected Agent, including AWS Organizations organization visibility and AWS Trusted Advisor read access. | October 1, 2026 | 
| AWS Well-Architected started tracking policy changes | AWS Well-Architected started tracking changes for its AWS managed policies. | October 1, 2026 | 
| AWS WA Tool changed managed policy | Added `"wellarchitected:Export*"` to ` WellArchitectedConsoleReadOnlyAccess`. | June 22, 2023 | 
| AWS WA Tool added service role policy | Added `AWSWellArchitectedDiscoveryServiceRolePolicy` to allow AWS Well-Architected Tool to access AWS services and resources that relate to AWS WA Tool resources. | May 3, 2023 | 
| AWS WA Tool added permissions | Added a new action to grant `ListAWSServiceAccessForOrganization` to allow AWS WA Tool to check if the AWS service access is enabled for AWS WA Tool. | July 22, 2022 | 
| AWS WA Tool started tracking changes | AWS WA Tool started tracking changes for its AWS managed policies. | July 22, 2022 | 