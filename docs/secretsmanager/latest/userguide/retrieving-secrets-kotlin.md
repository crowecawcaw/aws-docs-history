# Get a Secrets Manager secret value using the Kotlin AWS SDK

For Kotlin applications, call the SDK directly with [GetSecretValue](https://github.com/awslabs/aws-sdk-kotlin#generating-api-documentation "https://github.com/awslabs/aws-sdk-kotlin#generating-api-documentation") or [BatchGetSecretValue](https://github.com/awslabs/aws-sdk-kotlin#generating-api-documentation "https://github.com/awslabs/aws-sdk-kotlin#generating-api-documentation").

The following code example shows how to get a Secrets Manager secret value.

**Required permissions:** `secretsmanager:GetSecretValue`

```
suspend fun getValue(secretName: String?) {
    val valueRequest =
        GetSecretValueRequest {
            secretId = secretName
        }

    SecretsManagerClient.fromEnvironment { region = "us-east-1" }.use { secretsClient ->
        val response = secretsClient.getSecretValue(valueRequest)
        val secret = response.secretString
        println("The secret value is $secret")
    }
}

```
