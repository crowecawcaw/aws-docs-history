# AWS managed policies for AWS Organizations

This section identifies the AWS-managed policies provided for your use to manage your
organization. You can't modify or delete an AWS managed policy, but you can attach or
detach them to entities in your organization as needed.

## AWS Organizations managed policies for use with

AWS Identity and Access Management (IAM)

An IAM managed policy is provided and maintained by AWS. A managed policy provides
permissions for common tasks that you can assign to your users by attaching the managed
policy to the appropriate IAM user or role object. You don't have to write the policy
yourself, and when AWS updates the policy as appropriate to support new services, you
automatically and immediately get the benefit of the update.

You can see the list of
AWS managed policies in [Policies](https://console.aws.amazon.com/iam/home?#/policies "https://console.aws.amazon.com/iam/home?#/policies") page on the IAM console. Use the **Filter
policies** drop-down to select **AWS managed**.

You can use the following managed policies to grant permissions to users in your
organization.

### AWS managed policy: AWSOrganizationsFullAccess

Provides all of the permissions required to create and fully
administer an organization.

View the policy: [`AWSOrganizationsFullAccess`](../../../aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.md "../../../aws-managed-policy/latest/reference/AWSOrganizationsFullAccess.md").

### AWS managed policy: AWSOrganizationsReadOnlyAccess

Provides read only access to information about the organization. It
doesn't permit the user to make any changes.

View the policy:
[`AWSOrganizationsReadOnlyAccess`](../../../aws-managed-policy/latest/reference/AWSOrganizationsReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSOrganizationsReadOnlyAccess.md").

### AWS managed policy: DeclarativePoliciesEC2Report

This policy is used by the [AWSServiceRoleForDeclarativePoliciesEC2Report](orgs_integrate_services.md#ec2-report-policy "orgs_integrate_services.md#ec2-report-policy") service-linked role
to enable it to describe account attribute states for member accounts.

View the policy: [DeclarativePoliciesEC2Report](../../../aws-managed-policy/latest/reference/DeclarativePoliciesEC2Report.md "../../../aws-managed-policy/latest/reference/DeclarativePoliciesEC2Report.md").

## Updates to Organizations AWS managed

policies

The following table details updates to AWS managed policies since this service
began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the [Document
History](document-history.md "document-history.md") page.

| Change                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                 | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor") – updated to allow<br>account API permissions required to view or modify an account name<br>via the Organizations console.                  | Added the `account:GetAccountInformation` action to<br>enable access to view the account name of any account in an<br>organization and the `account:PutAccountName` action to<br>enable access to modify any account name in an organization.                                               | April 22, 2025    |
| [DeclarativePoliciesEC2Report](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/DeclarativePoliciesEC2Report$jsonEditor "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/DeclarativePoliciesEC2Report$jsonEditor") – New managed policy                                                                                                                | Added the `DeclarativePoliciesEC2Report` policy to enable the functionality of the `AWSServiceRoleForDeclarativePoliciesEC2Report` service-linked role.                                                                                                                                     | November 22, 2024 |
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor") – updated to<br>allow account API permissions required to view a root user email address.                                     | Added the `account:GetPrimaryEmail` action to<br>enable access to view the root user email address for any member<br>account in an organization and the<br>`account:GetRegionOptStatus`action to enable<br>access to view the enabled Regions for any member account in an<br>organization. | June 6, 2024      |
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor") – updated to<br>include `Sid` elements that describe the policy<br>statement.                                                               | Added `Sid` elements for the `AWSOrganizationsFullAccess` managed policy.                                                                                                                                                                                                                   | February 6, 2024  |
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor") – updated to<br>include `Sid` elements that describe the policy<br>statement.                                                 | Added `Sid` elements for the<br>`AWSOrganizationsReadOnlyAccess` managed<br>policy.                                                                                                                                                                                                         | February 6, 2024  |
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor") – updated to<br>allow account API permissions required to enable or disable<br>AWS Regions via the Organizations console.                   | Added the `account:ListRegions`,<br>`account:EnableRegion` and<br>`account:DisableRegion` action to the policy to<br>enable write access to enable or disable Regions for an<br>account.                                                                                                    | December 22, 2022 |
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor") – updated to<br>allow account API permissions required to list AWS Regions via<br>the Organizations console.                  | Added the `account:ListRegions` action to the<br>policy to enable access to view Regions for an account.                                                                                                                                                                                    | December 22, 2022 |
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor") – updated to<br>allow account API permissions required to add or edit account<br>contacts via the Organizations console.                    | Added the `account:GetContactInformation` and<br>`account:PutContactInformation` action to the<br>policy to enable write access to modify contacts for an<br>account.                                                                                                                       | October 21, 2022  |
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor") – updated to<br>allow account API permissions required to view account contacts<br>via the Organizations console.             | Added the `account:GetContactInformation`<br>action to the policy to enable access to view contacts for an<br>account.                                                                                                                                                                      | October 21, 2022  |
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor") – updated to<br>allow creating an organization.                                                                                             | Added the `CreateServiceLinkedRole` permission<br>to the policy to enable creating the service linked role<br>required to create an organization. The permission is restricted<br>to creating a role that can be used only by the<br>`organizations.amazonaws.com` service.                 | August 24, 2022   |
| [AWSOrganizationsFullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsFullAccess$jsonEditor") – updated to<br>allow account API permissions required to add, edit, or delete<br>account alternate contacts via the Organizations console. | Added the `account:GetAlternateContact`,<br>`account:DeleteAlternateContact`,<br>`account:PutAlternateContact` actions to the<br>policy to enable write access to modify alternate contacts for<br>an account.                                                                              | February 7, 2022  |
| [AWSOrganizationsReadOnlyAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSOrganizationsReadOnlyAccess$jsonEditor") – updated to<br>allow account API permissions required to view account alternate<br>contacts via the Organizations console.   | Added the `account:GetAlternateContact` action<br>to the policy to enable access to view alternate contacts for an<br>account.                                                                                                                                                              | February 7, 2022  |

## AWS managed authorization

policies

[Authorization policies](orgs_manage_policies_authorization_policies.md "orgs_manage_policies_authorization_policies.md") are
similar to IAM permission policies, but are a feature of AWS Organizations rather than IAM.
You use authorization policies to centrally configure and manage access for principals and resources in your member accounts.

You can see the list of
policies in your organization on the [Policies](https://console.aws.amazon.com/organizations/?#/policies "https://console.aws.amazon.com/organizations/?#/policies") page on the Organizations console.

| Policy name                                                                                                                                                                                                                             | Description                       | ARN                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ---------------------------------------------------------------------------- |
| [FullAWSAccess](https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy/p-FullAWSAccess "https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy/p-FullAWSAccess")            | Allows access to every operation. | arn:aws:organizations::aws:policy/service_control_policy/p-FullAWSAccess     |
| [RCPFullAWSAccess](https://console.aws.amazon.com/organizations/v2/home/policies/resource-control-policy/p-RCPFullAWSAccess "https://console.aws.amazon.com/organizations/v2/home/policies/resource-control-policy/p-RCPFullAWSAccess") | Allows access to every resource.  | arn:aws:organizations::aws:policy/resource_control_policy/p-RCPFullAWSAccess |
