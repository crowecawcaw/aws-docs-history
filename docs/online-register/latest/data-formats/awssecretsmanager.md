

# Data retrieval APIs for AWS Secrets Manager
<a name="awssecretsmanager"></a>

AWS Secrets Manager provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="secretsmanager-BatchGetSecretValue"></a>[BatchGetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_BatchGetSecretValue.html) | Retrieve and decrypt a list of secrets | Read | 
| <a name="secretsmanager-DescribeSecret"></a>[DescribeSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DescribeSecret.html) | Retrieve the metadata about a secret, but not the encrypted data | Read | 
| <a name="secretsmanager-GetRandomPassword"></a>[GetRandomPassword](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html) | Generate a random string for use in password creation | Read | 
| <a name="secretsmanager-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetResourcePolicy.html) | Get the resource policy attached to a secret | Read | 
| <a name="secretsmanager-GetSecretValue"></a>[GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) | Retrieve and decrypt the encrypted data | Read | 
| <a name="secretsmanager-ListSecretVersionIds"></a>[ListSecretVersionIds](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecretVersionIds.html) | List the available versions of a secret | Read | 
| <a name="secretsmanager-ListSecrets"></a>[ListSecrets](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecrets.html) | List the available secrets | List | 