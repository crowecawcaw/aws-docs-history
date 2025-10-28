# Setting up database credentials for RDS Proxy

RDS Proxy in Amazon RDS uses AWS Secrets Manager to store and manage database credentials securely.
Instead of embedding credentials in your application, you associate a proxy with a Secrets Manager
secret that contains the necessary authentication details. You create a separate Secrets Manager
secret for each database user account that the proxy connects to on the Aurora DB
cluster.

Alternatively, you can configure RDS Proxy to use end-to-end IAM authentication,
which eliminates the need to store database credentials in Secrets Manager. RDS Proxy uses IAM authentication
for both client-to-proxy and proxy-to-database connections. This provides a fully integrated
IAM-based authentication solution that doesn't require managing secrets or passwords.
For information about adding a new IAM DB user, see [Creating a database account using
IAM authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md").

###### Topics

- [Creating secrets to use with RDS Proxy](#rds-proxy-secrets-create "#rds-proxy-secrets-create")

## Creating secrets to use with RDS Proxy

Before you create a proxy, you must first create at least one secret that stores your
database credentials.

###### To create a secret

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. Choose **Credentials for Amazon RDS database**.
4. Enter a user name and password. The credentials that you enter must match the
   credentials of a database user that exists in the associated RDS database. RDS Proxy
   uses these credentials to authenticate and establish connections to the database on
   behalf of applications.

If there's a mismatch, you can update the secret to match the database password.
Until you update the secret, attempts to connect through the proxy using that secret
fail, but connections using other valid secrets still work.

###### Note

For RDS for SQL Server, RDS Proxy requires a case-sensitive secret in Secrets Manager, regardless of
the DB instance collation settings. If your application allows usernames with
different capitalizations, such as "Admin" and "admin," you must create separate
secrets for each. RDS Proxy doesn't support case-insensitive username authentication
between the client and proxy.

For more information about collation in SQL Server, see the [Microsoft SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver16 "https://docs.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver16")
documentation. 5. For **Database**, select the Amazon RDS database that the secret will
access. 6. Fill in other settings for the secret, then choose **Store**. For
comprehensive instructions, see [Creating an AWS Secrets Manager
secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_.
When you create a proxy through the AWS CLI, you specify the Amazon Resource Names
(ARNs) of the corresponding secrets. You do so for all the DB user accounts that the
proxy can access. In the AWS Management Console, you choose the secrets by their descriptive
names.

- To create a Secrets Manager secret for use with RDS Proxy, use the [create-secret](../../../cli/latest/reference/secretsmanager/create-secret.md "../../../cli/latest/reference/secretsmanager/create-secret.md")
  command:

```
aws secretsmanager create-secret \
  --name "`secret_name`" \
  --description "`secret_description`" \
  --region `region_name` \
  --secret-string '{"username":"db_user","password":"db_user_password"}'
```

- You can also create a custom key to encrypt your Secrets Manager secret. The following command creates an example key.

```
aws kms create-key --description "`test-key`" --policy '{
  "Id":"kms-policy",
  "Version": "2012-10-17",
  "Statement":
    [
      {
        "Sid":"Enable IAM User Permissions",
        "Effect":"Allow",
        "Principal":{"AWS":"arn:aws:iam::`account_id`:root"},
        "Action":"kms:*","Resource":"*"
      },
      {
        "Sid":"Allow access for Key Administrators",
        "Effect":"Allow",
        "Principal":
          {
            "AWS":
              ["$USER_ARN","arn:aws:iam:`account_id`::role/Admin"]
          },
        "Action":
          [
            "kms:Create*",
            "kms:Describe*",
            "kms:Enable*",
            "kms:List*",
            "kms:Put*",
            "kms:Update*",
            "kms:Revoke*",
            "kms:Disable*",
            "kms:Get*",
            "kms:Delete*",
            "kms:TagResource",
            "kms:UntagResource",
            "kms:ScheduleKeyDeletion",
            "kms:CancelKeyDeletion"
          ],
        "Resource":"*"
      },
      {
        "Sid":"Allow use of the key",
        "Effect":"Allow",
        "Principal":{"AWS":"$ROLE_ARN"},
        "Action":["kms:Decrypt","kms:DescribeKey"],
        "Resource":"*"
      }
    ]
}'
```

For example, the following commands create Secrets Manager secrets for two database users:

```
aws secretsmanager create-secret \
  --name `secret_name_1` --description "db admin user" \
  --secret-string '{"username":"admin","password":"`choose_your_own_password`"}'

aws secretsmanager create-secret \
  --name `secret_name_2` --description "application user" \
  --secret-string '{"username":"app-user","password":"`choose_your_own_password`"}'
```

To create these secrets encrypted with your custom AWS KMS key, use the following commands:

```
aws secretsmanager create-secret \
  --name `secret_name_1` --description "db admin user" \
  --secret-string '{"username":"admin","password":"`choose_your_own_password`"}' \
  --kms-key-id arn:aws:kms:us-east-2:`account_id`:key/`key_id`

aws secretsmanager create-secret \
  --name `secret_name_2` --description "application user" \
  --secret-string '{"username":"app-user","password":"`choose_your_own_password`"}' \
  --kms-key-id arn:aws:kms:us-east-2:`account_id`:key/`key_id`
```

To see the secrets owned by your AWS account, use the [list-secrets](../../../cli/latest/reference/secretsmanager/list-secrets.md "../../../cli/latest/reference/secretsmanager/list-secrets.md")
command:

```
aws secretsmanager list-secrets
```

When you create a proxy using the CLI, you pass the Amazon Resource Names (ARNs)
of one or more secrets to the `--auth` parameter. The following example
shows how to prepare a report with only the name and ARN of each secret owned by your
AWS account. This example uses the `--output table` parameter that is
available in AWS CLI version 2. If you are using AWS CLI version 1, use `--output
 text` instead.

```
aws secretsmanager list-secrets --query '*[].[Name,ARN]' --output table
```

To confirm that the secret contains the correct credentials in the proper format,
use the [get-secret-value](../../../cli/latest/reference/secretsmanager/get-secret-value.md "../../../cli/latest/reference/secretsmanager/get-secret-value.md") command. Replace
`your_secret_name` with the secret’s short
name or ARN.

```
aws secretsmanager get-secret-value --secret-id `your_secret_name`
```

The output contains a line with a JSON-encoded value similar to the
following:

```
...
"SecretString": "{\"username\":\"`your_username`\",\"password\":\"`your_password`\"}",
...
```
