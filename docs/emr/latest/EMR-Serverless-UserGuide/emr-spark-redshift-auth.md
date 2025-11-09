# Authenticating with the

Amazon Redshift integration for Apache Spark

## Use AWS Secrets Manager to retrieve

credentials and connect to Amazon Redshift

You can securely authenticate to Amazon Redshift by storing the credentials in Secrets Manager
and have the Spark job call the `GetSecretValue` API to fetch
it:

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

## Authenticate to Amazon Redshift with a JDBC

driver

**Set username and password inside the JDBC
URL**

You can authenticate a Spark job to an Amazon Redshift cluster by specifying the Amazon Redshift
database name and password in the JDBC URL.

###### Note

If you pass the database credentials in the URL, anyone who has access to
the URL can also access the credentials. This method isn't generally
recommended because it's not a secure option.

If security isn't a concern for your application, use the following
format to set the username and password in the JDBC URL:

```
jdbc:redshift://redshifthost:5439/database?user=`username`&password=`password`
```

## Use IAM based authentication with

Amazon EMR Serverless job execution role

Starting with Amazon EMR Serverless release 6.9.0, the Amazon Redshift JDBC driver 2.1
or higher is packaged into the environment. With JDBC driver 2.1 and higher, you
can specify the JDBC URL and not include the raw username and password.

Instead, specify `jdbc:redshift:iam://` scheme. This
commands the JDBC driver to use your EMR Serverless job execution role to fetch
the credentials automatically. Refer to [Configure a JDBC or ODBC connection to use IAM credentials](../../../redshift/latest/mgmt/generating-iam-credentials-configure-jdbc-odbc.md "../../../redshift/latest/mgmt/generating-iam-credentials-configure-jdbc-odbc.md") in the
_Amazon Redshift Management Guide_ for more information. An example of
this URL is:

```
jdbc:redshift:iam://`examplecluster.abc123xyz789`.`us-west-2`.redshift.amazonaws.com:5439/dev
```

The following permissions are required for your job execution role when the
provided conditions are met:

| Permission                           | Conditions when required for job execution role                                                                              |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `redshift:GetClusterCredentials`     | Required for JDBC driver to fetch the credentials from<br>Amazon Redshift                                                    |
| `redshift:DescribeCluster`           | Required if you specify the Amazon Redshift cluster and AWS Region<br>in the JDBC URL instead of endpoint                    |
| `redshift-serverless:GetCredentials` | Required for JDBC driver to fetch the credentials from<br>Amazon Redshift Serverless                                         |
| `redshift-serverless:GetWorkgroup`   | Required if you are using Amazon Redshift Serverless and you are<br>specifying the URL in terms of workgroup name and Region |

## Connecting to Amazon Redshift within a

different VPC

When you set up a provisioned Amazon Redshift cluster or Amazon Redshift Serverless workgroup under
a VPC, configure VPC connectivity for your Amazon EMR Serverless
application to access to the resources. For more information on how to configure
VPC connectivity on an EMR Serverless application, refer to [Configuring VPC access for EMR Serverless applications to connect to data](vpc-access.md "vpc-access.md").

- If your provisioned Amazon Redshift cluster or Amazon Redshift Serverless workgroup is
  publicly accessible, specify one or more private subnets that
  have a NAT gateway attached when you create EMR Serverless
  applications.
- If your provisioned Amazon Redshift cluster or Amazon Redshift Serverless workgroup isn't
  publicly accessible, you must create an Amazon Redshift managed VPC endpoint for
  your Amazon Redshift cluster as described in [Configuring VPC access for EMR Serverless applications to connect to data](vpc-access.md "vpc-access.md"). Alternatively, you can create your Amazon Redshift
  Serverless workgroup as described in [Connecting to
  Amazon Redshift Serverless](../../../redshift/latest/mgmt/serverless-connecting.md "../../../redshift/latest/mgmt/serverless-connecting.md") in the
  _Amazon Redshift Management Guide_. You must associate your
  cluster or your subgroup to the private subnets that you specify when
  you create your EMR Serverless application.

###### Note

If you use IAM based authentication, and your private subnets for the
EMR Serverless application don't have a NAT gateway attached, then you must
also create a VPC endpoint on those subnets for Amazon Redshift or Amazon Redshift Serverless.
This way, the JDBC driver can fetch the credentials.
