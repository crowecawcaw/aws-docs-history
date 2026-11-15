

# Configuring Avalara connections
<a name="avalara-configuring-connections"></a>

Avalara connections use HTTP Basic authentication with your AvaTax account ID and license key, or with an AvaTax username and password. You store the Base64-encoded credential in an Secrets Manager secret, and the connector adds the `Basic` scheme when it calls AvaTax.

To configure an Avalara connection:

1. Obtain your AvaTax account ID and license key, or an AvaTax username and password. For instructions on authenticating with AvaTax, see [Authentication in AvaTax REST v2](https://developer.avalara.com/avatax/authentication-in-rest/) on the Avalara developer website.

1. In Secrets Manager, create a secret with the key `api_key`. Set its value to the Base64 encoding of `{{accountId}}:{{licenseKey}}` or `{{username}}:{{password}}`. Don't include the `Basic` prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Avalara as the data source.

1. For the URL connection property, choose `https://rest.avatax.com` for production (the default) or `https://sandbox-rest.avatax.com` for sandbox. Use a credential from the same environment.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.