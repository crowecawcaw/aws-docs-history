# Get a Secrets Manager secret value using the Rust AWS SDK

In applications, you can retrieve your secrets by calling `GetSecretValue` or `BatchGetSecretValue`in any of the AWS SDKs. However, we recommend that you cache your secret values by using client-side caching. Caching secrets improves speed and reduces your costs.

For Rust applications, use the [Secrets Manager Rust-based caching component](retrieving-secrets_cache-rust.md "retrieving-secrets_cache-rust.md") or call the [SDK directly](https://docs.rs/releases/search?query=aws-sdk-secretsmanager "https://docs.rs/releases/search?query=aws-sdk-secretsmanager") with GetSecretValue or BatchGetSecretValue.

The following code example shows how to get a Secrets Manager secret value.

**Required permissions:** `secretsmanager:GetSecretValue`

```
async fn show_secret(client: &Client, name: &str) -> Result<(), Error> {
    let resp = client.get_secret_value().secret_id(name).send().await?;

    println!("Value: {}", resp.secret_string().unwrap_or("No value!"));

    Ok(())
}

```
