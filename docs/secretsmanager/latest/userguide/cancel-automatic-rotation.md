

# Cancel automatic rotation in Secrets Manager
<a name="cancel-automatic-rotation"></a>

If you configured [automatic rotation](rotating-secrets.md) for a secret and you want to stop rotating it, you can cancel rotation.

**To cancel automatic rotation**

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose your secret.

1. On the secret details page, under **Rotation configuration**, choose **Edit rotation**. 

1. In the **Edit rotation configuration** dialog box, turn off **Automatic rotation**, and then choose **Save**.

   Secrets Manager retains the rotation configuration information so that you can use it in the future if you decide to turn rotation back on.