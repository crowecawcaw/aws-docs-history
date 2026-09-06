

# Pass Secrets Manager secrets programmatically in Amazon ECS
<a name="secrets-app-secrets-manager"></a>

Instead of hardcoding sensitive information in plain text in your application, you can use Secrets Manager to store the sensitive data.

We recommend this method of retrieving sensitive data because if the Secrets Manager secret is subsequently updated, the application automatically retrieves the latest version of the secret.

Create a secret in Secrets Manager. After you create a Secrets Manager secret, update your application code to retrieve the secret.

Review the following considerations before securing sensitive data in Secrets Manager.
+ Only secrets that store text data, which are secrets created with the `SecretString` parameter of the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) API, are supported. Secrets that store binary data, which are secrets created with the `SecretBinary` parameter of the [CreateSecret](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html) API are not supported.
+ Use interface VPC endpoints to enhance security controls. You must create the interface VPC endpoints for Secrets Manager. For information about the VPC endpoint, see [Create VPC endpoints](https://docs.aws.amazon.com/secretsmanager/latest/userguide/setup-create-vpc.html) in the *AWS Secrets Manager User Guide*.
+ The VPC your task uses must use DNS resolution.
+ Your task definition must use a task role with the additional permissions for Secrets Manager. For more information, see [Amazon ECS task IAM role](task-iam-roles.md).

## Create the Secrets Manager secret
<a name="secrets-app-secrets-manager-create-secret"></a>

You can use the Secrets Manager console to create a secret for your sensitive data. For information about how to create secrets, see [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *AWS Secrets Manager User Guide*.

## Update your application to programmatically retrieve Secrets Manager secrets
<a name="secrets-app-secrets-manager-update-app"></a>

You can retrieve secrets with a call to the Secrets Manager APIs directly from your application. For information, see [Retrieve secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the *AWS Secrets Manager User Guide*.

To retrieve the sensitive data stored in the AWS Secrets Manager, see [Code examples for AWS Secrets Manager using AWS SDKs](https://docs.aws.amazon.com/code-library/latest/ug/secrets-manager_code_examples.html) in the *AWS SDK Code Examples Code Library*.