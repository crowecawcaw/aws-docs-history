For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# How Amazon Timestream for LiveAnalytics works with

IAM

Before you use IAM to manage access to Timestream for LiveAnalytics, you should understand what
IAM features are available to use with Timestream for LiveAnalytics. To get a high-level view of how
Timestream for LiveAnalytics and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Timestream for LiveAnalytics
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Timestream for LiveAnalytics
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  Timestream for LiveAnalytics tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Timestream for LiveAnalytics IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Timestream for LiveAnalytics

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Timestream for LiveAnalytics supports specific actions and resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

You can specify the following actions in the Action element of an IAM policy
statement. Use policies to grant permissions to perform an operation in AWS. When you
use an action in a policy, you usually allow or deny access to the API operation, CLI
command or SQL command with the same name.

In some cases, a single action controls access to an API operation as well as SQL
command. Alternatively, some operations require several different actions.

For a list of supported Timestream for LiveAnalytics `Action`'s, see the table
below:

###### Note

For all database-specific `Actions`, you can specify a database ARN
to limit the action to a particular database.

| Actions           | Description                                                                                                                                                                                                                                                                              | Access level | Resource types (\*required) |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------------- |
| DescribeEndpoints | Returns the Timestream endpoint that subsequent requests must be<br>made to.                                                                                                                                                                                                             | All          | \*                          |
| Select            | Run queries on Timestream that select data from one or more tables.<br>[See this note for a detailed explanation](#security_iam_service-with-iam-id-based-policies-actions.select-vs-selectvalues "#security_iam_service-with-iam-id-based-policies-actions.select-vs-selectvalues")     | Read         | table\*                     |
| CancelQuery       | Cancel a query.                                                                                                                                                                                                                                                                          | Read         | \*                          |
| ListTables        | Get the list of tables.                                                                                                                                                                                                                                                                  | List         | database\*                  |
| ListDatabases     | Get the list of databases.                                                                                                                                                                                                                                                               | List         | \*                          |
| ListMeasures      | Get the list of measures.                                                                                                                                                                                                                                                                | Read         | table\*                     |
| DescribeTable     | Get the table description.                                                                                                                                                                                                                                                               | Read         | table\*                     |
| DescribeDatabase  | Get the database description.                                                                                                                                                                                                                                                            | Read         | database\*                  |
| SelectValues      | Run queries that do not require a particular resource to be<br>specified. [See this note for a detailed explanation](#security_iam_service-with-iam-id-based-policies-actions.select-vs-selectvalues "#security_iam_service-with-iam-id-based-policies-actions.select-vs-selectvalues"). | Read         | \*                          |
| WriteRecords      | Insert data into Timestream.                                                                                                                                                                                                                                                             | Write        | table\*                     |
| CreateTable       | Create a table.                                                                                                                                                                                                                                                                          | Write        | database\*                  |
| CreateDatabase    | Create a database.                                                                                                                                                                                                                                                                       | Write        | \*                          |
| DeleteDatabase    | Delete a database.                                                                                                                                                                                                                                                                       | Write        | \*                          |
| UpdateDatabase    | Update a database.                                                                                                                                                                                                                                                                       | Write        | \*                          |
| DeleteTable       | Delete a table.                                                                                                                                                                                                                                                                          | Write        | database\*                  |
| UpdateTable       | Update a table.                                                                                                                                                                                                                                                                          | Write        | database\*                  |

#### SelectValues vs. select:

`SelectValues` is an `Action` that is used for queries
that _do not_ require a resource. An example of a query that
does not require a resource is as follows:

```
SELECT 1
```

Notice that this query does not refer to a particular Timestream for LiveAnalytics resource. Consider
another example:

```
SELECT now()
```

This query returns the current timestamp using the `now()` function,
but does not require a resource to be specified. `SelectValues` is
often used for testing, so that Timestream for LiveAnalytics can run queries without resources. Now,
consider a `Select` query:

```
SELECT * FROM database.table
```

This type of query requires a resource, specifcially an Timestream for LiveAnalytics `table`
, so that the specified data can be fetched from the table.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

In Timestream for LiveAnalytics databases and tables can be used in the `Resource` element of
IAM permissions.

The Timestream for LiveAnalytics database resource has the following ARN:

```
arn:${Partition}:timestream:${Region}:${Account}:database/${DatabaseName}
```

The Timestream for LiveAnalytics table resource has the following ARN:

```
arn:${Partition}:timestream:${Region}:${Account}:database/${DatabaseName}/table/${TableName}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `database` keyspace in your statement, use
the following ARN:

```
"Resource": "arn:aws:timestream:us-east-1:123456789012:database/mydatabase"
```

To specify all databases that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:timestream:us-east-1:123456789012:database/*"
```

Some Timestream for LiveAnalytics actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

### Condition keys

Timestream for LiveAnalytics does not provide any service-specific condition keys, but it does
support using some global condition keys. To see all AWS global condition keys, see
[AWS Global
Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

### Examples

To view examples of Timestream for LiveAnalytics identity-based policies, see [Amazon Timestream for LiveAnalytics identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Timestream for LiveAnalytics

resource-based policies

Timestream for LiveAnalytics does not support resource-based policies. To view an example of a
detailed resource-based policy page, see [https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md").

## Authorization based on

Timestream for LiveAnalytics tags

You can manage access to your Timestream for LiveAnalytics resources by using tags. To manage
resource access based on tags, you provide tag information in the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`timestream:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging
Timestream for LiveAnalytics resources, see [Adding tags and labels to resources](tagging-keyspaces.md "tagging-keyspaces.md").

To view example identity-based policies for limiting access to a resource based on
the tags on that resource, see [Timestream for LiveAnalytics resource
access based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags").

## Timestream for LiveAnalytics IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with Timestream for LiveAnalytics

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

### Service-linked

roles

Timestream for LiveAnalytics does not support service-linked roles.

### Service roles

Timestream for LiveAnalytics does not support service roles.
