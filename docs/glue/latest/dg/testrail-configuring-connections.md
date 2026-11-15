

# Configuring TestRail connections
<a name="testrail-configuring-connections"></a>

TestRail connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a TestRail connection:

1. In TestRail, each user creates an API key (My Settings → API Keys) with API access enabled for the instance. Store the login email and API key in Secrets Manager as the HTTP Basic username and password. The `instance` is supplied as a connection input.

1. In Secrets Manager, create a secret containing your TestRail credential with the keys `USERNAME` and `PASSWORD`.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose TestRail as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.