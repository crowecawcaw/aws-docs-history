# How Amazon VPC works with IAM

Before you use IAM to manage access to Amazon VPC, you should understand what IAM
features are available to use with Amazon VPC. To get a high-level view of how Amazon VPC and
other AWS services work with IAM, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Contents

- [Actions](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")
- [Resources](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")
- [Condition keys](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys")
- [Amazon VPC
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")
  With IAM identity-based policies, you can specify allowed or denied actions. For
  some actions, you can specify the resources and conditions under which actions are
  allowed or denied. Amazon VPC supports specific actions, resources, and condition keys. To
  learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements
  reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

## Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Amazon VPC shares its API namespace with Amazon EC2. Policy actions in Amazon VPC use the
following prefix before the action: `ec2:`. For example, to grant a user
permission to create a VPC using the `CreateVpc` API operation, you grant
access to the `ec2:CreateVpc` action. Policy statements must include
either an `Action` or `NotAction` element.

To specify multiple actions in a single statement, separate them with commas
as shown in the following example.

```
"Action": [
      "ec2:*action1*",
      "ec2:*action2*"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify
all actions that begin with the word `Describe`, include the following
action.

```
"Action": "ec2:Describe*"
```

To see a list of Amazon VPC actions, see [Actions defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions") in the _Service Authorization Reference_.

## Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The VPC resource has the ARN shown in the following example.

```
arn:${Partition}:ec2:${Region}:${Account}:vpc/${VpcId}
```

For example, to specify the `vpc-1234567890abcdef0` VPC in your
statement, use the ARN shown in the following example.

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-1234567890abcdef0"
```

To specify all VPCs in a specific Region that belong to a specific account,
use the wildcard (\*).

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:vpc/*"
```

Some Amazon VPC actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

Many Amazon EC2 API actions involve multiple resources. To specify multiple
resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
]
```

To see a list of Amazon VPC resource types and their ARNs, see [Resource types defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies") in the
_Service Authorization Reference_.

## Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

All Amazon EC2 actions support the `aws:RequestedRegion` and
`ec2:Region` condition keys. For more information, see [Example:
Restrict access to a specific Region](../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region "../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region").

Amazon VPC defines its own set of condition keys and also supports using some global
condition keys. To see a list of Amazon VPC condition keys, see [Condition keys for
Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-policy-keys "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-policy-keys") in the _Service Authorization Reference_. To learn with
which actions and resources you can use a condition key, see [Actions
defined by Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-actions-as-permissions").

## Amazon VPC

resource-based policies

Resource-based policies are JSON policy documents that specify what actions a
specified principal can perform on the Amazon VPC resource and under what
conditions.

To enable cross-account access, you can specify an entire account or IAM
entities in another account as the [principal in a
resource-based policy](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md"). Adding a cross-account principal to a
resource-based policy is only half of establishing the trust relationship. When the
principal and the resource are in different AWS accounts, you must also grant the
principal entity permission to access the resource. Grant permission by attaching an
identity-based policy to the entity. However, if a resource-based policy grants
access to a principal in the same account, no additional identity-based policy is
required. For more information, see [Cross
account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the
_IAM User Guide_.

## Authorization based on

tags

You can attach tags to Amazon VPC resources or pass tags in a request. To
control access based on tags, you provide tag information in the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using condition keys. For more information,
see [Grant permission to tag resources during creation](../../../AWSEC2/latest/UserGuide/supported-iam-actions-tagging.md "../../../AWSEC2/latest/UserGuide/supported-iam-actions-tagging.md") in the
_Amazon EC2 User Guide_.

To view an example identity-based policy for limiting access to a resource based
on the tags on that resource, see [Launch instances into a specific VPC](vpc-policy-examples.md#subnet-ami-example-iam "vpc-policy-examples.md#subnet-ami-example-iam").

## IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") is an entity within
your AWS account that has specific permissions.

### Use temporary

credentials

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon VPC supports using temporary credentials.

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") allow AWS services to access resources in
other services to complete an action on your behalf. Service-linked roles appear
in your IAM account and are owned by the service. An IAM administrator can
view but not edit the permissions for service-linked roles.

[Transit
gateways](../tgw/service-linked-roles.md "../tgw/service-linked-roles.md") support service-linked roles.

### Service

roles

This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") on your behalf. This role allows the service to access
resources in other services to complete an action on your behalf. Service roles
appear in your IAM account and are owned by the account. This means that an
IAM administrator can change the permissions for this role. However, doing so
might break the functionality of the service.

Amazon VPC supports service roles for flow logs. When you create a flow log, you
must choose a role that allows the flow logs service to access CloudWatch Logs. For more
information, see [IAM role for publishing flow logs to CloudWatch Logs](flow-logs-iam-role.md "flow-logs-iam-role.md").
