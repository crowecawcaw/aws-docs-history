

# Configuring RudderStack connections

RudderStack connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a RudderStack connection:

1. Create a workspace-level Service Access Token in the RudderStack workspace settings (Settings → Access tokens) with Transformations/Libraries read permissions. It is sent as a Bearer token. (RudderStack also allows a Personal Access Token with a Read-Write role, but documents it for testing/personal use only—see limitations.)

1. In Secrets Manager, create a secret containing the key `accessToken` set to your RudderStack credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose RudderStack as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.