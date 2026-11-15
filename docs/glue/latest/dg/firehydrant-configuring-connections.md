

# Configuring FireHydrant connections
<a name="firehydrant-configuring-connections"></a>

FireHydrant connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a FireHydrant connection:

1. A FireHydrant Owner opens Settings > API Keys and creates an API key. Store the raw token in Secrets Manager under the connector's `apiKey` property.

1. In Secrets Manager, create a secret containing the key `apiKey` set to your FireHydrant credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose FireHydrant as the data source.

1. For the connection URL, keep the default `https://api.firehydrant.io/v1` if your account uses the standard API host. If your account uses the EU API host, choose `https://api.eu.firehydrant.io/v1`. The AWS Region of your AWS Glue job does not determine the host.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.