

# Configuring Weaviate connections

Weaviate connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure a Weaviate connection:

1. In the Weaviate Cloud console, select your cluster. In **API Keys**, choose **New key** and create a key with a role that can read your collections, such as `viewer`. Copy the key, because it is shown only once. Also copy the cluster **REST Endpoint**. For more information, see [Connect to Weaviate Cloud](https://docs.weaviate.io/cloud/manage-clusters/connect) on the Weaviate website.

1. In Secrets Manager, create a secret with the key `api_key`. Set the value to the raw API key without the `Bearer` prefix. The connector adds the prefix.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Weaviate as the data source.

1. For the `SUBDOMAIN` connection property, enter the part of the REST endpoint host before `.weaviate.cloud`. For example, for `https://abc123.c0.us-west3.gcp.weaviate.cloud`, enter `abc123.c0.us-west3.gcp`.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.