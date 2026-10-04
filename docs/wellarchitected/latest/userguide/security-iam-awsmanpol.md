

AWS Well-Architected Agent is in preview release and is subject to change.

# AWS managed policies for AWS Well-Architected
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: WellArchitectedConsoleFullAccess
<a name="security-iam-awsmanpol-WellArchitectedConsoleFullAccess"></a>

You can attach the `WellArchitectedConsoleFullAccess` policy to your IAM identities.

This policy grants full access to AWS Well-Architected, including the Well-Architected Tool for workload reviews and lens management, and AWS Well-Architected Agent for automated architecture analysis. Includes permissions for AWS Organizations delegated administrator management, AWS Trusted Advisor data access, service-linked role management for Well-Architected service principals, IAM role and policy creation scoped to `service-role/*` for console-guided execution role setup, and `iam:PassRole` conditioned to Well-Architected and Agent service principals. 

For more details about this policy, including the full JSON policy document, see [WellArchitectedConsoleFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedConsoleFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: WellArchitectedConsoleReadOnlyAccess
<a name="security-iam-awsmanpol-WellArchitectedConsoleReadOnlyAccess"></a>

You can attach the `WellArchitectedConsoleReadOnlyAccess` policy to your IAM identities.

This policy grants read-only access to AWS Well-Architected, including the Well-Architected Tool for viewing workloads and lenses, and AWS Well-Architected Agent for viewing architecture analysis results. Includes read-only permissions for AWS Organizations organization structure visibility and AWS Trusted Advisor data access. 

For more details about this policy, including the full JSON policy document, see [WellArchitectedConsoleReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedConsoleReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: WellArchitectedAgentResourceScanning
<a name="security-iam-awsmanpol-WellArchitectedAgentResourceScanning"></a>

You can attach the `WellArchitectedAgentResourceScanning` policy to the access roles in your workload accounts that AWS Well-Architected Agent analyzes.

This policy grants AWS WA Agent read-only access to AWS resource configurations, security settings, and operational data across your accounts to generate optimization recommendations. The policy provides broad read-only access because AWS WA Agent must evaluate cross-service configurations holistically. All actions are read-only (`Get*`, `Describe*`, `List*`, `BatchGet*`). No create, update, delete, or invoke actions are included.

For more details about this policy, including the full JSON policy document, see [WellArchitectedAgentResourceScanning](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/WellArchitectedAgentResourceScanning.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSWellArchitectedOrganizationsServiceRolePolicy
<a name="security-iam-awsmanpol-AWSWellArchitectedOrganizationsServiceRolePolicy"></a>

You can attach the `AWSWellArchitectedOrganizationsServiceRolePolicy` policy to your IAM identities.

This policy grants administrative permissions in AWS Organizations that are required to support AWS Well-Architected Tool integration with Organizations. These permissions allow the organization management account to enable resource sharing with AWS WA Tool. 

**Permissions details**

This policy includes the following permissions.
+ `organizations:ListAWSServiceAccessForOrganization` – Allows principals to check if the AWS service access is enabled for AWS WA Tool. 
+ `organizations:DescribeAccount` – Allows principals to retrieve information about an account in the organization.
+ `organizations:DescribeOrganization` – Allows principals to retrieve information about the organization configuration.
+ `organizations:ListAccounts` – Allows principals to retrieve the list of accounts that belong to an organization.
+ `organizations:ListAccountsForParent` – Allows principals to retrieve the list of accounts that belong to an organization from a given root node in the organization.
+ `organizations:ListChildren` – Allows principals to retrieve the list of accounts and organization units that belong to an organization from a given root node in the organization.
+ `organizations:ListParents` – Allows principals to retrieve the list of immediate parents specified by the OU or account within an organization.
+ `organizations:ListRoots` – Allows principals to retrieve the list of all root nodes within an organization.

For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedOrganizationsServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedOrganizationsServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSWellArchitectedDiscoveryServiceRolePolicy
<a name="security-iam-awsmanpol-AWSWellArchitectedDiscoveryServiceRolePolicy"></a>

You can attach the `AWSWellArchitectedDiscoveryServiceRolePolicy` policy to your IAM identities.

This policy allows AWS Well-Architected Tool to access AWS services and resources that relate to AWS WA Tool resources. 

**Permissions details**

This policy includes the following permissions.
+ `trustedadvisor:DescribeChecks` – Lists Trusted Advisor checks available. 
+ `trustedadvisor:DescribeCheckItems` – Fetches Trusted Advisor check data, including status and resources flagged by Trusted Advisor.
+ `servicecatalog:GetApplication` – Fetches details of an AppRegistry application.
+ `servicecatalog:ListAssociatedResources` –Lists resources associated with an AppRegistry application. 
+ `cloudformation:DescribeStacks` –Gets details of CloudFormation stacks.
+ `cloudformation:ListStackResources` –Lists resources associated with the CloudFormation stacks. 
+ `resource-groups:ListGroupResources` –Lists resources from a ResourceGroup. 
+ `tag:GetResources` – Required for ListGroupResources.
+ `servicecatalog:CreateAttributeGroup` – Creates a service-managed attribute group when required.
+ `servicecatalog:AssociateAttributeGroup` – Associates a service-managed attribute group with an AppRegistry application.
+ `servicecatalog:UpdateAttributeGroup` – Updates a service-managed attribute group.
+ `servicecatalog:DisassociateAttributeGroup` –Disassociates a service-managed attribute group from an AppRegistry application.
+ `servicecatalog:DeleteAttributeGroup` – Deletes a service-managed attribute group when required.

For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedDiscoveryServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedDiscoveryServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS Well-Architected policy updates
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Well-Architected since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed in [Release notes](release-notes.md).


| Change | Description | Date | 
| --- | --- | --- | 
| [WellArchitectedAgentResourceScanning](#security-iam-awsmanpol-WellArchitectedAgentResourceScanning) – New policy | AWS Well-Architected Agent added a new managed policy for resource scanning access roles. This policy grants read-only access to resource configurations across your AWS accounts for optimization recommendation generation. | July 17, 2025 | 
| [WellArchitectedConsoleFullAccess](#security-iam-awsmanpol-WellArchitectedConsoleFullAccess) – Updated policy | Updated to include permissions for AWS Well-Architected Agent, including AWS Organizations delegated administrator management, IAM role and policy creation for execution role setup, and `iam:PassRole` for Well-Architected and Agent service principals. | July 17, 2025 | 
| [WellArchitectedConsoleReadOnlyAccess](#security-iam-awsmanpol-WellArchitectedConsoleReadOnlyAccess) – Updated policy | Updated to include read-only permissions for AWS Well-Architected Agent, including AWS Organizations organization visibility and AWS Trusted Advisor read access. | July 17, 2025 | 
| AWS Well-Architected started tracking policy changes | AWS Well-Architected started tracking changes for its AWS managed policies. | July 17, 2025 | 
| AWS WA Tool changed managed policy | Added `"wellarchitected:Export*"` to ` WellArchitectedConsoleReadOnlyAccess`. | June 22, 2023 | 
| AWS WA Tool added service role policy | Added `AWSWellArchitectedDiscoveryServiceRolePolicy` to allow AWS Well-Architected Tool to access AWS services and resources that relate to AWS WA Tool resources. | May 3, 2023 | 
| AWS WA Tool added permissions | Added a new action to grant `ListAWSServiceAccessForOrganization` to allow AWS WA Tool to check if the AWS service access is enabled for AWS WA Tool. | July 22, 2022 | 
| AWS WA Tool started tracking changes | AWS WA Tool started tracking changes for its AWS managed policies. | July 22, 2022 | 