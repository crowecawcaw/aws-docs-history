

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Strategy Recommendations database analysis
<a name="database-analysis"></a>

Strategy Recommendations automatically identifies the database servers in your portfolio and creates application components for them. For example, if there is a SQL Server database in your portfolio, it's identified as application component **sqlservr.exe**.

Strategy Recommendations analyzes individual databases in the identified SQL Server application component, sqlservr.exe, using the AWS Schema Conversion Tool. Strategy Recommendations also identifies incompatibilities in migrating the databases to AWS databases such as Amazon Aurora MySQL-Compatible Edition, Amazon Aurora PostgreSQL-Compatible Edition, Amazon RDS for MySQL, and Amazon RDS for PostgreSQL.

Currently, Strategy Recommendations database analysis is only available for SQL Server.

To configure Strategy Recommendations to analyze your databases, you must provide credentials for the Strategy Recommendations application data collector to connect to your databases. To do this, create a secret in AWS Secrets Manager in your AWS account. 

For information about the permissions and privileges of the credentials that you provide, see [Privileges needed for AWS Schema Conversion Tool credentials](#schema-conversion-tool-privileges). For information about creating a secret with the credentials, see [Creating a secret in Secrets Manager for database credentials](#schema-conversion-tool-secret).

After you set up the credentials and secret, you can configure AWS Schema Conversion Tool analysis on the database server. For more information, see [Configure database analysis for an application component](recommendations-view-app-components.md#recommendations-database-config).

 After you configure database analysis for the application component, a AWS Schema Conversion Tool inventory task is scheduled. After this task completes, you'll see the new application components being created for every individual database on that database server. For example, if your SQL Server has two databases (exampledbs1 and exampledbs2), an application component is created for each of the databases with the names exampledbs1 and exampledbs2.

If you would like to see anti-patterns in migrating each identified database to AWS databases, set up analysis for each database following the steps in [Configure database analysis for an application component](recommendations-view-app-components.md#recommendations-database-config). 

## Privileges needed for AWS Schema Conversion Tool credentials
<a name="schema-conversion-tool-privileges"></a>

The sign-in credentials that you provide to AWS Secrets Manager only needs `VIEW SERVER STATE` and `VIEW ANY DEFINITION` privileges.

You can provide any login name and password that you want when creating the SQL Server login.

## Creating a secret in Secrets Manager for database credentials
<a name="schema-conversion-tool-secret"></a>

After the credentials are ready for the Strategy Recommendations application data collector to connect to a database, create a secret in AWS Secrets Manager in your AWS account as described in the following procedure. 

**To create a secret with AWS Secrets Manager in your AWS account**

1. Using the AWS account that you created in [Setting up Strategy Recommendations](setting-up.md), sign in to the AWS Management Console and open the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. Select the secret type as **Other type of secrets**.

1. Under **Key/value pairs**, enter the following information.

   username - {{your-username}}

   Then choose **\+ Add row** and enter following information.

   password - {{your-password}}

1. Choose **Next**.

1. Enter **Secret name** as any string with the prefix **migrationhub-strategy-**. For example, **migrationhub-strategy-one**.
**Note**  
Store your secret name in a safe place for later use.

1. Choose **Next**, and then choose **Next** again.

1. Choose **Store**.

You can use the secret you created for database credentials when setting up database analysis in Strategy Recommendations.