# AWS Health identity-based

policy examples

By default, IAM users and roles don't have permission to create or modify
AWS Health resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the
  AWS Health console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Accessing the
  AWS Health Dashboard and the AWS Health API](#security_iam_id-based-policy-examples-access-dashboard "#security_iam_id-based-policy-examples-access-dashboard")
- [Resource- and action-based
  conditions](#resource-action-based-conditions "#resource-action-based-conditions")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS Health resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Using the

AWS Health console

To access the AWS Health console, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
AWS Health resources in your AWS account. If you create an identity-based policy
that is more restrictive than the minimum required permissions, the console won't
function as intended for entities (IAM users or roles) with that policy.

To ensure that those entities can still use the AWS Health console, you can
attach the following AWS managed policy, [AWSHealthFullAccess](https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess "https://console.aws.amazon.com//iam/home?#/policies/arn:aws:iam::aws:policy/AWSHealthFullAccess").

The `AWSHealthFullAccess` policy grants an entity full access to the
following:

- Enable or disable the AWS Health organizational view feature for all accounts
  in an AWS organization
- The AWS Health Dashboard in the AWS Health console
- AWS Health API operations and notifications
- View information about accounts that are part of your AWS organization
- View the organizational units (OU) of the management account

###### Example : AWSHealthFullAccess

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess",
 "organizations:DisableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": "health.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "health:*",
 "organizations:DescribeAccount",
 "organizations:ListAccounts",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListParents"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "health.amazonaws.com"
 }
 }
 }
 ]
}`

```

###### Note

You can also use the `Health_OrganizationsServiceRolePolicy` AWS
managed policy, so that AWS Health can view events for other accounts in your
organization. For more information, see [Using service-linked roles for
AWS Health](using-service-linked-roles.md "using-service-linked-roles.md").

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that you're trying to perform.

For more information, see [Adding Permissions to a User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

## Allow users

to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Accessing the

AWS Health Dashboard and the AWS Health API

The AWS Health Dashboard is available for all AWS accounts. The AWS Health API is available only
to accounts with a Business, Enterprise On-Ramp, or Enterprise Support plan. For more information, see [Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

You can use IAM to create entities (users, groups, or roles), and then give those
entities permissions to access the AWS Health Dashboard and the AWS Health API.

By default, IAM users don't have access to the AWS Health Dashboard or the AWS Health API. You
give users access to your account's AWS Health information by attaching IAM policies
to a single user, a group of users, or a role. For more information, see [Identities (Users, Groups, and Roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") and [Overview of IAM Policies](../../../IAM/latest/UserGuide/PoliciesOverview.md "../../../IAM/latest/UserGuide/PoliciesOverview.md").

After you create IAM users, you can give those users individual passwords. Then,
they can sign in to your account and view AWS Health information by using an
account-specific sign-in page. For more information, see [How Users Sign In to Your
Account](../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md "../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md").

###### Note

An IAM user with permissions to view AWS Health Dashboard has read-only access to health
information across all AWS services on the account, which can include, but is not
limited to, AWS resource IDs such as Amazon EC2 instance IDs, EC2 instance IP addresses,
and general security notifications.

For example, if an IAM policy grants access only to AWS Health Dashboard and the AWS Health
API, then the user or role that the policy applies to can access all information
posted about AWS services and related resources, even if other IAM policies don't
allow that access.

You can use two groups of APIs for AWS Health.

- Individual accounts – You can use the operations such as [DescribeEvents](../APIReference/API_DescribeEvents.md "../APIReference/API_DescribeEvents.md") and
  [DescribeEventDetails](../APIReference/API_DescribeEventDetails.md "../APIReference/API_DescribeEventDetails.md") to get information about AWS Health events for
  your account.
- Organizational account – You can use operations such as [DescribeEventsForOrganization](../APIReference/API_DescribeEventsForOrganization.md "../APIReference/API_DescribeEventsForOrganization.md") and [DescribeEventDetailsForOrganization](../APIReference/API_DescribeEventDetailsForOrganization.md "../APIReference/API_DescribeEventDetailsForOrganization.md") to get information about
  AWS Health events for accounts that are part of your organization.

For more information about the available API operations, see the
[AWS Health API Reference](../APIReference.md "../APIReference.md").

### Individual actions

You can set the `Action` element of an IAM policy to
`health:Describe*`. This allows access to the AWS Health Dashboard and AWS Health.
AWS Health supports access control to events based on the `eventTypeCode`
and service.

#### Describe access

This policy statement grants access to AWS Health Dashboard and any of the
`Describe*` AWS Health API operations. For example, an IAM user
with this policy can access the AWS Health Dashboard in the AWS Management Console and call the AWS Health
`DescribeEvents` API operation.

###### Example : Describe access

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "health:Describe*"
 ],
 "Resource": "*"
 }]
}`

```

#### Deny access

This policy statement denies access to AWS Health Dashboard and the AWS Health API. An IAM
user with this policy can't view the AWS Health Dashboard in the AWS Management Console and can't call any of
the AWS Health API operations.

###### Example : Deny access

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "health:*"
 ],
 "Resource": "*"
 }]
}`

```

### Organizational view

If you want to enable organizational view for AWS Health, you must allow access
to the AWS Health and AWS Organizations actions.

The `Action` element of an IAM policy must include the following
permissions:

- `iam:CreateServiceLinkedRole`
- `organizations:EnableAWSServiceAccess`
- `organizations:DescribeAccount`
- `organizations:DisableAWSServiceAccess`
- `organizations:ListAccounts`
- `organizations:ListDelegatedAdministrators`
- `organizations:ListParents`

To understand the exact permissions needed for each APIs, see [Actions Defined by AWS Health APIs and Notifications](../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-actions-as-permissions "../../../IAM/latest/UserGuide/list_awshealthapisandnotifications.md#awshealthapisandnotifications-actions-as-permissions") in the
_IAM User Guide_.

###### Note

You must use credentials from the management account for an organization to
access the AWS Health APIs for AWS Organizations. For more information, see [Aggregating AWS Health events across accounts](aggregate-events.md "aggregate-events.md").

#### Allow access to AWS Health

organizational view

This policy statement grants access to all AWS Health and AWS Organizations actions
that you need for the organizational view feature.

###### Example : Allow AWS Health organizational view access

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess",
 "organizations:DisableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": "health.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "health:*",
 "organizations:DescribeAccount",
 "organizations:ListAccounts",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListParents"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/health.amazonaws.com/AWSServiceRoleForHealth*"
 }
 ]
}`

```

#### Deny access to AWS Health

organizational view

This policy statement denies access to the AWS Organizations actions but allows access
to the AWS Health actions for an individual account.

###### Example : Deny AWS Health organizational view access

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "health:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "organizations:EnableAWSServiceAccess",
 "organizations:DisableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": "health.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "organizations:DescribeAccount",
 "organizations:ListAccounts",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListParents"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/health.amazonaws.com/AWSServiceRoleForHealth*"
 }
 ]
}`

```

###### Note

If the user or group that you want to give permissions to already has an IAM
policy, you can add the AWS Health-specific policy statement to that
policy.

## Resource- and action-based

conditions

AWS Health supports [IAM conditions](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md") for the [DescribeAffectedEntities](../APIReference/API_DescribeAffectedEntities.md "../APIReference/API_DescribeAffectedEntities.md") and [DescribeEventDetails](../APIReference/API_DescribeEventDetails.md "../APIReference/API_DescribeEventDetails.md") API operations. You can use resource- and action-based
conditions to restrict events that the AWS Health API sends to a user, group, or role.

To do so, update the `Condition` block of the IAM policy or set the
`Resource` element. You can use [String Conditions](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_String") to restrict access based on certain AWS Health event
fields.

You can use the following fields when you specify an AWS Health event in your
policy:

- `eventTypeCode`
- `service`

###### Notes

- The [DescribeAffectedEntities](../APIReference/API_DescribeAffectedEntities.md "../APIReference/API_DescribeAffectedEntities.md") and [DescribeEventDetails](../APIReference/API_DescribeEventDetails.md "../APIReference/API_DescribeEventDetails.md") API operations support resource-level
  permissions. For example, you can create a policy to allow or deny specific
  AWS Health events.
- The [DescribeAffectedEntitiesForOrganization](../APIReference/API_DescribeAffectedEntitiesForOrganization.md "../APIReference/API_DescribeAffectedEntitiesForOrganization.md") and [DescribeEventDetailsForOrganization](../APIReference/API_DescribeEventDetailsForOrganization.md "../APIReference/API_DescribeEventDetailsForOrganization.md") API operations don't support
  resource-level permissions.
- For more information, see [Actions, resources, and condition keys for AWS Health APIs and
  Notifications](../../../service-authorization/latest/reference/list_awshealthapisandnotifications.md "../../../service-authorization/latest/reference/list_awshealthapisandnotifications.md") in the _Service Authorization Reference_.

###### Example : Action-based condition

This policy statement grants access to AWS Health Dashboard and the AWS Health
`Describe*` API operations, but denies access to any AWS Health events
that relate to Amazon EC2.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "health:Describe*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "health:DescribeAffectedEntities",
 "health:DescribeEventDetails"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "health:service": "EC2"
 }
 }
 }
 ]
}`

```

###### Example : Resource-based condition

The following policy has the same effect, but uses the `Resource`
element instead.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "health:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "health:DescribeEventDetails",
 "health:DescribeAffectedEntities"
 ],
 "Resource": "arn:aws:health:*::event/EC2/*/*"
 }]
}`

```

###### Example : eventTypeCode condition

This policy statement grants access to AWS Health Dashboard and the AWS Health
`Describe*` API operations, but denies access to any AWS Health events
with the `eventTypeCode` that matches `AWS_EC2_*`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "health:Describe*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "health:DescribeAffectedEntities",
 "health:DescribeEventDetails"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "health:eventTypeCode": "AWS_EC2_*"
 }
 }
 }
 ]
}`

```

###### Important

If you call the [DescribeAffectedEntities](../APIReference/API_DescribeAffectedEntities.md "../APIReference/API_DescribeAffectedEntities.md") and [DescribeEventDetails](../APIReference/API_DescribeEventDetails.md "../APIReference/API_DescribeEventDetails.md") operations and don't have permission to access the
AWS Health event, the `AccessDeniedException` error appears. For more
information, see [Troubleshooting AWS Health identity
and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md").
