# How Resource Explorer works with IAM

Before you use IAM to manage access to AWS Resource Explorer, you should understand what IAM
features are available to use with Resource Explorer. To get a high-level view of how Resource Explorer and other
AWS services work with IAM, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Resource Explorer identity-based
  policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Authorization based on Resource Explorer
  tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Resource Explorer IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")
  Like any other AWS service, Resource Explorer requires permissions to use its operations to
  interact with your resources. To create indexes or views, or to modify them or any other
  Resource Explorer settings, you must have additional permissions.

Your search experience is automatically enabled based on your IAM permissions. If you
have, at minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy, you can
immediately search all tagged resources and supported untagged resources created after the
[immediate resource discovery](manage-immediate-resource-discovery-experience.md "manage-immediate-resource-discovery-experience.md") release. For complete resource inventory with automatic updates, you'll
also need the `iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy). After the service-linked role is
created in your account by any user, subsequent users need only need, at minimum, the
permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy to create an index
and view for full results in a Region on first search. Organizations can control access by
denying the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy to prevent all
search access, or denying `iam:CreateServiceLinkedRole` to limit users to partial
results only when a service-linked role does not already exist in an account.

Assign IAM identity-based policies that grant those
permissions to the appropriate IAM principals. Resource Explorer provides [several managed policies](security_iam_awsmanpol.md "security_iam_awsmanpol.md") that pre-define common
sets of permissions. You can assign these to your IAM principals.

## Resource Explorer identity-based

policies

With IAM identity-based policies, you can specify allowed or denied actions against
specific resources and the conditions under which those actions are allowed or denied.
Resource Explorer supports specific actions, resources, and condition keys. To learn about all of
the elements that you use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Resource Explorer use the `resource-explorer-2` service prefix
before the action. For example, to grant someone permission to search using a view,
with the Resource Explorer `Search` API operation, you include the
`resource-explorer-2:Search` action in a policy assigned to that
principal. Policy statements must include either an `Action` or
`NotAction` element. Resource Explorer defines its own set of actions that
describe tasks that you can perform with this service. These align with the Resource Explorer
API operations.

To specify multiple actions in a single statement, separate them with commas as
shown in the following example.

```
"Action": [
      "resource-explorer-2:*action1*",
      "resource-explorer-2:*action2*"
]
```

You can specify multiple actions using wildcard characters (`*`). For
example, to specify all actions that begin with the word `Describe`,
include the following action.

```
`"Action": "resource-explorer-2:Describe*"`
```

For a list of Resource Explorer actions, see [Actions
Defined by AWS Resource Explorer](../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-actions-as-permissions "../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-actions-as-permissions") in the _AWS
Service Authorization Reference_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

#### View

The primary Resource Explorer resource type is the _view_.

The Resource Explorer view resource has the following ARN format.

```
arn:${Partition}:resource-explorer-2:${Region}:${Account}:view/${ViewName}/${unique-id}
```

The Resource Explorer ARN format is shown in the following example.

```
arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-Search-View/1a2b3c4d-5d6e-7f8a-9b0c-abcd11111111
```

###### Note

The ARN for a view includes a unique identifier at the end to ensure that
every view is unique. This helps ensure that an IAM policy that granted
access to an old, deleted view can't be used to accidentally grant access to
a new view that happens to have the same name as the old view. Every new
view receives a new, unique ID at the end to ensure that ARNs are never
reused.

For more information about the format of ARNs, see [Amazon Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

You use
IAM identity-based policies assigned to the IAM principals and specify the
view as the `Resource`. Doing this lets you grant search access
through one view to one set of principals, and access through a completely
different view to a different set of principals.

For example, to grant permission to a single view named
`ProductionResourcesView` in an IAM policy statement, first get
the [Amazon resource name (ARN)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") of the view. You can use the **[Views](https://console.aws.amazon.com/resource-explorer/home#/views "https://console.aws.amazon.com/resource-explorer/home#/views")** page in the console
to view the details of a view, or invoke the `ListViews`
operation to retrieve the full ARN of the view you want. Then, include it in a
policy statement, like that shown in the following example that grants
permission to modify the definition of only one view.

```
"Effect": "Allow",
"Action": "UpdateView",
"Resource": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/ProductionResourcesView/`<unique-id>`"
```

To allow the actions on **_all_** views that belong to a specific account, use
the wildcard character (`*`) in the relevant part of the ARN. The
following example grants search permission to all views in a specified
AWS Region and account.

```
"Effect": "Allow",
"Action": "Search",
"Resource": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/*"
```

Some Resource Explorer actions, such as `CreateView`, aren't performed against
a specific resource, because, as in the following example, the resource doesn't
exist yet. In such cases, you must use the wildcard character (`*`)
for the entire resource ARN.

```
"Effect": "Allow",
"Action": "resource-explorer-2:CreateView"
"Resource": "*"
```

If you specify a path that ends in a wildcard character, then you can
restrict the `CreateView` operation to creating views with only the
approved path. The following example policy piece shows how to allow the
principal to create views only in the path
`view/ProductionViews/`.

```
"Effect": "Allow",
"Action": "resource-explorer-2:CreateView"
"Resource": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/`ProductionViews/`*""
```

#### Index

Another resource type that you can use to control access to Resource Explorer
functionality is the index.

The primary way that you interact with the index is to create an index in that
Region. After that, you do almost everything else by interacting with the
view.

One thing that you can do with the index is to control who can **_create_** views in
each Region.

###### Note

After you create a view, IAM authorizes all other view actions against
only the ARN of the view, and not the index.

The index has an [ARN](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") that you can reference in a permission
policy. A Resource Explorer index ARN has the following format.

```
arn:${Partition}:resource-explorer-2:${Region}:${Account}:index/${unique-id}
```

See the following example of an Resource Explorer index ARN.

```
arn:aws:resource-explorer-2:us-east-1:123456789012:index/1a2b3c4d-5d6e-7f8a-9b0c-abcd22222222
```

Some Resource Explorer actions check authentication against multiple resource types. For
example, the [CreateView](../apireference/API_CreateView.md "../apireference/API_CreateView.md") operation authorizes against both the ARN of the index and
the ARN of the view as it will be after Resource Explorer creates it. To grant administrators
permission to manage the Resource Explorer service, you can use `"Resource": "*"` to
authorize actions for any resource, index, or view.

Alternatively, you can restrict a principal to only being able to work with
specified Resource Explorer resources. For example, to limit actions to only Resource Explorer resources
in a specified Region, you can include an ARN template that matches both the index
and the view, but calls out only a single Region. In the following example, the ARN
matches both indexes or views in only the `us-west-2` Region of the
specified account. Specify the Region in the third field of the ARN, but use a
wildcard character (\*) in the final field to match any resource type.

```
"Resource": "arn:aws:resource-explorer-2:us-west-2:123456789012:*
```

For more information, see [Resources
Defined by AWS Resource Explorer](../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-resources-for-iam-policies") in the _AWS Service
Authorization Reference_. To learn with which actions you can specify
the ARN of each resource, see [Actions
Defined by AWS Resource Explorer](../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-actions-as-permissions "../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-actions-as-permissions").

### Condition keys

Resource Explorer doesn't provide any service-specific condition keys, but it does support
using some global condition keys. To see all AWS global condition keys, see [AWS global
condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of the condition keys that you can use with Resource Explorer, see
[Condition Keys for
AWS Resource Explorer](../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-policy-keys "../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-policy-keys") in the _AWS Service Authorization
Reference_. To learn which actions and resources you can use a
condition key with, see [Actions
Defined by AWS Resource Explorer](../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-actions-as-permissions "../../../service-authorization/latest/reference/list_awsresourceexplorer.md#awsresourceexplorer-actions-as-permissions").

### Examples

To view examples of Resource Explorer identity-based policies, see [AWS Resource Explorer identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Authorization based on Resource Explorer

tags

You can attach tags to Resource Explorer views or pass tags in a request to Resource Explorer. To control
access based on tags, you provide tag information in the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`resource-explorer-2:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging Resource Explorer
resources, see [Adding tags to views](configure-views-tag.md "configure-views-tag.md"). For using tag-based authorization in Resource Explorer, see [Using tag-based authorization to
control access to your views](configure-views-grant-access.md#configure-views-grant-access-abac "configure-views-grant-access.md#configure-views-grant-access-abac").

## Resource Explorer IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is a principal within
your AWS account that has specific permissions.

### Using temporary

credentials with Resource Explorer

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials
by calling AWS Security Token Service (AWS STS) API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Resource Explorer supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

Resource Explorer uses service-linked roles to perform its work. When users with both, at
minimum, the permissions in the `AWSResourceExplorerReadOnlyAccess` managed policy and the
`iam:CreateServiceLinkedRole` permission (included in the [AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy) initiate their first
resource search, Resource Explorer automatically creates the service-linked role at the account
level. Once the service-linked role exists, subsequent regions are automatically
enabled when users with search permissions invoke search operations. For details
about Resource Explorer service-linked roles, see [Using service-linked roles for
Resource Explorer](security_iam_service-linked-roles.md "security_iam_service-linked-roles.md").

**Troubleshooting service-linked role creation:** If
users lack the `iam:CreateServiceLinkedRole` permission (included in the
[AWSResourceExplorerFullAccess](../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md "../../../aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.md") managed policy), they will receive an
error when attempting to create the service-linked role. To resolve this issue,
users must either get permission from an administrator or sign in with a role that
has the required permission.
