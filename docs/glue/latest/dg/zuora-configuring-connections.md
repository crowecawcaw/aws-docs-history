

# Configuring Zuora connections
<a name="zuora-configuring-connections"></a>

Zuora connections use the OAuth 2.0 client credentials grant. This grant is two-legged: AWS Glue sends your Zuora OAuth client ID and client secret to the Zuora token endpoint and receives an access token. There is no consent screen or redirect URL. AWS Glue requests a new token when the current token expires.

To configure a Zuora connection:

1. In Zuora, create an OAuth client for an API user who can read the data that you want to transfer. A Zuora administrator creates OAuth clients on the user's details page under **Settings**, **Administration**, **Manage Users**. Copy the client secret when it is displayed, because Zuora shows it only once. For more information, see [Obtain your OAuth client credentials](https://developer.zuora.com/docs/get-started/oauth-client-setup-steps) in the Zuora developer documentation.

1. In Secrets Manager, create a secret that stores the client ID with key `CLIENT_ID` and the client secret with key `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET`. Store the raw values without a prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Zuora as the data source.

1. For `Url`, choose the Zuora REST API host for the tenant where you created the OAuth client. For `TokenUrl`, enter the token endpoint on the same host. The default is `https://rest.zuora.com/oauth/token`. For the available values, see the following table.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.

The following table lists the supported Zuora hosts and their `Url` and `TokenUrl` values.


| Environment | Url | TokenUrl | 
| --- | --- | --- | 
| US Production (Cloud 2) | https://rest.zuora.com | https://rest.zuora.com/oauth/token | 
| US Production (Cloud 1) | https://rest.na.zuora.com | https://rest.na.zuora.com/oauth/token | 
| EU Production | https://rest.eu.zuora.com | https://rest.eu.zuora.com/oauth/token | 
| APAC Production | https://rest.ap.zuora.com | https://rest.ap.zuora.com/oauth/token | 
| US API Sandbox (Cloud 2) | https://rest.apisandbox.zuora.com | https://rest.apisandbox.zuora.com/oauth/token | 
| US API Sandbox (Cloud 1) | https://rest.sandbox.na.zuora.com | https://rest.sandbox.na.zuora.com/oauth/token | 
| EU API Sandbox | https://rest.sandbox.eu.zuora.com | https://rest.sandbox.eu.zuora.com/oauth/token | 
| US Developer and Central Sandbox | https://rest.test.zuora.com | https://rest.test.zuora.com/oauth/token | 
| EU Developer and Central Sandbox | https://rest.test.eu.zuora.com | https://rest.test.eu.zuora.com/oauth/token | 
| APAC Developer and Central Sandbox | https://rest.test.ap.zuora.com | https://rest.test.ap.zuora.com/oauth/token | 

To find your environment, compare the address of the Zuora user interface with the environments listed in [Base URL](https://developer.zuora.com/v1-api-reference/introduction/) in the Zuora API reference.