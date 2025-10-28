# Create an AWS Secrets Manager secret with AWS CloudFormation

This example creates a secret named `CloudFormationCreatedSecret-`a1b2c3d4e5f6``.
The secret value is the following JSON, with a 32-character password that is generated when the secret is created.

```
{
    "password": "`EXAMPLE-PASSWORD`",
    "username": "saanvi"
}
```

This example uses the following CloudFormation resource:

- [`AWS::SecretsManager::Secret`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.md")
  For information about creating resources with AWS CloudFormation, see [Learn template basics](../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md "../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md") in the AWS CloudFormation User Guide.

## JSON

```
{
    "Resources": {
        "CloudFormationCreatedSecret": {
            "Type": "AWS::SecretsManager::Secret",
            "Properties": {
                "Description": "Simple secret created by AWS CloudFormation.",
                "GenerateSecretString": {
                    "SecretStringTemplate": "{\"username\": \"saanvi\"}",
                    "GenerateStringKey": "password",
                    "PasswordLength": 32
                }
            }
        }
    }
}
```

## YAML

```
Resources:
  CloudFormationCreatedSecret:
    Type: 'AWS::SecretsManager::Secret'
    Properties:
      Description: Simple secret created by AWS CloudFormation.
      GenerateSecretString:
        SecretStringTemplate: '{"username": "saanvi"}'
        GenerateStringKey: password
        PasswordLength: 32
```
