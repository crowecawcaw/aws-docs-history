# Get a Secrets Manager secret value using the Go AWS SDK

In applications, you can retrieve your secrets by calling `GetSecretValue` or `BatchGetSecretValue`in any of the AWS SDKs. However, we recommend that you cache your secret values by using client-side caching. Caching secrets improves speed and reduces your costs.

For Go applications, use the [Secrets Manager Go-based
caching component](retrieving-secrets_cache-go.md "retrieving-secrets_cache-go.md") or call the SDK directly with [`GetSecretValue`](../../../sdk-for-go/api/service/secretsmanager.md#SecretsManager.GetSecretValue "../../../sdk-for-go/api/service/secretsmanager.md#SecretsManager.GetSecretValue") or [`BatchGetSecretValue`](../../../sdk-for-go/api/service/secretsmanager.md#SecretsManager.BatchGetSecretValue "../../../sdk-for-go/api/service/secretsmanager.md#SecretsManager.BatchGetSecretValue").

The following code example shows how to get a Secrets Manager secret value.

**Required permissions:** `secretsmanager:GetSecretValue`

```
  // Use this code snippet in your app.
  // If you need more information about configurations or implementing the sample code, visit the AWS docs:
  // https://aws.github.io/aws-sdk-go-v2/docs/getting-started/

  import (
    "context"
    "log"

    "github.com/aws/aws-sdk-go-v2/aws"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/secretsmanager"
  )

  func main() {
    secretName := "<<{{MySecretName}}>>"
    region := "<<{{MyRegionName}}>>"

    config, err := config.LoadDefaultConfig(context.TODO(), config.WithRegion(region))
    if err != nil {
      log.Fatal(err)
    }

    // Create Secrets Manager client
    svc := secretsmanager.NewFromConfig(config)

    input := &secretsmanager.GetSecretValueInput{
      SecretId:     aws.String(secretName),
      VersionStage: aws.String("AWSCURRENT"), // VersionStage defaults to AWSCURRENT if unspecified
    }

    result, err := svc.GetSecretValue(context.TODO(), input)
    if err != nil {
      // For a list of exceptions thrown, see
      // https://<<{{DocsDomain}}>>/secretsmanager/latest/apireference/API_GetSecretValue.html
      log.Fatal(err.Error())
    }

    // Decrypts secret using the associated KMS key.
    var secretString string = *result.SecretString

    // Your code goes here.
  }
```
