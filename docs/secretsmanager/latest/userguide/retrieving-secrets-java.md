# Get a Secrets Manager secret value using Java

In applications, you can retrieve your secrets by calling `GetSecretValue` or `BatchGetSecretValue`in any of the AWS SDKs. However, we recommend that you cache your secret values by using client-side caching. Caching secrets improves speed and reduces your costs.

To connect to a database using the credentials in a secret, you can use the Secrets Manager SQL Connection drivers, which wrap the base JDBC driver. This also uses client-side caching, so it can reduce the cost for calling Secrets Manager APIs.

###### Topics

- [Get a Secrets Manager secret value using Java with client-side caching](retrieving-secrets_cache-java.md "retrieving-secrets_cache-java.md")
- [Connect to a SQL database using JDBC with credentials in an
  AWS Secrets Manager secret](retrieving-secrets_jdbc.md "retrieving-secrets_jdbc.md")
- [Get a Secrets Manager secret value using the Java AWS SDK](retrieving-secrets-java-sdk.md "retrieving-secrets-java-sdk.md")
