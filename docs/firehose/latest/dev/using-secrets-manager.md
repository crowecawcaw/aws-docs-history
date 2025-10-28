# Authenticate with AWS Secrets Manager in Amazon Data Firehose

Amazon Data Firehose integrates with AWS Secrets Manager to provide secure access to your secrets and automate
credential rotation. This integration allows Firehose to retrieve a secret from Secrets Manager at
runtime to connect to previously mentioned streaming destinations and deliver your data
streams. With this, your secrets are not visible in plain text during stream creation
workflow either in AWS Management Console or API parameters. It provides a secure practice to manage your
secrets and relieves you from complex credential management activities such as setting up
custom Lambda functions to manage password rotations.

For more information, see the [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide.md "../../../secretsmanager/latest/userguide.md").

###### Topics

- [Understand secrets](secrets-manager-whats-secret.md "secrets-manager-whats-secret.md")
- [Create a secret](secrets-manager-create.md "secrets-manager-create.md")
- [Use the secret](secrets-manager-how.md "secrets-manager-how.md")
- [Rotate the secret](secrets-manager-rotate.md "secrets-manager-rotate.md")
