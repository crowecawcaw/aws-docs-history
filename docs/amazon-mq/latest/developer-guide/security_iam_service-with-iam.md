# How Amazon MQ works with IAM

Before you use IAM to manage access to Amazon MQ, you should understand what
IAM features are available to use with Amazon MQ. To get a high-level view of how
Amazon MQ and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

Amazon MQ uses IAM for creating, updating, and deleting operations, but native ActiveMQ authentication for brokers.
For more information, see [Integrating ActiveMQ brokers with LDAP](security-authentication-authorization.md "security-authentication-authorization.md").

###### Topics

- [Amazon MQ identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon MQ Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on Amazon MQ tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon MQ IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon MQ identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Amazon MQ supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon MQ use the following prefix before the action:
`mq:`. For example, to grant someone permission to run
an Amazon MQ instance with the Amazon MQ `CreateBroker` API operation, you include
the `mq:CreateBroker` action in their policy. Policy statements must
include either an `Action` or `NotAction` element.
Amazon MQ defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "mq:*action1*",
      "mq:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "mq:Describe*"`
```

To see a list of Amazon MQ actions, see [Actions Defined by Amazon MQ](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

In the Amazon MQ, the primary AWS resources are an Amazon MQ message broker and its configuration. Amazon MQ brokers and configurations each have unique Amazon Resource Names (ARNs) associated with them, as shown in the following table.

| Resource Types | ARN                                                                          | Condition Keys                                                                                         |
| -------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| brokers        | `arn:aws:mq:us-east-1:123456789012:broker:${brokerName}:${brokerId}`         | [aws:ResourceTag/${TagKey}](#amazonmq-aws_ResourceTag___TagKey_ "#amazonmq-aws_ResourceTag___TagKey_") |
| configurations | `arn:${Partition}:mq:${Region}:${Account}:configuration:${configuration-id}` | [aws:ResourceTag/${TagKey}](#amazonmq-aws_ResourceTag___TagKey_ "#amazonmq-aws_ResourceTag___TagKey_") |

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the broker named `MyBroker` with brokerId `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9` in your
statement, use the following ARN:

```
"Resource": "arn:aws:mq:us-east-1:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9"
```

To specify all brokers and configurations that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:mq:us-east-1:123456789012:*"
```

Some Amazon MQ actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

The API action `CreateTags` requires both a broker and a configuration. To specify
multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of Amazon MQ resource types and their ARNs, see
[Resources Defined by Amazon MQ](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by Amazon MQ](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon MQ does not define any service-specific condition keys, but supports using
some global condition keys. To see a list of Amazon MQ condition keys, see the table below
or [Condition Keys for Amazon MQ](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-policy-keys "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-policy-keys") in the _IAM User Guide_.
To learn with which actions and resources you can use a condition key, see [Actions Defined by Amazon MQ](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-actions-as-permissions").

| Condition Keys                                                                                                                                                                                                             | Description                                                           | Type   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------ |
| [aws:RequestTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag")    | Filters actions based on the tags that are passed in the request.     | String |
| [aws:ResourceTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") | Filters actions based on the tags associated with the resource.       | String |
| [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys")                       | Filters actions based on the tag keys that are passed in the request. | String |

### Examples

To view examples of Amazon MQ identity-based policies, see [Amazon MQ Identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Amazon MQ Resource-based policies

Currently, Amazon MQ doesn't support IAM authentication using resource-based permissions or resource-based policies.

## Authorization based on Amazon MQ tags

You can attach tags to Amazon MQ resources or pass tags in a request to
Amazon MQ. To control access based on tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`mq:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys.

Amazon MQ supports policies based on tags. For instance, you could deny access to Amazon MQ
resources that include a tag with the key `environment` and the value
`production`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "mq:DeleteBroker",
 "mq:RebootBroker",
 "mq:DeleteTags"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/environment": "production"
 }
 }
 }
 ]
}`

```

This policy will `Deny` the ability to delete or reboot an Amazon MQ broker
that includes the tag `environment/production`.

For more information on tagging, see:

- [Adding tags to Amazon MQ resources](amazon-mq-tagging.md "amazon-mq-tagging.md")
- [Controlling Access Using IAM
  Tags](../../../IAM/latest/UserGuide/access_iam-tags.md "../../../IAM/latest/UserGuide/access_iam-tags.md")

## Amazon MQ IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using Temporary Credentials with Amazon MQ

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon MQ supports using temporary credentials.

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

Amazon MQ supports service roles.
