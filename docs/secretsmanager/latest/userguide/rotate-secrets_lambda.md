

# Rotation by Lambda function
<a name="rotate-secrets_lambda"></a>

For many types of secrets, Secrets Manager uses an AWS Lambda function to update the secret and the database or service. For information about the costs of using a Lambda function, see [Pricing](intro.md#asm_pricing).

For some [Secrets managed by other services](service-linked-secrets.md), you use *managed rotation*. To use [Managed rotation](rotate-secrets_managed.md), you first create the secret through the managing service.

During rotation, Secrets Manager logs events that indicate the state of rotation. For more information, see [Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md).

To rotate a secret, Secrets Manager calls a [ Lambda function](rotate-secrets_lambda-functions.md) according to the rotation schedule you set up. If you also manually update your secret value while automatic rotation is set up, then Secrets Manager considers that a valid rotation when it calculates the next rotation date. 

During rotation, Secrets Manager calls the same function several times, each time with different parameters. Secrets Manager invokes the function with the following JSON request structure of parameters: 

```
{
    "Step" : "request.type",
    "SecretId" : "string",
    "ClientRequestToken" : "string",
    "RotationToken" : "string"
}
```

**Parameters:**
+ **Step** – The rotation step: `create_secret`, `set_secret`, `test_secret`, or `finish_secret`. For more information, see [Four steps in a rotation function](rotate-secrets_lambda-functions.md#rotate-secrets_lambda-functions-code).
+ **SecretId** – The ARN of the secret to rotate.
+ **ClientRequestToken** – A unique identifier for the new version of the secret. This value helps ensure idempotency. For more information, see [PutSecretValue: ClientRequestToken](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_PutSecretValue.html#SecretsManager-PutSecretValue-request-ClientRequestToken) in the *AWS Secrets Manager API Reference*.
+ **RotationToken** – A unique identifier that indicates the source of the request. Required for secret rotation using an assumed role or cross-account rotation, in which you rotate a secret in one account by using a Lambda rotation function in another account. In both cases, the rotation function assumes an IAM role to call Secrets Manager and then Secrets Manager uses the rotation token to validate the IAM role identity. 

Rotation failures can occur because of issues with your Lambda function or with Secrets Manager. If any rotation step fails, Secrets Manager retries the entire rotation process multiple times during the open rotation windows on the secret.

**Topics**
+ [Automatic rotation for database secrets (console)](rotate-secrets_turn-on-for-db.md)
+ [Automatic rotation for non-database secrets (console)](rotate-secrets_turn-on-for-other.md)
+ [Automatic rotation (AWS CLI)](rotate-secrets_turn-on-cli.md)
+ [Lambda function rotation strategies](rotation-strategy.md)
+ [Lambda rotation functions](rotate-secrets_lambda-functions.md)
+ [Rotation function templates](reference_available-rotation-templates.md)
+ [Permissions for rotation](rotating-secrets-required-permissions-function.md)
+ [Network access for AWS Lambda rotation function](rotation-function-network-access.md)
+ [Troubleshoot rotation](troubleshoot_rotation.md)