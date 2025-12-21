# Getting started with

Security Hub policies

Before you configure Security Hub policies, ensure you understand the prerequisites and
implementation requirements. This topic guides you through the process of setting up and
managing these policies in your organization.

## Before you begin

Review the following requirements before implementing Security Hub policies:

- Your account must be part of an AWS Organizations organization
- You must be signed in as either:
  - The management account for the organization
  - A delegated administrator account with permissions to manage Security Hub
    policies

- You must enable trusted access for Security Hub in your organization
- You must enable the Security Hub policy type in the root of your organization

Additionally, verify that:

- Security Hub is supported in the Regions where you want to apply policies
- You have the `AWSServiceRoleForSecurityHubV2` service-linked role
  configured in your management account. To verify this role exists, run `aws iam get-role --role-name AWSServiceRoleForSecurityHubV2`.
  If you need to create this role, you can either run `aws securityhub 
enable-security-hub-v2` in any Region from your management account, or create it
  directly by running `aws iam create-service-linked-role --aws-service-name 
securityhubv2.amazonaws.com`.

## Implementation

steps

To implement Security Hub policies effectively, follow these steps in sequence. Each step
ensures proper configuration and helps prevent common issues during setup. The
management account or delegated administrator can perform these steps through the
AWS Organizations console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

1. [Enable trusted
   access for Security Hub](orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access "orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access").
2. [Enable
   Security Hub policies for your organization](enable-policy-type.md "enable-policy-type.md").
3. [Create a Security Hub
   policy](orgs_policies_create.md#create-security-hub-policy-procedure "orgs_policies_create.md#create-security-hub-policy-procedure").
4. [Attach the Security Hub policy to your organization's root, OU, or
   account](orgs_policies_attach.md "orgs_policies_attach.md").
5. [View the combined effective
   Security Hub policy that applies to an account](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").

For all of these steps, you sign in as an AWS Identity and Access Management (IAM) user, assume an IAM
role, or sign in as the root user ([not
recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization's management account.

###### Other information

- [Learn policy syntax
  for Security Hub policies and see policy examples](orgs_manage_policies_security_hub_syntax.md "orgs_manage_policies_security_hub_syntax.md")
