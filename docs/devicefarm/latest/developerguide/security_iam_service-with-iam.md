# How AWS Device Farm works with IAM

Before you use IAM to manage access to Device Farm, you should understand which IAM features are
available to use with Device Farm. To get a high-level view of how Device Farm and other AWS services work with
IAM, see [AWS Services That Work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Device Farm identity-based
  policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Device Farm resource-based
  policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Access control lists](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")
- [Authorization based on Device Farm tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Device Farm IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Device Farm identity-based

policies

With IAM identity-based policies, you can specify allowed or denied actions and resources and the
conditions under which actions are allowed or denied. Device Farm supports specific actions, resources, and
condition keys. To learn about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in
the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Device Farm use the following prefix before the action: `devicefarm:`. For
example, to grant someone permission to start Selenium sessions with the Device Farm desktop browser testing
`CreateTestGridUrl` API operation, you include the
`devicefarm:CreateTestGridUrl` action in the policy. Policy statements must include
either an `Action` or `NotAction` element. Device Farm defines its own set of
actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "devicefarm:*action1*",
      "devicefarm:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that
begin with the word `List`, include the following action:

```
`"Action": "devicefarm:List*"`
```

To see a list of Device Farm actions, see [Actions defined by AWS Device Farm](../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-actions-as-permissions "../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-actions-as-permissions") in the _IAM Service Authorization Reference_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The Amazon EC2 instance resource has the following ARN:

```
arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}
```

For more information about the format of ARNs, see [Amazon Resource
Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `i-1234567890abcdef0` instance in your statement, use the
following ARN:

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
```

To specify all instances that belong to an account, use the wildcard (\*):

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*"
```

Some Device Farm actions, such as those for creating resources, cannot be performed on a resource. In
those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

Many Amazon EC2 API actions involve multiple resources. For example, `AttachVolume` attaches
an Amazon EBS volume to an instance, so an IAM user must have permissions to use the volume and
the instance. To specify multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of Device Farm resource types and their ARNs, see [Resource types defined by AWS Device Farm](../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-resources-for-iam-policies "../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-resources-for-iam-policies") in the _IAM Service
Authorization Reference_. To learn with which actions you can specify the ARN of each
resource, see [Actions defined by AWS Device Farm](../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-actions-as-permissions "../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-actions-as-permissions") in the _IAM Service
Authorization Reference_.

### Condition

keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Device Farm defines its own set of condition keys and also supports the use of some global condition
keys. To see all AWS global condition keys, see [AWS Global Condition Context
Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

To see a list of Device Farm condition keys, see [Condition keys for AWS Device Farm](../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-policy-keys "../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-policy-keys") in the _IAM Service
Authorization Reference_. To learn with which actions and resources you can use a
condition key, see [Actions defined by AWS Device Farm](../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-actions-as-permissions "../../../service-authorization/latest/reference/list_awsdevicefarm.md#awsdevicefarm-actions-as-permissions") in the _IAM Service
Authorization Reference_.

### Examples

To view examples of Device Farm identity-based policies, see [AWS Device Farm identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Device Farm resource-based

policies

Device Farm does not support resource-based policies.

## Access control lists

Device Farm does not support access control lists (ACLs).

## Authorization based on Device Farm tags

You can attach tags to Device Farm resources or pass tags in a request to Device Farm. To control access
based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy
using the `aws:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or `aws:TagKeys`
condition keys. For more information about tagging Device Farm resources, see [Tagging AWS Device Farm resources](tagging.md "tagging.md").

To view an example identity-based policy for limiting access to a resource based on the tags on that
resource, see [Viewing Device Farm desktop browser
testing projects based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-project-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-project-tags").

## Device Farm IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity in your AWS account that
has specific permissions.

### Using temporary credentials with

Device Farm

Device Farm supports the use of temporary credentials.

You can use temporary credentials to sign in with federation to assume an IAM role
orcross-account role. You obtain temporary security credentials by calling AWS STS API operations
such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other services to
complete an action on your behalf. Service-linked roles appear in your IAM account and are owned
by the service. An IAM administrator can view, but cannot edit, the permissions for service-linked
roles.

Device Farm uses service-linked roles in the Device Farm desktop browser testing feature. For information on these roles, see
[Using Service-Linked Roles in Device Farm desktop browser testing](../testgrid/using-service-linked-roles.md "../testgrid/using-service-linked-roles.md") in the developer guide.

### Service roles

Device Farm does not support service roles.

This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role")
on your behalf. This role allows the service to access resources in other services to complete an
action on your behalf. Service roles appear in your IAM account and are owned by the account. This
means that an IAM administrator can change the permissions for this role. However, doing so might
break the functionality of the service.
