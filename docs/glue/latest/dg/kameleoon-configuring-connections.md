

# Configuring Kameleoon connections
<a name="kameleoon-configuring-connections"></a>

Kameleoon connections use OAuth 2.0 client credentials. You register an API client in Kameleoon to obtain a client ID and client secret, store them in Secrets Manager, and reference that secret when you create the connection in AWS Glue Studio. AWS Glue obtains and refreshes the access token for you; no user sign-in or consent step is required.

To configure a Kameleoon connection:

1. In Kameleoon, create an API client (client credentials grant) to obtain a client ID and client secret (see the Kameleoon API documentation).

1. In Secrets Manager, create a secret containing your Kameleoon OAuth application's `ClientId` and `ClientSecret`.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Kameleoon as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.