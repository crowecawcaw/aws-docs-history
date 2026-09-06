

# Create an AWS Secrets Manager secret
<a name="create_secret"></a>

A *secret* can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager. 

**Tip**  
For Amazon RDS and Amazon Redshift admin user credentials, we recommend you use [managed secrets](service-linked-secrets.md). You create the managed secret through the managing service, and then you can use [managed rotation](rotate-secrets_managed.md).

When you use the console to store database credentials for a source database that is replicated to other Regions, the secret contains connection information for the source database. If you then replicate the secret, the replicas are copies of the source secret and contain the same connection information. You can add additional key/value pairs to the secret for regional connection information.

To create a secret, you need the permissions granted by the [SecretsManagerReadWrite managed policy](reference_available-policies.md).

Secrets Manager generates a CloudTrail log entry when you create a secret. For more information, see [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md).

**To create a secret (console)**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following:

   1. For **Secret type**, do one of the following:
      + To store database credentials, choose the type of database credentials to store. Then choose the **Database** and then enter the **Credentials**.
      + To store API keys, access tokens, credentials that aren't for databases, choose **Other type of secret**.

        In **Key/value pairs**, either enter your secret in JSON **Key/value** pairs, or choose the **Plaintext** tab and enter the secret in any format. You can store up to 65536 bytes in the secret. Some examples:

------
#### [ API key ]

        Enter as key/value pairs:

        **ClientID** : {{my\_client\_id}}

        **ClientSecret** : {{wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY}}

------
#### [ OAuth token ]

        Enter as plaintext:

        {{AKIAI44QH8DHBEXAMPLE}}

------
#### [ Digital certificate ]

        Enter as plaintext:

        ```
        -----BEGIN CERTIFICATE-----
        EXAMPLE
        -----END CERTIFICATE-----
        ```

------
#### [ Private key ]

        Enter as plaintext:

        ```
        –--- BEGIN PRIVATE KEY ----
        EXAMPLE
        ––-- END PRIVATE KEY –---
        ```

------
      + To store a managed external secrets from an Secrets Manager partner, choose **Partner secret**. Then choose the partner and provide the details that identify the secret for the partner. For details, see [Using AWS Secrets Manager managed external secrets to manage Third Party secrets](managed-external-secrets.md).

   1. For **Encryption key**, choose the AWS KMS key that Secrets Manager uses to encrypt the secret value. For more information, see [Secret encryption and decryption](security-encryption.md).
      + For most cases, choose **aws/secretsmanager** to use the AWS managed key for Secrets Manager. There is no cost for using this key.
      + If you need to access the secret from another AWS account, or if you want to use your own KMS key so that you can rotate it or apply a key policy to it, choose a customer managed key from the list, enter the key ARN or alias ARN of a customer managed key, or choose **Add new key** to create one. For information about the costs of using a customer managed key, see [Pricing](intro.md#asm_pricing).

        You must have [Permissions for the KMS key](security-encryption.md#security-encryption-authz). For information about cross-account access, see [Access AWS Secrets Manager secrets from a different account](auth-and-access_examples_cross.md). 

   1. Choose **Next**.

1. On the **Configure secret** page, do the following:

   1. Enter a descriptive **Secret name** and **Description**. Secret names can contain 1-512 alphanumeric and /\_\+=.@- characters.

   1. (Optional) If you are created an external secret, enter the metadata required by the Secrets Manager partner that holds the secret.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tagging secrets in AWS Secrets Manager](managing-secrets_tagging.md). Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Resource-based policies](auth-and-access_resource-policies.md).

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Multi-region replication](replicate-secrets.md).

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate secrets](rotating-secrets.md). Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

## AWS CLI
<a name="create_secret_cli"></a>

When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. See [Mitigate the risks of using the AWS CLI to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md).

**Example Create a secret from database credentials in a JSON file**  
The following [`create-secret`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html) example creates a secret from credentials in a file. For more information, see [Loading AWS CLI parameters from a file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html) in the AWS CLI User Guide.  
For Secrets Manager to be able to rotate the secret, you must make sure the JSON matches the [JSON structure of a secret](reference_secret_json_structure.md).  

```
aws secretsmanager create-secret \
    --name MyTestSecret \
    --secret-string file://mycreds.json
```
Contents of mycreds.json:  

```
{
    "engine": "mysql",
    "username": "saanvis",
    "password": "EXAMPLE-PASSWORD",
    "host": "my-database-endpoint.us-west-2.rds.amazonaws.com",
    "dbname": "myDatabase",
    "port": "3306"
}
```

**Example Create a secret**  
The following [`create-secret`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html) example creates a secret with two key-value pairs.  

```
aws secretsmanager create-secret \
    --name MyTestSecret \
    --description "My test secret created with the CLI." \
    --secret-string '{"user":"diegor","password":"EXAMPLE-PASSWORD"}'
```

**Example Create a secret**  
The following [`create-secret`](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/create-secret.html) example creates a secret with two tags.  

```
aws secretsmanager create-secret \
    --name MyTestSecret \
    --description "My test secret created with the CLI." \
    --secret-string '{"user":"diegor","password":"EXAMPLE-PASSWORD"}'  \
    --tags '[{"Key": "FirstTag", "Value": "FirstValue"}, {"Key": "SecondTag", "Value": "SecondValue"}]'
```

## AWS SDK
<a name="create_secret_sdk"></a>

To create a secret by using one of the AWS SDKs, use the [`CreateSecret`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) action. For more information, see [AWS SDKs](asm_access.md#asm-sdks).