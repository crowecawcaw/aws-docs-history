

# Configuring Postman connections
<a name="postman-configuring-connections"></a>

Postman connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Postman connection:

1. In Postman, choose **Settings**, **Account settings**, **API keys**, and then choose **Generate API Key**. The key can read any Postman data that your user has permission to access. For more information, see [Generate and use Postman API keys](https://learning.postman.com/docs/developer/postman-api/authentication/) on the Postman website.

1. In Secrets Manager, create a secret with the key `api_key`. Set the value to the raw API key. The connector sends it in the `X-Api-Key` header.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Postman as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.