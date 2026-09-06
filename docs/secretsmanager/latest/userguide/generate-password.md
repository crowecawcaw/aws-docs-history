

# Generate a password with Secrets Manager
<a name="generate-password"></a>

A common pattern for using Secrets Manager is to generate a password in Secrets Manager and then use that password in your database or service. You can do this using the following methods:
+ CloudFormation – See [Create AWS Secrets Manager secrets in AWS CloudFormation](cloudformation.md).
+ AWS CLI – See [`get-random-password`](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/get-random-password.html).
+ AWS SDKs – See [`GetRandomPassword`](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetRandomPassword.html).