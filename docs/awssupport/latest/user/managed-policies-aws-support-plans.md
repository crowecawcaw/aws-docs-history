# AWS managed policies for

AWS Support Plans

AWS Support Plans has the following managed policies.

###### Contents

- [AWS managed policy:
  AWSSupportPlansFullAccess](managed-policies-aws-support-plans.md#support-plan-full-access-managed-policy "managed-policies-aws-support-plans.md#support-plan-full-access-managed-policy")
- [AWS managed policy:
  AWSSupportPlansReadOnlyAccess](managed-policies-aws-support-plans.md#support-plan-read-only-access-managed-policy "managed-policies-aws-support-plans.md#support-plan-read-only-access-managed-policy")
- [AWS Support Plans updates to
  AWS managed policies](managed-policies-aws-support-plans.md#security-iam-awsmanpol-updates-support-plans "managed-policies-aws-support-plans.md#security-iam-awsmanpol-updates-support-plans")

## AWS managed policy:

AWSSupportPlansFullAccess

AWS Support Plans uses the [AWSSupportPlansFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansFullAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansFullAccess$jsonEditor") AWS managed policy. The
IAM entity uses this policy to complete the following Support Plans actions for
you:

- View your support plan for your AWS account
- View details about the status for a request to change your support plan
- Change the support plan for your AWS account
- Create support plan schedules for your AWS account
- View a list of all support plan modifiers for your AWS account

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "supportplans:GetSupportPlan",
 "supportplans:GetSupportPlanUpdateStatus",
 "supportplans:StartSupportPlanUpdate",
 "supportplans:CreateSupportPlanSchedule",
 "supportplans:ListSupportPlanModifiers"
 ],
 "Resource": "*"
 }
 ]
}`

```

For a list of changes to the policies, see [AWS Support Plans updates to
AWS managed policies](#security-iam-awsmanpol-updates-support-plans "#security-iam-awsmanpol-updates-support-plans").

## AWS managed policy:

AWSSupportPlansReadOnlyAccess

AWS Support Plans uses the [AWSSupportPlansReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansReadOnlyAccess$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSSupportPlansReadOnlyAccess$jsonEditor") AWS managed policy. The
IAM entity uses this policy to complete the following read-only Support Plans actions for
you:

- View your support plan for your AWS account
- View details about the status for a request to change your support plan
- View a list of all support plan modifiers for your AWS account

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "supportplans:GetSupportPlan",
 "supportplans:GetSupportPlanUpdateStatus",
 "supportplans:ListSupportPlanModifiers"
 ],
 "Resource": "*"
 }
 ]
}`

```

For a list of changes to the policies, see [AWS Support Plans updates to
AWS managed policies](#security-iam-awsmanpol-updates-support-plans "#security-iam-awsmanpol-updates-support-plans").

## AWS Support Plans updates to

AWS managed policies

View details about updates to AWS managed policies for Support Plans since these
services began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the [Document history](History.md "History.md")
page.

The following table describes important updates to the Support Plans managed policies
since September 29, 2022.

| AWS Support                                                                                                                                                                                                                                                                                                       | Change                                                                                                                     | Description        | Date |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---- |
| [AWSSupportPlansReadOnlyAccess](#support-plan-read-only-access-managed-policy "#support-plan-read-only-access-managed-policy") <br>• Update to an existing policy [AWSSupportPlansFullAccess](#support-plan-full-access-managed-policy "#support-plan-full-access-managed-policy") - Update to an existing policy | Add `ListSupportPlanModifiers` action to `AWSSupportPlansFullAccess` and `AWSSupportPlansReadOnlyAccess` managed policies. | September 9, 2024  |
| [AWSSupportPlansFullAccess](#support-plan-full-access-managed-policy "#support-plan-full-access-managed-policy") - Update to an existing policy                                                                                                                                                                   | Add `CreateSupportPlanSchedule` action to `AWSSupportPlansFullAccess` managed policy.                                      | May 8, 2023        |
| Change log published                                                                                                                                                                                                                                                                                              | Change log for the Support Plans managed policies.                                                                         | September 29, 2022 |
