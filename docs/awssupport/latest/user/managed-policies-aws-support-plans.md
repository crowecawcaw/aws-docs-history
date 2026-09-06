

# AWS managed policies for AWS Support Plans
<a name="managed-policies-aws-support-plans"></a>

AWS Support Plans has the following managed policies.

**Contents**
+ [AWS managed policy: AWSSupportPlansFullAccess](#support-plan-full-access-managed-policy)
+ [AWS managed policy: AWSSupportPlansReadOnlyAccess](#support-plan-read-only-access-managed-policy)
+ [AWS managed policy: AWSSupportPlansServiceRolePolicy](#support-plans-service-role-policy-managed-policy)
+ [AWS Support Plans updates to AWS managed policies](#security-iam-awsmanpol-updates-support-plans)

## AWS managed policy: AWSSupportPlansFullAccess
<a name="support-plan-full-access-managed-policy"></a>

AWS Support Plans uses the [AWSSupportPlansFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansFullAccess$jsonEditor) AWS managed policy. The IAM entity uses this policy to complete the following Support Plans actions for you:
+ View your support plan for your AWS account
+ View details about the status for a request to change your support plan
+ Change the support plan for your AWS account
+ Create support plan schedules for your AWS account
+ View a list of all support plan modifiers for your AWS account
+ Accept a support agreement for your AWS account
+ Cancel a support agreement for your AWS account
+ Create a support agreement for your AWS account
+ View a support agreement for your AWS account
+ View a list of support agreements for your AWS account
+ View a list of support agreement revisions for your AWS account
+ Reject a support agreement for your AWS account
+ Update a support agreement for your AWS account
+ Create the AWS Support Plans service-linked role for your AWS account
+ View the AWS Support Plans service-linked role for your AWS account

To view the permissions for this policy, see [AWSSupportPlansFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSupportPlansFullAccess.html) in the *AWS Managed Policy Reference*.

For a list of changes to the policies, see [AWS Support Plans updates to AWS managed policies](#security-iam-awsmanpol-updates-support-plans).

## AWS managed policy: AWSSupportPlansReadOnlyAccess
<a name="support-plan-read-only-access-managed-policy"></a>

AWS Support Plans uses the [AWSSupportPlansReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansReadOnlyAccess$jsonEditor) AWS managed policy. The IAM entity uses this policy to complete the following read-only Support Plans actions for you:
+ View your support plan for your AWS account
+ View details about the status for a request to change your support plan
+ View a list of all support plan modifiers for your AWS account
+ View a support agreement for your AWS account
+ View a list of support agreements for your AWS account
+ View a list of support agreement revisions for your AWS account

To view the permissions for this policy, see [AWSSupportPlansReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSupportPlansReadOnlyAccess.html) in the *AWS Managed Policy Reference*.

For a list of changes to the policies, see [AWS Support Plans updates to AWS managed policies](#security-iam-awsmanpol-updates-support-plans).

## AWS managed policy: AWSSupportPlansServiceRolePolicy
<a name="support-plans-service-role-policy-managed-policy"></a>

This policy is attached to the `AWSServiceRoleForSupportPlans` service-linked role and allows Support Plans to read and update AWS resources used to manage your account's support plan on your behalf. You can't attach this policy to your IAM entities. For more information, see [Using service-linked roles for AWS Support Plans](using-service-linked-roles-sup-plans.md).

To view the permissions for this policy, see [AWSSupportPlansServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSupportPlansServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS Support Plans updates to AWS managed policies
<a name="security-iam-awsmanpol-updates-support-plans"></a>



View details about updates to AWS managed policies for Support Plans since these services began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document history](History.md) page.



The following table describes important updates to the Support Plans managed policies since September 29, 2022.


**AWS Support**  

| Change | Description | Date | 
| --- | --- | --- | 
| [AWSSupportPlansReadOnlyAccess](#support-plan-read-only-access-managed-policy) - Update to an existing policy<br />[AWSSupportPlansFullAccess](#support-plan-full-access-managed-policy) - Update to an existing policy | Added support agreement actions to the `AWSSupportPlansFullAccess` and `AWSSupportPlansReadOnlyAccess` managed policies. Also added service-linked role actions to the `AWSSupportPlansFullAccess` managed policy. | August 27, 2026 | 
| [AWSSupportPlansReadOnlyAccess](#support-plan-read-only-access-managed-policy) - Update to an existing policy<br />[AWSSupportPlansFullAccess](#support-plan-full-access-managed-policy) - Update to an existing policy | Add ListSupportPlanModifiers action to AWSSupportPlansFullAccess and AWSSupportPlansReadOnlyAccess managed policies. | September 9, 2024 | 
| [AWSSupportPlansFullAccess](#support-plan-full-access-managed-policy) - Update to an existing policy | Add CreateSupportPlanSchedule action to AWSSupportPlansFullAccess managed policy.  | May 8, 2023 | 
| Change log published | Change log for the Support Plans managed policies. | September 29, 2022 | 