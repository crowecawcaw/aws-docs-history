

# How Amazon Aurora uses AWS Secrets Manager
<a name="integrating-AUR"></a>

Amazon Aurora is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. 

To manage master user credentials for Aurora, Aurora can create a [managed secret](service-linked-secrets.md) for you. You are charged for that secret. Aurora also [manages rotation](rotate-secrets_managed.md) for these credentials. For more information, see [Password management with Amazon Aurora and AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide*. 

For other Aurora credentials, see [Create an AWS Secrets Manager secret](create_secret.md).

When you call the Amazon RDS Data API, you can pass credentials for the database by using a secret in Secrets Manager. For more information, see [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide*.

When you use the Amazon RDS query editor to connect to a database, you can store credentials for the database in Secrets Manager. For more information, see [Using the query editor](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/query-editor.html) in the *Amazon RDS User Guide*.