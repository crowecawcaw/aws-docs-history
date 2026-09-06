

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Getting started with Parameter Store
<a name="parameter-store-how-to-retrieve"></a>

 In this tutorial, you learn how to create, retrieve, update, and delete Parameter Store parameters by using the AWS CLI. The examples use a fictional application named `myapp`, the `dev` environment, account `111122223333`, and the `us-east-1` Region. 

## Prerequisites
<a name="parameter-store-getting-started-prerequisites"></a>

 Before you begin, make sure you have the following: 
+  An AWS account. 
+  A place to run AWS CLI commands. You can use AWS CloudShell, a local client with the AWS CLI installed and configured, or an Amazon EC2 instance that has the AWS CLI installed. 
+  IAM permissions to create, retrieve, update, and delete Parameter Store parameters. For this tutorial, the principal running the commands needs IAM permissions such as `ssm:PutParameter`, `ssm:GetParameter`, `ssm:GetParameters`, `ssm:GetParametersByPath`, `ssm:DeleteParameter`, and `ssm:DeleteParameters`. For more information, see [Managing access to Parameter Store parameters using IAM policies](parameter-store-setting-up.md#sysman-paramstore-access) 
+  AWS KMS permissions if you create or retrieve `SecureString` parameters encrypted with a customer managed key. If you use the default AWS managed key for Parameter Store, separate AWS KMS permissions aren't required. 

## Step 1: Create a parameter
<a name="parameter-store-getting-started-create-string"></a>

 Run the `put-parameter` command to create a `String` parameter named `/myapp/dev/log-level` with the value `INFO`. Because you don't specify a tier in this example, Parameter Store creates this parameter in the default standard tier. 

```
aws ssm put-parameter \
    --region us-east-1 \
    --name "/myapp/dev/log-level" \
    --type "String" \
    --value "INFO"
```

## Step 2: Retrieve the parameter value
<a name="parameter-store-getting-started-retrieve-string"></a>

Run the [get-parameter](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameter.html) command to retrieve the value of a single parameter. The following example retrieves the value of the `/myapp/dev/log-level` parameter.

```
aws ssm get-parameter \
    --region us-east-1 \
    --name "/myapp/dev/log-level"
```

 The following sample output prints the value of the parameter and related metadata. 

```
{
    "Parameter": {
        "Name": "/myapp/dev/log-level",
        "Type": "String",
        "Value": "INFO",
        "Version": 1,
        "LastModifiedDate": "2026-06-25T17:20:26.517000+00:00",
        "ARN": "arn:aws:ssm:us-east-1:111122223333:parameter/myapp/dev/log-level",
        "DataType": "text"
    }
}
```

## Step 3: Create a StringList parameter
<a name="parameter-store-getting-started-create-stringlist"></a>

 Run the following command to create a `StringList` parameter named `/myapp/dev/subnet-ids` with three comma-separated subnet IDs. 

```
aws ssm put-parameter \
    --region us-east-1 \
    --name "/myapp/dev/subnet-ids" \
    --type "StringList" \
    --value "subnet-123abc,subnet-456def,subnet-789ghi"
```

## Step 4: Retrieve multiple parameters
<a name="parameter-store-getting-started-get-parameters"></a>

 Run the [get-parameters](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters.html) command to specify up to 10 parameters in a list. The following example specifies the `/myapp/dev/log-level` and `/myapp/dev/subnet-ids` parameters by name. 

```
aws ssm get-parameters \
    --region us-east-1 \
    --names "/myapp/dev/log-level" "/myapp/dev/subnet-ids"
```

## Step 5: Create an encrypted parameter
<a name="parameter-store-getting-started-create-securestring"></a>

Use `SecureString` for configuration values that require encryption, such as service endpoints and account identifiers. For secrets such as database credentials, API keys, or tokens, we recommend AWS Secrets Manager, which provides purpose built security controls including automatic rotation and cross-region replication.

Run the following command to create a `SecureString` parameter named `/myapp/dev/vendor/merchant-id` with the encrypted value `merchant-739482`.

```
aws ssm put-parameter \
    --region us-east-1 \
    --name "/myapp/dev/vendor/merchant-id" \
    --type "SecureString" \
    --value "merchant-739482"
```

**Note**  
If you manage credentials such as usernames, passwords, or any other secrets, we recommend using [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). Secrets Manager is purpose-built for managing secrets such as database credentials, API keys, and supported third-party software-vended secrets. For more information, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*.

Run the following command to see what happens when you retrieve a `SecureString` value without decrypting it.

```
aws ssm get-parameter \
    --region us-east-1 \
    --name "/myapp/dev/vendor/merchant-id"
```

The output shows that encrypted value, not the plaintext.

```
{
    "Parameter": {
        "Name": "/myapp/dev/vendor/merchant-id",
        "Type": "SecureString",
        "Value": "AQICAHh1cV16RSGzfLARDIKV0croMvax6aMUDP1thWREL5ToawG6q+Xj8K...==",
        "Version": 1,
        "LastModifiedDate": "2026-06-25T17:27:56.401000+00:00",
        "ARN": "arn:aws:ssm:us-east-1:111122223333:parameter/myapp/dev/vendor/merchant-id",
        "DataType": "text"
    }
}
```

 Run the following command to retrieve the plaintext value of the `/myapp/dev/vendor/merchant-id` parameter. The `--with-decryption` option tells Parameter Store to return the decrypted value. 

```
aws ssm get-parameter \
    --region us-east-1 \
    --name "/myapp/dev/vendor/merchant-id" \
    --with-decryption
```

The following output shows the plaintext value.

```
{
    "Parameter": {
        "Name": "/myapp/dev/vendor/merchant-id",
        "Type": "SecureString",
        "Value": "merchant-739482",
        "Version": 1,
        "LastModifiedDate": "2026-06-25T17:27:56.401000+00:00",
        "ARN": "arn:aws:ssm:us-east-1:111122223333:parameter/myapp/dev/vendor/merchant-id",
        "DataType": "text"
    }
}
```

## Step 6: Update a parameter
<a name="parameter-store-getting-started-update"></a>

 Run the following command to update the value of the `/myapp/dev/log-level` parameter from `INFO` to `DEBUG`. The `--overwrite` option allows the command to replace the existing value. 

```
aws ssm put-parameter \
    --region us-east-1 \
    --name "/myapp/dev/log-level" \
    --type "String" \
    --value "DEBUG" \
    --overwrite
```

 Parameter Store creates a new version of the parameter each time you update it, as shown in the output. 

```
{
    "Version": 2,
    "Tier": "Standard"
}
```

 Run the [get-parameter-history](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameter-history.html) command to view the history of the `/myapp/dev/log-level` parameter. 

```
aws ssm get-parameter-history \
    --region us-east-1 \
    --name "/myapp/dev/log-level"
```

 The response includes previous versions of the parameter, including the version number, value, type, and last modified date. 

```
{
    "Parameters": [
        {
            "Name": "/myapp/dev/log-level",
            "Type": "String",
            "Value": "INFO",
            "Version": 1,
            "LastModifiedDate": "2026-06-25T15:30:00.000000-04:00",
            "DataType": "text"
        },
        {
            "Name": "/myapp/dev/log-level",
            "Type": "String",
            "Value": "DEBUG",
            "Version": 2,
            "LastModifiedDate": "2026-06-25T15:35:00.000000-04:00",
            "DataType": "text"
        }
    ]
}
```

## Step 7: Retrieve parameters by path
<a name="parameter-store-getting-started-retrieve-by-path"></a>

 Run the [get-parameters-by-path](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-parameters-by-path.html) command to retrieve parameters under the `/myapp/dev/` path. The `--recursive` option includes parameters in lower levels of the hierarchy. 

```
aws ssm get-parameters-by-path \
    --region us-east-1 \
    --path "/myapp/dev/" \
    --recursive
```

The output shows both parameters that you created. The `SecureString` parameter is encrypted.

```
{
    "Parameters": [
        {
            "Name": "/myapp/dev/log-level",
            "Type": "String",
            "Value": "DEBUG",
            "Version": 2,
            "LastModifiedDate": "2026-06-25T17:35:39.184000+00:00",
            "ARN": "arn:aws:ssm:us-east-1:111122223333:parameter/myapp/dev/log-level",
            "DataType": "text"
        },
        {
            "Name": "/myapp/dev/vendor/merchant-id",
            "Type": "SecureString",
            "Value": "AQICAHh1cV16RSGzfLARDIKV0croMvax6aMUDP1thWREL5ToawG6q+Xj8K...==",
            "Version": 1,
            "LastModifiedDate": "2026-06-25T17:27:56.401000+00:00",
            "ARN": "arn:aws:ssm:us-east-1:111122223333:parameter/myapp/dev/vendor/merchant-id",
            "DataType": "text"
        }
    ]
}
```

 Run the following command to retrieve parameters under the `/myapp/dev/` path and return decrypted values for any `SecureString` parameters that the principal is authorized to decrypt. 

```
aws ssm get-parameters-by-path \
    --region us-east-1 \
    --path "/myapp/dev/" \
    --recursive \
    --with-decryption
```

## Step 8: Delete a parameter
<a name="parameter-store-getting-started-delete"></a>

 Run the following command to delete the `/myapp/dev/log-level` parameter. 

```
aws ssm delete-parameter \
    --region us-east-1 \
    --name "/myapp/dev/log-level"
```

## Clean up
<a name="parameter-store-getting-started-cleanup"></a>

 Run the following command to delete the remaining example parameters. 

```
aws ssm delete-parameters \
    --region us-east-1 \
    --names "/myapp/dev/subnet-ids" "/myapp/dev/vendor/merchant-id"
```

## Next steps
<a name="parameter-store-getting-started-next-steps"></a>

 After you create your first parameters, consider the following next steps: 
+  Define a naming convention for applications, environments, and teams. For more information, see [https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-hierarchies.html#ps-hierarchy-examples](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-hierarchies.html#ps-hierarchy-examples). 
+  Use IAM policies to control who can read or update each parameter path. 
+ Use `SecureString` for configuration values that require encryption, such as service endpoints and account identifiers. For secrets such as database credentials, API keys, or tokens, we recommend AWS Secrets Manager, which provides purpose built security controls including automatic rotation and cross-region replication.
+  Use `AWS AppConfig` for feature flags and dynamic application configuration. 