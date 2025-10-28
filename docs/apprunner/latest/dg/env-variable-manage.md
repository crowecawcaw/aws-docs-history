# Managing your environment variables

Manage the environment variables for your App Runner service by using one of the following methods:

- [App Runner console](#env-variable-manage.console "#env-variable-manage.console")
- [App Runner API or AWS CLI](#env-variable-manage.api "#env-variable-manage.api")

## App Runner console

When you [create a service](manage-create.md "manage-create.md") or [update a service](manage-configure.md "manage-configure.md") on the App Runner console, you
can add environment variables.

### Adding environment variable

###### To add environment variable

1.  Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2.  Based on whether you're creating or updating a service, perform one of the following steps:
    - If you're creating a new service, choose **Create an App Runner service** and go to **Configure
      Service**.
    - If you're updating an existing service, select the service that you want to update and go to the **Configuration** tab of
      the service.

3.  Go to **Environment variables - optional** under **Service settings**.
4.  Choose any of the following options based on your requirement:
    - Choose **Plain Text** from the **Environment variable source** and enter its key-value pairs under
      **Environment variable name** and **Environment variable value**, respectively.

    ###### Note

    Choose **Plain Text** if you want to reference non-sensitive data. This data isn't encrypted and is visible to others in
    the App Runner service configuration and application logs.
    - Choose **Secrets Manager** from the **Environment variable source** to reference the secret that's stored in
      AWS Secrets Manager as environment variable in your service. Provide the environment variable name and Amazon Resource Name (ARN) of the secret that you're referencing under
      **Environment variable name** and **Environment variable
      value** respectively.
    - Choose **SSM Parameter Store** from the **Environment variable source** to reference the parameter
      stored in SSM Parameter Store as environment variable in your service. Provide the environment variable name and ARN of the parameter that
      you're referencing under **Environment variable name** and **Environment variable value** respectively.

    ###### Note

        + You cannot assign `PORT` as a name for an environment variable when creating or updating your App Runner service.
         It's a reserved environment variable for App Runner service.
        + If the SSM Parameter Store parameter is in the same AWS Region as the service that you want to launch, you can specify the full
         Amazon Resource Name (ARN) or the name of the parameter. If the parameter is in a different Region, you need to specify the full ARN.
        + Make sure that parameter that you're referencing to is in the same account as the service that you're launching or updating.
         Currently, you can't reference SSM Parameter Store parameter across accounts.

5.  Choose **Add environment variable** to reference to another environment variable.
6.  Expand **IAM policy templates** to view and copy the IAM policy templates provided for the AWS Secrets Manager and SSM Parameter
    Store. You only need to do this if you didn't yet update the IAM policy of your instance role with the required permissions. For more information,
    see [Permissions](env-variable.md#env-variable.sensitivedata.permissions "env-variable.md#env-variable.sensitivedata.permissions").

### Removing environment variable

Before you delete an environment variable make sure that your application code is updated to reflect the same. If the application code is not
updated, your App Runner service might fail.

###### To remove environment variables

1. Open the [App Runner console](https://console.aws.amazon.com/apprunner "https://console.aws.amazon.com/apprunner"), and in the **Regions** list, select your AWS Region.
2. Go to **Configuration** tab of the service you want to update.
3. Go to **Environment variables - optional** under **Service settings**.
4. Choose **Remove** next to the environment variable
   that you want to remove. You receive a message to confirm the deletion.
5. Choose **Delete**.

## App Runner API or AWS CLI

You can reference sensitive data stored in Secrets Manager and SSM Parameter Store by adding them as environment variables in your service.

###### Note

Update the IAM policy of your instance role so App Runner can access secrets and parameters stored in Secrets Manager and SSM Parameter Store. For more
information, see [Permissions](env-variable.md#env-variable.sensitivedata.permissions "env-variable.md#env-variable.sensitivedata.permissions").

###### To reference secrets and configurations as environment variables

1. Create a secret or configuration in the Secrets Manager or SSM Parameter Store.

The following examples show how to create a secret and a parameter using the SSM Parameter Store.

###### Example Creating a secret - Request

The following example shows how to create a secret that represents the database credential.

```
aws secretsmanager create-secret \
—name DevRdsCredentials \
—description "Rds credentials for development account." \
—secret-string "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}"
```

###### Example Creating a secret - Response

```
arn:aws:secretsmanager:<region>:<aws_account_id>:secret:DevRdsCredentials
```

###### Example Creating a configuration - Request

The following example shows how to create a parameter that represents the RDS connection string.

```
aws systemsmanager put-parameter \
—name DevRdsConnectionString \
—value "mysql2://dev-mysqlcluster-rds.com:3306/diegor" \
—type "String" \
—description "Rds connection string for development account."
```

###### Example Creating a configuration - Response

```
arn:aws:ssm:<region>:<aws_account_id>:parameter/DevRdsConnectionString
```

2. Reference the secrets and configurations that are stored in Secrets Manager and SSM Parameter Store by adding them as environment variables. You can add
   environment variables when you create or update your App Runner service.

The following examples shows how to reference secrets and configurations as environment variables on a code-based and an image-based App Runner
service.

###### Example Input.json file for image-based App Runner

service

```
{
  "ServiceName": "example-secrets",
  "SourceConfiguration": {
    "ImageRepository": {
      "ImageIdentifier": "<image-identifier>",
      "ImageConfiguration": {
        "Port": "<port>",
        "RuntimeEnvironmentSecrets": {
          "Credential1":"arn:aws:secretsmanager:<region>:<aws_account_id>:secret:XXXXXXXXXXXX",
          "Credential2":"arn:aws:ssm:<region>:<aws_account_id>:parameter/<parameter-name>"
        }
      },
      "ImageRepositoryType": "ECR_PUBLIC"
    }
  },
  "InstanceConfiguration": {
    "Cpu": "1 vCPU",
    "Memory": "3 GB",
    "InstanceRoleArn": "<instance-role-arn>"
  }
}
```

###### Example Image-based App Runner

service – Request

```
aws apprunner create-service \
--cli-input-json file://input.json
```

###### Example Image-based App Runner

service – Response

```
{
...
      "ImageRepository": {
         "ImageIdentifier":"<image-identifier>",
         "ImageConfiguration":{
            "Port": "<port>",
            "RuntimeEnvironmentSecrets":{
               "Credential1": "arn:aws:secretsmanager:<region>:<aws_account_id>:secret:XXXXXXXXXXXX",
               "Credential2": "arn:aws:ssm:<region>:<aws_account_id>:parameter/<parameter-name>"
            },
            "ImageRepositoryType":"ECR"
      }
   },
   "InstanceConfiguration": {
        "CPU": "1 vCPU",
        "Memory": "3 GB",
        "InstanceRoleArn: "<instance-role-arn>"
   }
...
}
```

###### Example Input.json file for code-based App Runner service

```
{
  "ServiceName": "example-secrets",
  "SourceConfiguration": {
    "AuthenticationConfiguration": {
      "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/XXXXXXXXXX"
    },
    "AutoDeploymentsEnabled": false,
    "CodeRepository": {
      "RepositoryUrl": "<repository-url>",
      "SourceCodeVersion": {
        "Type": "BRANCH",
        "Value": "main"
      },
      "CodeConfiguration": {
        "ConfigurationSource": "API",
        "CodeConfigurationValues": {
          "Runtime": "<runtime>",
          "BuildCommand": "<build-command>",
          "StartCommand": "<start-command>",
          "Port": "<port>",
          "RuntimeEnvironmentSecrets": {
            "Credential1":"arn:aws:secretsmanager:<region>:<aws_account_id>:secret:XXXXXXXXXXXX",
            "Credential2":"arn:aws:ssm:<region>:<aws_account_id>:parameter/<parameter-name>"
          }
        }
      }
    }
  },
  "InstanceConfiguration": {
    "Cpu": "1 vCPU",
    "Memory": "3 GB",
    "InstanceRoleArn": "<instance-role-arn>"
  }
}
```

###### Example Code-based App Runner

service – Request

```
aws apprunner create-service \
--cli-input-json file://input.json
```

###### Example Code-based App Runner

service – Response

```
{
...
   "SourceConfiguration":{
      "CodeRepository":{
         "RepositoryUrl":"<repository-url>",
         "SourceCodeVersion":{
            "Type":"Branch",
            "Value":"main"
         },
         "CodeConfiguration":{
            "ConfigurationSource":"API",
            "CodeConfigurationValues":{
               "Runtime":"<runtime>",
               "BuildCommand":"<build-command>",
               "StartCommand":"<start-command>",
               "Port":"<port>",
               "RuntimeEnvironmentSecrets":{
                  "Credential1" : "arn:aws:secretsmanager:<region>:<aws_account_id>:secret:XXXXXXXX",
                  "Credential2" : "arn:aws:ssm:<region>:<aws_account_id>:parameter/<parameter-name>"
               }
            }
         }
      },
      "InstanceConfiguration": {
        "CPU": "1 vCPU",
        "Memory": "3 GB",
        "InstanceRoleArn: "<instance-role-arn>"
   }
...
}
```

3. The
   `apprunner.yaml` model is updated to reflect the added secrets.

The following is an example of the updated `apprunner.yaml`model.

###### Example `apprunner.yaml`

```
version: 1.0
runtime: python3
build:
  commands:
    build:
      - python -m pip install flask
run:
  command: python app.py
  network:
    port: 8080
  env:
    - name: MY_VAR_EXAMPLE
      value: "example"
  secrets:
    - name: my-secret
      value-from: "arn:aws:secretsmanager:<region>:<aws_account_id>:secret:XXXXXXXXXXXX"
    - name: my-parameter
      value-from: "arn:aws:ssm:<region>:<aws_account_id>:parameter/<parameter-name>"
    - name: my-parameter-only-name
      value-from: "parameter-name"
```
