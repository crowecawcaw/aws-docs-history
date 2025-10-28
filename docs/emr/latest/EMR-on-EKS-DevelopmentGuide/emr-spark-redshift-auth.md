# Authenticating with the

Amazon Redshift integration for Apache Spark

The following sections show authentication options with Amazon Redshift when you're integrating with Apache Spark. The sections show how to
retrieve login credentials and also details regarding using the JDBC driver with IAM authentication.

## Use AWS Secrets Manager to retrieve

credentials and connect to Amazon Redshift

You can store credentials in Secrets Manager to authenticate securely to Amazon Redshift. You
can have your Spark job call the `GetSecretValue` API to fetch the
credentials:

```

from pyspark.sql import SQLContextimport boto3

sc = # existing SparkContext
sql_context = SQLContext(sc)

secretsmanager_client = boto3.client('`secretsmanager`', region_name=os.getenv('`AWS_REGION`'))
secret_manager_response = secretsmanager_client.get_secret_value(
    SecretId='string',
    VersionId='string',
    VersionStage='string'
)
username = # get username from secret_manager_response
password = # get password from secret_manager_response
url = "jdbc:redshift://redshifthost:5439/database?user=" + `username` + "&password=" + `password`

# Access to Redshift cluster using Spark

```

## Use IAM based authentication with

Amazon EMR on EKS job execution role

Starting with Amazon EMR on EKS release 6.9.0, the Amazon Redshift JDBC driver version 2.1 or
higher is packaged into the environment. With JDBC driver 2.1 and higher, you
can specify the JDBC URL and not include the raw username and password. Instead,
you can specify `jdbc:redshift:iam://` scheme. This commands the JDBC
driver to use your Amazon EMR on EKS job execution role to fetch the credentials
automatically.

See [Configure a JDBC or ODBC connection to use IAM credentials](../../../redshift/latest/mgmt/generating-iam-credentials-configure-jdbc-odbc.md "../../../redshift/latest/mgmt/generating-iam-credentials-configure-jdbc-odbc.md") in the
_Amazon Redshift Management Guide_ for more information.

The following example URL uses a `jdbc:redshift:iam://`
scheme.

```
jdbc:redshift:iam://`examplecluster.abc123xyz789`.`us-west-2`.redshift.amazonaws.com:5439/dev
```

The following permissions are required for your job execution role when it
meets the provided conditions.

| Permission                           | Conditions when required for job execution role                                                                    |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `redshift:GetClusterCredentials`     | Required for JDBC driver to fetch the credentials from Amazon Redshift                                             |
| `redshift:DescribeCluster`           | Required if you specify the Amazon Redshift cluster and AWS Region in the JDBC URL instead of endpoint             |
| `redshift-serverless:GetCredentials` | Required for JDBC driver to fetch the credentials from Amazon Redshift Serverless                                  |
| `redshift-serverless:GetWorkgroup`   | Required if you are using Amazon Redshift Serverless and you specify the URL in terms of workgroup name and Region | Your job execution role policy should have the following permissions. ``{ "Effect": "Allow", "Action": [ "redshift:GetClusterCredentials", "redshift:DescribeCluster", "redshift-serverless:GetCredentials", "redshift-serverless:GetWorkgroup" ], "Resource": [ "arn:aws:redshift:`AWS_REGION`:`ACCOUNT_ID`:dbname:`CLUSTER_NAME`/`DATABASE_NAME`", "arn:aws:redshift:`AWS_REGION`:`ACCOUNT_ID`:dbuser:`DATABASE_NAME`/`USER_NAME`" ] }`` ## Authenticate to Amazon Redshift with a JDBC driver **Set username and password inside the JDBC URL** To authenticate a Spark job to an Amazon Redshift cluster, you can specify the Amazon Redshift database name and password in the JDBC URL. ###### Note If you pass the database credentials in the URL, anyone who has access to the URL can also access the credentials. This method isn't generally recommended because it's not a secure option. If security isn't a concern for your application, you can use the following format to set the username and password in the JDBC URL: `` jdbc:redshift://redshifthost:5439/database?user=`username`&password=`password` `` |
