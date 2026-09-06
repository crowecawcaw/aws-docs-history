

# Create secrets for database access credentials in Secrets Manager
<a name="sagemaker-sql-extension-glue-connection-secrets"></a>

Before creating your connection, we recommend storing your database access credentials as a secret in AWS Secrets Manager. Alternatively, you can generate temporary database credentials based on permissions granted through an AWS Identity and Access Management (IAM) permissions policy to manage the access that your users have to your database. For more information, see [Using IAM authentication to generate database user credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-credentials.html)

## Create a secret for Amazon Redshift access credentials
<a name="sagemaker-sql-extension-redshift-secret"></a>

**To store Amazon Redshift information in AWS Secrets Manager**

1. From the AWS Management Console, navigate to Secrets Manager.

1. Choose **Store a new secret**.

1. Under **Secret type**, choose **Credentials for Amazon Redshift**.

1. Enter the administrator username and password configured when launching the Amazon Redshift cluster. 

1. Select the Amazon Redshift cluster associated with the secrets.

1. Name your secret.

1. The remaining settings can be left at their default values for initial secret creation, or customized if required. 

1. Create the secret and retrieve its ARN.

## Create a secret for Amazon Redshift Serverless access credentials
<a name="sagemaker-sql-extension-redshift-serverless-secret"></a>

**If you need to connect to Amazon Redshift Serverless, follow these steps**

1. From the AWS Management Console, navigate to Secrets Manager.

1. Choose **Store a new secret**.

1. Under **Secret type**, choose **Other type of secret**.

1. In the **Key-value pairs**, choose **Plaintext**, and then copy the following JSON content. Replace the user, and password with their actual values: 

   ```
   {
     "user": "{{redshift_user}}",
     "password": "{{redshift_password}}"
   }
   ```

1. Create the secret and retrieve its ARN..

1. When creating a new connection in SQL extension in JupyterLab, supply all other Amazon Redshift connection parameters as needed.

## Create a secret for Snowflake access credentials
<a name="sagemaker-sql-extension-snowflake-secret"></a>

This section provides details on the secret and connection properties in JSON definition files that are specific to Snowflake. Before creating your connection, we recommend storing your Snowflake access credentials as a secret in Secrets Manager.

**To store Amazon Redshift information in Secrets Manager**

1. From the AWS Management Console, navigate to Secrets Manager.

1. Choose **Store a new secret**.

1. Under **Secret type**, choose **Other type of secret**.

1. In the key-value pair, choose **Plaintext**, and then copy the following JSON content. Replace the `user`, `password`, and `account` by their values.

   ```
   {
       "user":"{{snowflake_user}}",
       "password":"{{snowflake_password}}",
       "account":"{{account_id}}"
   }
   ```

1. Name the secret.

1. The remaining settings can be left at their default values for initial secret creation, or customized if required.

1. Create the secret and retrieve its ARN.