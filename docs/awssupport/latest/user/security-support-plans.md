# Manage access to AWS Support Plans

###### Topics

- [Permissions for the Support Plans
  console](#using-the-trusted-advisor-console "#using-the-trusted-advisor-console")
- [Support Plans actions](#support-plans-actions "#support-plans-actions")
- [Example IAM policies for
  Support Plans](#support-plans-policies "#support-plans-policies")
- [Troubleshooting](#troubleshooting-changing-support-plans "#troubleshooting-changing-support-plans")

## Permissions for the Support Plans

console

To access the Support Plans console, a user must have a minimum set of permissions. These
permissions must allow the user to list and view details about the Support Plans resources
in your AWS account.

You can create an AWS Identity and Access Management (IAM) policy with the `supportplans`
namespace. You can use this policy to specify permissions for actions and
resources.

When you create a policy, you can specify the namespace of the service to allow or
deny an action. The namespace for Support Plans is `supportplans`.

You can use AWS managed policies and attach them to your IAM entities. For more
information, see [AWS managed policies for
AWS Support Plans](managed-policies-aws-support-plans.md "managed-policies-aws-support-plans.md").

## Support Plans actions

You can perform the following Support Plans actions in the console. You can also specify
these Support Plans actions in an IAM policy to allow or deny specific actions.

| Action                       | Description                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------- |
| `GetSupportPlan`             | Grants permission to view details about the current support plan<br>for this AWS account.     |
| `GetSupportPlanUpdateStatus` | Grants permission to view details about the status for a request<br>to update a support plan. |
| `StartSupportPlanUpdate`     | Grants permission to start the request to update the support plan<br>for this AWS account.    |
| `CreateSupportPlanSchedule`  | Grants permission to create support plan schedules for this<br>AWS account.                   |
| `ListSupportPlanModifiers`   | Grants permission to view a list of all support plan modifiers for<br>this AWS account.       |

## Example IAM policies for

Support Plans

You can use the following example policies to manage access to Support Plans.

### Full access to

Support Plans

The following policy allows users full access to Support Plans.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "supportplans:*",
 "Resource": "*"
 }
 ]
}`

```

### Read-only access to

Support Plans

The following policy allows read-only access to Support Plans.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "supportplans:Get*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "supportplans:List*",
 "Resource": "*"
 }
 ]
}`

```

### Deny access to Support Plans

The following policy doesn't allow users access to Support Plans.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "supportplans:*",
 "Resource": "*"
 }
 ]
}`

```

## Troubleshooting

See the following topics to manage access to Support Plans.

### When I try to view or change my support

plan, the Support Plans console says that I'm missing the
`GetSupportPlan` permission

IAM users must have the required permissions to access the Support Plans console.
You can update your IAM policy to include the missing permission or use an AWS
managed policy, such as AWSSupportPlansFullAccess or
AWSSupportPlansReadOnlyAccess. For more information, see [AWS managed policies for
AWS Support Plans](managed-policies-aws-support-plans.md "managed-policies-aws-support-plans.md").

If you don't have access to update your IAM policies, contact your AWS account
administrator.

#### Related

information

For more information, see the following topics in the
_IAM User Guide_:

- [Testing IAM policies with the IAM policy
  simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md")
- [Troubleshooting access denied error
  messages](../../../IAM/latest/UserGuide/troubleshoot_access-denied.md "../../../IAM/latest/UserGuide/troubleshoot_access-denied.md")

### I have the correct Support Plans

permissions, but I still get the same error

If your AWS account is a member account that's part of AWS Organizations, the service
control policy (SCP) might need to be updated. SCPs are a type of policy that
manages permissions in an organization.

Because Support Plans is a _global_ service, policies that restrict
AWS Regions might prevent member accounts from viewing or changing their support
plan. To allow global services for your organization, such as IAM and Support Plans,
you must add the service to the exclusion list in any applicable SCP. This means
that accounts in the organization can access these services, even if the SCP denies
a specified AWS Region.

To add Support Plans as an exception, enter `"supportplans:*"` to the
`"NotAction"` list in the SCP.

```
"supportplans:*",
```

Your SCP might appear as the following policy snippet.

###### Example: SCP that allows Support Plans access in an organization

```
{ "Version": "2012-10-17",
   "Statement": [
     { "Sid":  "GRREGIONDENY",
       "Effect":  "Deny",
       "NotAction": [
         "aws-portal:*",
         "budgets:*",
         "chime:*"
         "iam:*",
         "supportplans:*",
         ....
```

If you have a member account and can't update the SCP, contact your AWS account
administrator. The management account might need to update the SCP so that all member
accounts can access Support Plans.

###### Notes for AWS Control Tower

- If your organization uses an SCP with AWS Control Tower, you can update the
  **Deny access to AWS based on the requested
  AWS Region** control (commonly referred to as the Region
  deny control).
- If you update the SCP for AWS Control Tower to allow
  `supportplans`, repairing the drift will remove your
  update to the SCP. For more information, see [Detect and resolve drift in AWS Control Tower](../../../controltower/latest/userguide/drift.md "../../../controltower/latest/userguide/drift.md").

#### Related information

For more information, see the following topics:

- [Service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the
  _AWS Organizations User Guide._
- [Configure the
  Region deny control](../../../controltower/latest/userguide/region-deny.md "../../../controltower/latest/userguide/region-deny.md") in the _AWS Control Tower User
  Guide_
- [Deny access to AWS based on the requested
  AWS Region](../../../controltower/latest/userguide/data-residency-controls.md#primary-region-deny-policy "../../../controltower/latest/userguide/data-residency-controls.md#primary-region-deny-policy") in the _AWS Control Tower User
  Guide_
