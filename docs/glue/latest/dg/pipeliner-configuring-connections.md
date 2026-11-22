

# Configuring Pipeliner connections

Pipeliner connections use basic authentication. You store the credential in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Pipeliner connection:

1. Obtain your Pipeliner API credential (see the Pipeliner API documentation on the Pipeliner website).

1. In Secrets Manager, create a secret with the keys `USERNAME` and `PASSWORD`. Set their values to your Pipeliner credentials.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Pipeliner as the data source.

1. For connection properties, enter your `INSTANCE_HOST` and `SPACE_ID` values in the corresponding required fields.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.