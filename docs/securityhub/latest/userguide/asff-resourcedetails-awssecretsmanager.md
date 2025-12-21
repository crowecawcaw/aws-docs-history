# AwsSecretsManager resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsSecretsManager` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsSecretsManagerSecret

The `AwsSecretsManagerSecret` object provides details about a Secrets Manager
secret.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsSecretsManagerSecret` object. To view descriptions of
`AwsSecretsManagerSecret` attributes, see [AwsSecretsManagerSecretDetails](../../1.0/APIReference/API_AwsSecretsManagerSecretDetails.md "../../1.0/APIReference/API_AwsSecretsManagerSecretDetails.md") in the
_AWS Security Hub API Reference_.

**Example**

```
"AwsSecretsManagerSecret": {
    "RotationRules": {
        "AutomaticallyAfterDays": 30
    },
    "RotationOccurredWithinFrequency": true,
    "KmsKeyId": "kmsKeyId",
    "RotationEnabled": true,
    "RotationLambdaArn": "arn:aws:lambda:us-west-2:777788889999:function:MyTestRotationLambda",
    "Deleted": false,
    "Name": "MyTestDatabaseSecret",
    "Description": "My test database secret"
}

```
