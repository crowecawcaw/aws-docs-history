

# How Amazon RDS uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_RDS"></a>

Amazon Relational Database Service (Amazon RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. 

To manage master user credentials for Amazon Relational Database Service (Amazon RDS), including Aurora, Amazon RDS can create a [managed secret](service-linked-secrets.md) for you. You are charged for that secret. Amazon RDS also [manages rotation](rotate-secrets_managed.md) for these credentials. For more information, see [Password management with Amazon RDS and AWS Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide*. 

For other Amazon RDS credentials, see [Create an AWS Secrets Manager secret](create_secret.md).

When you use the Amazon RDS query editor to connect to a database, you can store credentials for the database in Secrets Manager. For more information, see [Using the query editor](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/query-editor.html) in the *Amazon RDS User Guide*.