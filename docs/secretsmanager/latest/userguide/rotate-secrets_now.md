

# Rotate an AWS Secrets Manager secret immediately
<a name="rotate-secrets_now"></a>

You can only rotate a secret that has rotation configured. To determine whether a secret has been configured for rotation, in the console, view the secret and scroll down to the **Rotation configuration** section. If **Rotation status** is **Enabled**, then the secret is configured for rotation. If not, see [Rotate AWS Secrets Manager secrets](rotating-secrets.md).

**To rotate a secret immediately (console)**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose your secret.

1. On the secret details page, under **Rotation configuration**, choose **Rotate secret immediately**. 

1. In the **Rotate secret** dialog box, choose **Rotate**.

## AWS CLI
<a name="rotate-secrets_now_cli"></a>

**Example Rotate a secret immediately**  
The following [**rotate-secret**](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/rotate-secret.html) example starts an immediate rotation. The secret must already have rotation configured.  

```
$ aws secretsmanager rotate-secret \
    --secret-id {{MyTestSecret}}
```