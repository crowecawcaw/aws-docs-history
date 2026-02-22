# Using Quick with

IAM

|                                                                 |
| --------------------------------------------------------------- |
| \*_Applies<br>to:_<br>• Enterprise Edition and Standard Edition |

|                                             |
| ------------------------------------------- |
| Intended audience:<br>System administrators |

Before you use IAM to manage access to Amazon Quick, you should understand what
IAM features are available to use with Amazon Quick. To get a high-level view of how
Amazon Quick and other AWS services work with IAM, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Amazon Quick
  Policies (identity-based)](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon Quick
  policies (resource-based)](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  Amazon Quick tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon Quick IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon Quick

Policies (identity-based)

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Amazon Quick supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

You can use AWS root credentials or IAM user credentials to create an
Amazon Quick account. AWS root and administrator credentials already have all of
the required permissions for managing Amazon Quick access to AWS resources.

However, we recommend that you protect your root credentials, and instead use
IAM user credentials. To do this, you can create a policy and attach it to the
IAM user and roles that you plan to use for Amazon Quick. The policy must include
the appropriate statements for the Amazon Quick administrative tasks you need to
perform, as described in the following sections.

###### Important

Be aware of the following when working with Quick and IAM
policies:

- Avoid directly modifying a policy that was created by
  Quick. When you modify it yourself, Quick can't
  edit it. This inability can cause an issue with the policy. To fix this
  issue, delete the previously modified policy.
- If you get an error on permissions when you try to create an
  Amazon Quick account, see [Actions Defined by Amazon Quick](../../../service-authorization/latest/reference/list_amazonquicksight.md#amazonquicksight-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonquicksight.md#amazonquicksight-actions-as-permissions") in the
  _IAM User Guide_.
- In some cases, you might have an Amazon Quick account that you can't
  access even from the root account (for example, if you accidentally
  deleted its directory service). In this case, you can delete your old
  Amazon Quick account, then recreate it. For more information, see [Deleting your Amazon Quick subscription and
  closing the account](../../../quicksight/latest/user/closing-account.md "../../../quicksight/latest/user/closing-account.md").

###### Topics

- [Actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")
- [Resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")
- [Condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys")
- [Examples](#security_iam_service-with-iam-id-based-policies-examples "#security_iam_service-with-iam-id-based-policies-examples")

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon Quick use the following prefix before the action:
`quicksight:`. For example, to grant someone permission to
run an Amazon EC2 instance with the Amazon EC2 `RunInstances` API operation,
you include the `ec2:RunInstances` action in their policy. Policy
statements must include either an `Action` or `NotAction`
element. Amazon Quick defines its own set of actions that describe tasks that
you can perform with this service.

To specify multiple actions in a single statement, separate them with commas
as follows:

```
"Action": [
	      "quicksight:*action1*",
	      "quicksight:*action2*"]
```

You can specify multiple actions using wildcards (\*). For example, to specify
all actions that begin with the word `Create`, include the following
action:

```
`"Action": "quicksight:Create*"`
```

Amazon Quick provides a number of AWS Identity and Access Management (IAM) actions. All Amazon Quick
actions are prefixed with `quicksight:`, such as
`quicksight:Subscribe`. For information about using Amazon Quick
actions in an IAM policy, see [IAM policy examples for Amazon Quick](../../../quicksight/latest/user/iam-policy-examples.md "../../../quicksight/latest/user/iam-policy-examples.md").

To see the most up-to-date list of Amazon Quick actions, see
[Actions Defined by Amazon Quick](../../../service-authorization/latest/reference/list_amazonquicksight.md#amazonquicksight-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonquicksight.md#amazonquicksight-actions-as-permissions") in the _IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Following is an example policy. It means that the caller with this policy
attached, is able to invoke the `CreateGroupMembership` operation on
any group, provided that the user name they are adding to the group is not
`user1`.

```
{
    "Effect": "Allow",
    "Action": "quicksight:CreateGroupMembership",
    "Resource": "arn:aws:quicksight:us-east-1:`aws-account-id`:group/default/*",
    "Condition": {
        "StringNotEquals": {
            "quicksight:UserName": "user1"
        }
    }
}
```

Some Amazon Quick actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

Some API actions involve multiple resources. To specify multiple resources in
a single statement, separate the ARNs with commas.

```
"Resource": [
	      "*resource1*",
	      "*resource2*"
```

To see a list of Amazon Quick resource types and their Amazon Resource Names
(ARNs), see [Resources Defined by Amazon Quick](../../../service-authorization/latest/reference/list_amazonquicksight.md#amazonquicksight-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonquicksight.md#amazonquicksight-resources-for-iam-policies") in the
_IAM User Guide_. To learn with which actions you can
specify the ARN of each resource, see [Actions Defined by Amazon Quick](../../../service-authorization/latest/reference/list_amazonquicksight.md#amazonquicksight-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonquicksight.md#amazonquicksight-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon Quick does not provide any service-specific condition keys, but it does
support using some global condition keys. To see all AWS global condition
keys, see [AWS Global Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

### Examples

To view examples of Amazon Quick identity-based policies, see [Amazon Quick Policies (identity-based)](../../../quicksight/latest/user/security_iam_service-with-iam-id-based-policies.md "../../../quicksight/latest/user/security_iam_service-with-iam-id-based-policies.md").

## Amazon Quick

policies (resource-based)

Amazon Quick doesn't support resource-based policies. However, you can use
the Amazon Quick console to configure access to other AWS resources
in your AWS account.

## Authorization based on

Amazon Quick tags

Amazon Quick does not support tagging resources or controlling access based on
tags.

## Amazon Quick IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions. You can use IAM roles to group
permissions together to make it easier to manage user's access to Amazon Quick
actions.

Amazon Quick doesn't support the following role features:

- Service-linked roles.
- Service roles.
- Temporary credentials (direct use): However, Amazon Quick uses temporary
  credentials to allow users to assume an IAM role to access embedded
  dashboards. For more information, see [Embedded analytics for Amazon Quick](../../../quicksight/latest/user/embedded-analytics.md "../../../quicksight/latest/user/embedded-analytics.md").

For more information on how Amazon Quick uses IAM roles, see [Using Amazon Quick with IAM](../../../quicksight/latest/user/security_iam_service-with-iam.md "../../../quicksight/latest/user/security_iam_service-with-iam.md") and [IAM
policy examples for Amazon Quick](../../../quicksight/latest/user/iam-policy-examples.md "../../../quicksight/latest/user/iam-policy-examples.md").
