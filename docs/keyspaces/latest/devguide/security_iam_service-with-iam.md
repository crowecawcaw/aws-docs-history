# How Amazon Keyspaces works with

IAM

Before you use IAM to manage access to Amazon Keyspaces, you should understand what
IAM features are available to use with Amazon Keyspaces. To get a high-level view of how
Amazon Keyspaces and other AWS services work with IAM, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Amazon Keyspaces
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon Keyspaces
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  Amazon Keyspaces tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon Keyspaces IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon Keyspaces

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Amazon Keyspaces supports specific actions and resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

To see the Amazon Keyspaces service-specific resources and actions, and condition context keys
that can be used for IAM permissions policies, see the [Actions, resources, and condition keys for Amazon Keyspaces (for Apache Cassandra)](../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md "../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md") in the
_Service Authorization Reference_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon Keyspaces use the following prefix before the action:
`cassandra:`. For example, to grant someone permission to
create an Amazon Keyspaces keyspace with the Amazon Keyspaces `CREATE` CQL statement, you
include the `cassandra:Create` action in their policy. Policy statements
must include either an `Action` or `NotAction` element.
Amazon Keyspaces defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas
as follows:

```
"Action": [
      "cassandra:*CREATE*",
      "cassandra:*MODIFY*"
          ]
```

To see a list of Amazon Keyspaces actions, see [Actions Defined by Amazon Keyspaces (for Apache Cassandra)](../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-actions-as-permissions") in the
_Service Authorization Reference_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

In Amazon Keyspaces, keyspaces, tables, and streams can be used in the `Resource` element of IAM permissions.

###### Note

To access user keyspaces and tables in Amazon Keyspaces, your IAM policy must include `cassandra:Select` permissions on
system tables:

```
arn:${Partition}:cassandra:${Region}:${Account}:/keyspace/system*
```

This applies to the following scenarios:

- AWS Management Console access
- SDK resource operations, for example `GetKeyspace`, `GetTable`, `ListKeyspaces`, and `ListTables`
- Standard Apache Cassandra client driver connections, because drivers automatically read system tables during connection initialization
  System tables are read-only and cannot be modified.

The Amazon Keyspaces keyspace resource has the following ARN:

```
arn:${Partition}:cassandra:${Region}:${Account}:/keyspace/${keyspaceName}/
```

The Amazon Keyspaces table resource has the following ARN:

```
arn:${Partition}:cassandra:${Region}:${Account}:/keyspace/${keyspaceName}/table/${tableName}
```

The Amazon Keyspaces stream resource has the following ARN:

```
arn:${Partition}:cassandra:{Region}:${Account}:/keyspace/${keyspaceName}/table/${tableName}/stream/${streamLabel}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS service namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `mykeyspace` keyspace in your
statement, use the following ARN:

```
"Resource": "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/mykeyspace/"
```

To specify all keyspaces that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/*"
```

Some Amazon Keyspaces actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

For example, to grant `SELECT` permissions to an IAM principal for `mytable` in `mykeyspace`, the principal
must have permissions to read both, `mytable` and `keyspace/system*`. To specify
multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/mykeyspace/table/mytable",
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"

```

To see a list of Amazon Keyspaces resource types and their ARNs, see
[Resources Defined by Amazon Keyspaces (for Apache Cassandra)](../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-resources-for-iam-policies") in the _Service Authorization Reference_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by Amazon Keyspaces (for Apache Cassandra)](../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon Keyspaces defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS global condition
context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

All Amazon Keyspaces actions support the `aws:RequestTag/${TagKey}`, the
`aws:ResourceTag/${TagKey}`, and the `aws:TagKeys` condition
keys. For more information, see [Amazon Keyspaces resource access based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags").

To see a list of Amazon Keyspaces condition keys, see [Condition Keys for Amazon Keyspaces (for Apache Cassandra)](../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-policy-keys "../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-policy-keys")
in the _Service Authorization Reference_. To learn with which actions and
resources you can use a condition key, see [Actions Defined by Amazon Keyspaces (for Apache Cassandra)](../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.md#amazonkeyspacesforapachecassandra-actions-as-permissions").

### Examples

To view examples of Amazon Keyspaces identity-based policies, see [Amazon Keyspaces identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Amazon Keyspaces

resource-based policies

Amazon Keyspaces
does not support resource-based policies. To view an example of a detailed
resource-based policy page, see [https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md").

## Authorization based on

Amazon Keyspaces tags

You can manage access to your Amazon Keyspaces resources by using tags. To manage resource access based on tags,
you provide tag information in
the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`cassandra:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging
Amazon Keyspaces resources, see [Working with tags and labels for Amazon Keyspaces resources](tagging-keyspaces.md "tagging-keyspaces.md").

To view example identity-based policies for limiting access to a resource based on
the tags on that resource, see [Amazon Keyspaces resource access based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags").

## Amazon Keyspaces IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with Amazon Keyspaces

You can use temporary credentials to sign in with federation, to assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon Keyspaces supports using temporary credentials with the AWS Signature Version
4 (SigV4) authentication plugin available from the Github repo for the following languages:

- Java: [https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin").
- Node.js: [https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin").
- Python: [https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin").
- Go: [https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin").

For examples and tutorials that implement the authentication plugin to access
Amazon Keyspaces programmatically, see [Using a Cassandra client driver to access
Amazon Keyspaces programmatically](programmatic.md "programmatic.md").

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

For details about creating or
managing Amazon Keyspaces service-linked roles, see **[Using service-linked roles for
Amazon Keyspaces](using-service-linked-roles.md "using-service-linked-roles.md")**.

### Service roles

Amazon Keyspaces does not support service roles.
