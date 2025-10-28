# Data retrieval APIs for AWS Secrets Manager

AWS Secrets Manager provides the following APIs for data retrieval.

| Actions                                                                                                                                                                   | Description                                                      | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------ |
| [BatchGetSecretValue](../../../secretsmanager/latest/apireference/API_BatchGetSecretValue.md "../../../secretsmanager/latest/apireference/API_BatchGetSecretValue.md")    | Retrieve and decrypt a list of secrets                           | List         |
| [DescribeSecret](../../../secretsmanager/latest/apireference/API_DescribeSecret.md "../../../secretsmanager/latest/apireference/API_DescribeSecret.md")                   | Retrieve the metadata about a secret, but not the encrypted data | Read         |
| [GetRandomPassword](../../../secretsmanager/latest/apireference/API_GetRandomPassword.md "../../../secretsmanager/latest/apireference/API_GetRandomPassword.md")          | Generate a random string for use in password creation            | Read         |
| [GetResourcePolicy](../../../secretsmanager/latest/apireference/API_GetResourcePolicy.md "../../../secretsmanager/latest/apireference/API_GetResourcePolicy.md")          | Get the resource policy attached to a secret                     | Read         |
| [GetSecretValue](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md")                   | Retrieve and decrypt the encrypted data                          | Read         |
| [ListSecretVersionIds](../../../secretsmanager/latest/apireference/API_ListSecretVersionIds.md "../../../secretsmanager/latest/apireference/API_ListSecretVersionIds.md") | List the available versions of a secret                          | Read         |
| [ListSecrets](../../../secretsmanager/latest/apireference/API_ListSecrets.md "../../../secretsmanager/latest/apireference/API_ListSecrets.md")                            | List the available secrets                                       | List         |
