# How AWS User Notifications works with

IAM

Before you use IAM to manage access to User Notifications, you should understand what IAM
features are available to use with User Notifications. To get a high-level view of how User Notifications and other
AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Note

User Notifications uses resource-level permissions and managed policies to define what actions users can take.

###### Topics

- [User Notifications
  Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Authorization based on
  User Notifications tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [User Notifications IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## User Notifications

Identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources. You can also specify the conditions under which actions are allowed or
denied. User Notifications supports specific actions, resources, and condition keys. To learn about
all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in User Notifications use the following prefixes before the action:

- `notifications-contacts:` - Used for email contact actions.
- `notifications:` - Used for all other actions.

For example, to grant someone permission to update notification configurations with the `UpdateNotificationConfiguration` API operation, you include
the `notifications:UpdateNotificationConfiguration` action in their policy. Policy statements must
include either an `Action` or `NotAction` element.
User Notifications defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "notifications:*action1*",
      "notifications:*action2*"
```

You can specify multiple actions using wildcards (**\***). For
example, to specify all actions that begin with the word `Get`, include
the following action:

```
`"Action": "notifications:Get*"`
```

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

For a list of resource types and their ARNs for User Notifications and User Notifications Contacts, see
[Resources Defined by AWS User Notifications](../../../IAM/latest/UserGuide/list_awsusernotifications.md#awsusernotifications-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsusernotifications.md#awsusernotifications-resources-for-iam-policies") and [Resources Defined by AWS User Notifications Contacts](../../../IAM/latest/UserGuide/list_awsusernotificationscontacts.md#awsusernotificationscontacts-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsusernotificationscontacts.md#awsusernotificationscontacts-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by AWS User Notifications](../../../IAM/latest/UserGuide/list_awsusernotifications.md#awsusernotifications-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsusernotifications.md#awsusernotifications-actions-as-permissions") .

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

User Notifications defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

To see a list of condition keys for User Notifications and User Notifications Contacts, see [Condition Keys for AWS User Notifications](../../../IAM/latest/UserGuide/list_awsusernotifications.md#awsusernotifications-policy-keys "../../../IAM/latest/UserGuide/list_awsusernotifications.md#awsusernotifications-policy-keys") and [Condition Keys for AWS User Notifications Contacts](../../../IAM/latest/UserGuide/list_awsusernotificationscontacts.md#awsusernotificationscontacts-policy-keys "../../../IAM/latest/UserGuide/list_awsusernotificationscontacts.md#awsusernotificationscontacts-policy-keys")
in the _IAM User Guide_. To learn with which actions and
resources you can use a condition key, see [Actions Defined by AWS User Notifications](../../../IAM/latest/UserGuide/list_awsusernotifications.md#awsusernotifications-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsusernotifications.md#awsusernotifications-actions-as-permissions") and [Actions Defined by AWS User Notifications Contacts](../../../IAM/latest/UserGuide/list_awsusernotificationscontacts.md#awsusernotificationscontacts-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsusernotificationscontacts.md#awsusernotificationscontacts-actions-as-permissions").

### Examples

To view examples of User Notifications identity-based policies, see [AWS User Notifications identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Authorization based on

User Notifications tags

You can attach tags to User Notifications resources or pass tags in a request to
User Notifications. To control access based on tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`notifications:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging
User Notifications resources, see [Tagging your AWS User Notifications resources](tagging-resources.md "tagging-resources.md").

To view an example identity-based policy for limiting access to a resource based on
the tags on that resource, see [Viewing
User Notifications notification configurations based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-resource-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-resource-tags").

## User Notifications IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

User Notifications supports service-linked roles. For details about creating or
managing User Notifications service-linked roles, see
[Using Service-Linked Roles for User Notifications](using-service-linked-roles.md "using-service-linked-roles.md").
