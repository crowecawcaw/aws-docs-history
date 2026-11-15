

# Configuring BambooHR connections
<a name="bamboohr-configuring-connections"></a>

BambooHR connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a BambooHR connection:

1. Obtain your BambooHR API credential (see the BambooHR API documentation on the BambooHR website).

1. In Secrets Manager, create a secret containing your BambooHR credential with the `username` and `password` keys.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose BambooHR as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.