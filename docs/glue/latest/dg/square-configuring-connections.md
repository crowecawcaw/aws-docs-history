

# Configuring Square connections

Square connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Square connection:

1. Copy the personal access token for your application from the **Credentials** page of the Square Developer Console. Use the production token for live data or the Sandbox token for test data. For more information, see [Access Tokens and Other Credentials](https://developer.squareup.com/docs/build-basics/access-tokens) on the Square Developer website.

1. In Secrets Manager, create a secret containing the key `access_token` set to your Square access token. Store only the token value. The connector adds the `Bearer` prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Square as the data source.

1. For the URL, choose `https://connect.squareup.com` for a production access token or `https://connect.squareupsandbox.com` for a Sandbox access token.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.