# Identity-based policy examples

for AWS Glue

By default, users and roles don't have permission to create or modify AWS Glue
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by AWS Glue, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Glue](../../../service-authorization/latest/reference/list_awsglue.md "../../../service-authorization/latest/reference/list_awsglue.md") in the _Service Authorization Reference_.

###### Note

The examples provided in this section all use the `us-west-2` Region.
You can replace this with the AWS Region that you want to use.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Resource-level permissions
  only apply to specific AWS Glue objects](#glue-identity-based-policy-limitations "#glue-identity-based-policy-limitations")
- [Using the AWS Glue
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow
  users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Grant read-only permission to a table](#security_iam_id-based-policy-examples-read-only-table-access "#security_iam_id-based-policy-examples-read-only-table-access")
- [Filter tables by GetTables permission](#security_iam_id-based-policy-examples-filter-tables "#security_iam_id-based-policy-examples-filter-tables")
- [Grant full access to a table and all partitions](#security_iam_id-based-policy-examples-full-access-tables-partitions "#security_iam_id-based-policy-examples-full-access-tables-partitions")
- [Control access by name prefix and explicit denial](#security_iam_id-based-policy-examples-deny-by-name-prefix "#security_iam_id-based-policy-examples-deny-by-name-prefix")
- [Grant access using
  tags](#tags-control-access-example-triggers-allow "#tags-control-access-example-triggers-allow")
- [Deny access using
  tags](#tags-control-access-example-triggers-deny "#tags-control-access-example-triggers-deny")
- [Use tags with list
  and batch API operations](#tags-control-access-example-triggers-list-batch "#tags-control-access-example-triggers-list-batch")
- [Control settings using
  condition keys or context keys](#glue-identity-based-policy-condition-keys "#glue-identity-based-policy-condition-keys")
- [Deny an identity the ability to create data preview sessions](#deny-data-preview-sessions-per-identity "#deny-data-preview-sessions-per-identity")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS Glue resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Resource-level permissions

only apply to specific AWS Glue objects

You can only define fine-grained control for specific objects in
AWS Glue. Therefore you must write your client's IAM policy so that
API operations that allow Amazon Resource Names (ARNs) for the `Resource`
statement are not mixed with API operations that don't allow ARNs.

For example, the following IAM policy allows API operations for
`GetClassifier` and `GetJobRun`. It defines the
`Resource` as `*` because AWS Glue doesn't allow
ARNs for classifiers and job runs. Because ARNs are allowed for specific API
operations such as `GetDatabase` and `GetTable`, ARNs can be
specified in the second half of the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetClassifier*",
 "glue:GetJobRun*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:Get*"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/default",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/default/e*1*",
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/connection2"
 ]
 }
 ]
}`

```

For a list of AWS Glue objects that allow ARNs, see [Specifying AWS Glue Resource ARNs](glue-specifying-resource-arns.md "glue-specifying-resource-arns.md").

## Using the AWS Glue

console

To access the AWS Glue console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the AWS Glue resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the AWS Glue console, also attach
the AWS Glue `ConsoleAccess` or
`ReadOnly` AWS managed policy to the
entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

For a user to work with the AWS Glue console, that user must have a
minimum set of permissions that allows them to work with the AWS Glue
resources for their AWS account. In addition to these AWS Glue
permissions, the console requires permissions from the following services:

- Amazon CloudWatch Logs permissions to display logs.
- AWS Identity and Access Management (IAM) permissions to list and pass roles.
- AWS CloudFormation permissions to work with stacks.
- Amazon Elastic Compute Cloud (Amazon EC2) permissions to list VPCs, subnets, security groups,
  instances, and other objects.
- Amazon Simple Storage Service (Amazon S3) permissions to list buckets and objects, and to retrieve and
  save scripts.
- Amazon Redshift permissions to work with clusters.
- Amazon Relational Database Service (Amazon RDS) permissions to list instances.

For more information about the permissions that users require to view and work
with the AWS Glue console, see [Step 3: Attach a policy to users or groups that access AWS Glue](attach-policy-iam-user.md "attach-policy-iam-user.md").

If you create an IAM policy that is more restrictive than the minimum required
permissions, the console won't function as intended for users with that IAM policy.
To ensure that those users can still use the AWS Glue console, also
attach the `AWSGlueConsoleFullAccess` managed policy as described in [AWS managed (predefined) policies for
AWS Glue](security-iam-awsmanpol.md#access-policy-examples-aws-managed "security-iam-awsmanpol.md#access-policy-examples-aws-managed").

## Allow

users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Grant read-only permission to a table

The following policy grants read-only permission to a `books` table in
database `db1`. For more information about resource Amazon Resource Names
(ARNs), see [Data Catalog ARNs](glue-specifying-resource-arns.md#data-catalog-resource-arns "glue-specifying-resource-arns.md#data-catalog-resource-arns").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetTablesActionOnBooks",
 "Effect": "Allow",
 "Action": [
 "glue:GetTables",
 "glue:GetTable"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/db1",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/books"
 ]
 }
 ]
}`

```

This policy grants read-only permission to a table named `books` in the
database named `db1`. To grant `Get` permission to a table,
permission to the catalog and database resources is also required.

The following policy grants the minimum necessary permissions to create table
`tb1` in database `db1`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateTable"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/tbl1",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/db1",
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog"
 ]
 }
 ]
}`

```

## Filter tables by GetTables permission

Assume that there are three tables—`customers`,
`stores`, and `store_sales`—in database `db1`.
The following policy grants `GetTables` permission to `stores` and
`store_sales`, but not to `customers`. When you call
`GetTables` with this policy, the result contains only the two authorized
tables (the `customers` table is not returned).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetTablesExample",
 "Effect": "Allow",
 "Action": [
 "glue:GetTables"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/db1",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/store_sales",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/stores"
 ]
 }
 ]
}`

```

You can simplify the preceding policy by using `store*` to match any table
names that start with `store`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetTablesExample2",
 "Effect": "Allow",
 "Action": [
 "glue:GetTables"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/db1",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/store*"
 ]
 }
 ]
}`

```

Similarly, using `/db1/*` to match all tables in `db1`, the
following policy grants `GetTables` access to all the tables in
`db1`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetTablesReturnAll",
 "Effect": "Allow",
 "Action": [
 "glue:GetTables"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/db1",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/*"
 ]
 }
 ]
}`

```

If no table ARN is provided, a call to `GetTables` succeeds, but it
returns an empty list.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetTablesEmptyResults",
 "Effect": "Allow",
 "Action": [
 "glue:GetTables"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/db1"
 ]
 }
 ]
}`

```

If the database ARN is missing in the policy, a call to `GetTables` fails
with an `AccessDeniedException`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GetTablesAccessDeny",
 "Effect": "Allow",
 "Action": [
 "glue:GetTables"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/*"
 ]
 }
 ]
}`

```

## Grant full access to a table and all partitions

The following policy grants all permissions on a table named `books` in
database `db1`. This includes read and write permissions on the table itself,
on archived versions of it, and on all its partitions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "FullAccessOnTable",
 "Effect": "Allow",
 "Action": [
 "glue:CreateTable",
 "glue:GetTable",
 "glue:GetTables",
 "glue:UpdateTable",
 "glue:DeleteTable",
 "glue:BatchDeleteTable",
 "glue:GetTableVersion",
 "glue:GetTableVersions",
 "glue:DeleteTableVersion",
 "glue:BatchDeleteTableVersion",
 "glue:CreatePartition",
 "glue:BatchCreatePartition",
 "glue:GetPartition",
 "glue:GetPartitions",
 "glue:BatchGetPartition",
 "glue:UpdatePartition",
 "glue:DeletePartition",
 "glue:BatchDeletePartition"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/db1",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/books"
 ]
 }
 ]
}`

```

The preceding policy can be simplified in practice.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "FullAccessOnTable",
 "Effect": "Allow",
 "Action": [
 "glue:*Table*",
 "glue:*Partition*"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/db1",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/db1/books"
 ]
 }
 ]
}`

```

Notice that the minimum granularity of fine-grained access control is at the table
level. This means that you can't grant a user access to some partitions in a table but
not others, or to some table columns but not to others. A user either has access to all
of a table, or to none of it.

## Control access by name prefix and explicit denial

In this example, suppose that the databases and tables in your AWS Glue Data Catalog are
organized using name prefixes. The databases in the development stage have the name
prefix `dev-`, and those in production have the name prefix
`prod-`. You can use the following policy to grant developers full access
to all databases, tables, UDFs, and so on, that have the `dev-` prefix. But
you grant read-only access to everything with the `prod-` prefix.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DevAndProdFullAccess",
 "Effect": "Allow",
 "Action": [
 "glue:*Database*",
 "glue:*Table*",
 "glue:*Partition*",
 "glue:*UserDefinedFunction*",
 "glue:*Connection*"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:catalog",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/dev-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:database/prod-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/dev-*/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/*/dev-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/prod-*/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/*/prod-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:userDefinedFunction/dev-*/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:userDefinedFunction/*/dev-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:userDefinedFunction/prod-*/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:userDefinedFunction/*/prod-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/dev-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/prod-*"
 ]
 },
 {
 "Sid": "ProdWriteDeny",
 "Effect": "Deny",
 "Action": [
 "glue:*Create*",
 "glue:*Update*",
 "glue:*Delete*"
 ],
 "Resource": [
 "arn:aws:glue:`us-east-1`:`111122223333`:database/prod-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/prod-*/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:table/*/prod-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:userDefinedFunction/prod-*/*",
 "arn:aws:glue:`us-east-1`:`111122223333`:userDefinedFunction/*/prod-*",
 "arn:aws:glue:`us-east-1`:`111122223333`:connection/prod-*"
 ]
 }
 ]
}`

```

The second statement in the preceding policy uses explicit `deny`. You can
use explicit `deny` to overwrite any `allow` permissions that are
granted to the principal. This lets you lock down access to critical resources and
prevent another policy from accidentally granting access to them.

In the preceding example, even though the first statement grants full access to
`prod-` resources, the second statement explicitly revokes write access to
them, leaving only read access to `prod-` resources.

## Grant access using

tags

For example, suppose that you want to limit access to a trigger `t2` to
a specific user named `Tom` in your account. All other users, including
`Sam`, have access to trigger `t1`. The triggers
`t1` and `t2` have the following properties.

```
aws glue get-triggers
{
    "Triggers": [
        {
            "State": "CREATED",
            "Type": "SCHEDULED",
            "Name": "t1",
            "Actions": [
                {
                    "JobName": "j1"
                }
            ],
            "Schedule": "cron(0 0/1 * * ? *)"
        },
        {
            "State": "CREATED",
            "Type": "SCHEDULED",
            "Name": "t2",
            "Actions": [
                {
                    "JobName": "j1"
                }
            ],
            "Schedule": "cron(0 0/1 * * ? *)"
        }
    ]
}
```

The AWS Glue administrator attached a tag value `Tom`
(`aws:ResourceTag/Name": "Tom"`) to trigger `t2`. The
AWS Glue administrator also gave Tom an IAM policy with a condition
statement based on the tag. As a result, Tom can only use an AWS Glue
operation that acts on resources with the tag value `Tom`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "glue:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Name": "Tom"
 }
 }
 }
 ]
}`

```

When Tom tries to access the trigger `t1`, he receives an access denied
message. Meanwhile, he can successfully retrieve trigger `t2`.

```
aws glue get-trigger --name t1

An error occurred (AccessDeniedException) when calling the GetTrigger operation: User: Tom is not authorized to perform: glue:GetTrigger on resource: arn:aws:glue:us-east-1:123456789012:trigger/t1

aws glue get-trigger --name t2
{
    "Trigger": {
        "State": "CREATED",
        "Type": "SCHEDULED",
        "Name": "t2",
        "Actions": [
            {
                "JobName": "j1"
            }
        ],
        "Schedule": "cron(0 0/1 * * ? *)"
    }
}
```

Tom can't use the plural `GetTriggers` API operation to list triggers
because this operation doesn't support filtering on tags.

To give Tom access to `GetTriggers`, the AWS Glue
administrator creates a policy that splits the permissions into two sections. One
section allows Tom access to all triggers with the `GetTriggers` API
operation. The second section allows Tom access to API operations that are tagged
with the value `Tom`. With this policy, Tom is allowed both
`GetTriggers` and `GetTrigger` access to trigger
`t2`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "glue:GetTriggers",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "glue:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Name": "Tom"
 }
 }
 }
 ]
}`

```

## Deny access using

tags

Another resource policy approach is to explicitly deny access to resources.

###### Important

An explicit denial policy does not work for plural API operations such as
`GetTriggers`.

In the following example policy, all AWS Glue job operations are
allowed. However, the second `Effect` statement _explicitly_ denies access to jobs tagged with the `Team` key
and `Special` value.

When an administrator attaches the following policy to an identity, the identity
can access all jobs _except_ those tagged with the
`Team` key and `Special` value.

## Use tags with list

and batch API operations

A third approach to writing a resource policy is to allow access to resources
using a `List` API operation to list out resources for a tag value. Then,
use the corresponding `Batch` API operation to allow access to details of
specific resources. With this approach, the administrator doesn't need to allow
access to the plural `GetCrawlers`, `GetDevEndpoints`,
`GetJobs`, or `GetTriggers` API operations. Instead, you can
allow the ability to list the resources with the following API operations:

- `ListCrawlers`
- `ListDevEndpoints`
- `ListJobs`
- `ListTriggers`

And, you can allow the ability to get details about individual resources with the
following API operations:

- `BatchGetCrawlers`
- `BatchGetDevEndpoints`
- `BatchGetJobs`
- `BatchGetTriggers`

As an administrator, to use this approach, you can do the following:

1. Add tags to your crawlers, development endpoints, jobs, and triggers.
2. Deny user access to `Get` API operations such as
   `GetCrawlers`, `GetDevEndponts`, `GetJobs`,
   and `GetTriggers`.
3. To enable users to find out which tagged resources they have access to,
   allow user access to `List` API operations such as
   `ListCrawlers`, `ListDevEndponts`,
   `ListJobs`, and `ListTriggers`.
4. Deny user access to AWS Glue tagging APIs, such as
   `TagResource` and `UntagResource`.
5. Allow user access to resource details with `BatchGet` API
   operations such as `BatchGetCrawlers`,
   `BatchGetDevEndponts`, `BatchGetJobs`, and
   `BatchGetTriggers`.

For example, when calling the `ListCrawlers` operation, provide a tag
value to match the user name. Then the result is a list of crawlers that match the
provided tag values. Provide the list of names to `BatchGetCrawlers` to
get details about each crawler with the given tag.

For example, if Tom should only be able to retrieve details of triggers that are
tagged with `Tom`, the administrator can add tags to triggers for
`Tom`, deny access to the `GetTriggers` API operation to all
users, and allow access to all users to `ListTriggers` and
`BatchGetTriggers`.

The following is the resource policy that the AWS Glue administrator
grants to Tom. In the first section of the policy, AWS Glue API
operations are denied for `GetTriggers`. In the second section of the
policy, `ListTriggers` is allowed for all resources. However, in the third
section, those resources tagged with `Tom` are allowed access with the
`BatchGetTriggers` access.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "glue:GetTriggers",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:ListTriggers"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:BatchGetTriggers"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Name": "Tom"
 }
 }
 }
 ]
}`

```

Using the same triggers as the previous example, Tom can access trigger
`t2`, but not trigger `t1`. The following example shows the
results when Tom tries to access `t1` and `t2` with
`BatchGetTriggers`.

```
aws glue batch-get-triggers --trigger-names t2
{
    "Triggers": {
        "State": "CREATED",
        "Type": "SCHEDULED",
        "Name": "t2",
        "Actions": [
            {
                "JobName": "j2"
            }
        ],
        "Schedule": "cron(0 0/1 * * ? *)"
    }
}

aws glue batch-get-triggers  --trigger-names t1

An error occurred (AccessDeniedException) when calling the BatchGetTriggers operation: No access to any requested resource.

```

The following example shows the results when Tom tries to access both trigger
`t2` and trigger `t3` (which does not exist) in the same
`BatchGetTriggers` call. Notice that because Tom has access to trigger
`t2` and it exists, only `t2` is returned. Although Tom is
allowed to access trigger `t3`, trigger `t3` does not exist, so
`t3` is returned in the response in a list of `"TriggersNotFound":
 []`.

```
aws glue batch-get-triggers --trigger-names t2 t3
{
    "Triggers": {
        "State": "CREATED",
        "Type": "SCHEDULED",
        "Name": "t2",
        "Actions": [
            {
                "JobName": "j2"
            }
        ],
        "TriggersNotFound": ["t3"],
        "Schedule": "cron(0 0/1 * * ? *)"
    }
}
```

## Control settings using

condition keys or context keys

You can use condition keys or context keys when granting permissions to create and
update jobs. These sections discuss the keys:

- [Control policies
  that control settings using condition keys](#glue-identity-based-policy-condition-key-vpc "#glue-identity-based-policy-condition-key-vpc")
- [Control policies
  that control settings using context keys](#glue-identity-based-policy-context-key-glue "#glue-identity-based-policy-context-key-glue")

### Control policies

that control settings using condition keys

AWS Glue provides three IAM condition keys `glue:VpcIds`,
`glue:SubnetIds`, and `glue:SecurityGroupIds`. You can
use the condition keys in IAM policies when granting permissions to create and
update jobs. You can use this setting to ensure that jobs or sessions are not created (or
updated to) to run outside of a desired VPC environment. The VPC setting
information is not a direct input from the `CreateJob` request, but
inferred from the job "connections" field that points to an AWS Glue
connection.

###### Example usage

Create an AWS Glue network type connection named
"traffic-monitored-connection" with the desired VpcId "vpc-id1234", SubnetIds,
and SecurityGroupIds.

Specify the condition keys condition for the `CreateJob` and `UpdateJob`
action in the IAM policy.

```
{
  "Effect": "Allow",
  "Action": [
    "glue:CreateJob",
    "glue:UpdateJob"
  ],
  "Resource": [
    "*"
  ],
  "Condition": {
    "ForAnyValue:StringLike": {
      "glue:VpcIds": [
        "vpc-id1234"
      ]
    }
  }
}

```

You can create a similar IAM policy to prohibit creating an
AWS Glue job without specifying connection information.

**Restricting sessions on VPCs**

To enforce created sessions to run
within a specified VPC, you restrict role permission by adding a `Deny` effect on the `glue:CreateSession` action
with the condition that the glue:vpc-id not equal to vpc-<123>. For example:

```
"Effect": "Deny",
"Action": [
    "glue:CreateSession"
 ],
"Condition": {
    "StringNotEquals" : {"glue:VpcIds" : ["vpc-123"]}
}

```

You also can enforce created sessions to run within a VPC by adding a `Deny` effect on the `glue:CreateSession` action
with the condition that the `glue:vpc-id` is null. For example:

```
{
    "Effect": "Deny",
    "Action": [
        "glue:CreateSession"
    ],
      "Condition": {
        "Null": {"glue:VpcIds": true}
    }
},
{
    "Effect": "Allow",
    "Action": [
        "glue:CreateSession"
    ],
    "Resource": ["*"]
}

```

### Control policies

that control settings using context keys

AWS Glue provides a context key (`glue:CredentialIssuingService=
 glue.amazonaws.com`) to each role session that AWS Glue makes
available to the job and developer endpoint. This allows you to implement security
controls for the actions taken by AWS Glue scripts.
AWS Glue provides another context key
(`glue:RoleAssumedBy=glue.amazonaws.com`) to each role session where
AWS Glue makes a call to another AWS service on the customer's
behalf (not by a job/dev endpoint, but directly by the AWS Glue
service).

###### Example usage

Specify the conditional permission in an IAM policy and attach it to the
role to be used by an AWS Glue job. This ensures certain actions
are allowed/denied based on whether the role session is used for an
AWS Glue job runtime environment.

```
{
    "Effect": "Allow",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
    "Condition": {
        "StringEquals": {
            "glue:CredentialIssuingService": "glue.amazonaws.com"
        }
    }
}

```

## Deny an identity the ability to create data preview sessions

This section contains an IAM policy example used to deny an identity the ability to create data preview sessions.
Attach this policy to the identity, which is separate from the role used by the data preview session during its run.

```
{
    "Sid": "DatapreviewDeny",
    "Effect": "Deny",
     "Action": [
           "glue:CreateSession"
     ],
     "Resource": [
          "arn:aws:glue:*:*:session/glue-studio-datapreview*"
      ]
 }
```
