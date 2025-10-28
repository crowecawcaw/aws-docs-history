# Tutorial: Create a secret for private registry authentication

Complete the following steps to create a secret for your private registry credentials with AWS Secrets Manager.

###### Create a basic secret

1. Open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. For **Select secret type**, choose **Other type of secrets**.
4. Select **Plaintext** and enter your private registry credentials using the following
   format:

```
{
  "username" : "`privateRegistryUsername`",
  "password" : "`privateRegistryPassword`"
}
```

5. Choose **Next**.
6. For **Secret name**, enter an optional path and name, such as
   `production/MyAwesomeAppSecret` or `development/TestSecret`, and choose
   **Next**. You can optionally add a description to help you remember the purpose of this secret
   later.

The secret name must be ASCII letters, digits, or any of the following characters:
`/_+=.@-`. 7. (Optional) At this point, you can configure rotation for your secret. For this procedure, leave it at
**Disable automatic rotation** and choose **Next**.

For instructions on how to configure rotation on new or existing secrets, see [Rotating Your AWS Secrets Manager Secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md"). 8. Review your settings, and then choose **Store secret** to save everything that you entered as
a new secret in Secrets Manager.
Register a job definition and under **Private registry**, turn on **Private registry
authentication**. Then, in **Secrets Manager ARN or name**, enter the Amazon Resource Name
(ARN) of the secret. For more information, see [Required IAM permissions for private registry authentication](private-auth-iam.md "private-auth-iam.md").
