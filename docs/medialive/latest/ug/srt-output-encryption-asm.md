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

`arn:aws:secretsmanager:`region`:123456789012:secret:`Sample-abcdef``

###### Important

Store SRT passphrases in Secrets Manager as plaintext (for example, `secretpassword123`). Do not use the key/value option or JSON format when creating the Secret, as this may cause interoperability issues with other services. Store the passphrase as plaintext only.

Ensure your passphrase is between 10 and 79 characters. 3. Make sure that you obtain the full ARN of the secret to use for your SRT output's encryption passphrase Secret ARN.
