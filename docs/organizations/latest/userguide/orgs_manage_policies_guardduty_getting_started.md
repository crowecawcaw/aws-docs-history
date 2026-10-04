

# Getting started with Amazon GuardDuty policies
<a name="orgs_manage_policies_guardduty_getting_started"></a>

Before you configure Amazon GuardDuty policies, ensure you understand the prerequisites and implementation requirements. This topic guides you through the process of setting up and managing these policies in your organization.

## Learn about required permissions
<a name="guardduty_getting_started-permissions"></a>

To enable or attach Amazon GuardDuty policies, you must have the following permissions in the management account:
+ `organizations:EnableAWSServiceAccess` for `guardduty.amazonaws.com`
+ `organizations:RegisterDelegatedAdministrator` for `guardduty.amazonaws.com`
+ `organizations:AttachPolicy`, `organizations:CreatePolicy`, and `organizations:DescribeEffectivePolicy`
+ `guardduty:EnableOrganizationAdminAccount` (for the management account)
+ `guardduty:CreateDetector` (for the management account)

## Before you begin
<a name="guardduty_getting_started-before-begin"></a>

Review the following requirements before implementing Amazon GuardDuty policies:
+ Your account must be part of an AWS organization.
+ You must be signed in as either:
  + The management account for the organization
  + An AWS Organizations delegated administrator with permissions to manage Amazon GuardDuty policies
+ You must enable trusted access for Amazon GuardDuty in your organization.
+ You must enable the Amazon GuardDuty policy type in the root of your organization.

Additionally, verify that:
+ Amazon GuardDuty is supported in the Regions where you want to apply policies.
+ You have the `AWSServiceRoleForAmazonGuardDuty` service-linked role configured in your management account. To verify this role exists, run `aws iam get-role --role-name AWSServiceRoleForAmazonGuardDuty`. If you need to create this role, you can either run `aws guardduty create-detector --enable` in any Region from your management account, or create it directly by running `aws iam create-service-linked-role --aws-service-name guardduty.amazonaws.com`.

## Implementation steps
<a name="guardduty_getting_started-implementation"></a>

To implement Amazon GuardDuty policies effectively, follow these steps in sequence. The management account or delegated administrator can perform these steps through the AWS Organizations console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

1. [Enable trusted access for Amazon GuardDuty](orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access).

1. [Enable Amazon GuardDuty policies for your organization](enable-policy-type.md).

1. [Create an Amazon GuardDuty policy](#create-guardduty-policy-procedure).

1. [Attach the Amazon GuardDuty policy to your organization's root, OU, or account](orgs_policies_attach.md).

1. [View the combined effective Amazon GuardDuty policy that applies to an account](orgs_manage_policies_effective.md).

For all of these steps, you sign in as an AWS Identity and Access Management (IAM) user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization's management account.

## Create an Amazon GuardDuty policy
<a name="create-guardduty-policy-procedure"></a>

**Minimum permissions**  
To create an Amazon GuardDuty policy, you need permission to run the following action:  
`organizations:CreatePolicy`

------
#### [ AWS Management Console ]

**To create an Amazon GuardDuty policy**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. Set a delegated administrator (recommended) for the service in use within the Amazon GuardDuty console.

1. Once the delegated administrator has been set up for Amazon GuardDuty, visit the AWS Organizations console to set up the policies. On the **[Amazon GuardDuty policies](https://console.aws.amazon.com/organizations/v2/home/policies/guardduty-policy)** page, choose **Create policy**.

1. On the **Create new Amazon GuardDuty policy** page, enter a **Policy name** and an optional **Policy description**.

1. (Optional) You can add one or more tags to the policy by choosing **Add tag** and then entering a key and an optional value. Leaving the value blank sets it to an empty string; it isn't `null`. You can attach up to 50 tags to a policy. For more information, see [Tagging AWS Organizations resources](orgs_tagging.md).

1. Enter or paste the policy text in the JSON code box. For information about the Amazon GuardDuty policy syntax, and example policies you can use as a starting point, see [Amazon GuardDuty policy syntax and examples](orgs_manage_policies_guardduty_syntax.md).

1. When you're finished editing your policy, choose **Create policy** at the lower-right corner of the page.

------

**Other information**
+ [Learn policy syntax for Amazon GuardDuty policies and see policy examples](orgs_manage_policies_guardduty_syntax.md)