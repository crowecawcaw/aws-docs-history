

# Configuring Amplitude connections
<a name="amplitude-configuring-connections"></a>

Amplitude connections use basic authentication. You store your Amplitude credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure an Amplitude connection:

1. Obtain your Amplitude API credential (see the Amplitude API documentation on the Amplitude website).

1. In Secrets Manager, create a secret containing the keys `USERNAME` and `PASSWORD` set to your Amplitude credentials.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Amplitude as the data source.

1. For the connection URL, keep the default `https://amplitude.com`, or set it to the EU host `https://analytics.eu.amplitude.com` for EU data residency.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.