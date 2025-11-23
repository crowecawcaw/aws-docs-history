# Identity-based policy

examples for Amazon One Enterprise

By default, users and roles don't have permission to create or modify Amazon One Enterprise
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon One Enterprise, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon One Enterprise](actions-resources-contextkeys.md "actions-resources-contextkeys.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon One Enterprise
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Read-only access to Amazon One Enterprise](#read-only-config-permission "#read-only-config-permission")
- [Full access to Amazon One Enterprise](#full-config-permission "#full-config-permission")
- [Supported Resource-Level Permissions
  for Amazon One Enterprise Rule API Actions](#supported-resource-level-permissions "#supported-resource-level-permissions")
- [Additional Information](#config-permissions-more-info "#config-permissions-more-info")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon One Enterprise resources in your
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

## Using the Amazon One Enterprise

console

To access the Amazon One Enterprise console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the Amazon One Enterprise resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the Amazon One Enterprise console, also attach the
Amazon One Enterprise `ConsoleAccess` or `ReadOnly` AWS managed policy to
the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
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

## Read-only access to Amazon One Enterprise

The following example shows an AWS managed policy, `AmazonOneEnterpriseReadOnlyAccess`
that grants read-only access to Amazon One Enterprise.

In the policy statements, the `Effect` element specifies whether the
actions are allowed or denied. The `Action` element lists the specific
actions that the user is allowed to perform. The `Resource` element lists the
AWS resources the user is allowed to perform those actions on. For policies that
control access to Amazon One Enterprise actions, the `Resource` element is always set to
`*`, a wildcard that means "all resources."

The values in the `Action` element correspond to the APIs that the services
support. The actions are preceded by `config:` to indicate that they refer to
Amazon One Enterprise actions. You can use the `*` wildcard character in the
`Action` element, such as in the following examples:

- `"Action": ["one:*DeviceInstanceConfiguration"]`

This allows all Amazon One Enterprise actions that end with "DeviceInstance"
(`GetDeviceInstanceConfiguration`,
`CreateDeviceInstanceConfiguration`).

- `"Action": ["one:*"]`

This allows all Amazon One Enterprise actions, but not actions for other AWS services.

- `"Action": ["*"]`

This allows all AWS actions. This permission is suitable for a user who acts
as an AWS administrator for your account.

The read-only policy doesn't grant user permission for actions such as
`CreateDeviceInstance`, `UpdateDeviceInstance`, and
`DeleteDeviceInstance`. Users with this policy are not allowed to create a
device instance, update a device instance, or delete a device instance. For the list of
Amazon One Enterprise actions, see [Actions, resources, and condition keys for Amazon One Enterprise](actions-resources-contextkeys.md "actions-resources-contextkeys.md").

## Full access to Amazon One Enterprise

The following example shows a policy that grants full access to Amazon One Enterprise. It grants users
the permission to perform all Amazon One Enterprise actions.

###### Important

This policy grants broad permissions. Before granting full access, consider
starting with a minimum set of permissions and granting additional permissions as
necessary. Doing so is better practice than starting with permissions that are too
lenient and then trying to tighten them later.

## Supported Resource-Level Permissions

for Amazon One Enterprise Rule API Actions

Resource-level permissions refers to the ability to specify which resources users are
allowed to perform actions on. Amazon One Enterprise supports resource-level permissions for certain
Amazon One Enterprise rule API actions. This means that for certain Amazon One Enterprise rule actions, you can
control the conditions under which when users are allowed to use those actions. These
conditions can be actions that must be fulfilled, or specific resources that users are
allowed to use.

The following table describes the Amazon One Enterprise rule API actions that currently support
resource-level permissions. It also describes the supported resources and their ARNs
for each action. When specifying an ARN, you can use the \* wildcard in your paths;
for example, when you cannot or do not want to specify exact resource IDs.

###### Important

If an Amazon One Enterprise rule API action is not listed in this table, then it does not support
resource-level permissions. If an Amazon One Enterprise rule action does not support resource-level
permissions, you can grant users permissions to use the action, but you have to specify
a \* for the resource element of your policy statement.

| API Action                        | Resources                                                                                                                  |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| CreateDeviceInstance              | Device Instance<br>arn:aws:one:`region:accountID`:device-instance/`deviceInstanceId`                                       |
| GetDeviceInstance                 | Device Instance<br>arn:aws:one:`region:accountID`:device-instance/`deviceInstanceId`                                       |
| UpdateDeviceInstance              | Device Instance<br>arn:aws:one:`region:accountID`:device-instance/`deviceInstanceId`                                       |
| DeleteDeviceInstance              | Device Instance<br>arn:aws:one:`region:accountID`:device-instance/`deviceInstanceId`                                       |
| CreateDeviceActivationQrCode      | Device Instance<br>arn:aws:one:`region:accountID`:device-instance/`deviceInstanceId`                                       |
| DeleteAssociatedDevice            | Device Instance<br>arn:aws:one:`region:accountID`:device-instance/`deviceInstanceId`                                       |
| RebootDevice                      | Device Instance<br>arn:aws:one:`region:accountID`:device-instance/`deviceInstanceId`                                       |
| CreateDeviceInstanceConfiguration | Device Instance Configuration<br>arn:aws:one:`region:accountID`:device-instance/`deviceInstanceId`/configuration/`version` |
| GetDeviceInstanceConfiguration    | Device Instance Configuration<br>arn:aws:one:`region:accountID`:device-instance/`deviceInstanceId`/configuration/`version` |
| CreateSite                        | Site<br>arn:aws:one:`region:accountID`:site/`siteId`                                                                       |
| DeleteSite                        | Site<br>arn:aws:one:`region:accountID`:site/`siteId`                                                                       |
| GetSiteAddress                    | Site<br>arn:aws:one:`region:accountID`:site/`siteId`                                                                       |
| UpdateSite                        | Site<br>arn:aws:one:`region:accountID`:site/`siteId`                                                                       |
| UpdateSiteAddress                 | Site<br>arn:aws:one:`region:accountID`:site/`siteId`                                                                       |
| CreateDeviceConfigurationTemplate | Device Configuration Template<br>arn:aws:one:`region:accountID`:device-configuration-template/`templateId`                 |
| DeleteDeviceConfigurationTemplate | Device Configuration Template<br>arn:aws:one:`region:accountID`:device-configuration-template/`templateId`                 |
| GetDeviceConfigurationTemplate    | Device Configuration Template<br>arn:aws:one:`region:accountID`:device-configuration-template/`templateId`                 |
| UpdateDeviceConfigurationTemplate | Device Configuration Template<br>arn:aws:one:`region:accountID`:device-configuration-template/`templateId`                 |

For example, you want to allow read access and deny write access to specific rules to
specific users.

In the first policy, you allow the AWS Config rule read actions such as `GetSite` on
the specified rules.

In the second policy, you deny the Amazon One Enterprise rule write actions on the specific rule.

With resource-level permissions, you can allow read access and deny write access to
perform specific actions on Amazon One Enterprise rule API actions.

## Additional Information

To learn more about creating IAM users, groups, policies, and permissions, see
[Creating Your First IAM
User and Administrators Group](../../../IAM/latest/UserGuide/GSGHowToCreateAdminsGroup.md "../../../IAM/latest/UserGuide/GSGHowToCreateAdminsGroup.md") and [Access Management](../../../IAM/latest/UserGuide/PermissionsAndPolicies.md "../../../IAM/latest/UserGuide/PermissionsAndPolicies.md") in the
_IAM User Guide_.
