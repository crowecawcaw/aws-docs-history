

# Configuring Ontraport connections
<a name="ontraport-configuring-connections"></a>

Ontraport connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure an Ontraport connection:

1. Obtain your Ontraport API credential (see the Ontraport API documentation on the Ontraport website).

1. In Secrets Manager, create a secret containing the keys `Api-Key` and `Api-Appid` set to your Ontraport credentials.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Ontraport as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.