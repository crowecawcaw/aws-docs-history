# Set up the passphrase in AWS Secrets Manager

You must set up for the mandatory encryption of the SRT output. Follow these
steps:

1. You and the operator of the downstream system should have already agreed about
   an encryption passphrase.
2. Give the passphrase to a person in your organization who works with AWS Secrets Manager.
   That person must store the passphrase in a secret in Secrets Manager. For more
   information, see [Storing an encryption or decryption passphrase](encryption-srt-password.md "encryption-srt-password.md") .

Secrets Manager generates an ARN that looks like this:

`arn:aws:secretsmanager:`region`:123456789012:secret:`Sample-abcdef``3. Make sure that you obtain the name of the secret. For example,
`Sample-abcdef`. You don't need the ARN.
