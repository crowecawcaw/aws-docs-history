

# Configuring Harness connections
<a name="harness-configuring-connections"></a>

Harness connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Harness connection:

1. In Harness, create a personal access token or a service account token, and copy the token value. For more information, see the [Harness API documentation](https://apidocs.harness.io/) on the Harness website.

1. In Secrets Manager, create a secret with the key `apiKey` set to the token value. Store only the token value.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Harness as the data source. For the `accountIdentifier` connection property, enter your Harness account ID. The account ID appears in the Harness URL after `/account/`.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.