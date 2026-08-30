# AWS managed policies for AWS Support Plans

AWS Support Plans has the following managed policies.

###### Contents

- [AWS managed policy: AWSSupportPlansFullAccess](managed-policies-aws-support-plans.md#support-plan-full-access-managed-policy "managed-policies-aws-support-plans.md#support-plan-full-access-managed-policy")
- [AWS managed policy: AWSSupportPlansReadOnlyAccess](managed-policies-aws-support-plans.md#support-plan-read-only-access-managed-policy "managed-policies-aws-support-plans.md#support-plan-read-only-access-managed-policy")
- [AWS managed policy: AWSSupportPlansServiceRolePolicy](managed-policies-aws-support-plans.md#support-plans-service-role-policy-managed-policy "managed-policies-aws-support-plans.md#support-plans-service-role-policy-managed-policy")
- [AWS Support Plans updates to AWS managed policies](managed-policies-aws-support-plans.md#security-iam-awsmanpol-updates-support-plans "managed-policies-aws-support-plans.md#security-iam-awsmanpol-updates-support-plans")

## AWS managed policy: AWSSupportPlansFullAccess

AWS Support Plans uses the [AWSSupportPlansFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansFullAccess$jsonEditor") AWS managed policy. The
IAM entity uses this policy to complete the following Support Plans actions for
you:

- View your support plan for your AWS account
- View details about the status for a request to change your support plan
- Change the support plan for your AWS account
- Create support plan schedules for your AWS account
- View a list of all support plan modifiers for your AWS account
- Accept a support agreement for your AWS account
- Cancel a support agreement for your AWS account
- Create a support agreement for your AWS account
- View a support agreement for your AWS account
- View a list of support agreements for your AWS account
- View a list of support agreement revisions for your AWS account
- Reject a support agreement for your AWS account
- Update a support agreement for your AWS account
- Create the AWS Support Plans service-linked role for your AWS account
- View the AWS Support Plans service-linked role for your AWS account

To view the permissions for this policy, see [AWSSupportPlansFullAccess](../../../aws-managed-policy/latest/reference/AWSSupportPlansFullAccess.md "../../../aws-managed-policy/latest/reference/AWSSupportPlansFullAccess.md") in the _AWS
Managed Policy Reference_.

For a list of changes to the policies, see [AWS Support Plans updates to AWS managed policies](#security-iam-awsmanpol-updates-support-plans "#security-iam-awsmanpol-updates-support-plans").

## AWS managed policy: AWSSupportPlansReadOnlyAccess

AWS Support Plans uses the [AWSSupportPlansReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansReadOnlyAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansReadOnlyAccess$jsonEditor") AWS managed policy. The
IAM entity uses this policy to complete the following read-only Support Plans actions for
you:

- View your support plan for your AWS account
- View details about the status for a request to change your support plan
- View a list of all support plan modifiers for your AWS account
- View a support agreement for your AWS account
- View a list of support agreements for your AWS account
- View a list of support agreement revisions for your AWS account

To view the permissions for this policy, see [AWSSupportPlansReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSSupportPlansReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSSupportPlansReadOnlyAccess.md") in the _AWS
Managed Policy Reference_.

For a list of changes to the policies, see [AWS Support Plans updates to AWS managed policies](#security-iam-awsmanpol-updates-support-plans "#security-iam-awsmanpol-updates-support-plans").

## AWS managed policy: AWSSupportPlansServiceRolePolicy

This policy is attached to the `AWSServiceRoleForSupportPlans`
service-linked role and allows Support Plans to read and update AWS resources used to
manage your account's support plan on your behalf. You can't attach this policy to your
IAM entities. For more information, see [Using service-linked roles for AWS Support Plans](using-service-linked-roles-sup-plans.md "using-service-linked-roles-sup-plans.md").

To view the permissions for this policy, see [AWSSupportPlansServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSSupportPlansServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSSupportPlansServiceRolePolicy.md") in the _AWS
Managed Policy Reference_.

## AWS Support Plans updates to AWS managed policies

View details about updates to AWS managed policies for Support Plans since these
services began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the [Document history](History.md "History.md")
page.

The following table describes important updates to the Support Plans managed policies
since September 29, 2022.

AWS Support| Change | Description | Date |
| --- | --- | --- |
| [AWSSupportPlansReadOnlyAccess](#support-plan-read-only-access-managed-policy "#support-plan-read-only-access-managed-policy")<br>• Update to an existing policy<br>[AWSSupportPlansFullAccess](#support-plan-full-access-managed-policy "#support-plan-full-access-managed-policy") -<br>Update to an existing policy | Added support agreement actions to the<br>`AWSSupportPlansFullAccess` and<br>`AWSSupportPlansReadOnlyAccess` managed policies.<br>Also added service-linked role actions to the<br>`AWSSupportPlansFullAccess` managed policy. | August 27, 2026 |
| [AWSSupportPlansReadOnlyAccess](#support-plan-read-only-access-managed-policy "#support-plan-read-only-access-managed-policy")<br>• Update to an existing policy<br>[AWSSupportPlansFullAccess](#support-plan-full-access-managed-policy "#support-plan-full-access-managed-policy") -<br>Update to an existing policy | Add `ListSupportPlanModifiers` action to<br>`AWSSupportPlansFullAccess` and `AWSSupportPlansReadOnlyAccess` managed<br>policies. | September 9, 2024 |
| [AWSSupportPlansFullAccess](#support-plan-full-access-managed-policy "#support-plan-full-access-managed-policy")<br>• Update to<br>an existing policy | Add `CreateSupportPlanSchedule` action to<br>`AWSSupportPlansFullAccess` managed policy. | May 8, 2023 |
| Change log published | Change log for the Support Plans managed policies. | September 29, 2022 |
