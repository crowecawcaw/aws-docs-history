

# Configuring mabl connections
<a name="mabl-configuring-connections"></a>

mabl connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a mabl connection:

1. In mabl, open Settings → APIs and create an API key for the workspace. Store it in Secrets Manager as the HTTP Basic password (username `key`). The `workspace_id` is supplied as a connection input.

1. In Secrets Manager, create a secret containing your mabl credential with the keys `USERNAME` and `PASSWORD`.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose mabl as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.