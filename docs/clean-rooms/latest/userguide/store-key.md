# Step 6: Store the shared secret key in an environment

variable

An environment variable is a convenient and extensible way for users to provide a secret
key from various key stores like AWS Secrets Manager and pass it to the C3R encryption client.

The C3R encryption client can use keys stored in AWS services if you use the AWS CLI to store
those keys in the relevant environment variable. For example, the C3R encryption client can use a key
from AWS Secrets Manager. For more information, see [Create and
manage secrets with AWS Secrets Manager](../../../secretsmanager/latest/userguide/managing-secrets.md "../../../secretsmanager/latest/userguide/managing-secrets.md") in the _AWS Secrets Manager User
Guide_.

###### Note

However, before you use an AWS service such as AWS Secrets Manager to hold your C3R
keys, verify that your use case permits it. Certain use cases might require that the key be
withheld from AWS. This is to ensure that the encrypted data and the key are never held by
the same third party.

The only requirements for a shared secret key are that the shared secret key is
base64-encoded and stored in the environment variable
`C3R_SHARED_SECRET`.

The following sections describe the console commands for converting a
`secret.key` file to base64 and storing it as an environment
variable. The `secret.key` file could have been generated from any of the commands
listed in [Step 5: Create a shared secret key](create-SSK.md "create-SSK.md") and is only an example
source.

## Store key in an environment variable on

Windows using PowerShell

To convert to base64 and set the environment variable on
Windows using PowerShell, run the following command.

```
`$Bytes=[IO.File]::ReadAllBytes((Get-Location).ToString()+'\secret.key'); $env:C3R_SHARED_SECRET=[Convert]::ToBase64String($Bytes)`
```

## Store key in an environment variable on

Linux or macOS

To convert to base64 and set the environment variable on
Linux or macOS, run the following command.

```
`export C3R_SHARED_SECRET="$(cat secret.key | base64)"`
```
