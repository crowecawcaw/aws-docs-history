

# Configuring an Apache Airflow connection using a AWS Secrets Manager secret
<a name="connections-secrets-manager"></a>

AWS Secrets Manager is a supported alternative Apache Airflow backend on an Amazon Managed Workflows for Apache Airflow environment. This topic explains how to use AWS Secrets Manager to securely store secrets for Apache Airflow variables and an Apache Airflow connection on Amazon Managed Workflows for Apache Airflow.

**Note**  
You are charged for the secrets you create. For more information about Secrets Manager pricing, refer to [AWS Pricing](https://aws.amazon.com/secrets-manager/pricing/).
[AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store) is also supported as a secrets backend in Amazon MWAA. For more information, refer to [Amazon Provider Package documentation](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/secrets-backends/aws-ssm-parameter-store.html).

**Contents**
+ [Step one: Provide Amazon MWAA with permission to access Secrets Manager secret keys](#connections-sm-policy)
+ [Step two: Create the Secrets Manager backend as an Apache Airflow configuration option](#connections-sm-aa-configuration)
+ [Step three: Generate an Apache Airflow AWS connection URI string](#connections-sm-aa-uri)
+ [Step four: Add the variables in Secrets Manager](#connections-sm-createsecret-variables)
+ [Step five: Add the connection in Secrets Manager](#connections-sm-createsecret-connection)
+ [Sample code](#connections-sm-samples)
+ [Resources](#connections-sm-blogs)
+ [What's next?](#connections-sm-next-up)

## Step one: Provide Amazon MWAA with permission to access Secrets Manager secret keys
<a name="connections-sm-policy"></a>

The [execution role](mwaa-create-role.md) for your Amazon MWAA environment needs read access to the secret key in AWS Secrets Manager. The following IAM policy allows read-write access using the AWS-managed [SecretsManagerReadWrite](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/SecretsManagerReadWrite$jsonEditor) policy.

**To attach the policy to your execution role**

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1. Choose an environment.

1. Choose your execution role on the **Permissions** pane.

1. Choose **Attach policies**.

1. Type `SecretsManagerReadWrite` in the **Filter policies** text field.

1. Choose **Attach policy**.

If you do not want to use an AWS-managed permission policy, you can directly update your environment's execution role to allow any level of access to your Secrets Manager resources. The following JSON policy grants read access to all secrets in a specific AWS Region. Replace `{{us-east-1}}` with your Region, and replace `{{111122223333}}` with your AWS account ID:

**Example – IAM policy for Secrets Manager read access**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:*"
        },
        {
            "Effect": "Allow",
            "Action": "secretsmanager:ListSecrets",
            "Resource": "*"
        }
    ]
}
```

**Wildcard resource for ListSecrets**  
The preceding policy grants `ListSecrets` access to all secrets (`"Resource": "*"`). `ListSecrets` does not support resource-level permissions, so the wildcard is required. If you use this policy in production, any principal that assumes this role can list every secret in your account. Restrict the role's trust policy and other permissions to limit the scope of access.

**Optional: DescribeSecret permission**  
If your provider version checks for secret existence before retrieval, add `secretsmanager:DescribeSecret`. This permission might also reduce `ResourceNotFoundException` errors in your logs.

## Step two: Create the Secrets Manager backend as an Apache Airflow configuration option
<a name="connections-sm-aa-configuration"></a>

The following section describes how to create an Apache Airflow configuration option on the Amazon MWAA console for the AWS Secrets Manager backend. If you're using a configuration setting of the same name in `airflow.cfg`, the configuration you create in the following steps takes precedence and override the configuration settings.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments) page on the Amazon MWAA console.

1. Choose an environment.

1. Choose **Edit**.

1. Choose **Next**.

1. Choose **Add custom configuration** in the **Airflow configuration options** pane. Add the following key-value pairs:

   1. **`secrets.backend`**: **`airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend`**

   1. **`secrets.backend_kwargs`**: **`{"connections_prefix":"airflow/connections","variables_prefix":"airflow/variables"}`** This configures Apache Airflow to search for connection strings and variables at `airflow/connections/*` and `airflow/variables/*` paths.

      You can use a [lookup pattern](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/secrets-backends/aws-secrets-manager.html#optional-lookup) on the Apache Airflow website to reduce the number of API calls Amazon MWAA makes to Secrets Manager on your behalf. If you do not specify a lookup pattern, Apache Airflow searches for all connections and variables in the configured backend. By specifying a pattern, you narrow the possible paths that Apache Airflow searches. This lowers your costs when using Secrets Manager with Amazon MWAA.

      To specify a lookup pattern, specify the `connections_lookup_pattern` and `variables_lookup_pattern` parameters. These parameters accept a RegEx string as input. For example, to search for secrets that start with `test`, enter the following for `secrets.backend_kwargs`:

      ```
      {
        "connections_prefix": "airflow/connections",
        "connections_lookup_pattern": "^test",
        "variables_prefix" : "airflow/variables",
        "variables_lookup_pattern": "^test"
      }
      ```
**Note**  
To use `connections_lookup_pattern` and `variables_lookup_pattern`, you must install `apache-airflow-providers-amazon` version 7.3.0 or higher. For more information about updating provder pacakges for to newer versions, refer to [Constraints file](connections-packages.md#connections-packages-constraints).

1. Choose **Save**.

## Step three: Generate an Apache Airflow AWS connection URI string
<a name="connections-sm-aa-uri"></a>

To create a connection string, use the "tab" key on your keyboard to indent the key-value pairs in the [Connection](https://airflow.apache.org/docs/stable/howto/connection/index.html) object. We also recommend creating a variable for the `extra` object in your shell session. The following section walks you through the steps to [generate an Apache Airflow connection URI](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#generating-a-connection-uri) string for an Amazon MWAA environment using Apache Airflow or a Python script.

------
#### [ Apache Airflow CLI ]

The following shell session uses your local Airflow CLI to generate a connection string. If you don't have the CLI installed, we recommend using the Python script.

1. Open a Python shell session:

   ```
   python3
   ```

1. Enter the following command:

   ```
   >>> import json
   ```

1. Enter the following command:

   ```
   >>> from airflow.models.connection import Connection
   ```

1. Create a variable in your shell session for the `extra` object. Substitute the sample values in {{YOUR\_EXECUTION\_ROLE\_ARN}} with the execution role ARN, and the region in {{us-east-1}} (such as `us-east-1`).

   ```
   >>> extra=json.dumps({'role_arn': '{{YOUR_EXECUTION_ROLE_ARN}}', 'region_name': '{{us-east-1}}'})
   ```

1. Create the connection object. Substitute the sample value in `myconn` with the name of the Apache Airflow connection.

   ```
   >>> {{myconn}} = Connection(
   ```

1. Use the "tab" key on your keyboard to indent each of the following key-value pairs in your connection object. Substitute the sample values in {{red}}.

   1. Specify the AWS connection type:

      ```
      ... conn_id='{{aws}}',
      ```

   1. Specify the Apache Airflow database option:

      ```
      ... conn_type='{{mysql}}',
      ```

   1. Specify the Apache Airflow UI URL on Amazon MWAA:

      ```
      ... host='{{288888a0-50a0-888-9a88-1a111aaa0000.a1.us-east-1.airflow.amazonaws.com/home}}',
      ```

   1. Specify the AWS access key ID (username) to log in to Amazon MWAA:

      ```
      ... login='{{YOUR_AWS_ACCESS_KEY_ID}}',
      ```

   1. Specify the AWS secret access key (password) to log in to Amazon MWAA:

      ```
      ... password='{{YOUR_AWS_SECRET_ACCESS_KEY}}',
      ```

   1. Specify the `extra` shell session variable:

      ```
      ... extra=extra
      ```

   1. Close the connection object.

      ```
      ... )
      ```

1. Print the connection URI string:

   ```
   >>> {{myconn.get_uri()}}
   ```

   Refer to the connection URI string in the response:

   ```
   'mysql://288888a0-50a0-888-9a88-1a111aaa0000.a1.us-east-1.airflow.amazonaws.com%2Fhome?role_arn=arn%3Aaws%3Aiam%3A%3A001122332255%3Arole%2Fservice-role%2FAmazonMWAA-MyAirflowEnvironment-iAaaaA&region_name=us-east-1'
   ```

------
#### [ Python script ]

The following Python script does not require the Apache Airflow CLI.

1. Copy the contents of the following code sample and save locally as `mwaa_connection.py`.

   ```
   import urllib.parse
   								
   								conn_type = '{{YOUR_DB_OPTION}}'
   								host = '{{YOUR_MWAA_AIRFLOW_UI_URL}}'
   								port = '{{YOUR_PORT}}'
   								login = '{{YOUR_AWS_ACCESS_KEY_ID}}'
   								password = '{{YOUR_AWS_SECRET_ACCESS_KEY}}'
   								role_arn = urllib.parse.quote_plus('{{YOUR_EXECUTION_ROLE_ARN}}')
   								region_name = '{{us-east-1}}'
   								
   								conn_string = '{0}://{1}:{2}@{3}:{4}?role_arn={5}&region_name={6}'.format(conn_type, login, password, host, port, role_arn, region_name)
   								print(conn_string)
   ```

1. Substitute the placeholders in {{red}}.

1. Run the following script to generate a connection string.

   ```
   python3 mwaa_connection.py
   ```

------

## Step four: Add the variables in Secrets Manager
<a name="connections-sm-createsecret-variables"></a>

The following section describes how to create the secret for a variable in Secrets Manager.

**To create the secret**

1. Open the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/home#/environments).

1. Choose **Store a new secret**.

1. Choose **Other type of secret**.

1. On the **Specify the key/value pairs to be stored in this secret** pane, choose **Plaintext**.

1. Add the variable value as **Plaintext** in the following format.

   ```
   "{{YOUR_VARIABLE_VALUE}}"
   ```

   For example, to specify an integer:

   ```
   14
   ```

   For example, to specify a string:

   ```
   "mystring"
   ```

1. For **Encryption key**, choose an AWS KMS key option from the dropdown list.

1. Enter a name in the text field for **Secret name** in the following format.

   ```
   airflow/variables/{{YOUR_VARIABLE_NAME}}
   ```

   For example:

   ```
   airflow/variables/test-variable
   ```

1. Choose **Next**.

1. On the **Configure secret** page, on the **Secret name and description** pane, do the following.

   1. For **Secret name**, provide a name for your secret.

   1. (Optional) For **Description**, provide a description for your secret.

   Choose **Next**.

1. On the **Configure rotation - optional** leave the default options and choose **Next**.

1. Repeat these steps in Secrets Manager for any additional variables you want to add.

1. On the **Review** page, review your secret, then choose **Store**.

## Step five: Add the connection in Secrets Manager
<a name="connections-sm-createsecret-connection"></a>

The following section describes how to create the secret for your connection string URI in Secrets Manager.

**To create the secret**

1. Open the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/home#/environments).

1. Choose **Store a new secret**.

1. Choose **Other type of secret**.

1. On the **Specify the key/value pairs to be stored in this secret** pane, choose **Plaintext**.

1. Add the connection URI string as **Plaintext** in the following format.

   ```
   {{YOUR_CONNECTION_URI_STRING}}
   ```

   For example:

   ```
   mysql://288888a0-50a0-888-9a88-1a111aaa0000.a1.us-east-1.airflow.amazonaws.com%2Fhome?role_arn=arn%3Aaws%3Aiam%3A%3A001122332255%3Arole%2Fservice-role%2FAmazonMWAA-MyAirflowEnvironment-iAaaaA&region_name=us-east-1
   ```
**Warning**  
Apache Airflow parses each of the values in the connection string. You must **not** use single nor double quotes, or it parses the connection as a single string.

1. For **Encryption key**, choose an AWS KMS key option from the dropdown list.

1. Enter a name in the text field for **Secret name** in the following format.

   ```
   airflow/connections/{{YOUR_CONNECTION_NAME}}
   ```

   For example:

   ```
   airflow/connections/myconn
   ```

1. Choose **Next**.

1. On the **Configure secret** page, on the **Secret name and description** pane, do the following.

   1. For **Secret name**, provide a name for your secret.

   1. (Optional) For **Description**, provide a description for your secret.

   Choose **Next**.

1. On the **Configure rotation - optional** leave the default options and choose **Next**.

1. Repeat these steps in Secrets Manager for any additional variables you want to add.

1. On the **Review** page, review your secret, then choose **Store**.

## Sample code
<a name="connections-sm-samples"></a>
+ Learn how to use the secret key for the Apache Airflow connection (`myconn`) on this page using the sample code at [Using a secret key in AWS Secrets Manager for an Apache Airflow connection](samples-secrets-manager.md).
+ Learn how to use the secret key for the Apache Airflow variable (`test-variable`) on this page using the sample code at [Using a secret key in AWS Secrets Manager for an Apache Airflow variable](samples-secrets-manager-var.md).

## Resources
<a name="connections-sm-blogs"></a>
+ For more information about configuring Secrets Manager secrets using the console and the AWS CLI, refer to [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide*.
+ Use a Python script to migrate a large volume of Apache Airflow variables and connections to Secrets Manager in [Move your Apache Airflow connections and variables to AWS Secrets Manager](https://aws.amazon.com/blogs/opensource/move-apache-airflow-connections-variables-aws-secrets-manager/).

## What's next?
<a name="connections-sm-next-up"></a>
+ Learn how to generate a token to access the Apache Airflow UI in [Accessing Apache Airflow](access-airflow-ui.md).