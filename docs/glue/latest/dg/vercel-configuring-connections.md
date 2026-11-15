

# Configuring Vercel connections
<a name="vercel-configuring-connections"></a>

Vercel connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Vercel connection:

1. In Vercel, open your account settings and create an access token under **Tokens**. Set the token scope to your personal account or to the team that you want to read. For more information, see [Vercel REST API](https://vercel.com/docs/rest-api) on the Vercel website.

1. In Secrets Manager, create a secret with the key `accessToken`. Set the value to the raw access token without the `Bearer` prefix. The connector adds the prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Vercel as the data source.

1. (Optional) To read resources that a Vercel team owns, set the `teamId` connection property to the team ID, or the `slug` connection property to the team slug. If you leave both empty, the connector reads only the resources in your personal account.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.