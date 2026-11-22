

# Configuring LogRocket connections

LogRocket connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a LogRocket connection:

1. Obtain your LogRocket API credential (see the LogRocket API documentation on the LogRocket website).

1. In Secrets Manager, create a secret containing the key `apiKey` set to your LogRocket credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose LogRocket as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.