# Generate a password with Secrets Manager

A common pattern for using Secrets Manager is to generate a password in Secrets Manager and then use that password in your database or service. You can do this using the following methods:

- CloudFormation – See [Create AWS Secrets Manager secrets in AWS CloudFormation](cloudformation.md "cloudformation.md").
- AWS CLI – See [`get-random-password`](../../../cli/latest/reference/secretsmanager/get-random-password.md "../../../cli/latest/reference/secretsmanager/get-random-password.md").
- AWS SDKs – See [`GetRandomPassword`](../apireference/API_GetRandomPassword.md "../apireference/API_GetRandomPassword.md").
