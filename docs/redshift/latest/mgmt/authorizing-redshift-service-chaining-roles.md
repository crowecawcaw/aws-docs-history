Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Chaining IAM roles in

Amazon Redshift

When you attach a role to your cluster, your cluster can assume that role to access
Amazon S3, Amazon Athena, AWS Glue, and AWS Lambda on your behalf. If a role attached to your cluster
doesn't have access to the necessary resources, you can chain another role,
possibly belonging to another account. Your cluster then temporarily assumes the chained
role to access the data. You can also grant cross-account access by chaining roles. Each
role in the chain assumes the next role in the chain, until the cluster assumes the role
at the end of chain. The maximum number of IAM roles that you can associate is subject
to a quota. For more information, see the quota "Cluster IAM roles for Amazon Redshift to access
other AWS services" in [Quotas for Amazon Redshift objects](amazon-redshift-limits.md#amazon-redshift-limits-quota "amazon-redshift-limits.md#amazon-redshift-limits-quota").

###### Note

You must specify the IAM roles in order for the chain to work correctly.

For example, suppose Company A wants to access data in an Amazon S3 bucket that
belongs to Company B. Company A creates an AWS service role for Amazon Redshift named
`RoleA` and attaches it to their cluster. Company B creates a role named
`RoleB` that's authorized to access the data in the Company B
bucket. To access the data in the Company B bucket, Company A runs a COPY command using
an `iam_role` parameter that chains `RoleA` and
`RoleB`. For the duration of the COPY operation, `RoleA`
temporarily assumes `RoleB` to access the Amazon S3 bucket.

To chain roles, you establish a trust relationship between the roles. A role that
assumes another role (for example, `RoleA`) must have a permissions policy
that allows it to assume the next chained role (for example, `RoleB`). In
turn, the role that passes permissions (`RoleB`) must have a trust policy
that allows it to pass its permissions to the previous chained role
(`RoleA`). For more information, see [Using IAM roles](../../../IAM/latest/UserGuide/id_roles_use.md "../../../IAM/latest/UserGuide/id_roles_use.md") in the
IAM User Guide.

The first role in the chain must be a role attached to the cluster. The first role,
and each subsequent role that assumes the next role in the chain, must have a policy
that includes a specific statement. This statement has the `Allow` effect on
the `sts:AssumeRole` action and the Amazon Resource Name (ARN) of the next
role in a `Resource` element. In our example, `RoleA` has the
following permission policy that allows it to assume `RoleB`, owned by AWS
account `210987654321`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt1487639602000",
 "Effect": "Allow",
 "Action": [
 "sts:AssumeRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/RoleB"
 }
 ]
}`

```

A role that passes to another role must establish a trust relationship with the role
that assumes the role or with the AWS account that owns the role. In our example,
`RoleB` has the following trust policy to establish a trust relationship
with `RoleA`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/RoleA"
 }
 }
 ]
}`

```

The following trust policy establishes a trust relationship with the owner of
`RoleA`, AWS account `123456789012`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:root"
 }
 }
 ]
}`

```

###### Note

To restrict role chaining authorization to specific users, define a condition. For
more information, see [Restricting access to IAM
roles](authorizing-redshift-service-database-users.md "authorizing-redshift-service-database-users.md").

When you run an UNLOAD, COPY, CREATE EXTERNAL FUNCTION, or CREATE EXTERNAL SCHEMA
command, you chain roles by including a comma-separated list of role ARNs in the
`iam_role` parameter. The following shows the syntax for chaining roles
in the `iam_role` parameter.

```
unload ('select * from venue limit 10')
to 's3://acmedata/redshift/venue_pipe_'
IAM_ROLE 'arn:aws:iam::<`aws-account-id-1`>:role/<`role-name-1`>[,arn:aws:iam::<`aws-account-id-2`>:role/<`role-name-2`>][,...]';
```

###### Note

The entire role chain is enclosed in single quotes and must not contain
spaces.

In the following examples, `RoleA` is attached to the cluster belonging to
AWS account `123456789012`. `RoleB`, which belongs to account
`210987654321`, has permission to access the bucket named
`s3://companyb/redshift/`. The following example chains
`RoleA` and `RoleB` to UNLOAD data to the
s3://companyb/redshift/ bucket.

```
unload ('select * from venue limit 10')
to 's3://companyb/redshift/venue_pipe_'
iam_role 'arn:aws:iam::123456789012:role/RoleA,arn:aws:iam::210987654321:role/RoleB';
```

The following example uses a COPY command to load the data that was unloaded in the
previous example.

```
copy venue
from 's3://companyb/redshift/venue_pipe_'
iam_role 'arn:aws:iam::123456789012:role/RoleA,arn:aws:iam::210987654321:role/RoleB';
```

In the following example, CREATE EXTERNAL SCHEMA uses chained roles to assume the role
`RoleB`.

```
create external schema spectrumexample from data catalog
database 'exampledb' region 'us-west-2'
iam_role 'arn:aws:iam::123456789012:role/RoleA,arn:aws:iam::210987654321:role/RoleB';
```

In the following example, CREATE EXTERNAL FUNCTION uses chained roles to assume the
role `RoleB`.

```
create external function lambda_example(varchar)
returns varchar
volatile
lambda 'exampleLambdaFunction'
iam_role 'arn:aws:iam::123456789012:role/RoleA,arn:aws:iam::210987654321:role/RoleB';
```
