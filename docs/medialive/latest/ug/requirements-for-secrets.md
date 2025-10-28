# Requirements for Secrets Manager secrets

Your deployment might include the following resources:

- SRT inputs for SRT content that is encrypted by the upstream system.

When the user creates this type of input, they must enter or select the ARN of a secret
that holds the passphrase
for decrypting the content.

- SRT caller outputs. MediaLive always encrypts this
  type of
  output

When the user creates
this type of output, they must enter or select the ARN of a secret that holds the passphrase
for encrypting content.

- AWS Elemental Link hardware devices that are used in MediaLive or in MediaConnect. For more information about
  permissions for this use case, see [Requirements for AWS Elemental Link](requirements-for-link.md "requirements-for-link.md").

| Permissions                                                                                                                                                                                           | Service name in IAM | Actions       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| On the MediaLive console, when creating an SRT Caller input, to view secrets in the dropdown list.On the MediaLive console, when creating an SRT Caller output, to view secrets in the dropdown list. | Secrets Manager     | `ListSecrets` | ## Required permissions **Permission to create an ARN** A user with permissions on Secrets Manager must set up the passphrase as a secret, then provide the MediaLive user with the ARN of that secret. **Permission to select a passphrase** For a list of ARNs to appear in the dropdown list on the console, the console user must have `ListSecrets` in Secrets Manager. The user can then select an ARN from the list. **Permission to enter an ARN** No special permission is required to enter the passphrase on the AWS Elemental MediaLive console. |
