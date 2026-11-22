

# Configuring Maxio connections

Maxio connections use basic authentication. You store your Maxio credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Maxio connection:

1. Obtain your Maxio API key (see the Maxio API documentation on the Maxio website).

1. In Secrets Manager, create a secret with `USERNAME` set to your API key and `PASSWORD` set to a nonempty value, such as `x`.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Maxio as the data source.

1. For connection properties, enter your site subdomain in the required `SUBDOMAIN` field.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.