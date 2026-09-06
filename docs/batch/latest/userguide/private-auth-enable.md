

# Tutorial: Create a secret for private registry authentication
<a name="private-auth-enable"></a>

Complete the following steps to create a secret for your private registry credentials with AWS Secrets Manager.

**Create a basic secret**

1. Open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. For **Select secret type**, choose **Other type of secrets**.

1. Select **Plaintext** and enter your private registry credentials using the following format:

   ```
   {
     "username" : "{{privateRegistryUsername}}",
     "password" : "{{privateRegistryPassword}}"
   }
   ```

1. Choose **Next**.

1. For **Secret name**, enter an optional path and name, such as **production/MyAwesomeAppSecret** or **development/TestSecret**, and choose **Next**. You can optionally add a description to help you remember the purpose of this secret later.

   The secret name must be ASCII letters, digits, or any of the following characters: `/_+=.@-`.

1. (Optional) At this point, you can configure rotation for your secret. For this procedure, leave it at **Disable automatic rotation** and choose **Next**.

   For instructions on how to configure rotation on new or existing secrets, see [Rotating Your AWS Secrets Manager Secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).

1. Review your settings, and then choose **Store secret** to save everything that you entered as a new secret in Secrets Manager.

Register a job definition and under **Private registry**, turn on **Private registry authentication**. Then, in **Secrets Manager ARN or name**, enter the Amazon Resource Name (ARN) of the secret. For more information, see [Required IAM permissions for private registry authentication](private-auth-iam.md).