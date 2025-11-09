Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Identity and Access Management and Amazon CodeCatalyst

In
Amazon CodeCatalyst, you create and use an AWS Builder ID in order to sign in and access your spaces and
projects. An AWS Builder ID is not an identity in
AWS Identity and Access Management (IAM) and does not exist in an AWS account. However, CodeCatalyst does
integrate with IAM when verifying a space for billing purposes, and when connected to
an AWS account to create and use resources in that AWS account.

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use resources. IAM is an AWS service that you can use with no
additional charge.

When you create a space in Amazon CodeCatalyst, you must connect an AWS account
as the billing account for your space. You must have administrator permissions in the
AWS account to verify the CodeCatalyst space, or have the

permission. You also have the option to add an IAM role for your space that CodeCatalyst can use
to create and access resources in that connected AWS account. This is called a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role"). You can choose to create connections to more than one AWS account and
create service roles for CodeCatalyst in each of those accounts.

###### Note

Billing for CodeCatalyst takes place in the AWS account designated as the billing account.
However, if you create a CodeCatalyst service role in that AWS account or in any other
connected AWS account, resources created and used by the CodeCatalyst service role will be
billed in that connected AWS account. For more information, see [Managing billing](../adminguide/managing-billing.md "../adminguide/managing-billing.md") in the Amazon CodeCatalyst Administrator Guide.

###### Topics

- [Identity-based policies in IAM](#id-based-policies "#id-based-policies")
- [Policy actions in IAM](#id-based-policies-actions "#id-based-policies-actions")
- [Policy resources in IAM](#id-based-policies-resources "#id-based-policies-resources")
- [Policy condition keys in IAM](#id-based-policies-conditionkeys "#id-based-policies-conditionkeys")
- [Identity-based policy examples for CodeCatalyst
  connections](#id-based-policy-examples "#id-based-policy-examples")
- [Using tags to control access to account
  connection resources](id-based-policy-examples-tags.md "id-based-policy-examples-tags.md")
- [CodeCatalyst permissions reference](#permissions-reference "#permissions-reference")
- [Using service-linked roles for
  CodeCatalyst](using-service-linked-roles.md "using-service-linked-roles.md")
- [AWS managed policies for Amazon CodeCatalyst](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Grant access to project AWS resources with IAM roles](ipa-iam-roles.md "ipa-iam-roles.md")

## Identity-based policies in IAM

Identity-based policies are JSON permissions policy documents that you can attach to an
identity. That identity could be a user, a group of users, or a role. These policies
control what actions users and roles can perform, on which resources, and under what
conditions. To learn how to create an identity-based policy, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. You
can't specify the principal in an identity-based policy because it applies to the user
or role to which it is attached. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Identity-based policy examples for

CodeCatalyst

To view examples of CodeCatalyst identity-based policies, see [Identity-based policy examples for CodeCatalyst
connections](#id-based-policy-examples "#id-based-policy-examples").

## Policy actions in IAM

Administrators can use AWS JSON policies to specify who has access to what. That is,
which **principal** can perform which **actions** on what **resources**, and under what
**conditions**.

The `Action` element of a JSON policy describes the actions that you can use
to allow or deny access in a policy. Policy actions usually have the same name as the
associated AWS API operation. There are some exceptions, such as
_permission-only actions_ that don't have a matching API
operation. There are also some operations that require multiple actions in a policy. These
additional actions are called _dependent actions_.

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "prefix:`action1`",
      "prefix:`action2`"
         ]
```

## Policy resources in IAM

Administrators can use AWS JSON policies to specify who has access to what. That is,
which **principal** can perform which **actions** on what **resources**, and under what
**conditions**.

The `Resource` JSON policy element specifies the object or objects to which
the action applies. Statements must include either a `Resource` or a
`NotResource` element. As a best practice, specify a resource using its
[Amazon Resource Name
(ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md"). You can do this for actions that support a specific resource type, known
as _resource-level permissions_.

For actions that don't support resource-level permissions, such as listing
operations, use a wildcard (\*) to indicate that the statement applies to all
resources.

```
"Resource": "*"
```

## Policy condition keys in IAM

Administrators can use AWS JSON policies to specify who has access to what. That is,
which **principal** can perform which **actions** on what **resources**, and under what
**conditions**.

The `Condition` element (or `Condition`
_block_) lets you specify conditions in which a statement
is in effect. The `Condition` element is optional. You can create conditional
expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the policy
with values in the request.

If you specify multiple `Condition` elements in a statement, or multiple keys
in a single `Condition` element, AWS evaluates them using a logical
`AND` operation. If you specify multiple values for a single condition key, AWS
evaluates the condition using a logical `OR` operation. All of the conditions must
be met before the statement's permissions are granted.

You can also use placeholder variables when you specify conditions.
For more information, see [IAM policy elements: variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the
_IAM User Guide_.

AWS supports global condition keys and service-specific condition keys. To see all AWS
global condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

## Identity-based policy examples for CodeCatalyst

connections

In CodeCatalyst, AWS accounts are required to manage billing for a space and to access
resources in project workflows. An account connection is used to authorize adding
AWS accounts to a space. Identity-based polices are used in the connected
AWS accounts.

By default, users and roles don't have permission to create or modify CodeCatalyst
resources. They also can't perform tasks by using the AWS Management Console, AWS Command Line Interface (AWS CLI), or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform actions on the resources that they need. The administrator must then
attach those policies for users that require them.

The following example IAM policies grant permissions for actions related to account
connections. Use them to limit access for connecting accounts to CodeCatalyst.

### Example 1: Allow a user to accept

connection requests in a single AWS Region

The following permissions policy only allows users to view and accept requests for
connections between CodeCatalyst and AWS accounts. In addition, the policy uses a condition
to only allow the actions in the us-west-2 Region and not from other AWS Regions. To
view and approve the request, the user signs in to the AWS Management Console with the same account
as that specified in the request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecatalyst:AcceptConnection",
 "codecatalyst:GetPendingConnection"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "us-west-2"
 }
 }
 }
 ]
}`

```

### Example 2: Allow managing connections

in the console for a single AWS Region

The following permissions policy allows users to manage connections between CodeCatalyst
and AWS accounts in a single Region. The policy uses a condition to only allow the
actions in the us-west-2 Region and not from other AWS Regions. After you create a
connection, you can create the **CodeCatalystWorkflowDevelopmentRole-`spaceName`** role by choosing the option in the AWS Management Console.
In the example policy, the condition for the `iam:PassRole` action includes
the service principals for CodeCatalyst. Only roles with that access will be
created
in the AWS Management Console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecatalyst:*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "us-west-2"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:CreatePolicy",
 "iam:AttachRolePolicy",
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "codecatalyst.amazonaws.com",
 "codecatalyst-runner.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

### Example 3: Deny managing

connections

The following permissions policy denies users any ability to manage connections
between CodeCatalyst and AWS accounts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "codecatalyst:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## CodeCatalyst permissions reference

This section provides a permissions reference for actions used with the account
connection resource for AWS accounts that are connected to CodeCatalyst. The following section
describes permissions-only actions that are related to connecting accounts.

### Required permissions for account

connections

The following permissions are required for working with account connections.

| CodeCatalyst permissions for account connections | Required permissions                                                                                                                                | Resources                                                               |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| AcceptConnection                                 | Required to accept a request to connect this account to a CodeCatalyst<br>space.<br>This<br>is an IAM policy permission only, not an API<br>action. | Supports only a wildcard (\*) in the policy `Resource`<br>element.      |
| AssociateIamRoleToConnection                     | Required to associate an IAM role to an account connection. This is an<br>IAM policy permission only, not an API action.                            | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |
| DeleteConnection                                 | Required to delete an account connection. This is an IAM policy<br>permission only, not an API action.                                              | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |
| DisassociateIamRoleFromConnection                | Required to disassociate an IAM role from an account connection. This is<br>an IAM policy permission only, not an API action.                       | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |
| GetBillingAuthorization                          | Required to describe the billing authorization for an account<br>connection. This is an IAM policy permission only, not an API<br>action.           | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |
| GetConnection                                    | Required to get an account connection. This is an IAM policy<br>permission only, not an API action.                                                 | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |
| GetPendingConnection                             | Required to get a pending request to connect this account to a CodeCatalyst<br>space. This is an IAM policy permission only, not an API<br>action.  | Supports only a wildcard (\*) in the policy `Resource`<br>element.      |
| ListConnections                                  | Required to list account connections that are not pending. This is an<br>IAM policy permission only, not an API action.                             | Supports only a wildcard (\*) in the policy `Resource`<br>element.      |
| ListIamRolesForConnection                        | Required to list IAM roles associated with an account connection. This<br>is an IAM policy permission only, not an API action.                      | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |
| ListTagsForResource                              | Required to list tags associated with an account connection. This is an<br>IAM policy permission only, not an API action.                           | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |
| PutBillingAuthorization                          | Required to create or update the billing authorization for an account<br>connection. This is an IAM policy permission only, not an API<br>action.   | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |
| RejectConnection                                 | Required to reject a request to connect this account to a CodeCatalyst<br>space. This is an IAM policy permission only, not an API<br>action.       | Supports only a wildcard (\*) in the policy `Resource`<br>element.      |
| TagResource                                      | Required to create or edit tags associated with an account connection.<br>This is an IAM policy permission only, not an API action.                 | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |
| UntagResource                                    | Required to remove tags associated with an account connection. This is<br>an IAM policy permission only, not an API action.                         | `arn:aws:codecatalyst:region:`account_ID`:/connections/`connection_ID`` |

### Required permissions for IAM Identity Center applications

The following permissions are required for working with IAM Identity Center applications.

| CodeCatalyst permissions for IAM Identity Center applications | Required permissions                                                                                                                                                                    | Resources                                                                                                 |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| AssociateIdentityCenterApplicationToSpace                     | Required to associate an IAM Identity Center application with a CodeCatalyst space.<br>This is an IAM policy permission only, not an API action.                                        | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| AssociateIdentityToIdentityCenterApplication                  | Required to associate an identity with an IAM Identity Center application for a CodeCatalyst<br>space. This is an IAM policy permission only, not an API<br>action.                     | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| BatchAssociateIdentitiesToIdentityCenterApplication           | Required to associate multiple identities with an IAM Identity Center application for<br>a CodeCatalyst space. This is an IAM policy permission only, not an API<br>action.             | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| BatchDisassociateIdentitiesFromIdentityCenterApplication      | Required to disassociate multiple identities from an IAM Identity Center application<br>for a CodeCatalyst space. This is an IAM policy permission only, not an API<br>action.          | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| CreateIdentityCenterApplication                               | Required to create an IAM Identity Center application. This is an IAM policy<br>permission only, not an API action.                                                                     | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| CreateSpaceAdminRoleAssignment                                | Required to create an administrator role assignment for a given CodeCatalyst<br>space and IAM Identity Center application. This is an IAM policy permission only,<br>not an API action. | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| DeleteIdentityCenterApplication                               | Required to delete an IAM Identity Center application. This is an IAM policy<br>permission only, not an API action.                                                                     | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| DisassociateIdentityCenterApplicationFromSpace                | Required to disassociate an IAM Identity Center application from a CodeCatalyst space.<br>This is an IAM policy permission only, not an API action.                                     | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| DisassociateIdentityFromIdentityCenterApplication             | Required to disassociate an identity from an IAM Identity Center application for a<br>CodeCatalyst space. This is an IAM policy permission only, not an API<br>action.                  | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| GetIdentityCenterApplication                                  | Required to get information about an IAM Identity Center application. This is an IAM<br>policy permission only, not an API action.                                                      | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| ListIdentityCenterApplications                                | Required to view a list of all IAM Identity Center applications in the account. This<br>is an IAM policy permission only, not an API action.                                            | Supports only a wildcard (\*) in the policy `Resource`<br>element.                                        |
| ListIdentityCenterApplicationsForSpace                        | Required to view a list of IAM Identity Center applications by CodeCatalyst space. This<br>is an IAM policy permission only, not an API action.                                         | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| ListSpacesForIdentityCenterApplication                        | Required to view a list of CodeCatalyst spaces by IAM Identity Center application. This<br>is an IAM policy permission only, not an API action.                                         | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| SynchronizeIdentityCenterApplication                          | Required to synchronize an IAM Identity Center application with the backing identity<br>store. This is an IAM policy permission only, not an API action.                                | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
| UpdateIdentityCenterApplication                               | Required to update an IAM Identity Center application. This is an IAM policy<br>permission only, not an API action.                                                                     | `arn:aws:codecatalyst:region:`account_ID`:/identity-center-applications/`identity-center-application_ID`` |
