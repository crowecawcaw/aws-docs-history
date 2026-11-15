

# Configuring Fivetran connections
<a name="fivetran-configuring-connections"></a>

Fivetran connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Fivetran connection:

1. Generate a Fivetran API key and API secret. For more information, see [Authentication](https://fivetran.com/docs/developer-resources/rest-api/getting-started/authentication) on the Fivetran website.

1. In Secrets Manager, create a secret with the key `USERNAME` set to your Fivetran API key and the key `PASSWORD` set to your API secret. Do not Base64-encode the values.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Fivetran as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.