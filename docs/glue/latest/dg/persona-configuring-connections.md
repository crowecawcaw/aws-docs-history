

# Configuring Persona connections
<a name="persona-configuring-connections"></a>

Persona connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Persona connection:

1. In the Persona Dashboard, choose **API**, then **API Keys**, and create or copy an API key for the environment (sandbox or production) that you want to read. If the key has restricted permissions, grant `account.read`, `list.read`, `inquiry.read`, and `api_log.read`. For more information, see [API keys](https://docs.withpersona.com/2025-12-08/api-reference/api-overview) on the Persona website.

1. In Secrets Manager, create a secret with the key `api_key`. Set the value to the raw API key without the `Bearer` prefix. The connector adds the prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Persona as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.