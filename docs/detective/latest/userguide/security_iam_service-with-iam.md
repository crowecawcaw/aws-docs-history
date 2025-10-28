# How Amazon Detective works with IAM

By default, users and roles don't have permission to create or modify Amazon Detective
resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. A
Detective administrator must have AWS Identity and Access Management (IAM) policies that grant IAM users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the principal that require those
permissions.

Detective uses IAM identity-based policies to grant permissions for the following types of
users and actions:

- **Administrator accounts** – The administrator
  account is the owner of a behavior graph, which uses data from their account.
  Administrator accounts can invite member accounts to contribute their data to the
  behavior graph. The administrator account can also use the behavior graph for triage
  and investigation of findings and resources associated with those accounts.

You can set up policies to allow users other than the administrator account to
perform different types of tasks. For example, a user from an administrator account
might only have permissions to manage member accounts. Another user might only have
permissions to use the behavior graph for investigation.

- **Member accounts** – A member account is an
  account that is invited to contribute data to a behavior graph. A member account
  responds to an invitation. After accepting an invitation, a member account can remove
  their account from the behavior graph.
  To get a high-level view of how Detective and other AWS services work with IAM, see
  [Creating policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") in the
  _IAM User Guide_.

## Detective identity-based

policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources, as well as the conditions under which actions are allowed or denied. Detective
supports specific actions, resources, and condition keys.

To learn about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy statements must include either an `Action` element or a
`NotAction` element. The `Action` element lists the actions
allowed by the policy. The `NotAction` element lists the actions that are
not allowed.

The actions defined for Detective reflect tasks that you can perform using Detective.
Policy actions in Detective have the following prefix:
`detective:`.

For example, to grant permission to use the `CreateMembers` API
operation to invite member accounts to a behavior graph, you include the
`detective:CreateMembers` action in their policy.

To specify multiple actions in a single statement, separate them with commas. For
example, for a member account, the policy includes the set of actions related to
managing an invitation:

```
"Action": [
      "detective:ListInvitations",
      "detective:AcceptInvitation",
      "detective:RejectInvitation",
      "detective:DisassociateMembership
]
```

You can also use wildcards (\*) to specify multiple actions. For example, to manage
the data used in their behavior graph, administrator accounts in Detective must be able to
perform the following tasks:

- View their list of member accounts (`ListMembers`).
- Get information about selected member accounts
  (`GetMembers`).
- Invite member accounts to their behavior graph
  (`CreateMembers`).
- Remove members from their behavior graph
  (`DeleteMembers`).

Instead of listing these actions separately, you can grant access to all actions
that end with the word `Members`. The policy for that could include the
following action:

```
`"Action": "detective:*Members"`
```

To see a list of Detective actions, see [Actions defined by Amazon Detective](../../../service-authorization/latest/reference/list_amazondetective.md#amazondetective-actions-as-permissions "../../../service-authorization/latest/reference/list_amazondetective.md#amazondetective-actions-as-permissions") in the
_Service Authorization Reference_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For Detective, the only resource type is the behavior graph. The behavior graph
resource in Detective has the following ARN:

```
arn:aws:detective:${Region}:${AccountId}:graph:${GraphId}
```

For example, a behavior graph has the following values:

- The Region for the behavior graph is `us-east-1`.
- The account ID for the administrator account ID is
  `111122223333`.
- The graph ID of the behavior graph is
  `027c7c4610ea4aacaf0b883093cab899`.

To identify this behavior graph in a `Resource` statement, you would
use the following ARN:

```
"Resource": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899"
```

To specify multiple resources in a `Resource` statement, use commas to
separate them.

```
"Resource": [
      "*resource1*",
      "*resource2*"
]
```

For example, the same AWS account may be invited to be a member account in more
than one behavior graph. In the policy for that member account, the
`Resource` statement would list the behavior graphs they were invited
to.

```
"Resource": [
      "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
      "arn:aws:detective:us-east-1:444455556666:graph:056d2a9521xi2bbluw1d164680eby416"
]
```

Some Detective actions, such as creating a behavior graph, listing behavior graphs,
and listing behavior graph invitations, are not performed on a specific behavior
graph. For those actions, the `Resource` statement must use the wildcard
(\*).

```
"Resource": "*"
```

For administrator account actions, Detective always verifies that the user making the request
belongs to the administrator account for the affected behavior graph. For member account
actions, Detective always verifies that the user making the request belongs to the member
account. Even if an IAM policy grants access to a behavior graph, if the user does
not belong to the correct account, the user cannot perform the action.

For all actions that are performed on a specific behavior graph, the IAM policy
should include the graph ARN. The graph ARN can be added later. For example, when an
account first enables Detective, the initial IAM policy provides access to all Detective
actions, using the wildcard for the graph ARN. This allows the user to immediately
start to manage member accounts for and conduct investigations in their behavior
graph. After the behavior graph is created, you can update the policy to add the
graph ARN.

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Detective does not define its own set of condition keys. It does support
using global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

To learn which actions and resources allow you to use a condition key, see [Actions defined by Amazon Detective](../../../service-authorization/latest/reference/list_amazondetective.md#amazondetective-actions-as-permissions "../../../service-authorization/latest/reference/list_amazondetective.md#amazondetective-actions-as-permissions").

### Examples

To view examples of Detective identity-based policies, see [Amazon Detective identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Detective

resource-based policies (Not supported)

Detective does not support resource-based policies.

## Authorization based on

Detective behavior graph tags

Each behavior graph can be assigned tag values. You can use those tag values in
condition statements to manage access to the behavior graph.

The condition statement for a tag value uses the following format.

```
{"StringEquals"{"aws:ResourceTag/`<tagName>`": "`<tagValue>`"}}
```

For example, use the following code to allow or deny an action when the value of the
`Department` tag is `Finance`.

```
{"StringEquals"{"aws:ResourceTag/Department": "Finance"}}
```

For examples of policies that use resource tag values, see [Administrator
account: Restricting access based on tag values](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-graph-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-graph-tags").

## Detective IAM Roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with Detective

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Detective supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

For details about creating or managing Detective service-linked roles, see
[Using service-linked roles for
Detective](using-service-linked-roles.md "using-service-linked-roles.md").

### Service roles (Not

supported)

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

Detective does not support service roles.
