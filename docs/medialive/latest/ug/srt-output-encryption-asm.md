# Set up the passphrase in AWS Secrets Manager

You must set up for the mandatory encryption of the SRT output. Follow these
steps:

1. You and the operator of the downstream system should have already agreed about
   an encryption passphrase.
2. Give the passphrase to a person in your organization who works with AWS Secrets Manager.
   That person must store the passphrase in a secret in Secrets Manager. For more
   information, see [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"). Create a secret of type
   **Other type of secret**.

Secrets Manager generates an ARN that looks like this:

`arn:aws:secretsmanager:`region`:123456789012:secret:`Sample-abcdef``3. Make sure that you obtain the name of the secret. For example,
`Sample-abcdef`. You don't need the ARN.
