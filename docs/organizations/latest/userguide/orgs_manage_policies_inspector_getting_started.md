# Getting started with

Amazon Inspector policies

Before you configure Amazon Inspector policies, ensure you understand the prerequisites and
implementation requirements. This topic guides you through the process of setting up and
managing these policies in your organization.

## Learn about required permissions

To enable or attach Amazon Inspector policies, you must have the following permissions in the management account:

- `organizations:EnableAWSServiceAccess` for `inspector2.amazonaws.com`
- `organizations:RegisterDelegatedAdministrator` for `inspector2.amazonaws.com`
- `organizations:AttachPolicy`, `organizations:CreatePolicy`, `organizations:DescribeEffectivePolicy`
- `inspector2:Enable` (for management account and delegated admin)

## Before you begin

Review the following requirements before implementing Amazon Inspector policies:

- Your account must be part of an AWS organization
- You must be signed in as either:
  - The management account for the organization
  - An AWS Organizations delegated administrator with permissions to manage Amazon Inspector
    policies

- You must enable trusted access for Amazon Inspector in your organization
- You must enable the Amazon Inspector policy type in the root of your organization

Additionally, verify that:

- Amazon Inspector is supported in the Regions where you want to apply policies
- You have the `AWSServiceRoleForInspectorV2` service-linked role
  configured in your management account. To verify this role exists, run `aws iam get-role --role-name AWSServiceRoleForInspectorV2`.
  If you need to create this role, you can either run `aws inspector2 enable` in any Region from your management account, or create it
  directly by running `aws iam create-service-linked-role --aws-service-name 
inspector2.amazonaws.com`.

## Implementation

steps

To implement Amazon Inspector policies effectively, follow these steps in sequence. Each step
ensures proper configuration and helps prevent common issues during setup. The
management account or delegated administrator can perform these steps through the
AWS Organizations console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

1. [Enable trusted
   access for Amazon Inspector](orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access "orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access").
2. [Enable
   Amazon Inspector policies for your organization](enable-policy-type.md "enable-policy-type.md").
3. [Create an Amazon Inspector
   policy](orgs_manage_policies_inspector_syntax.md "orgs_manage_policies_inspector_syntax.md").
4. [Attach the Amazon Inspector policy to your organization's root, OU, or
   account](orgs_policies_attach.md "orgs_policies_attach.md").
5. [View the combined effective
   Amazon Inspector policy that applies to an account](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").

## Create an Amazon Inspector policy

### Minimum permissions

To create an Amazon Inspector policy, you need permission to run the following action:

- `organizations:CreatePolicy`

### AWS Management Console

**To create an Amazon Inspector policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Set a delegated administrator for the service in use within Amazon Inspector console.
3. Once the delegated administrator has been set up for Amazon Inspector, visit AWS organization console to set up the policies. On AWS organization console, visit the Amazon Inspector Policies page, choose **Create policy**.
4. On the **Create new Amazon Inspector policy** page, enter a **Policy name** and an optional **Policy description**.
5. (Optional) You can add one or more tags to the policy by choosing
   **Add tag** and then entering a key and an
   optional value. Leaving the value blank sets it to an empty string;
   it isn't `null`. You can attach up to 50 tags to a
   policy. For more information, see [Tagging AWS Organizations resources](orgs_tagging.md "orgs_tagging.md").
6. Enter or paste the policy text in the JSON code box. For information about the Amazon Inspector policy syntax, and example policies you can use as a starting point, see [Amazon Inspector policy syntax and
   examples](orgs_manage_policies_inspector_syntax.md "orgs_manage_policies_inspector_syntax.md").
7. When you're finished editing your policy, choose **Create policy** at the lower-right corner of the page.
