

# AWS managed policies for AWS Organizations
<a name="orgs_reference_available-policies"></a>

This section identifies the AWS-managed policies provided for your use to manage your organization. You can't modify or delete an AWS managed policy, but you can attach or detach them to entities in your organization as needed.

## AWS Organizations managed policies for use with AWS Identity and Access Management (IAM)
<a name="ref-iam-managed-policies"></a>

An IAM managed policy is provided and maintained by AWS. A managed policy provides permissions for common tasks that you can assign to your users by attaching the managed policy to the appropriate IAM user or role object. You don't have to write the policy yourself, and when AWS updates the policy as appropriate to support new services, you automatically and immediately get the benefit of the update.

You can see the list of AWS managed policies in [Policies](https://console.aws.amazon.com/iam/home?#/policies) page on the IAM console. Use the **Filter policies** drop-down to select **AWS managed**. 

You can use the following managed policies to grant permissions to users in your organization.

### AWS managed policy: AWSOrganizationsFullAccess
<a name="security-iam-awsmanpol-AWSOrganizationsFullAccess"></a>

Provides all of the permissions required to create and fully administer an organization.

View the policy: [`AWSOrganizationsFullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.html).

### AWS managed policy: AWSOrganizationsReadOnlyAccess
<a name="security-iam-awsmanpol-AWSOrganizationsReadOnlyAccess"></a>

Provides read only access to information about the organization. It doesn't permit the user to make any changes.

View the policy: [`AWSOrganizationsReadOnlyAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSOrganizationsReadOnlyAccess.html).

### AWS managed policy: DeclarativePoliciesEC2Report
<a name="security-iam-awsmanpol-DeclarativePoliciesEC2Report"></a>

This policy is used by the [AWSServiceRoleForDeclarativePoliciesEC2Report](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#ec2-report-policy) service-linked role to enable it to describe account attribute states for member accounts.

View the policy: [DeclarativePoliciesEC2Report](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/DeclarativePoliciesEC2Report.html).

## Updates to Organizations AWS managed policies
<a name="ref-iam-managed-policies-updates"></a>

The following table details updates to AWS managed policies since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document History](document-history.md) page.



| Change | Description | Date | 
| --- | --- | --- | 
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor) – updated to allow account API permissions required to view or modify an account name via the Organizations console. | Added the `account:GetAccountInformation` action to enable access to view the account name of any account in an organization and the `account:PutAccountName` action to enable access to modify any account name in an organization. | April 22, 2025 | 
| [DeclarativePoliciesEC2Report](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/DeclarativePoliciesEC2Report$jsonEditor) – New managed policy | Added the `DeclarativePoliciesEC2Report` policy to enable the functionality of the `AWSServiceRoleForDeclarativePoliciesEC2Report` service-linked role. | November 22, 2024 | 
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor) – updated to allow account API permissions required to view a root user email address. | Added the `account:GetPrimaryEmail` action to enable access to view the root user email address for any member account in an organization and the `account:GetRegionOptStatus`action to enable access to view the enabled Regions for any member account in an organization. | June 6, 2024 | 
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor) – updated to include `Sid` elements that describe the policy statement. | Added `Sid` elements for the `AWSOrganizationsFullAccess` managed policy. | February 6, 2024 | 
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor) – updated to include `Sid` elements that describe the policy statement. | Added `Sid` elements for the `AWSOrganizationsReadOnlyAccess` managed policy. | February 6, 2024 | 
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor) – updated to allow account API permissions required to enable or disable AWS Regions via the Organizations console. | Added the `account:ListRegions`, `account:EnableRegion` and `account:DisableRegion` action to the policy to enable write access to enable or disable Regions for an account. | December 22, 2022 | 
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor) – updated to allow account API permissions required to list AWS Regions via the Organizations console. | Added the `account:ListRegions` action to the policy to enable access to view Regions for an account. | December 22, 2022 | 
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor) – updated to allow account API permissions required to add or edit account contacts via the Organizations console. | Added the `account:GetContactInformation` and `account:PutContactInformation` action to the policy to enable write access to modify contacts for an account. | October 21, 2022 | 
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor) – updated to allow account API permissions required to view account contacts via the Organizations console. | Added the `account:GetContactInformation` action to the policy to enable access to view contacts for an account. | October 21, 2022 | 
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor) – updated to allow creating an organization. | Added the `CreateServiceLinkedRole` permission to the policy to enable creating the service linked role required to create an organization. The permission is restricted to creating a role that can be used only by the `organizations.amazonaws.com` service. | August 24, 2022 | 
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor) – updated to allow account API permissions required to add, edit, or delete account alternate contacts via the Organizations console. | Added the `account:GetAlternateContact`, `account:DeleteAlternateContact`, `account:PutAlternateContact` actions to the policy to enable write access to modify alternate contacts for an account. | February 7, 2022 | 
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor) – updated to allow account API permissions required to view account alternate contacts via the Organizations console. | Added the `account:GetAlternateContact` action to the policy to enable access to view alternate contacts for an account. | February 7, 2022 | 

## AWS managed authorization policies
<a name="ref-managed-scp-policies"></a>

[Authorization policies](orgs_manage_policies_authorization_policies.md) are similar to IAM permission policies, but are a feature of AWS Organizations rather than IAM. You use authorization policies to centrally configure and manage access for principals and resources in your member accounts.

You can see the list of policies in your organization on the [Policies](https://console.aws.amazon.com/organizations/?#/policies) page on the Organizations console.



| Policy name | Description | ARN | 
| --- | --- | --- | 
| [FullAWSAccess](https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy/p-FullAWSAccess) | Allows access to every operation. | arn:aws:organizations::aws:policy/service\_control\_policy/p-FullAWSAccess | 
| [RCPFullAWSAccess](https://console.aws.amazon.com/organizations/v2/home/policies/resource-control-policy/p-RCPFullAWSAccess) | Allows access to every resource. | arn:aws:organizations::aws:policy/resource\_control\_policy/p-RCPFullAWSAccess | 