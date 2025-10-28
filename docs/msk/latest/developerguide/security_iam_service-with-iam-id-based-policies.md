# Amazon MSK

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Amazon MSK supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

## Actions for Amazon MSK identity-based policies

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon MSK use the following prefix before the action:
`kafka:`. For example, to grant someone permission
to describe an MSK cluster with the Amazon MSK `DescribeCluster`
API operation, you include the `kafka:DescribeCluster` action in
their policy. Policy statements must include either an `Action` or
`NotAction` element. Amazon MSK defines its own set of
actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas
as follows:

```
"Action": ["kafka:*action1*", "kafka:*action2*"]
```

You can specify multiple actions using wildcards (\*). For example, to specify
all actions that begin with the word `Describe`, include the
following action:

```
`"Action": "kafka:Describe*"`
```

To see a list of Amazon MSK actions, see [Actions, resources, and condition keys for Amazon Managed Streaming for
Apache Kafka](../../../service-authorization/latest/reference/list_amazonmanagedstreamingforapachekafka.md "../../../service-authorization/latest/reference/list_amazonmanagedstreamingforapachekafka.md") in the _IAM User Guide_.

## Resources for Amazon MSK identity-based policies

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The Amazon MSK instance resource has the following ARN:

```
arn:${Partition}:kafka:${Region}:${Account}:cluster/${ClusterName}/${UUID}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `CustomerMessages` instance in your
statement, use the following ARN:

```
"Resource": "arn:aws:kafka:us-east-1:123456789012:cluster/CustomerMessages/abcd1234-abcd-dcba-4321-a1b2abcd9f9f-2"
```

To specify all instances that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:kafka:us-east-1:123456789012:cluster/*"
```

Some Amazon MSK actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

To specify multiple resources in a single statement, separate the ARNs with
commas.

```
"Resource": ["*resource1*", "*resource2*"]
```

To see a list of Amazon MSK resource types and their ARNs, see
[Resources Defined by Amazon Managed Streaming for Apache Kafka](../../../IAM/latest/UserGuide/list_amazonmanagedstreamingforkafka.md#amazonmanagedstreamingforkafka-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmanagedstreamingforkafka.md#amazonmanagedstreamingforkafka-resources-for-iam-policies") in the _IAM User Guide_. To
learn with which actions you can specify the ARN of each resource, see
[Actions Defined by Amazon Managed Streaming for Apache Kafka](../../../IAM/latest/UserGuide/list_amazonmanagedstreamingforkafka.md#amazonmanagedstreamingforkafka-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonmanagedstreamingforkafka.md#amazonmanagedstreamingforkafka-actions-as-permissions").

## Condition keys for Amazon MSK identity-based policies

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon MSK defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS Global
Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Amazon MSK condition keys, see
[Condition Keys for Amazon Managed Streaming for Apache Kafka](../../../IAM/latest/UserGuide/list_amazonmanagedstreamingforkafka.md#amazonmanagedstreamingforkafka-policy-keys "../../../IAM/latest/UserGuide/list_amazonmanagedstreamingforkafka.md#amazonmanagedstreamingforkafka-policy-keys") in the _IAM User Guide_. To
learn with which actions and resources you can use a condition key, see
[Actions Defined by Amazon Managed Streaming for Apache Kafka](../../../IAM/latest/UserGuide/list_amazonmanagedstreamingforkafka.md#amazonmanagedstreamingforkafka-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonmanagedstreamingforkafka.md#amazonmanagedstreamingforkafka-actions-as-permissions").

## Examples for Amazon MSK identity-based policies

To view examples of Amazon MSK identity-based policies, see [Amazon MSK identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
