

# Configuring Pinecone connections
<a name="pinecone-configuring-connections"></a>

Pinecone connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Pinecone connection:

1. In the Pinecone console, select the project that you want to read, choose **API keys**, and then choose **\+ API key**. Copy the generated key. For more information, see [Manage API keys](https://docs.pinecone.io/admin/projects/manage-api-keys) on the Pinecone website.

1. In Secrets Manager, create a secret with the key `api_key`. Set the value to the raw API key. The connector sends it in the `Api-Key` header.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Pinecone as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.