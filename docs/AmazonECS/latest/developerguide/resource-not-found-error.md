# Troubleshooting Amazon ECS ResourceNotFoundException

errors

The following are some `ResourceNotFoundException` error messages and actions that
you can take to fix the errors.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md "stopped-task-errors.md").

## The task can't retrieve the secret with ARN

'`sercretARN`' from AWS Secrets Manager. Check whether the secret
exists in the specified Region.

This error occurs when the task can't retrieve the secret from Secrets Manager. This means that
the secret specified in the task definition (and contained in the error message) does
not exist in Secrets Manager.

The Region is in the error message.

Fetching secret data from AWS Secrets Manager in region `region`:
secret `sercretARN`: ResourceNotFoundException: Secrets Manager can't
find the specified secret.

For information about finding a secret, see [Find secrets in
AWS Secrets Manager](../../../secretsmanager/latest/userguide/manage_search-secret.md "../../../secretsmanager/latest/userguide/manage_search-secret.md") in the _AWS Secrets Manager User
Guide_.

Use the following table to determine and address the error.

| Issue                                                                                           | Actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The secret is in a different Region from the the task definition.                               | 1. Create the secret in the same Region as the task. For more information, see [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"). 2. Update the task definition with the new secret. For more information, see [Updating an Amazon ECS task definition using the console](update-task-definition-console-v2.md "update-task-definition-console-v2.md") or [RegisterTaskDefinition](../APIReference/API_RegisterTaskDefinition.md "../APIReference/API_RegisterTaskDefinition.md") in the _Amazon Elastic Container Service API Reference_. |
| The task definition has the incorrect secret ARN. The correct secret exists in Secrets Manager. | Update the task definition with the correct secret. For more information, see [Updating an Amazon ECS task definition using the console](update-task-definition-console-v2.md "update-task-definition-console-v2.md") or [RegisterTaskDefinition](../APIReference/API_RegisterTaskDefinition.md "../APIReference/API_RegisterTaskDefinition.md") in the _Amazon Elastic Container Service API Reference_.                                                                                                                                                                                                                                              |
| The secret no longer exists.                                                                    | 1. Create the secret in the same Region as the task. For more information, see [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"). 2. Update the task definition with the new secret. For more information, see [Updating an Amazon ECS task definition using the console](update-task-definition-console-v2.md "update-task-definition-console-v2.md") or [RegisterTaskDefinition](../APIReference/API_RegisterTaskDefinition.md "../APIReference/API_RegisterTaskDefinition.md") in the _Amazon Elastic Container Service API Reference_. |
