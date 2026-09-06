

# How Amazon Redshift uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_RS"></a>

Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud.

To manage admin credentials for Amazon Redshift, Amazon Redshift can create a [managed secret](service-linked-secrets.md) for you. You are charged for that secret. Amazon Redshift also [manages rotation](rotate-secrets_managed.md) for these credentials. For more information, see [Managing Amazon Redshift admin passwords using AWS Secrets Manager](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-secrets-manager-integration.html) in the *Amazon Redshift Management Guide*.

For other Amazon Redshift credentials, see [Create an AWS Secrets Manager secret](create_secret.md). 

When you call the Amazon Redshift Data API, you can pass credentials for the cluster by using a secret in Secrets Manager. For more information, see [Using the Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html).

When you use the Amazon Redshift query editor to connect to a database, Amazon Redshift can store your credentials in a Secrets Manager secret with the prefix `redshiftqueryeditor`. You are charged for that secret. For more information, see [Querying a database using the query editor](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor.html) in the *Amazon Redshift Management Guide*.

For query editor v2, see [Amazon Redshift query editor v2](integrating_how-services-use-secrets_sqlworkbench.md).