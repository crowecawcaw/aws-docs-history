# Update the value for an AWS Secrets Manager secret

To update the value of your secret, you can use the console, the CLI, or an SDK. When you update the secret value, Secrets Manager creates a new version of the secret with the staging label `AWSCURRENT`. You can still access the old version, which has the label `AWSPREVIOUS`. You can also add your own labels. For more information, see [Secrets Manager versioning](whats-in-a-secret.md#term_version "whats-in-a-secret.md#term_version").

###### To update the secret value (console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. From the list of secrets, choose your secret.
3. On the secret details page, on the **Overview** tab, in the **Secret value** section, choose
   **Retrieve secret value** and then choose **Edit**.

## AWS CLI

###### To update the secret value (AWS CLI)

- When you enter commands in a command shell, there is a risk of the command
  history being accessed or utilities having access to your command parameters. See [Mitigate the risks of using the AWS CLI
  to store your AWS Secrets Manager secrets](security_cli-exposure-risks.md "security_cli-exposure-risks.md").

The following [`put-secret-value`](../../../cli/latest/reference/secretsmanager/put-secret-value.md "../../../cli/latest/reference/secretsmanager/put-secret-value.md") creates a new version of a secret with two key-value pairs.

```
aws secretsmanager put-secret-value \
      --secret-id MyTestSecret \
      --secret-string "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}"
```

The following [`put-secret-value`](../../../cli/latest/reference/secretsmanager/put-secret-value.md "../../../cli/latest/reference/secretsmanager/put-secret-value.md") creates a new version with a custom staging label. The new version will have the labels `MyLabel` and `AWSCURRENT`.

```
aws secretsmanager put-secret-value \
      --secret-id MyTestSecret \
      --secret-string "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}"
      --version-stages "MyLabel"
```

## AWS SDK

We recommend you avoid calling `PutSecretValue` or `UpdateSecret` at a sustained rate of more than once every 10 minutes. When you call `PutSecretValue` or `UpdateSecret` to update the secret value, Secrets Manager creates a new version of the secret. Secrets Manager removes unlabeled versions when there are more than 100, but it does not remove versions created less than 24 hours ago. If you update the secret value more than once every 10 minutes, you create more versions than Secrets Manager removes, and you will reach the quota for secret versions.

To update a secret value, use the following actions:
[`UpdateSecret`](../apireference/API_UpdateSecret.md "../apireference/API_UpdateSecret.md") or [`PutSecretValue`](../apireference/API_PutSecretValue.md "../apireference/API_PutSecretValue.md"). For more information, see [AWS SDKs](asm_access.md#asm-sdks "asm_access.md#asm-sdks").
