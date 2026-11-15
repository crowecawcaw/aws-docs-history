

# Configuring Amplitude Experiment connections
<a name="amplitude-experiment-configuring-connections"></a>

Amplitude Experiment connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure an Amplitude Experiment connection:

1. Create a Management API key in the Amplitude app under the Experiment sidebar → Management API. It is distinct from deployment keys used to fetch flag variants.

1. In Secrets Manager, create a secret containing the key `management_api_key` set to your Amplitude Experiment credential.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Amplitude Experiment as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.