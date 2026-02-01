Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring IAM permissions

Amazon Redshift provides the `AmazonRedshiftDataFullAccess` managed policy. This
policy provides full access to Amazon Redshift Data API operations. This policy also allows
scoped access to specific Amazon Redshift, AWS Secrets Manager, and IAM API operations needed to
authenticate and access an Amazon Redshift cluster or Redshift Serverless workgroup.

You can also create your own IAM policy that allows access to specific
resources. To create your policy, use the `AmazonRedshiftDataFullAccess`
policy as your starting template. After you create your policy, add it to each user
that requires access to the Data API.

Consider the following requirements of the IAM policy associated with the
user:

- If you use AWS Secrets Manager to authenticate, confirm the policy allows use of the
  `secretsmanager:GetSecretValue` action to retrieve the secret
  tagged with the key `RedshiftDataFullAccess`.
- If you use temporary credentials to authenticate to a cluster, confirm the
  policy allows the use of the `redshift:GetClusterCredentials`
  action to the database user name `redshift_data_api_user` for any
  database in the cluster. This user name must have already been created in
  your database.
- If you use temporary credentials to authenticate to a serverless
  workgroup, confirm the policy allows the use of the
  `redshift-serverless:GetCredentials` action to retrieve the
  workgroup tagged with the key `RedshiftDataFullAccess`. The
  database user is mapped 1:1 to the source AWS Identity and Access Management (IAM) identity. For
  example, the user sample_user is mapped to database user
  `IAM:sample_user`, and IAM role sample_role is mapped to
  `IAMR:sample_role`.

For more information about IAM identities, see [IAM Identities (users, user groups,
and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the IAM User Guide.

- The IAM action `redshift-data:GetStatementResult` allows
  access to both `GetStatementResult` and
  `GetStatementResultV2` API operations.
  The following links provide more information about AWS Identity and Access Management in the
  _IAM User Guide_.

- For information about creating an IAM roles, see [Creating IAM roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md").
- For information about creating an IAM policy, see [Creating IAM
  policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").
- For information about adding an IAM policy to a user, see [Adding and
  removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

## Run a query on a cluster

that is owned by another account

To run a query on a cluster that is owned by another account, the owning
account must provide an IAM role that the Data API can assume in the
calling account. For example, suppose Account B owns a cluster that Account A
needs to access. Account B can attach the AWS managed policy
`AmazonRedshiftDataFullAccess` to Account B's IAM role. Then
Account B trusts Account A using a trust policy such as the
following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:role/someRoleA"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Finally, the Account A IAM role needs to be able to assume the Account B
IAM role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/someRoleB"
 }
}`

```

## Specify an IAM role that

restricts resources to Redshift Serverless workgroups and Amazon Redshift clusters in an
AWS account

You can specify resource ARNs in your identity-based policy to control access
to Redshift Serverless workgroups and Amazon Redshift clusters in an AWS account. This example shows
how you might create a policy that allows access to the Data API for only
the workgroup and clusters in the specified AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "redshift-data:CancelStatement",
 "redshift-data:DescribeStatement",
 "redshift-data:GetStatementResult",
 "redshift-data:ListStatements"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "redshift-data:*",
 "Resource": [
 "arn:aws:redshift:`us-east-1`:`111122223333`:workgroup/*",
 "arn:aws:redshift:`us-east-1`:`111122223333`:cluster:*"
 ]
 }
 ]
}`

```

## Configure an IAM policy

that restricts access to SQL statement information to only the statement
owner

By default, Amazon Redshift Data API treats the IAM role used when calling
`ExecuteStatement` and `BatchExecuteStatement` as the
owner of the SQL statement. Anyone who is allowed to assume the role is able to
access information about the SQL statement, including its results. To restrict
SQL statement information access to an IAM role session with a particular
owner, add condition `redshift-data:statement-owner-iam-userid:
 "${aws:userid}"`. The following IAM policy restricts access.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "redshift-data:CancelStatement",
 "redshift-data:DescribeStatement",
 "redshift-data:GetStatementResult",
 "redshift-data:ListStatements"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "redshift-data:statement-owner-iam-userid": "${aws:userid}"
 }
 }
 }
 ]
}`

```

You can use the condition `statement-owner-iam-userid` with
`CancelStatement`, `DescribeStatement`,
`GetStatementResult`, and `ListStatements`. For more
information, see [Actions defined by Amazon Redshift Data API](../../../service-authorization/latest/reference/list_amazonredshiftdataapi.md#amazonredshiftdataapi-redshift-data_statement-owner-iam-userid "../../../service-authorization/latest/reference/list_amazonredshiftdataapi.md#amazonredshiftdataapi-redshift-data_statement-owner-iam-userid").

## Configure an IAM policy that

restricts access to SQL results to only the session owner

By default, Amazon Redshift Data API treats the IAM role used when calling
`ExecuteStatement` and `BatchExecuteStatement` as the
owner of the database session that runs the SQL statement. Anyone who is allowed
to assume the role is able to submit queries to the database session. To
restrict session access to an IAM role session with a particular owner, add
condition `redshift-data:session-owner-iam-userid: "${aws:userid}"`.
The following IAM policy restricts access.

The following IAM policy allows only the session owner to get statement
results. The condition `session-owner-iam-userid` is used to limit
resource access to the specified `userid`.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "redshift-data:ExecuteStatement",
 "redshift-data:BatchExecuteStatement"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "redshift-data:session-owner-iam-userid": "${aws:userid}"
 }
 }
 }
 ]
}`

```

You can use the condition `session-owner-iam-userid` with
`ExecuteStatement` and `BatchExecuteStatement`. For
more information, see [Actions defined by Amazon Redshift Data API](../../../service-authorization/latest/reference/list_amazonredshiftdataapi.md#amazonredshiftdataapi-redshift-data_statement-owner-iam-userid "../../../service-authorization/latest/reference/list_amazonredshiftdataapi.md#amazonredshiftdataapi-redshift-data_statement-owner-iam-userid").
