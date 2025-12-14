# Invoking a Lambda function from an Amazon Aurora MySQL DB

cluster

You can invoke an AWS Lambda function from an Amazon Aurora MySQL-Compatible Edition DB cluster with the native function
`lambda_sync` or `lambda_async`.
Before invoking a Lambda function from an Aurora MySQL, the Aurora DB cluster
must have access to Lambda. For details about granting access to Aurora MySQL, see
[Giving Aurora access to Lambda](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
For information about the `lambda_sync` and `lambda_async` stored functions, see
[Invoking a Lambda function with an Aurora MySQL native function](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").

You can also call an AWS Lambda function by using a stored procedure.
However, using a stored procedure is deprecated. We strongly recommend using an
Aurora MySQL native function if you are using one of the following Aurora MySQL versions:

- Aurora MySQL version 2, for MySQL 5.7-compatible clusters.
- Aurora MySQL version 3.01 and higher, for MySQL 8.0-compatible clusters. The stored procedure isn't available in Aurora MySQL
  version 3.
  For information about giving Aurora access to Lambda and invoking a Lambda function, see the following topics.

###### Topics

- [Giving Aurora access to Lambda](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md")
- [Invoking a Lambda function with an Aurora MySQL native function](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md")
- [Invoking a Lambda function with an Aurora MySQL stored procedure (deprecated)](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md")
