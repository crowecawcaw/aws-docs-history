Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Authenticating a

scheduled query

When you schedule a query, you use one of the following authentication methods
when the SQL runs. Each method requires a different combination of input on the
query editor v2. These authentication methods are supported by the Data API which is
used to run your SQL statements.

The database user or role that is used to run the query must have the necessary
database privileges. For example, to grant `IAMR:MyRedshiftQEv2Scheduler`
privileges to table `mytable`, run the following SQL command.

```
GRANT all ON TABLE mytable TO "IAMR:MyRedshiftQEv2Scheduler";
```

To view the list of database users in your cluster or workgroup, query the system
view `PG_USER_INFO`.

###### Note

Any Redshift Serverless workgroup for which you schedule queries much be tagged with the key
`RedshiftDataFullAccess`. For more information, see [Authorizing access to the Amazon Redshift Data API](data-api-access.md "data-api-access.md").

As an alternative to tagging the workgroup, you can add an inline policy to
the IAM role (that is specified with the schedule) that allows
`redshift-serverless:GetCredentials`. For example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "UseTemporaryCredentialsForAllServerlessWorkgroups",
 "Effect": "Allow",
 "Action": "redshift-serverless:GetCredentials",
 "Resource": [
 "arn:aws:redshift-serverless:*:*:workgroup/*"
 ]
 }
 ]
}`

```

**AWS Secrets Manager**

With this method, provide a secret value for
**secret-arn** that is stored in AWS Secrets Manager. This secret
contains credentials to connect to your database. You might have created a
secret with the proper credentials when you created your cluster or
workgroup. The secret must be tagged with the key
`RedshiftDataFullAccess`. If the tag key is not already
present, use the AWS Secrets Manager console to add it. For information about creating
a secret, see [Creating a secret for
database connection credentials](redshift-secrets-manager-integration-create.md "redshift-secrets-manager-integration-create.md").

For more information about the minimum permissions, see [Creating and Managing Secrets
with AWS Secrets Manager](../../../secretsmanager/latest/userguide/managing-secrets.md "../../../secretsmanager/latest/userguide/managing-secrets.md") in the
_AWS Secrets Manager User Guide_.

**Temporary credentials**

With this method, provide your **Database name** and
**Database user** values when connecting to a database
in a cluster. You only need to provide your **Database
name** when connecting to a database in a workgroup.

When connecting to a cluster, the
`AmazonRedshiftDataFullAccess` policy allows the database
user named `redshift_data_api_user` permission for
`redshift:GetClusterCredentials`. If you want to use a
different database user to run the SQL statement, then add a policy to the
IAM role attached to your cluster to allow
`redshift:GetClusterCredentials`. The following example
policy allows database users `awsuser` and `myuser`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "UseTemporaryCredentialsForAllDbUsers",
 "Effect": "Allow",
 "Action": "redshift:GetClusterCredentials",
 "Resource": [
 "arn:aws:redshift:*:*:dbuser:*/awsuser",
 "arn:aws:redshift:*:*:dbuser:*/myuser"
 ]
 }
 ]
}`

```
