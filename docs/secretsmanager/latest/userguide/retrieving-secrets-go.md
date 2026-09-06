

# Get a Secrets Manager secret value using Go
<a name="retrieving-secrets-go"></a>

In applications, you can retrieve your secrets by calling `GetSecretValue` or `BatchGetSecretValue`in any of the AWS SDKs. However, we recommend that you cache your secret values by using client-side caching. Caching secrets improves speed and reduces your costs.

**Topics**
+ [Get a Secrets Manager secret value using Go with client-side caching](retrieving-secrets_cache-go.md)
+ [Get a Secrets Manager secret value using the Go AWS SDK](retrieving-secrets-go-sdk.md)