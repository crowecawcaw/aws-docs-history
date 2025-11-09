# Identity-based policy examples for

Direct Connect

By default, users and roles don't have permission to create or modify Direct Connect
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Direct Connect, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for Direct Connect](../../../IAM/latest/UserGuide/list_awsdirectconnect.md "../../../IAM/latest/UserGuide/list_awsdirectconnect.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Actions, resources, and conditions](#security_iam_service-dx-id-based-policies "#security_iam_service-dx-id-based-policies")
- [Using the console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Read-only access to
  AWS Direct Connect](#security_iam_id-based-policy-examples-read-access "#security_iam_id-based-policy-examples-read-access")
- [Full access to
  AWS Direct Connect](#security_iam_id-based-policy-examples-full-access "#security_iam_id-based-policy-examples-full-access")
- [Tag-based condition keys](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Direct Connect resources in your
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
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
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

## Direct Connect actions,

resources, and conditions

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. Direct Connect
supports specific actions, resources, and condition keys. To learn about all of the
elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Direct Connect use the following prefix before the action:
`directconnect:`. For example, to grant someone permission to run an
Amazon EC2 instance with the Amazon EC2 `DescribeVpnGateways` API operation, you
include the `ec2:DescribeVpnGateways` action in their policy. Policy
statements must include either an `Action` or `NotAction`
element. Direct Connect defines its own set of actions that describe tasks that you can
perform with this service.

The following example policy grants read access to AWS Direct Connect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "directconnect:Describe*",
 "ec2:DescribeVpnGateways"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following example policy grants full access to AWS Direct Connect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "directconnect:*",
 "ec2:DescribeVpnGateways"
 ],
 "Resource": "*"
 }
 ]
}`

```

To see a list of Direct Connect actions, see [Actions Defined by Direct Connect](../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Direct Connect uses the following ARNs:

| Direct connect resource ARNs | Resource Type                                                                     | ARN |
| ---------------------------- | --------------------------------------------------------------------------------- | --- |
| dxcon                        | `arn:${Partition}:directconnect:${Region}:${Account}:dxcon/${ConnectionId}`       |
| dxlag                        | `arn:${Partition}:directconnect:${Region}:${Account}:dxlag/${LagId}`              |
| dx-vif                       | `arn:${Partition}:directconnect:${Region}:${Account}:dxvif/${VirtualInterfaceId}` |
| dx-gateway                   | `arn:${Partition}:directconnect::${Account}:dx-gateway/${DirectConnectGatewayId}` |

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `dxcon-11aa22bb` interface in your
statement, use the following ARN:

```
"Resource": "arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-11aa22bb
```

To specify all virtual interfaces that belong to a specific account, use the
wildcard (\*):

```
"Resource": "arn:aws:directconnect:*:*:dxvif/*"
```

Some Direct Connect actions, such as those for creating resources, cannot be performed
on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

To see a list of Direct Connect resource types and their ARNs, see [Resource Types Defined by AWS Direct Connect](../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-resources-for-iam-policies") in the
_IAM User Guide_. To learn with which actions you can specify
the ARN of each resource, see [Actions Defined by Direct Connect](../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-actions-as-permissions").

If a resource ARN or a resource ARN pattern other than `*` is specified
in the `Resource` field of the IAM policy statement for
DescribeConnections, DescribeVirtualInterfaces, DescribeDirectConnectGateways,
DescribeInterconnects, or DescribeLags, then the specified `Effect` will
not occur unless the matching resource ID is also passed in the API call. However, if
you provide `*` as the resource instead of a specific resource ID in the
IAM policy statement, the specified `Effect` will work.

In the following example, neither specified `Effect` will succeed if
the `DescribeConnections` action is called without a
`connectionId` passed in the request.

```
"Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "directconnect:DescribeConnections"
        ],
        "Resource": [
            "arn:aws:directconnect:*:123456789012:dxcon/*"
        ]
    },
{
        "Effect": "Deny",
        "Action": [
            "directconnect:DescribeConnections"
        ],
        "Resource": [
            "arn:aws:directconnect:*:123456789012:dxcon/example1"
        ]
    }
]
```

However, in the following example, `"Effect": "Allow"` will succeed
for the `DescribeConnections` action since `*` was provided for
the `Resource` field of the IAM policy statement, regardless of whether
the `connectionId` was specified in the request.

```
"Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "directconnect:DescribeConnections
        ],
        "Resource": [
            "*"
        ]
    }
]
```

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Direct Connect defines its own set of condition keys and also supports using some
global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

You can use condition keys with the tag resource. For more information, see [Example:
Restricting Access to a Specific Region](../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region "../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region").

To see a list of Direct Connect condition keys, see [Condition Keys for Direct Connect](../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-policy-keys "../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-policy-keys") in the
_IAM User Guide_. To learn with which actions and resources
you can use a condition key, see [Actions Defined by Direct Connect](../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsdirectconnect.md#awsdirectconnect-actions-as-permissions").

## Using the Direct Connect

console

To access the Direct Connect console, you must have a minimum set of permissions. These
permissions must allow you to list and view details about the Direct Connect resources in
your AWS account. If you create an identity-based policy that is more restrictive than
the minimum required permissions, the console won't function as intended for entities (s
or roles) with that policy.

To ensure that those entities can still use the Direct Connect console, also attach the
following AWS managed policy to the entities. For more information, see [Adding Permissions to a User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_:

```
directconnect
```

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that you're trying to perform.

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

## Read-only access to

AWS Direct Connect

The following example policy grants read access to AWS Direct Connect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "directconnect:Describe*",
 "ec2:DescribeVpnGateways"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Full access to

AWS Direct Connect

The following example policy grants full access to AWS Direct Connect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "directconnect:*",
 "ec2:DescribeVpnGateways"
 ],
 "Resource": "*"
 }
 ]
}`

```
