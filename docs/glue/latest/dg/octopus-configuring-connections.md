

# Configuring Octopus Deploy connections

Octopus Deploy connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure an Octopus Deploy connection:

1. In the Octopus Web Portal, choose your profile image, choose **Profile**, choose **My API Keys**, and then choose **New API key**. Copy the key when Octopus Deploy generates it, because you can't view it again. The key has the permissions of the user or service account that owns it. For more information, see [Create an API key](https://octopus.com/docs/api/authentication/create-an-api-key) on the Octopus Deploy website.

1. In Secrets Manager, create a secret with the key `apiKey`. Set its value to the API key, which starts with `API-`. The connector sends it in the `X-Octopus-ApiKey` header.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Octopus Deploy as the data source.

1. For the URL connection property, enter the URL of your Octopus Cloud or self-hosted Octopus Server instance followed by `/api`, for example `https://{{your-instance}}.octopus.app/api`.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.