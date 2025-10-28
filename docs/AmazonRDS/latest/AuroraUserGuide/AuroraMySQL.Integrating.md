# Authorizing Amazon Aurora MySQL to

access other AWS services on your behalf

For your Aurora MySQL DB cluster to access other services on your behalf, create and
configure an AWS Identity and Access Management (IAM) role. This role authorizes database users in your DB
cluster to access other AWS services. For more information, see [Setting up IAM roles to
access AWS services](AuroraMySQL.Integrating.Authorizing.md "AuroraMySQL.Integrating.Authorizing.md").

You must also configure your Aurora DB cluster to allow outbound connections to the
target AWS service. For more information, see [Enabling network
communication from Amazon Aurora to other AWS services](AuroraMySQL.Integrating.Authorizing.md "AuroraMySQL.Integrating.Authorizing.md").

If you do so, your database users can perform these actions using other AWS
services:

- Synchronously or asynchronously invoke an AWS Lambda function using the native functions
  `lambda_sync` or `lambda_async`. Or, asynchronously invoke an AWS Lambda
  function using the `mysql.lambda_async` procedure. For more information, see [Invoking a Lambda function with an Aurora MySQL native function](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- Load data from text or XML files stored in an Amazon S3 bucket into your DB cluster
  by using the `LOAD DATA FROM S3` or `LOAD XML FROM S3`
  statement. For more information, see [Loading data into an Amazon Aurora MySQL DB cluster from
  text files in an Amazon S3 bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- Save data from your DB cluster into text files stored in an Amazon S3 bucket by
  using the `SELECT INTO OUTFILE S3` statement. For more information,
  see [Saving data from an Amazon Aurora MySQL DB cluster into text files in an Amazon S3
  bucket](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- Export log data to Amazon CloudWatch Logs MySQL. For more information, see [Publishing Amazon Aurora MySQL logs to Amazon CloudWatch Logs](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").
- Automatically add or remove Aurora Replicas with Application Auto Scaling. For more information,
  see [Amazon Aurora Auto Scaling with Aurora Replicas](Aurora.Integrating.md "Aurora.Integrating.md").

## Related

topics

- [Integrating Aurora with other AWS services](Aurora.md "Aurora.md")
- [Managing an Amazon Aurora DB cluster](CHAP_Aurora.md "CHAP_Aurora.md")
