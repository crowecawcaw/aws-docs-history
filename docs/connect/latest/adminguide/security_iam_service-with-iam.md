# How Connect Customer works with IAM

Before you use IAM to manage access to Connect Customer, you should understand what
IAM features are available to use with Connect Customer. To get a high-level view of how
Connect Customer and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Contents

- [Connect Customer identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Authorization based on Connect Customer tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Connect Customer IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Connect Customer identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Connect Customer supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Connect Customer use the following prefix before the action:
`connect:`.

Policy statements must include either an `Action` or
`NotAction` element. Connect Customer defines its own set of actions
that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "connect:*action1*",
      "connect:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "connect:Describe*"`
```

To see a list of Connect Customer actions, [Actions,
Resources, and Condition Keys for Connect Customer](../../../service-authorization/latest/reference/list_amazonconnect.md "../../../service-authorization/latest/reference/list_amazonconnect.md").

### Resources

Connect Customer supports resource-level permissions (specifying a resource ARN in an IAM
policy). Following is a list of Connect Customer resources:

- Instance
- Contact
- User
- Routing profile
- Security profile
- Hierarchy group
- Queue
- File
- Flow
- Hours of operation
- Phone number
- Task templates
- Customer profile domain
- Customer profile object type
- Outbound campaigns

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The Connect Customer instance resource has the following ARN:

```
arn:${Partition}:connect:${Region}:${Account}:instance/${InstanceId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs)
and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `i-1234567890abcdef0` instance in your
statement, use the following ARN:

```
"Resource": "arn:aws:connect:us-east-1:123456789012:instance/i-1234567890abcdef0"
```

To specify all instances that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:connect:us-east-1:123456789012:instance/*"
```

Some Connect Customer actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

Many Connect Customer; API actions involve multiple resources. For example,

To specify multiple resources in a single statement, separate the ARNs with
commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of Connect Customer resource types and their ARNs, see [Actions,
Resources, and Condition Keys for Connect Customer](../../../service-authorization/latest/reference/list_amazonconnect.md "../../../service-authorization/latest/reference/list_amazonconnect.md"). The same article explains with
which actions you can specify the ARN of each resource.

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Connect Customer defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

All Amazon EC2 actions support the `aws:RequestedRegion` and
`ec2:Region` condition keys. For more information, see [Example:
Restricting Access to a Specific Region](../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region "../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region").

To see a list of Connect Customer condition keys, see [Actions,
Resources, and Condition Keys for Connect Customer](../../../service-authorization/latest/reference/list_amazonconnect.md "../../../service-authorization/latest/reference/list_amazonconnect.md").

### Examples

To view examples of Connect Customer identity-based policies, see [Connect Customer identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Authorization based on Connect Customer tags

You can attach tags to Connect Customer resources or pass tags in a request to
Connect Customer. To control access based on tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`connect:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys.

To view an example identity-based policy for limiting access to a resource based on
the tags on that resource, see [Describe and update Connect Customer users based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-widget-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-widget-tags").

## Connect Customer IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary credentials with Connect Customer

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Connect Customer supports using temporary credentials.

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

Connect Customer supports service-linked roles. For details about creating or
managing Connect Customer service-linked roles, see [Use service-linked roles and role permissions for Connect Customer](connect-slr.md "connect-slr.md").

### Choosing an IAM role in Connect Customer

When you create a resource in Connect Customer, you must choose a role to allow
Connect Customer to access Amazon EC2 on your behalf. If you have previously created a
service role or service-linked role, then Connect Customer provides you with a list
of roles to choose from. It's important to choose a role that allows access to start
and stop Amazon EC2 instances.
