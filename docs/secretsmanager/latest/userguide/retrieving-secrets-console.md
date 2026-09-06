

# Get a secret value using the AWS console
<a name="retrieving-secrets-console"></a>

**To retrieve a secret (console)**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. In the list of secrets, choose the secret you want to retrieve.

1. In the **Secret value** section, choose **Retrieve secret value**.

   Secrets Manager displays the current version (`AWSCURRENT`) of the secret. To see [other versions](whats-in-a-secret.md#term_version) of the secret, such as `AWSPREVIOUS` or custom labeled versions, use the [Get a secret value using the AWS CLI](retrieving-secrets_cli.md).