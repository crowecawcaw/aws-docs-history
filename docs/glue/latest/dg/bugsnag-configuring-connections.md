

# Configuring BugSnag connections
<a name="bugsnag-configuring-connections"></a>

BugSnag connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a BugSnag connection:

1. In BugSnag, open Settings → My account → Personal auth tokens and create a Data Access API token. Store it in Secrets Manager. The connector sends it as `Authorization: token <value>`.

1. In Secrets Manager, create a secret containing the key `authToken` set to your BugSnag credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose BugSnag as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.