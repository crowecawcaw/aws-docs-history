# How Amazon RDS uses AWS Secrets Manager

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a
relational database in the AWS Cloud.

To manage master user credentials for Amazon Relational Database Service (Amazon RDS), including Aurora, Amazon RDS can create
a [managed secret](service-linked-secrets.md "service-linked-secrets.md") for you. You are charged for
that secret. Amazon RDS also [manages rotation](rotate-secrets_managed.md "rotate-secrets_managed.md") for
these credentials. For more information, see [Password management with Amazon RDS and
AWS Secrets Manager](../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md") in the _Amazon RDS User Guide_.

For other Amazon RDS credentials, see [Create an AWS Secrets Manager secret](create_secret.md "create_secret.md").

When you use the Amazon RDS query editor to connect to a database, you can store credentials
for the database in Secrets Manager. For more information, see [Using the query editor](../../../AmazonRDS/latest/AuroraUserGuide/query-editor.md "../../../AmazonRDS/latest/AuroraUserGuide/query-editor.md") in
the _Amazon RDS User Guide_.
