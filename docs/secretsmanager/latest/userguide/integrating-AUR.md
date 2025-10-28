# How Amazon Aurora uses AWS Secrets Manager

Amazon Aurora is a fully managed relational database engine that's compatible with MySQL and
PostgreSQL.

To manage master user credentials for Aurora, Aurora can create a [managed secret](service-linked-secrets.md "service-linked-secrets.md") for you. You are charged for that
secret. Aurora also [manages rotation](rotate-secrets_managed.md "rotate-secrets_managed.md") for these
credentials. For more information, see [Password management with
Amazon Aurora and AWS Secrets Manager](../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md") in the _Amazon Aurora User Guide_.

For other Aurora credentials, see [Create an AWS Secrets Manager secret](create_secret.md "create_secret.md").

When you call the Amazon RDS Data API, you can pass credentials for the database by using a
secret in Secrets Manager. For more information, see [Using the Data API for Aurora
Serverless](../../../AmazonRDS/latest/AuroraUserGuide/data-api.md "../../../AmazonRDS/latest/AuroraUserGuide/data-api.md") in the _Amazon Aurora User Guide_.

When you use the Amazon RDS query editor to connect to a database, you can store credentials
for the database in Secrets Manager. For more information, see [Using the query editor](../../../AmazonRDS/latest/AuroraUserGuide/query-editor.md "../../../AmazonRDS/latest/AuroraUserGuide/query-editor.md") in
the _Amazon RDS User Guide_.
