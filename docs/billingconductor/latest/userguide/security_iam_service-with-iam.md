# How AWS Billing Conductor works with

IAM

Before you use IAM to manage access to Billing Conductor, you should understand what
IAM features are available to use with Billing Conductor. To get a high-level view of how
Billing Conductor and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Billing Conductor
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Billing Conductor
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Access control lists (ACLs)](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")
- [Authorization based on
  Billing Conductor tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Billing Conductor IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Billing Conductor

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Billing Conductor supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Billing Conductor use the following prefix before the action:
`Billing Conductor:`. For example, to grant someone permission to run
an Amazon EC2 instance with the Amazon EC2 `RunInstances` API operation, you include
the `ec2:RunInstances` action in their policy. Policy statements must
include either an `Action` or `NotAction` element.
Billing Conductor defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "ec2:*action1*",
      "ec2:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "ec2:Describe*"`
```

To see a list of Billing Conductor actions, see [Actions Defined by AWS Billing Conductor](../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-actions-as-permissions") in the
_IAM User Guide_.

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

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `i-1234567890abcdef0` instance in your
statement, use the following ARN:

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
```

To specify all instances that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*"
```

Some Billing Conductor actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

Many Amazon EC2 API actions involve multiple resources. For example,
`AttachVolume` attaches an Amazon EBS volume to an instance, so an
IAM user must have permissions to use the volume and the instance. To specify
multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of Billing Conductor resource types and their ARNs, see
[Resources Defined by AWS Billing Conductor](../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by AWS Billing Conductor](../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Billing Conductor defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

All Amazon EC2 actions support the `aws:RequestedRegion` and
`ec2:Region` condition keys. For more information, see [Example:
Restricting Access to a Specific Region](../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region "../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region").

To see a list of Billing Conductor condition keys, see [Condition Keys for AWS Billing Conductor](../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-policy-keys "../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-policy-keys")
in the _IAM User Guide_. To learn with which actions and
resources you can use a condition key, see [Actions Defined by AWS Billing Conductor](../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsbillingconductor.md#awsbillingconductor-actions-as-permissions").

### Examples

To view examples of Billing Conductor identity-based policies, see [AWS Billing Conductor identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Billing Conductor

resource-based policies

Resource-based policies are JSON policy documents that specify what actions a
specified principal can perform on the Billing Conductor resource and under what
conditions. Amazon S3 supports resource-based permissions policies for Amazon S3
`buckets`. Resource-based policies let you grant usage
permission to other accounts on a per-resource basis. You can also use a resource-based
policy to allow an AWS service to access your Amazon S3
`buckets`.

To enable cross-account access, you can specify an entire account or IAM entities
in another account as the [principal in a
resource-based policy](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md"). Adding a cross-account principal to a resource-based
policy is only half of establishing the trust relationship. When the principal and the
resource are in different AWS accounts, you must also grant the principal entity
permission to access the resource. Grant permission by attaching an identity-based
policy to the entity. However, if a resource-based policy grants access to a principal
in the same account, no additional identity-based policy is required. For more
information, see [How
IAM Roles Differ from Resource-based Policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the
_IAM User Guide_.

The Amazon S3 service supports only one type of resource-based policy called a _`bucket` policy_, which is attached
to a `bucket`. This policy defines which principal entities
(accounts, users, roles, and federated users) can perform actions on the
`Billing Conductor`.

### Examples

To view examples of Billing Conductor resource-based policies, see [AWS Billing Conductor
resource-based policy examples](security_iam_resource-based-policy-examples.md "security_iam_resource-based-policy-examples.md"),

## Access control lists (ACLs)

Access control lists (ACLs) are lists of grantees that you can attach to resources.
They grant accounts permissions to access the resource to which they are attached. You
can attach ACLs to an Amazon S3 `bucket` resource.

With Amazon S3 access control lists (ACLs), you can manage access to
`bucket` resources. Each `bucket`
has an ACL attached to it as a subresource. It defines which AWS accounts, IAM users
or groups of users, or IAM roles are granted access and the type of access. When a
request is received for a resource, AWS checks the corresponding ACL to verify that
the requester has the necessary access permissions.

When you create a `bucket` resource, Amazon S3 creates a default
ACL that grants the resource owner full control over the resource. In the following
example `bucket` ACL, John Doe is listed as the owner of the
`bucket` and is granted full control over that
`bucket`. An ACL can have up to 100 grantees.

```
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy xmlns="http://Billing Conductor.amazonaws.com/doc/2006-03-01/">
  <Owner>
    <ID>`c1daexampleaaf850ea79cf0430f33d72579fd1611c97f7ded193374c0b163b6`</ID>
    <DisplayName>`john-doe`</DisplayName>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:type="Canonical User">
        <ID>`c1daexampleaaf850ea79cf0430f33d72579fd1611c97f7ded193374c0b163b6`</ID>
        <DisplayName>`john-doe`</DisplayName>
      </Grantee>
      <Permission>FULL_CONTROL</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

The ID field in the ACL is the AWS account canonical user ID. To learn how to view
this ID in an account that you own, see [Finding an AWS Account
Canonical User ID](../../../general/latest/gr/acct-identifiers.md#FindingCanonicalId "../../../general/latest/gr/acct-identifiers.md#FindingCanonicalId").

## Authorization based on

Billing Conductor tags

You can attach tags to Billing Conductor resources or pass tags in a request to
Billing Conductor. To control access based on tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`Billing Conductor:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys.

## Billing Conductor IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with Billing Conductor

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Billing Conductor supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

Billing Conductor supports service roles.

### Choosing an IAM role

in Billing Conductor

When you create a resource in Billing Conductor, you must choose a role to allow
Billing Conductor to access Amazon EC2 on your behalf. If you have previously created a
service role or service-linked role, then Billing Conductor provides you with a list
of roles to choose from. It's important to choose a role that allows access to start
and stop Amazon EC2 instances.
