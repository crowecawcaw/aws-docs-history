# Configuring an Apache Airflow connection using a AWS Secrets Manager secret

AWS Secrets Manager is a supported alternative Apache Airflow backend on an Amazon Managed Workflows for Apache Airflow environment. This topic explains how to use AWS Secrets Manager to securely store secrets for Apache Airflow variables and an Apache Airflow connection on Amazon Managed Workflows for Apache Airflow.

###### Note

- You are charged for the secrets you create. For more information about Secrets Manager pricing, refer to [AWS Pricing](https://aws.amazon.com/secrets-manager/pricing/ "https://aws.amazon.com/secrets-manager/pricing/").
- [AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") is also supported as a secrets backend in
  Amazon MWAA. For more information, refer to [Amazon Provider Package documentation](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/secrets-backends/aws-ssm-parameter-store.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/secrets-backends/aws-ssm-parameter-store.html").

###### Contents

- [Step one: Provide Amazon MWAA with permission to access Secrets Manager secret keys](connections-secrets-manager.md#connections-sm-policy "connections-secrets-manager.md#connections-sm-policy")
- [Step two: Create the Secrets Manager backend as an Apache Airflow configuration option](connections-secrets-manager.md#connections-sm-aa-configuration "connections-secrets-manager.md#connections-sm-aa-configuration")
- [Step three: Generate an Apache Airflow AWS connection URI string](connections-secrets-manager.md#connections-sm-aa-uri "connections-secrets-manager.md#connections-sm-aa-uri")
- [Step four: Add the variables in Secrets Manager](connections-secrets-manager.md#connections-sm-createsecret-variables "connections-secrets-manager.md#connections-sm-createsecret-variables")
- [Step five: Add the connection in Secrets Manager](connections-secrets-manager.md#connections-sm-createsecret-connection "connections-secrets-manager.md#connections-sm-createsecret-connection")
- [Sample code](connections-secrets-manager.md#connections-sm-samples "connections-secrets-manager.md#connections-sm-samples")
- [Resources](connections-secrets-manager.md#connections-sm-blogs "connections-secrets-manager.md#connections-sm-blogs")
- [What's next?](connections-secrets-manager.md#connections-sm-next-up "connections-secrets-manager.md#connections-sm-next-up")

## Step one: Provide Amazon MWAA with permission to access Secrets Manager secret keys

The [execution role](mwaa-create-role.md "mwaa-create-role.md") for your Amazon MWAA environment needs read access to the secret key in AWS Secrets Manager.
The following IAM policy allows read-write access using the AWS-managed
[SecretsManagerReadWrite](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/SecretsManagerReadWrite$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/SecretsManagerReadWrite$jsonEditor") policy.

###### To attach the policy to your execution role

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Choose your execution role on the **Permissions** pane.
4. Choose **Attach policies**.
5. Type `SecretsManagerReadWrite` in the **Filter policies** text field.
6. Choose **Attach policy**.

If you do not want to use an AWS-managed permission policy, you can directly update your environment's execution role to allow any level of access to your
Secrets Manager resources. For example, the following policy statement grants read access to all secrets you create in a specific AWS Region in Secrets Manager.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecretVersionIds"
 ],
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:*"
 },
 {
 "Effect": "Allow",
 "Action": "secretsmanager:ListSecrets",
 "Resource": "*"
 }
 ]
}`

```

## Step two: Create the Secrets Manager backend as an Apache Airflow configuration option

The following section describes how to create an Apache Airflow configuration option on the Amazon MWAA console for the AWS Secrets Manager backend. If you're using a configuration setting of the same name in `airflow.cfg`,
the configuration you create in the following steps takes precedence and override the configuration settings.

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Choose **Edit**.
4. Choose **Next**.
5. Choose **Add custom configuration** in the **Airflow configuration options** pane. Add the following key-value pairs:
   1. `secrets.backend`: `airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend`
   2. `secrets.backend_kwargs`: `{"connections_prefix" : "airflow/connections", "variables_prefix" : "airflow/variables"}`
      This configures Apache Airflow to search for connection strings and variables at `airflow/connections/*` and `airflow/variables/*` paths.

   You can use a [lookup pattern](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/secrets-backends/aws-secrets-manager.html#optional-lookup "https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/secrets-backends/aws-secrets-manager.html#optional-lookup") to reduces
   the number of API calls Amazon MWAA makes to Secrets Manager on your behalf. If you do not specify a lookup pattern, Apache Airflow searches for all connections and variables
   in the configured backend. By specifying a pattern, you narrow the possible paths that Apache Airflow searches. This lowers your costs when using Secrets Manager with
   Amazon MWAA.

   To specify a lookup pattern, specify the `connections_lookup_pattern` and `variables_lookup_pattern` parameters.
   These parameters accept a RegEx string as input. For example, to search for secrets that start with `test`, enter the following for
   `secrets.backend_kwargs`:

   ```
   {
     "connections_prefix": "airflow/connections",
     "connections_lookup_pattern": "**^test**",
     "variables_prefix" : "airflow/variables",
     "variables_lookup_pattern": "**^test**"
   }
   ```

   ###### Note

   To use `connections_lookup_pattern` and `variables_lookup_pattern`, you must install `apache-airflow-providers-amazon` version 7.3.0 or higher. For more information about updating provder pacakges for to newer versions, refer to [Constraints file](connections-packages.md#connections-packages-constraints "connections-packages.md#connections-packages-constraints").

6. Choose **Save**.

## Step three: Generate an Apache Airflow AWS connection URI string

To create a connection string, use the "tab" key on your keyboard to indent the key-value pairs in the [Connection](https://airflow.apache.org/docs/stable/howto/connection/index.html "https://airflow.apache.org/docs/stable/howto/connection/index.html") object. We also recommend creating a variable for the `extra` object in your shell session. The following section walks you through the steps to [generate an Apache Airflow connection URI](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#generating-a-connection-uri "https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#generating-a-connection-uri") string for an Amazon MWAA environment using Apache Airflow or a Python script.

Apache Airflow CLI
The following shell session uses your local Airflow CLI to generate a connection string. If you don't have the CLI installed, we recommend using the Python script.

1. Open a Python shell session:

```
python3
```

2. Enter the following command:

```
**>>>** import json
```

3. Enter the following command:

```
**>>>** from airflow.models.connection import Connection
```

4. Create a variable in your shell session for the `extra` object. Substitute the sample values in `YOUR_EXECUTION_ROLE_ARN` with the execution role ARN, and the region in `us-east-1` (such as `us-east-1`).

```
**>>>** extra=json.dumps({'role_arn': '`YOUR_EXECUTION_ROLE_ARN`', 'region_name': '`us-east-1`'})

```

5. Create the connection object. Substitute the sample value in `myconn` with the name of the Apache Airflow connection.

```
**>>>** `myconn` = Connection(
```

6. Use the "tab" key on your keyboard to indent each of the following key-value pairs in your connection object. Substitute the sample values in `red`.
   1. Specify the AWS connection type:

   ```
   **...** conn_id='`aws`',
   ```

   2. Specify the Apache Airflow database option:

   ```
   **...** conn_type='`mysql`',
   ```

   3. Specify the Apache Airflow UI URL on Amazon MWAA:

   ```
   **...** host='`288888a0-50a0-888-9a88-1a111aaa0000.a1.us-east-1.airflow.amazonaws.com/home`',
   ```

   4. Specify the AWS access key ID (username) to log in to Amazon MWAA:

   ```
   **...** login='`YOUR_AWS_ACCESS_KEY_ID`',
   ```

   5. Specify the AWS secret access key (password) to log in to Amazon MWAA:

   ```
   **...** password='`YOUR_AWS_SECRET_ACCESS_KEY`',
   ```

   6. Specify the `extra` shell session variable:

   ```
   **...** extra=extra
   ```

   7. Close the connection object.

   ```
   **...** )
   ```

7. Print the connection URI string:

```
**>>>** `myconn.get_uri()`
```

Refer to the connection URI string in the response:

```
'mysql://288888a0-50a0-888-9a88-1a111aaa0000.a1.us-east-1.airflow.amazonaws.com%2Fhome?role_arn=arn%3Aaws%3Aiam%3A%3A001122332255%3Arole%2Fservice-role%2FAmazonMWAA-MyAirflowEnvironment-iAaaaA&region_name=us-east-1'
```

Python script
The following Python script does not require the Apache Airflow CLI.

1. Copy the contents of the following code sample and save locally as `mwaa_connection.py`.

```
import urllib.parse

								conn_type = '`YOUR_DB_OPTION`'
								host = '`YOUR_MWAA_AIRFLOW_UI_URL`'
								port = '`YOUR_PORT`'
								login = '`YOUR_AWS_ACCESS_KEY_ID`'
								password = '`YOUR_AWS_SECRET_ACCESS_KEY`'
								role_arn = urllib.parse.quote_plus('`YOUR_EXECUTION_ROLE_ARN`')
								region_name = '`us-east-1`'

								conn_string = '{0}://{1}:{2}@{3}:{4}?role_arn={5}&region_name={6}'.format(conn_type, login, password, host, port, role_arn, region_name)
								print(conn_string)
```

2. Substitute the placeholders in `red`.
3. Run the following script to generate a connection string.

```
python3 mwaa_connection.py
```

## Step four: Add the variables in Secrets Manager

The following section describes how to create the secret for a variable in Secrets Manager.

###### To create the secret

1. Open the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/home#/environments "https://console.aws.amazon.com/secretsmanager/home#/environments").
2. Choose **Store a new secret**.
3. Choose **Other type of secret**.
4. On the **Specify the key/value pairs to be stored in this secret** pane, choose **Plaintext**.
5. Add the variable value as **Plaintext** in the following format.

```
"`YOUR_VARIABLE_VALUE`"
```

For example, to specify an integer:

```
14
```

For example, to specify a string:

```
"mystring"
```

6. For **Encryption key**, choose an AWS KMS key option from the dropdown list.
7. Enter a name in the text field for **Secret name** in the following format.

```
airflow/variables/`YOUR_VARIABLE_NAME`
```

For example:

```
airflow/variables/test-variable
```

8. Choose **Next**.
9. On the **Configure secret** page, on the **Secret name and description** pane, do the following.
   1. For **Secret name**, provide a name for your secret.
   2. (Optional) For **Description**, provide a description for your secret.Choose **Next**.

10. On the **Configure rotation - optional** leave the default options and choose **Next**.
11. Repeat these steps in Secrets Manager for any additional variables you want to add.
12. On the **Review** page, review your secret, then choose **Store**.

## Step five: Add the connection in Secrets Manager

The following section describes how to create the secret for your connection string URI in Secrets Manager.

###### To create the secret

1. Open the [AWS Secrets Manager console](https://console.aws.amazon.com/secretsmanager/home#/environments "https://console.aws.amazon.com/secretsmanager/home#/environments").
2. Choose **Store a new secret**.
3. Choose **Other type of secret**.
4. On the **Specify the key/value pairs to be stored in this secret** pane, choose **Plaintext**.
5. Add the connection URI string as **Plaintext** in the following format.

```
`YOUR_CONNECTION_URI_STRING`
```

For example:

```
mysql://288888a0-50a0-888-9a88-1a111aaa0000.a1.us-east-1.airflow.amazonaws.com%2Fhome?role_arn=arn%3Aaws%3Aiam%3A%3A001122332255%3Arole%2Fservice-role%2FAmazonMWAA-MyAirflowEnvironment-iAaaaA&region_name=us-east-1
```

###### Warning

Apache Airflow parses each of the values in the connection string. You must **not** use single nor double quotes, or it parses the connection as a single string. 6. For **Encryption key**, choose an AWS KMS key option from the dropdown list. 7. Enter a name in the text field for **Secret name** in the following format.

```
airflow/connections/`YOUR_CONNECTION_NAME`
```

For example:

```
airflow/connections/myconn
```

8. Choose **Next**.
9. On the **Configure secret** page, on the **Secret name and description** pane, do the following.
   1. For **Secret name**, provide a name for your secret.
   2. (Optional) For **Description**, provide a description for your secret.Choose **Next**.

10. On the **Configure rotation - optional** leave the default options and choose **Next**.
11. Repeat these steps in Secrets Manager for any additional variables you want to add.
12. On the **Review** page, review your secret, then choose **Store**.

## Sample code

- Learn how to use the secret key for the Apache Airflow connection (`myconn`) on this page using the sample code at [Using a secret key in AWS Secrets Manager for an Apache Airflow connection](samples-secrets-manager.md "samples-secrets-manager.md").
- Learn how to use the secret key for the Apache Airflow variable (`test-variable`) on this page using the sample code at [Using a secret key in AWS Secrets Manager for an Apache Airflow variable](samples-secrets-manager-var.md "samples-secrets-manager-var.md").

## Resources

- For more information about configuring Secrets Manager secrets using the console and the AWS CLI, refer to [Create a secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_.
- Use a Python script to migrate a large volume of Apache Airflow variables and connections to Secrets Manager in [Move your Apache Airflow connections and variables to AWS Secrets Manager](https://aws.amazon.com/blogs/opensource/move-apache-airflow-connections-variables-aws-secrets-manager/ "https://aws.amazon.com/blogs/opensource/move-apache-airflow-connections-variables-aws-secrets-manager/").

## What's next?

- Learn how to generate a token to access the Apache Airflow UI in [Accessing Apache Airflow](access-airflow-ui.md "access-airflow-ui.md").
