

# Configuring Grafana connections
<a name="grafana-configuring-connections"></a>

Grafana connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Grafana connection:

1. In Grafana, choose **Administration**, **Users and access**, **Service accounts**. Create a service account with a role that can read the entities that you plan to use, and then add a service account token. For more information, see [Authentication options for the HTTP API](https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/authentication/) in the Grafana documentation.

1. In Secrets Manager, create a secret that stores the service account token with key `api_key`. Store the raw token without a `Bearer` prefix. The connector sends it in the `Authorization` header as a Bearer token.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Grafana as the data source. For the URL connection property, enter the base URL of your Grafana HTTP API, including the `/api` path. For example, use `https://{{your-stack}}.grafana.net/api` for Grafana Cloud, or `https://{{grafana.example.com}}/api` for a self-managed instance.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.