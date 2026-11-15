

# Configuring dbt Cloud connections
<a name="dbt-configuring-connections"></a>

dbt Cloud connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a dbt Cloud connection:

1. Create a dbt Cloud service token or personal access token. For more information, see [Authentication tokens](https://docs.getdbt.com/docs/dbt-apis/authentication) on the dbt Developer Hub website.

1. In Secrets Manager, create a secret containing the key `api_key` set to your dbt Cloud token. Store only the token value. The connector adds the `Token` prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose dbt Cloud as the data source.

1. For the URL connection property, enter the access URL of your dbt Cloud account without an `/api` path, for example `https://cloud.getdbt.com` or `https://{{ACCOUNT_PREFIX}}.us1.dbt.com`. You can find the access URL in your dbt Cloud account settings.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.