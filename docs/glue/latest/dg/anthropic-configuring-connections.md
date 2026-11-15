

# Configuring Anthropic connections
<a name="anthropic-configuring-connections"></a>

Anthropic connections authenticate with an API key (or token). You store the key in Secrets Manager and reference that secret when you create the connection in AWS Glue Studio.

To configure an Anthropic connection:

1. Two credential classes are used, in the `x-api-key` header. (1) An Admin API key (`sk-ant-admin01-…`), created in the Console by an organization admin (Settings → API keys), reaches the organization/admin and usage/cost entities. (2) A workspace-scoped API key (`sk-ant-…`), created inside a workspace, reaches the model, message-batch, and file entities. See "Known limitations" below—a single key cannot read both groups.

1. In Secrets Manager, create a secret containing the key `apiKey` set to your Anthropic credential. The connector sets the `anthropic-version` header automatically, so don't include it in the secret.

1. In the AWS Glue Studio console, choose **Connections** under **Data Catalog**, then choose **Create connection**.

1. Search for and choose Anthropic as the data source.

1. For credentials, choose the Secrets Manager secret you created, select the IAM role that AWS Glue can assume to read the secret, optionally set network options, and complete the connection creation.

1. Grant the IAM role associated with your AWS Glue job permission to read the secret.