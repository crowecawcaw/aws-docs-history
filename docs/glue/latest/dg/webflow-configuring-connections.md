

# Configuring Webflow connections
<a name="webflow-configuring-connections"></a>

Webflow connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Webflow connection:

1. Obtain your Webflow API credential (see the Webflow API documentation on the Webflow website).

1. In Secrets Manager, create a secret containing the key `accessToken` set to your Webflow credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Webflow as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.