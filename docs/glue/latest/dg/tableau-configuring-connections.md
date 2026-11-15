

# Configuring Tableau connections
<a name="tableau-configuring-connections"></a>

Tableau connections authenticate with a credentials token returned by the Tableau REST API sign-in operation. You store the token in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Tableau connection:

1. Sign in to the Tableau REST API to obtain a credentials token. Also obtain your `INSTANCE_HOST` and `SITE_ID` values (see the Tableau API documentation on the Tableau website).

1. In Secrets Manager, create a secret with the key `session_token`, and set its value to the credentials token returned by the sign-in operation. If the token expires, sign in again and update the secret.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Tableau as the data source.

1. For connection properties, enter your `INSTANCE_HOST` and `SITE_ID` values in the corresponding required fields.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.