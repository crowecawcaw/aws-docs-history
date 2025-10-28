# How Amazon Redshift uses AWS Secrets Manager

Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud.

To manage admin credentials for Amazon Redshift, Amazon Redshift can create a [managed secret](service-linked-secrets.md "service-linked-secrets.md") for you. You are charged for that
secret. Amazon Redshift also [manages rotation](rotate-secrets_managed.md "rotate-secrets_managed.md") for these
credentials. For more information, see [Managing Amazon Redshift admin
passwords using AWS Secrets Manager](../../../redshift/latest/mgmt/redshift-secrets-manager-integration.md "../../../redshift/latest/mgmt/redshift-secrets-manager-integration.md") in the _Amazon Redshift Management Guide_.

For other Amazon Redshift credentials, see [Create an AWS Secrets Manager secret](create_secret.md "create_secret.md").

When you call the Amazon Redshift Data API, you can pass credentials for the cluster by using a
secret in Secrets Manager. For more information, see [Using the Amazon Redshift Data API](../../../redshift/latest/mgmt/data-api.md "../../../redshift/latest/mgmt/data-api.md").

When you use the Amazon Redshift query editor to connect to a database, Amazon Redshift can store your
credentials in a Secrets Manager secret with the prefix `redshiftqueryeditor`. You are
charged for that secret. For more information, see [Querying a database using the query
editor](../../../redshift/latest/mgmt/query-editor.md "../../../redshift/latest/mgmt/query-editor.md") in the _Amazon Redshift Management Guide_.

For query editor v2, see [Amazon Redshift query editor
v2](integrating_how-services-use-secrets_sqlworkbench.md "integrating_how-services-use-secrets_sqlworkbench.md").
