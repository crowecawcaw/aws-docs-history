Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a secret for

database connection credentials

You can create a Secrets Manager secret to store credentials used to connect to an Amazon Redshift
provisioned cluster or Redshift Serverless namespace and workgroup. You can also use this secret when
scheduling a query in Amazon Redshift query editor v2.

###### To create a secret for a database in an Amazon Redshift provisioned cluster using the Secrets Manager

console

1. Open the Secrets Manager console ([https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/")).
2. Navigate to the list of **Secrets** and choose
   **Store a new secret**.
3. Choose **Credentials for Amazon Redshift data warehouse**. Enter your
   information in the steps to create a secret as follows:
   - In **Credentials** for **User
     name**, enter the name of the administrative user of the data
     warehouse.
   - In **Credentials** for **Password**,
     enter the password for the **User name**.
   - For **Encryption key**, choose your encryption
     key.
   - For **Data warehouse**, choose the Amazon Redshift provisioned
     cluster that contains your data.
   - For **Secret name**, enter a name for the
     secret.
   - For **Description**, enter a description of the
     secret.
   - For **Tags**, enter a **Tag key**
     with the word `Redshift`. This tag key is needed to
     list secrets when you attempt to connect to your data warehouse using
     Amazon Redshift query editor v2. The
     secret must have a tag key that starts with the string
     `Redshift` for the secret to be listed under
     AWS Secrets Manager on the management console.

4. Continue entering information about your secret through several steps until
   you **Store** your changes on the **Review**
   step.

The specific values of your credentials, engine, host, port, and cluster
identifier are stored in the secret. Also, the secret is tagged with the tag key
`Redshift`.

###### To create a secret for a database in a Redshift Serverless namespace using the Redshift Serverless

console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. Choose **Redshift serverless** and navigate to
   **Namespace configuration**.
3. Choose a namespace for which to create secret credentials.
4. Open **Actions**, **Edit admin
   credentials**.
5. For **Admin password**, choose **Manage admin
   credentials in AWS Secrets Manager**.
6. Choose **Save changes** to save your changes.
   Confirm that a message appears that the password successfully changed. You can also
   view the secret in the Secrets Manager console. You can use this secret to connect to a database
   in a workgroup in the Redshift Serverless console and Amazon Redshift query editor v2, using the AWS Secrets Manager connection
   method. The secret must have a tag key that starts with the string "Redshift"
   for the secret to be listed on the query editor v2 web application.
   The secret must have a tag key
   that starts with the string `Redshift` for the secret to be listed
   under AWS Secrets Manager on the management console.

###### To create a secret for a database in a Redshift Serverless namespace using the Secrets Manager

console

1. Open the Secrets Manager console ([https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/")).
2. Navigate to the list of **Secrets** and choose
   **Store a new secret**.
3. Choose **Credentials for Amazon Redshift data warehouse**. Enter your
   information in the steps to create a secret as follows:
   - In **Credentials** for **User
     name**, enter the name of the administrative user of the data
     warehouse.
   - In **Credentials** for **Password**,
     enter the password for the **User name**.
   - For **Encryption key**, choose your encryption
     key.
   - For **Data warehouse**, choose the Redshift Serverless namespace
     that contains your data.
   - For **Secret name**, enter a name for the
     secret.
   - For **Description**, enter a description of the
     secret.
   - For **Tags**, enter a **Tag key**
     with the word `Redshift`. This tag key is needed to
     list secrets when you attempt to connect to your data warehouse using
     Amazon Redshift query editor v2. The
     secret must have a tag key that starts with the string
     `Redshift` for the secret to be listed under
     AWS Secrets Manager on the management console.

4. Continue entering information about your secret through several steps until
   you **Store** your changes on the **Review**
   step.

The specific values of your credentials, database name, host, port, namespace,
and engine are stored in the secret. Also, the secret is tagged with the tag key
`Redshift`.

###### To create a secret for a database in a Redshift Serverless namespace using the AWS CLI

You can use the AWS CLI to create a secret. One method is to use AWS CloudShell to run the
Secrets Manager AWS CLI command as follows. You must have the proper permissions to run the
AWS CLI commands shown in the following procedure.

1. On the AWS console, open the AWS CloudShell command prompt. For more information
   about AWS CloudShell, see [What is AWS CloudShell](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") in
   the _AWS CloudShell User Guide_.
2. For example, for the secret `MyTestSecret` enter an Secrets Manager command
   to store the secret that is used to connect to a database or schedule an
   Amazon Redshift query editor v2 query. Replace the following values in the command with values for
   your environment:
   - `admin` is the administrator user name for
     the data warehouse.
   - `passw0rd` is the password of the
     administrator.
   - `dev` is the initial database name in the
     data warehouse.
   - `region` is the AWS Region that contains
     the data warehouse. For example `us-east-1`.
   - `123456789012` is the AWS account.
   - `namespace-id` is the namespace identifier
     similar to `c3928f0e-c889-4d2b-97a5-5738324d5d3e`. You can
     find this identifier on the Amazon Redshift console details page for the serverless
     namespace.

```
aws secretsmanager create-secret \
--name MyTestSecret \
--description "My test secret created with the CLI." \
--secret-string "{\"username\":\"`admin`\",\"password\":\"`passw0rd`\",\"dbname\":\"`dev`\",\"engine\":\"redshift\"}" \
--tags "[{\"Key\":\"redshift-serverless:namespaceArn\",\"Value\":\"arn:aws:redshift-serverless:`region`:`123456789012`:namespace/`namespace-id`\"}]"

```
