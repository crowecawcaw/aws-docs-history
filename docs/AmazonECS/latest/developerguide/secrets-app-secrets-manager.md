# Pass Secrets Manager secrets programmatically in

Amazon ECS

Instead of hardcoding sensitive information in plain text in your application, you
can use Secrets Manager to store the sensitive data.

We recommend this method of retrieving sensitive data because if the Secrets Manager secret
is subsequently updated, the application automatically retrieves the latest version
of the secret.

Create a secret in Secrets Manager. After you create a Secrets Manager secret, update your application code
to retrieve the secret.

Review the following considerations before securing sensitive data in
Secrets Manager.

- Only secrets that store text data, which are secrets created with the
  `SecretString` parameter of the [CreateSecret](../../../secretsmanager/latest/apireference/API_CreateSecret.md "../../../secretsmanager/latest/apireference/API_CreateSecret.md") API, are supported. Secrets that store binary
  data, which are secrets created with the `SecretBinary` parameter
  of the [CreateSecret](../../../secretsmanager/latest/apireference/API_CreateSecret.md "../../../secretsmanager/latest/apireference/API_CreateSecret.md") API are not supported.
- Use interface VPC endpoints to enhance security controls. You must create the
  interface VPC endpoints for Secrets Manager. For information about the VPC
  endpoint, see [Create VPC endpoints](../../../secretsmanager/latest/userguide/setup-create-vpc.md "../../../secretsmanager/latest/userguide/setup-create-vpc.md") in the
  _AWS Secrets Manager User Guide_.
- The VPC your task uses must use DNS resolution.
- Your task definition must use a task role with the additional permissions for Secrets Manager.
  For more information, see [Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md").

## Create the Secrets Manager secret

You can use the Secrets Manager console to create a secret for your sensitive data. For information
about how to create secrets, see [Create an AWS Secrets Manager
secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_.

## Update your application to

programmatically retrieve Secrets Manager secrets

You can retrieve secrets with a call to the Secrets Manager APIs directly from your application.
For information, see [Retrieve secrets
from AWS Secrets Manager](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md") in the _AWS Secrets Manager User Guide_.

To retrieve the sensitive data stored in the AWS Secrets Manager, see [Code examples for AWS Secrets Manager
using AWS SDKs](../../../code-library/latest/ug/secrets-manager_code_examples.md "../../../code-library/latest/ug/secrets-manager_code_examples.md") in the _AWS SDK Code
Examples Code Library_.
