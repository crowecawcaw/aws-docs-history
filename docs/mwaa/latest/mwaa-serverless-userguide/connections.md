

# Managing connections and variables
<a name="connections"></a>

 Apache Airflow connections store the credentials and endpoint information that your tasks use to reach external systems, such as a database or an HTTP API. Apache Airflow variables store reusable configuration values as key-value pairs. Your task code retrieves a connection with `BaseHook.get_connection` and a variable with `Variable.get`. Operators that take a connection ID, such as `http_conn_id`, make the same lookup for you. 

 With Amazon MWAA Serverless, you use the native Apache Airflow mechanisms for connections and variables. For background on these concepts, see [Managing connections](https://airflow.apache.org/docs/apache-airflow/3.0.6/howto/connection.html), [Variables](https://airflow.apache.org/docs/apache-airflow/3.0.6/core-concepts/variables.html), and [Secrets backend](https://airflow.apache.org/docs/apache-airflow/3.0.6/security/secrets/secrets-backend/index.html) in the Apache Airflow documentation. 

 You can store connections and variables in a secrets backend that you configure for the workflow, such as AWS Secrets Manager or AWS Systems Manager Parameter Store. You can also define connections and variables that don't contain secrets as environment variables. 

**Topics**
+ [How Amazon MWAA Serverless looks up connections and variables](#connections-lookup-order)
+ [Default connections](#connections-defaults)
+ [Choosing where to store connections and variables](#connections-choosing)
+ [Using the Secrets Manager backend](#connections-secrets-manager)
+ [Execution role permissions](#connections-permissions)
+ [Configuring a secrets backend](#connections-backend-override)
+ [Defining connections and variables with environment variables](#connections-environment-variables)
+ [Combining backend settings with other environment variables](#connections-combining)
+ [Example – Reading a connection and a variable in a task](#connections-example)
+ [Limitations for connections and variables](#connections-limitations)
+ [Troubleshooting connections and variables](#connections-troubleshooting)

## How Amazon MWAA Serverless looks up connections and variables
<a name="connections-lookup-order"></a>

When a task looks up a connection or a variable, Apache Airflow checks the following locations in order and returns the first value it finds:

1. The secrets backend, if you configured one.

1. Environment variables: `AIRFLOW_CONN_{{CONN_ID}}` for connections and `AIRFLOW_VAR_{{KEY}}` for variables. For more information, see [Defining connections and variables with environment variables](#connections-environment-variables).

**Important**  
When you use the Secrets Manager backend, every connection or variable lookup calls the Secrets Manager API. This includes lookups for keys that don't exist in Secrets Manager. These calls can increase your Secrets Manager charges. To limit the lookups, use lookup patterns, as described in [Option A: Secrets Manager with custom prefixes](#connections-backend-secrets-manager-prefixes).

 The same lookup applies when you reference a connection or variable through Jinja templating in your workflow definition, with `{{ conn.{{conn_id}} }}`, `{{ var.value.{{key}} }}`, or `{{ var.json.{{key}} }}`. In the following example, a `BashOperator` task reads the host of the `my_http` connection and the value of the `app_stage` variable: 

```
templated_dag:
  start_date: "2024-01-01"
  schedule: null
  tasks:
    print_values:
      operator: airflow.providers.standard.operators.bash.BashOperator
      bash_command: 'echo "host={{ conn.my_http.host }} stage={{ var.value.app_stage }}"'
```

 For the list of supported template variables, see [Template variables, filters, and macros](supported-jinja-parameters.md). 

 If neither location has a value, the lookup fails: `BaseHook.get_connection` raises `AirflowNotFoundException`, `Variable.get` raises `KeyError`, and a template that references the missing key fails to render. 

## Default connections
<a name="connections-defaults"></a>

Amazon MWAA Serverless provides two default Apache Airflow connections to every task, so you don't need to define them:
+ `aws_default` (`AIRFLOW_CONN_AWS_DEFAULT=aws://`) – uses your workflow execution role credentials.
+ `duckdb_default` (`AIRFLOW_CONN_DUCKDB_DEFAULT={"conn_type": "duckdb_aws"}`) – the default DuckDB connection, of type `duckdb_aws`.

You can overwrite either default connection by setting the same key in `Environment.Variables`. For example, the following entry changes `aws_default` for every task so that it targets the `eu-west-1` Region: 

```
"AIRFLOW_CONN_AWS_DEFAULT": "aws://?region_name=eu-west-1"
```

**Note**  
AWS operators use the `aws_default` connection unless a task sets `aws_conn_id`. Overriding `aws_default` affects every such task in the workflow.

## Choosing where to store connections and variables
<a name="connections-choosing"></a>

Use the following guidance to choose where to store a value:
+  **Secrets backend** – Use for credentials, tokens, and any other sensitive value. You can use AWS Secrets Manager, AWS Systems Manager Parameter Store, or your own backend class, with your own prefixes, lookup patterns, or secrets in another account. For more information, see [Configuring a secrets backend](#connections-backend-override). 
+  **Environment variables** – Use only for non-secret values, such as a public endpoint or a stage name, because `GetWorkflow` returns them in plain text. For more information, see [Defining connections and variables with environment variables](#connections-environment-variables). 

The following table compares the storage options.


| Storage option | Where values are stored | Configuration needed | Use for secrets? | 
| --- | --- | --- | --- | 
| Secrets Manager backend | AWS Secrets Manager secrets under prefixes that you choose, optionally in another account. | Secrets backend environment variables | Yes | 
| AWS Systems Manager Parameter Store | Parameter Store parameters, stored as SecureString for sensitive values. | Secrets backend environment variables | Yes | 
| Custom secrets backend class | Any store that your own backend class reads. You include the class in your code package. | Secrets backend environment variables and code package | Yes, depending on the store that you use. | 
| Environment variables | The workflow's Environment block, which GetWorkflow returns in plain text. | None | No | 

## Using the Secrets Manager backend
<a name="connections-secrets-manager"></a>

 To read connections and variables from Secrets Manager, set the backend class `airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend` and its keyword arguments (`connections_prefix`, `variables_prefix`, and `region_name`) in the workflow's `Environment` block, as in the following example. Replace {{us-east-1}} with the Region of your secrets. 

```
--environment '{"Variables": {
    "AIRFLOW__WORKERS__SECRETS_BACKEND": "airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend",
    "AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS": "{\"connections_prefix\": \"airflow/connections\", \"variables_prefix\": \"airflow/variables\", \"region_name\": \"{{us-east-1}}\"}"
}}'
```

 For more information about these variables, see [Configuring a secrets backend](#connections-backend-override). For more information about this backend class, see [Secrets Manager backend](https://airflow.apache.org/docs/apache-airflow-providers-amazon/9.38.0/secrets-backends/aws-secrets-manager.html) in the Apache Airflow documentation. 

 To read secrets in another account, see [Option D: Secrets Manager secrets in another account](#connections-cross-account). 

 Apache Airflow builds the secret name from the prefix and the key that you pass to the lookup call. With the prefixes in the preceding example, the names are as shown in the following table. 


| Lookup call in your task | Secrets Manager secret name | 
| --- | --- | 
| BaseHook.get\_connection("my\_db") | airflow/connections/my\_db | 
| Variable.get("my\_variable") | airflow/variables/my\_variable | 

Store the secret value in the format that matches the lookup:
+  For a connection, store an Apache Airflow connection URI string, such as `postgresql://my-user:my-password@mydb.example.com:5432/app`. Don't wrap the URI in quotation marks, and URL-encode special characters in the user name and password. Apache Airflow also accepts a JSON representation of a connection. 
+ For a variable, store the plaintext value.

You can both create new secrets and update existing ones. Grant your execution role permission to read them, as described in [Execution role permissions](#connections-permissions).

### Creating a connection or variable secret
<a name="connections-secrets-manager-create"></a>

 Use the following AWS CLI `create-secret` commands to create a connection secret and a variable secret. Before you run them, replace the following values: 
+ The connection URI in the first command – the Apache Airflow connection URI for your external system
+ {{my-value}} in the second command – the value of your variable
+ {{us-east-1}} – the Region of your workflow

```
aws secretsmanager create-secret \
    --name airflow/connections/my_db \
    --secret-string '{{postgresql://my-user:my-password@mydb.example.com:5432/app}}' \
    --region {{us-east-1}}
```

```
aws secretsmanager create-secret \
    --name airflow/variables/my_variable \
    --secret-string '{{my-value}}' \
    --region {{us-east-1}}
```

### Updating a connection or variable secret
<a name="connections-secrets-manager-update"></a>

 To change the value of an existing connection or variable, store a new version of the secret with `put-secret-value`. Replace the values and the Region as in the create commands. 

```
aws secretsmanager put-secret-value \
    --secret-id airflow/connections/my_db \
    --secret-string '{{postgresql://my-user:my-new-password@mydb.example.com:5432/app}}' \
    --region {{us-east-1}}
```

```
aws secretsmanager put-secret-value \
    --secret-id airflow/variables/my_variable \
    --secret-string '{{my-new-value}}' \
    --region {{us-east-1}}
```

 After you change a secret, you don't need to update the workflow. Your tasks read the secret each time they look it up, so you get the new value in any task that starts after the change. 

**Important**  
 Secrets Manager charges for the secrets that you store and for the API calls that Amazon MWAA Serverless makes to retrieve them. For more information about pricing, see [AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing/). To reduce the number of API calls, you can limit which keys Apache Airflow looks up in the backend with lookup patterns, as described in [Option A: Secrets Manager with custom prefixes](#connections-backend-secrets-manager-prefixes). 

## Execution role permissions
<a name="connections-permissions"></a>

 Your workflow execution role needs permission to read the secrets or parameters that hold your connections and variables. Add the statements that match the backend that you use. For more information about execution roles, see [Execution roles](get-started-execution-role.md). 

 The following policy grants the `secretsmanager:GetSecretValue` permission on secrets stored under the `airflow/connections/` and `airflow/variables/` prefixes in one account and Region. The Secrets Manager backend needs this permission when you use these prefixes. 

------
#### [ JSON ]

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": [
        "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:airflow/connections/*",
        "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:airflow/variables/*"
      ]
    }
  ]
}
```

------

 Replace {{us-east-1}} with your Region and {{123456789012}} with your account ID. If you use different prefixes, change `airflow/connections/*` and `airflow/variables/*` in the `Resource` element to match your prefixes. 

 If you use the AWS Systems Manager Parameter Store backend (Option B in [Configuring a secrets backend](#connections-backend-override)), grant the `ssm:GetParameter` and `ssm:GetParameters` permissions on parameters stored under the `/airflow/connections/` and `/airflow/variables/` prefixes instead. 

------
#### [ JSON ]

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:GetParameter",
        "ssm:GetParameters"
      ],
      "Resource": [
        "arn:aws:ssm:{{us-east-1}}:{{123456789012}}:parameter/airflow/connections/*",
        "arn:aws:ssm:{{us-east-1}}:{{123456789012}}:parameter/airflow/variables/*"
      ]
    }
  ]
}
```

------

 Replace {{us-east-1}} with your Region and {{123456789012}} with your account ID. Adjust the parameter prefixes to match the prefixes that you configure in the backend. 

 If you encrypt your secrets or `SecureString` parameters with a customer managed AWS KMS key, also grant the `kms:Decrypt` permission on that key. 

------
#### [ JSON ]

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
    }
  ]
}
```

------

 Replace {{us-east-1}} with your Region, {{123456789012}} with your account ID, and the key ID {{1234abcd-12ab-34cd-56ef-1234567890ab}} with the ID of your key. 

**Note**  
 If you use a custom secrets backend class, grant your execution role the permissions for the API calls that the class makes. The required permissions depend on the store that your backend reads. 

## Configuring a secrets backend
<a name="connections-backend-override"></a>

 To configure where Amazon MWAA Serverless reads connections and variables, set both of the following environment variables in the workflow's `Environment` block: 
+ `AIRFLOW__WORKERS__SECRETS_BACKEND` – the full class path of the backend.
+ `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS` – a JSON string of keyword arguments for the backend.

 The `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS` value is a JSON string inside the `Environment` JSON. Escape its inner quotation marks with a backslash, as shown in the following examples. 

 These variables map to the Apache Airflow 3 `[workers]` `secrets_backend` and `secrets_backend_kwargs` settings, which configure the backend that task workers use. Set them with the [Environment parameter](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateWorkflow.html#mwaaserverless-CreateWorkflow-request-Environment) of `CreateWorkflow` or the [Environment parameter](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_UpdateWorkflow.html#mwaaserverless-UpdateWorkflow-request-Environment) of `UpdateWorkflow`. 

### Option A: Secrets Manager with custom prefixes
<a name="connections-backend-secrets-manager-prefixes"></a>

 To keep your connections and variables under prefixes that you choose, use the Secrets Manager backend class with custom `connections_prefix` and `variables_prefix` values. The following AWS CLI command creates a workflow with this configuration. Replace {{my-workflow}} with your workflow name. Replace {{dags/my\_dag.yaml}} with the Amazon S3 object key of your YAML workflow definition. Replace the role ARN with your execution role ARN, and replace {{us-east-1}} with your Region. 

```
aws mwaa-serverless create-workflow \
    --name {{my-workflow}} \
    --definition-s3-location '{"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{dags/my_dag.yaml}}"}' \
    --environment '{"Variables": {"AIRFLOW__WORKERS__SECRETS_BACKEND": "airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend", "AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS": "{\"connections_prefix\": \"my-app/connections\", \"variables_prefix\": \"my-app/variables\", \"region_name\": \"us-east-1\"}"}}' \
    --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
    --region {{us-east-1}}
```

 With this configuration, `BaseHook.get_connection("my_db")` reads the secret `my-app/connections/my_db`, and `Variable.get("my_variable")` reads `my-app/variables/my_variable`. 

 To reduce the number of Secrets Manager API calls, add the `connections_lookup_pattern` and `variables_lookup_pattern` keyword arguments. Each is a regular expression, and Apache Airflow queries the backend only for keys that match. In the following example, Apache Airflow looks up only connection IDs `my_db` and `my_http`, and only variables whose keys start with `my_`: 

```
--environment '{"Variables": {"AIRFLOW__WORKERS__SECRETS_BACKEND": "airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend", "AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS": "{\"connections_prefix\": \"my-app/connections\", \"variables_prefix\": \"my-app/variables\", \"region_name\": \"us-east-1\", \"connections_lookup_pattern\": \"^(my_db|my_http)$\", \"variables_lookup_pattern\": \"^my_\"}"}}'
```

### Option B: AWS Systems Manager Parameter Store
<a name="connections-backend-parameter-store"></a>

 To read connections and variables from AWS Systems Manager Parameter Store, use the Parameter Store backend class. Parameter names begin with a forward slash, so `get_connection("my_db")` reads the parameter `/airflow/connections/my_db`: 

```
--environment '{"Variables": {"AIRFLOW__WORKERS__SECRETS_BACKEND": "airflow.providers.amazon.aws.secrets.systems_manager.SystemsManagerParameterStoreBackend", "AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS": "{\"connections_prefix\": \"/airflow/connections\", \"variables_prefix\": \"/airflow/variables\", \"region_name\": \"us-east-1\"}"}}'
```

 Store sensitive values as a `SecureString` parameter. Use the following AWS CLI `put-parameter` commands to create a connection parameter and a variable parameter. Replace the connection URI with the URI for your system, {{my-value}} with your variable value, and {{us-east-1}} with the Region of your workflow. 

```
aws ssm put-parameter \
    --name /airflow/connections/my_db \
    --type SecureString \
    --value '{{postgresql://my-user:my-password@mydb.example.com:5432/app}}' \
    --region {{us-east-1}}
```

```
aws ssm put-parameter \
    --name /airflow/variables/my_variable \
    --type SecureString \
    --value '{{my-value}}' \
    --region {{us-east-1}}
```

 To update an existing parameter, run the same `put-parameter` command with the new value and the `--overwrite` option: 

```
aws ssm put-parameter \
    --name /airflow/connections/my_db \
    --type SecureString \
    --value '{{postgresql://my-user:my-new-password@mydb.example.com:5432/app}}' \
    --overwrite \
    --region {{us-east-1}}
```

 For more information about this backend class, see [Parameter Store backend](https://airflow.apache.org/docs/apache-airflow-providers-amazon/9.38.0/secrets-backends/aws-ssm-parameter-store.html) in the Apache Airflow documentation. 

 Grant your execution role the Parameter Store permissions shown in [Execution role permissions](#connections-permissions), and `kms:Decrypt` if your `SecureString` parameters use a customer managed key. 

### Option C: Your own secrets backend class
<a name="connections-backend-custom"></a>

 To read connections and variables from a store that the built-in backends don't support, write your own backend class. Subclass `airflow.secrets.BaseSecretsBackend` and implement two methods: 
+  `get_conn_value(conn_id)` – return a connection URI or JSON string, or `None` so that Apache Airflow continues to the next lookup location. 
+  `get_variable(key)` – return the variable value as a string, or `None`. 

 Apache Airflow passes each key in the `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS` JSON to your class's `__init__` method as a keyword argument. The following example reads from a store of your choice. It returns `None` when a secret doesn't exist, and logs and re-raises any other error so that a failed lookup isn't silently treated as a missing value. 

```
# my_secrets_backend.py
from airflow.secrets import BaseSecretsBackend


class MySecretsBackend(BaseSecretsBackend):
    """Reads Airflow connections and variables from your own secret store."""

    def __init__(self, prefix="airflow", **kwargs):
        super().__init__(**kwargs)
        self.prefix = prefix

    def _fetch_from_store(self, path):
        # Replace with a call to your secret store, using the workflow
        # execution role credentials. Raise LookupError if the secret
        # doesn't exist.
        raise LookupError(path)

    def _read_secret(self, path):
        try:
            return self._fetch_from_store(path)
        except LookupError:
            # The secret doesn't exist. Return None so that Airflow
            # continues to the next lookup location.
            return None
        except Exception:
            self.log.exception("Failed to read secret %s", path)
            raise

    def get_conn_value(self, conn_id):
        # Return a connection URI or JSON string, or None so that Airflow
        # continues to the next lookup location.
        return self._read_secret(f"{self.prefix}/connections/{conn_id}")

    def get_variable(self, key):
        # Return the variable value as a string, or None.
        return self._read_secret(f"{self.prefix}/variables/{key}")
```

 Set the backend class path and its keyword arguments in the `Environment` block: 

```
--environment '{"Variables": {"AIRFLOW__WORKERS__SECRETS_BACKEND": "my_secrets_backend.MySecretsBackend", "AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS": "{\"prefix\": \"my-app\"}"}}'
```

 Include the module in your workflow code package, and pass the package in the `--code` parameter. You don't need a separate install or registration step. Amazon MWAA Serverless extracts your code onto the task's import path. The class path that you set in `AIRFLOW__WORKERS__SECRETS_BACKEND` is `{{module}}.{{Class}}` for a module at the root of the package, or `{{package}}.{{module}}.{{Class}}` for a module inside a folder. For more information about building a code package, see [Preparing your code package](custom-code-operators.md#operators-python-bash-zip). 

 Your backend class needs the IAM permissions for the API calls that its code makes. Grant those permissions to your execution role. 

 The following AWS CLI command creates a workflow that uses the custom backend. Replace {{my-workflow}} with your workflow name. Replace {{dags/my\_dag.yaml}} and {{code/my\_package.zip}} with the Amazon S3 object keys of your YAML workflow definition and your code package. Replace the role ARN with your execution role ARN, and replace {{us-east-1}} with your Region. 

```
aws mwaa-serverless create-workflow \
    --name {{my-workflow}} \
    --definition-s3-location '{"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{dags/my_dag.yaml}}"}' \
    --code '{"S3Location": {"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{code/my_package.zip}}"}}' \
    --environment '{"Variables": {"AIRFLOW__WORKERS__SECRETS_BACKEND": "my_secrets_backend.MySecretsBackend", "AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS": "{\"prefix\": \"my-app\"}"}}' \
    --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
    --region {{us-east-1}}
```

### Option D: Secrets Manager secrets in another account
<a name="connections-cross-account"></a>

 To read Secrets Manager secrets that are in another account, set `connections_prefix` and `variables_prefix` to the ARN prefix of the secrets in that account. In the following example, the workflow runs in account {{111122223333}} and the secrets are in account {{444455556666}}: 

```
--environment '{"Variables": {"AIRFLOW__WORKERS__SECRETS_BACKEND": "airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend", "AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS": "{\"connections_prefix\": \"arn:aws:secretsmanager:us-east-1:444455556666:secret:airflow/connections\", \"variables_prefix\": \"arn:aws:secretsmanager:us-east-1:444455556666:secret:airflow/variables\", \"region_name\": \"us-east-1\"}"}}'
```

 With this configuration, `BaseHook.get_connection("my_conn")` reads the secret `arn:aws:secretsmanager:us-east-1:444455556666:secret:airflow/connections/my_conn`. The two prefixes can point at the same account or at different accounts. 

 Standard Secrets Manager cross-account requirements apply: 
+ The secret's resource policy must allow the workflow execution role to read it.
+  The secret must be encrypted with a customer managed AWS KMS key whose key policy allows the execution role to use it. You can't use the AWS managed key `aws/secretsmanager` for cross-account access. 
+  The execution role's identity policy must allow `secretsmanager:GetSecretValue` on the secrets and `kms:Decrypt` on the key. 

 In the account that owns the secrets ({{444455556666}}), attach a resource policy to each secret that allows your workflow execution role in account {{111122223333}} to call `secretsmanager:GetSecretValue`. 

------
#### [ JSON ]

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyMWAAServerlessRole}}"
      },
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "*"
    }
  ]
}
```

------

 In the workflow account ({{111122223333}}), grant your execution role permission to call `secretsmanager:GetSecretValue` on the secrets and `kms:Decrypt` on the customer managed key in the other account ({{444455556666}}). 

------
#### [ JSON ]

```
{
  "Version": "2012-10-17", 		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": [
        "arn:aws:secretsmanager:{{us-east-1}}:{{444455556666}}:secret:airflow/connections/*",
        "arn:aws:secretsmanager:{{us-east-1}}:{{444455556666}}:secret:airflow/variables/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "kms:Decrypt",
      "Resource": "arn:aws:kms:{{us-east-1}}:{{444455556666}}:key/{{1234abcd-12ab-34cd-56ef-1234567890ab}}"
    }
  ]
}
```

------

 For more information about cross-account access to secrets, see [Permissions to access secrets in a different account](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples_cross.html) in the *AWS Secrets Manager User Guide*. 

## Defining connections and variables with environment variables
<a name="connections-environment-variables"></a>

You can define an Apache Airflow connection without a secrets backend by setting an `AIRFLOW_CONN_{{CONN_ID}}` environment variable to an Apache Airflow connection URI. Apache Airflow parses the URI into connection fields.

For example, set `AIRFLOW_CONN_MY_HTTP` to `http://api.example.com:8443/v1?timeout=30`. `BaseHook.get_connection("my_http")` then returns a connection with the following fields:
+ Host: `api.example.com`
+ Port: `8443`
+ Schema: `v1`
+ Extra: `{"timeout": "30"}`

Similarly, set an `AIRFLOW_VAR_{{KEY}}` environment variable to define a variable, which `Variable.get("{{key}}")` then returns. 

For more information about the connection URI format, see [Storing connections in environment variables](https://airflow.apache.org/docs/apache-airflow/3.0.6/howto/connection.html#storing-connections-in-environment-variables) and [Storing variables in environment variables](https://airflow.apache.org/docs/apache-airflow/3.0.6/howto/variable.html#storing-variables-in-environment-variables) in the Apache Airflow documentation.

If you configured a secrets backend, Apache Airflow looks up a connection or variable there first, and checks environment variables only if the backend returns no value. For more information about the lookup order, see [How Amazon MWAA Serverless looks up connections and variables](#connections-lookup-order). For instructions on setting environment variables and their limits, see [Using environment variables in Amazon MWAA Serverless workflows](workflows-environment-variables.md).

**Note**  
Use environment variables only for connections and variables that don't contain secrets. Keep credentials and other sensitive values in a secrets backend.

## Combining backend settings with other environment variables
<a name="connections-combining"></a>

The secrets backend variables, `AIRFLOW_CONN_{{CONN_ID}}` and `AIRFLOW_VAR_{{KEY}}` entries, and your own application variables all go in the single `Variables` map in the workflow's `Environment` block. The following example combines backend settings, a connection, and two application variables. Replace the secrets prefixes `my-app/connections` and `my-app/variables`, the Region `us-east-1`, and the connection URI with your own values.

```
--environment '{"Variables": {"AIRFLOW__WORKERS__SECRETS_BACKEND": "airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend", "AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS": "{\"connections_prefix\": \"my-app/connections\", \"variables_prefix\": \"my-app/variables\", \"region_name\": \"us-east-1\"}", "AIRFLOW_CONN_MY_HTTP": "http://api.example.com:8443/v1?timeout=30", "APP_STAGE": "production", "FEATURE_X_ENABLED": "true"}}'
```

The example sets the following variables:
+ `AIRFLOW__WORKERS__SECRETS_BACKEND` – The secrets backend class. This example uses the Secrets Manager backend class.
+ `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS` – A JSON string of keyword arguments for the backend class. This example sets the connections prefix, the variables prefix, and the Region.
+ `AIRFLOW_CONN_MY_HTTP` – An Apache Airflow connection URI that defines the `my_http` connection.
+ `APP_STAGE` and `FEATURE_X_ENABLED` – Your own application variables. Your task code can read them as environment variables.

**Important**  
Define each connection in only one place: either the secrets backend or an `AIRFLOW_CONN_{{CONN_ID}}` environment variable, not both. If both exist, Apache Airflow uses the secrets backend value.

## Example – Reading a connection and a variable in a task
<a name="connections-example"></a>

 This example reads one connection and one variable with the Secrets Manager backend. For a version that reads the same values from a custom operator, see [Example: a custom operator that reads a connection and a variable](custom-code-operators.md#operators-custom-example). 

 First, create a connection secret and a variable secret in the workflow's account and Region: 

```
aws secretsmanager create-secret \
    --name airflow/connections/my_db \
    --secret-string '{{postgresql://my-user:my-password@mydb.example.com:5432/app}}' \
    --region {{us-east-1}}

aws secretsmanager create-secret \
    --name airflow/variables/my_variable \
    --secret-string '{{my-value}}' \
    --region {{us-east-1}}
```

 Next, write a Python callable that reads the connection and the variable. The callable logs only non-secret fields, such as the host, port, and schema of the connection, and the value of a non-secret variable. 

```
# my_module.py
import logging

from airflow.exceptions import AirflowException, AirflowNotFoundException

try:
    from airflow.sdk import BaseHook, Variable  # Apache Airflow 3
except ImportError:
    from airflow.hooks.base import BaseHook
    from airflow.models import Variable

logger = logging.getLogger(__name__)


def read_connection_and_variable():
    # Look up a connection through the configured secrets backend.
    try:
        conn = BaseHook.get_connection("my_db")
    except AirflowNotFoundException as e:
        raise AirflowException("Connection my_db not found") from e
    # Log only non-secret fields. Never log the password or the full URI.
    logger.info("host=%s port=%s schema=%s", conn.host, conn.port, conn.schema)

    # Look up a non-secret variable.
    try:
        my_variable = Variable.get("my_variable")
    except KeyError as e:
        raise AirflowException("Variable my_variable not found") from e
    logger.info("my_variable=%s", my_variable)
```

 Define a workflow that runs the callable as a `PythonOperator` task in the following YAML workflow definition: 

```
my_dag:
  start_date: "2024-01-01"
  schedule: null
  tasks:
    read_task:
      operator: airflow.providers.standard.operators.python.PythonOperator
      python_callable: my_module.read_connection_and_variable
```

 Package the module with `zip`, and then use the following AWS CLI commands to upload the code package and the YAML definition to your Amazon S3 bucket. Replace `amzn-s3-demo-bucket` with your bucket name. 

```
zip my_package.zip my_module.py

aws s3 cp my_package.zip s3://amzn-s3-demo-bucket/code/my_package.zip
aws s3 cp my_dag.yaml s3://amzn-s3-demo-bucket/dags/my_dag.yaml
```

 In the following command, replace {{my-workflow}} with your workflow name. Replace {{dags/my\_dag.yaml}} and {{code/my\_package.zip}} with the Amazon S3 object keys of your YAML definition and code package. Replace the role ARN with your execution role ARN, and replace {{us-east-1}} with your Region. The following AWS CLI command creates the workflow with the code package, the YAML definition, and the Secrets Manager backend settings: 

```
aws mwaa-serverless create-workflow \
    --name {{my-workflow}} \
    --definition-s3-location '{"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{dags/my_dag.yaml}}"}' \
    --code '{"S3Location": {"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{code/my_package.zip}}"}}' \
    --environment '{"Variables": {
        "AIRFLOW__WORKERS__SECRETS_BACKEND": "airflow.providers.amazon.aws.secrets.secrets_manager.SecretsManagerBackend",
        "AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS": "{\"connections_prefix\": \"airflow/connections\", \"variables_prefix\": \"airflow/variables\", \"region_name\": \"{{us-east-1}}\"}"
    }}' \
    --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
    --region {{us-east-1}}
```

 Use the following AWS CLI command to start a workflow run. Replace the workflow ARN and the Region with your own values. 

```
aws mwaa-serverless start-workflow-run \
    --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/my-workflow-a1b2c3d4e5}} \
    --region {{us-east-1}}
```

 The task logs the non-secret connection fields and the variable value. To find these log messages, see [Viewing task logs](custom-code-operators.md#operators-python-bash-troubleshooting-logs). 

## Limitations for connections and variables
<a name="connections-limitations"></a>

The following limitations apply to connections and variables in Amazon MWAA Serverless:
+ To configure a secrets backend, set both `AIRFLOW__WORKERS__SECRETS_BACKEND` and `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS`. Both count toward the limit of 50 environment variables per workflow. For more information, see [Limits and reserved keys](workflows-environment-variables.md#workflows-environment-variables-limits).
+ A workflow uses one secrets backend. You can't chain multiple backends.
+ To read Secrets Manager secrets across accounts, use a customer managed AWS KMS key. You can't use the AWS managed key `aws/secretsmanager`.
+ `GetWorkflow` returns connections and variables that you define as environment variables in plain text. Use them only for non-secret values.

## Troubleshooting connections and variables
<a name="connections-troubleshooting"></a>

 Errors from connection and variable lookups appear in the task logs. To find the logs, see [Viewing task logs](custom-code-operators.md#operators-python-bash-troubleshooting-logs). The following table lists common problems, along with their causes and fixes. 


| Error or symptom | Cause | Fix | 
| --- | --- | --- | 
| AirflowNotFoundException for a connection, or KeyError for a variable | You haven't configured a secrets backend, or no location in the lookup order has the key. For example, your secret name doesn't match the prefix and key, your secret is in a different Region or account, or your lookup pattern excludes the key. | Check that the secret name is the prefix followed by / and the exact key, in the workflow's Region. If you set lookup patterns, check that the key matches them. If you store the value in a secrets backend, set the backend variables as described in [Configuring a secrets backend](#connections-backend-override). | 
| AccessDeniedException when reading a secret or parameter | The execution role lacks secretsmanager:GetSecretValue, or ssm:GetParameter and ssm:GetParameters, on the resource. | Add the policy for your backend, with Resource values that match your prefixes. For more information about the policy, see [Execution role permissions](#connections-permissions). | 
| AWS KMS AccessDeniedException or a decrypt error | The secret or SecureString parameter uses a customer managed key that the execution role can't use. | Grant kms:Decrypt on the key in the role's policy and allow the role in the key policy. | 
| A connection has incorrect or empty fields | The URI is wrapped in quotation marks, or special characters in the user name or password aren't URL-encoded. | Store the URI without quotation marks and URL-encode special characters, or store the connection as JSON. | 
| The secrets backend has no effect | Only one of the two backend variables is set, or the AIRFLOW\_\_WORKERS\_\_SECRETS\_BACKEND\_KWARGS JSON is malformed. | Set both variables, escape the inner quotation marks in the kwargs JSON, and run update-workflow. | 
| ModuleNotFoundError for a custom backend class | The class path in AIRFLOW\_\_WORKERS\_\_SECRETS\_BACKEND doesn't match the module's location in the code package, or the workflow has no --code package. | Match the class path to the package layout. For more information, see [Preparing your code package](custom-code-operators.md#operators-python-bash-zip). | 
| Cross-account lookups fail | The secret's resource policy doesn't allow the execution role, or the secret uses the aws/secretsmanager key. | Meet the cross-account requirements. For more information about the requirements, see [Option D: Secrets Manager secrets in another account](#connections-cross-account). | 
| An AIRFLOW\_CONN\_\* or AIRFLOW\_VAR\_\* value isn't used | A value with the same key exists in the secrets backend, which Apache Airflow checks first. | Define each connection and variable in only one place. For more information, see [How Amazon MWAA Serverless looks up connections and variables](#connections-lookup-order). | 
| Higher than expected Secrets Manager charges | Every lookup, including lookups for keys that don't exist in Secrets Manager, calls the Secrets Manager API. | Add lookup patterns to the backend keyword arguments so that Apache Airflow queries Secrets Manager only for keys that you store there. | 