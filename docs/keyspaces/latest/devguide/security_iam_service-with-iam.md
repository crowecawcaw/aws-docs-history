

# How Amazon Keyspaces works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon Keyspaces, you should understand what IAM features are available to use with Amazon Keyspaces. To get a high-level view of how Amazon Keyspaces and other AWS services work with IAM, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [Amazon Keyspaces identity-based policies](#security_iam_service-with-iam-id-based-policies)
+ [Amazon Keyspaces resource-based policies](#security_iam_service-with-iam-resource-based-policies)
+ [Authorization based on Amazon Keyspaces tags](#security_iam_service-with-iam-tags)
+ [Amazon Keyspaces IAM roles](#security_iam_service-with-iam-roles)

## Amazon Keyspaces identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. Amazon Keyspaces supports specific actions and resources, and condition keys. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

To see the Amazon Keyspaces service-specific resources and actions, and condition context keys that can be used for IAM permissions policies, see the [Actions, resources, and condition keys for Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.html) in the *Service Authorization Reference*.

### Actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon Keyspaces use the following prefix before the action: `cassandra:`. For example, to grant someone permission to create an Amazon Keyspaces keyspace with the Amazon Keyspaces `CREATE` CQL statement, you include the `cassandra:Create` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Amazon Keyspaces defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "cassandra:CREATE",
      "cassandra:MODIFY"
          ]
```

To see a list of Amazon Keyspaces actions, see [Actions Defined by Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.html#amazonkeyspacesforapachecassandra-actions-as-permissions) in the *Service Authorization Reference*.

### Resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

In Amazon Keyspaces, keyspaces, tables, and streams can be used in the `Resource` element of IAM permissions.

**Note**  
To access user keyspaces and tables in Amazon Keyspaces, your IAM policy must include `cassandra:Select` permissions on system tables:  

```
arn:${Partition}:cassandra:${Region}:${Account}:/keyspace/system*
```
This applies to the following scenarios:  
AWS Management Console access
SDK resource operations, for example `GetKeyspace`, `GetTable`, `ListKeyspaces`, and `ListTables`
Standard Apache Cassandra client driver connections, because drivers automatically read system tables during connection initialization
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

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS service namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

For example, to specify the `mykeyspace` keyspace in your statement, use the following ARN:

```
"Resource": "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/"
```

To specify all keyspaces that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/*"
```

Some Amazon Keyspaces actions, such as those for creating resources, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

 For example, to grant `SELECT` permissions to an IAM principal for `mytable` in `mykeyspace`, the principal must have permissions to read both, `mytable` and `keyspace/system*`. To specify multiple resources in a single statement, separate the ARNs with commas. 

```
"Resource": "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/mykeyspace/table/mytable",
            "arn:aws:cassandra:{{us-east-1}}:{{111122223333}}:/keyspace/system*"
```

To see a list of Amazon Keyspaces resource types and their ARNs, see [Resources Defined by Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.html#amazonkeyspacesforapachecassandra-resources-for-iam-policies) in the *Service Authorization Reference*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.html#amazonkeyspacesforapachecassandra-actions-as-permissions).

### Condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Amazon Keyspaces defines its own set of condition keys and also supports using some global condition keys. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.



 All Amazon Keyspaces actions support the `aws:RequestTag/${TagKey}`, the `aws:ResourceTag/${TagKey}`, and the `aws:TagKeys` condition keys. For more information, see [Amazon Keyspaces resource access based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags). 

To see a list of Amazon Keyspaces condition keys, see [Condition Keys for Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.html#amazonkeyspacesforapachecassandra-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions Defined by Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonkeyspacesforapachecassandra.html#amazonkeyspacesforapachecassandra-actions-as-permissions).

### Examples
<a name="security_iam_service-with-iam-id-based-policies-examples"></a>

To view examples of Amazon Keyspaces identity-based policies, see [Amazon Keyspaces identity-based policy examples](security_iam_id-based-policy-examples.md).

## Amazon Keyspaces resource-based policies
<a name="security_iam_service-with-iam-resource-based-policies"></a>

Amazon Keyspaces does not support resource-based policies. To view an example of a detailed resource-based policy page, see [https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html).

## Authorization based on Amazon Keyspaces tags
<a name="security_iam_service-with-iam-tags"></a>

You can manage access to your Amazon Keyspaces resources by using tags. To manage resource access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `cassandra:ResourceTag/{{key-name}}`, `aws:RequestTag/{{key-name}}`, or `aws:TagKeys` condition keys. For more information about tagging Amazon Keyspaces resources, see [Working with tags and labels for Amazon Keyspaces resources](tagging-keyspaces.md).

To view example identity-based policies for limiting access to a resource based on the tags on that resource, see [Amazon Keyspaces resource access based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags).

## Amazon Keyspaces IAM roles
<a name="security_iam_service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

### Using temporary credentials with Amazon Keyspaces
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, to assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html). 

Amazon Keyspaces supports using temporary credentials with the AWS Signature Version 4 (SigV4) authentication plugin available from the Github repo for the following languages:
+ Java: [https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin).
+ Node.js: [https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin).
+ Python: [https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin).
+ Go: [https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin).

For examples and tutorials that implement the authentication plugin to access Amazon Keyspaces programmatically, see [Using a Cassandra client driver to access Amazon Keyspaces programmatically](programmatic.drivers.md). 

### Service-linked roles
<a name="security_iam_service-with-iam-roles-service-linked"></a>

[Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow AWS services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. An IAM administrator can view but not edit the permissions for service-linked roles.

For details about creating or managing Amazon Keyspaces service-linked roles, see **[Using service-linked roles for Amazon Keyspaces](using-service-linked-roles.md)**.

### Service roles
<a name="security_iam_service-with-iam-roles-service"></a>

Amazon Keyspaces does not support service roles.