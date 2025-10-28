# Create an AWS Secrets Manager secret

A _secret_ can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager.

###### Tip

For Amazon RDS and Amazon Redshift admin user credentials, we recommend you use [managed secrets](service-linked-secrets.md "service-linked-secrets.md"). You create the managed secret through the managing service, and then you can use [managed rotation](rotate-secrets_managed.md "rotate-secrets_managed.md").

When you use the console to store database credentials for a source database that is replicated to other Regions, the secret contains connection information for the source database. If you then replicate the secret, the replicas are copies of the source secret and contain the same connection information. You can add additional key/value pairs to the secret for regional connection information.

To create a secret, you need the permissions granted by the [SecretsManagerReadWrite managed policy](reference_available-policies.md "reference_available-policies.md").

Secrets Manager generates a CloudTrail log entry when you create a secret. For more information, see [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").

###### To create a secret (console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. On the **Choose secret type** page, do the following:
   1. For **Secret type**, do one of the following:
      - To store database credentials, choose the type of database credentials to
        store. Then choose the **Database** and then enter the **Credentials**.
      - To store API keys, access tokens, credentials that aren't for databases, choose **Other type of
        secret**.

      In **Key/value pairs**, either enter your secret in JSON
      **Key/value** pairs, or choose the **Plaintext**
      tab and enter the secret in any format. You can store up to 65536
      bytes in the secret. Some examples:

      API key
      Enter as key/value pairs:

      `ClientID` :
      `my_client_id`

      `ClientSecret` :
      `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

      OAuth token
      Enter as plaintext:

      `AKIAI44QH8DHBEXAMPLE`

      Digital certificate
      Enter as plaintext:

      ```
      -----BEGIN CERTIFICATE-----
      *EXAMPLE*
      -----END CERTIFICATE-----
      ```

      Private key
      Enter as plaintext:

      ```
      –--- BEGIN PRIVATE KEY ----
      *EXAMPLE*
      ––-- END PRIVATE KEY –---
      ```

   2. For **Encryption key**, choose the AWS KMS key that Secrets Manager uses
      to encrypt the secret value. For more information, see [Secret encryption and decryption](security-encryption.md "security-encryption.md").
      - For most cases, choose **aws/secretsmanager** to use the
        AWS managed key for Secrets Manager. There is no cost for using this key.
      - If you need to access the secret from another AWS account, or if you want to use
        your own KMS key so that you can rotate it or apply a key policy to it, choose a
        customer managed key from the list or choose **Add new key** to create one.
        For information about the costs of using a customer managed key, see [Pricing](intro.md#asm_pricing "intro.md#asm_pricing").

      You must have [Permissions for the KMS key](security-encryption.md#security-encryption-authz "security-encryption.md#security-encryption-authz"). For
      information about cross-account access, see [Access AWS Secrets Manager secrets from a different
      account](auth-and-access_examples_cross.md "auth-and-access_examples_cross.md").

   3. Choose **Next**.

4. On the **Configure secret** page, do the following:
   1. Enter a descriptive **Secret name** and
      **Description**. Secret names can contain 1-512 alphanumeric and /\_+=.@- characters.
   2. (Optional) In the **Tags** section, add tags to your secret. For
      tagging strategies, see [Tagging secrets in AWS Secrets Manager](managing-secrets_tagging.md "managing-secrets_tagging.md"). Don't store
      sensitive information in tags because they aren't encrypted.
   3. (Optional) In **Resource permissions**, to add a resource policy
      to your secret, choose **Edit permissions**. For more information,
      see [Resource-based policies](auth-and-access_resource-policies.md "auth-and-access_resource-policies.md").
   4. (Optional) In **Replicate secret**, to replicate your secret to
      another AWS Region, choose **Replicate secret**. You can replicate
      your secret now or come back and replicate it later. For more information, see [Multi-region replication](replicate-secrets.md "replicate-secrets.md").
   5. Choose **Next**.

5. (Optional) On the **Configure rotation** page, you can turn on automatic
   rotation. You can also keep rotation off for now and then turn it on later. For more
   information, see [Rotate secrets](rotating-secrets.md "rotating-secrets.md"). Choose **Next**.
6. On the **Review** page, review your secret details, and then choose
   **Store**.

Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the
refresh button.

## AWS CLI

When you enter commands in a command shell, there is a risk of the command
history being accessed or utilities having access to your command parameters. See [Mitigate the risks of using the AWS CLI
to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md "security_cli-exposure-risks.md").

###### Example Create a secret from database credentials in a JSON file

The following [`create-secret`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html") example creates a secret from credentials in a file. For more information, see [Loading AWS CLI parameters from a file](../../../cli/latest/userguide/cli-usage-parameters-file.md "../../../cli/latest/userguide/cli-usage-parameters-file.md") in the AWS CLI User Guide.

For Secrets Manager to be able to rotate the secret, you must make sure the JSON matches the [JSON structure of a secret](reference_secret_json_structure.md "reference_secret_json_structure.md").

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

###### Example Create a secret

The following [`create-secret`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html") example creates a secret with two key-value pairs.

```
aws secretsmanager create-secret \
    --name MyTestSecret \
    --description "My test secret created with the CLI." \
    --secret-string '{"user":"diegor","password":"EXAMPLE-PASSWORD"}'
```

###### Example Create a secret

The following [`create-secret`](../../../cli/latest/reference/secretsmanager/create-secret.md "../../../cli/latest/reference/secretsmanager/create-secret.md") example creates a secret with two tags.

```
aws secretsmanager create-secret \
    --name MyTestSecret \
    --description "My test secret created with the CLI." \
    --secret-string '{"user":"diegor","password":"EXAMPLE-PASSWORD"}'  \
    --tags '[{"Key": "FirstTag", "Value": "FirstValue"}, {"Key": "SecondTag", "Value": "SecondValue"}]'
```

## AWS SDK

To create a secret by using one of the AWS SDKs, use the [`CreateSecret`](../apireference/API_CreateSecret.md "../apireference/API_CreateSecret.md") action. For more
information, see [AWS SDKs](asm_access.md#asm-sdks "asm_access.md#asm-sdks").
