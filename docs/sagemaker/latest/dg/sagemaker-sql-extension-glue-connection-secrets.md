# Create secrets for database

access credentials in Secrets Manager

Before creating your connection, we recommend storing your database access credentials as
a secret in AWS Secrets Manager. Alternatively, you can generate temporary database credentials based on
permissions granted through an AWS Identity and Access Management (IAM) permissions policy to manage the access that
your users have to your database. For more information, see [Using IAM authentication to
generate database user credentials](../../../redshift/latest/mgmt/generating-user-credentials.md "../../../redshift/latest/mgmt/generating-user-credentials.md")

## Create a secret for Amazon Redshift access

credentials

###### To store Amazon Redshift information in AWS Secrets Manager

1. From the AWS Management Console, navigate to Secrets Manager.
2. Choose **Store a new secret**.
3. Under **Secret type**, choose **Credentials for
   Amazon Redshift**.
4. Enter the administrator username and password configured when launching the Amazon Redshift
   cluster.
5. Select the Amazon Redshift cluster associated with the secrets.
6. Name your secret.
7. The remaining settings can be left at their default values for initial secret
   creation, or customized if required.
8. Create the secret and retrieve its ARN.

## Create a secret for

Amazon Redshift Serverless access credentials

###### If you need to connect to Amazon Redshift Serverless, follow these steps

1. From the AWS Management Console, navigate to Secrets Manager.
2. Choose **Store a new secret**.
3. Under **Secret type**, choose **Other type of
   secret**.
4. In the **Key-value pairs**, choose **Plaintext**,
   and then copy the following JSON content. Replace the user, and password with their
   actual values:

```
{
  "user": "`redshift_user`",
  "password": "`redshift_password`"
}
```

5. Create the secret and retrieve its ARN..
6. When creating a new connection in SQL extension in JupyterLab, supply all
   other Amazon Redshift connection parameters as needed.

## Create a secret for Snowflake

access credentials

This section provides details on the secret and connection properties in JSON definition
files that are specific to Snowflake. Before creating your connection, we recommend storing
your Snowflake access credentials as a secret in Secrets Manager.

###### To store Amazon Redshift information in Secrets Manager

1. From the AWS Management Console, navigate to Secrets Manager.
2. Choose **Store a new secret**.
3. Under **Secret type**, choose **Other type of
   secret**.
4. In the key-value pair, choose **Plaintext**, and then copy the
   following JSON content. Replace the `user`, `password`, and
   `account` by their values.

```
{
    "user":"`snowflake_user`",
    "password":"`snowflake_password`",
    "account":"`account_id`"
}
```

5. Name the secret.
6. The remaining settings can be left at their default values for initial secret
   creation, or customized if required.
7. Create the secret and retrieve its ARN.
