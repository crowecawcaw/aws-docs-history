

# Authenticating with Amazon Redshift integration for Apache Spark
<a name="emr-spark-redshift-auth"></a>

## Using AWS Secrets Manager to retrieve credentials and connect to Amazon Redshift
<a name="emr-spark-redshift-secrets"></a>

The following code sample shows how you can use AWS Secrets Manager to retrieve credentials to connect to an Amazon Redshift cluster with the PySpark interface for Apache Spark in Python.

```
from pyspark.sql import SQLContext
import boto3

sc = # existing SparkContext
sql_context = SQLContext(sc)

secretsmanager_client = boto3.client('secretsmanager')
secret_manager_response = secretsmanager_client.get_secret_value(
    SecretId='string',
    VersionId='string',
    VersionStage='string'
)
username = # get username from secret_manager_response
password = # get password from secret_manager_response
url = "jdbc:redshift://redshifthost:5439/database?user=" + username + "&password=" + password

# Read data from a table
df = sql_context.read \
    .format("io.github.spark_redshift_community.spark.redshift") \
    .option("url", url) \
    .option("dbtable", "my_table") \
    .option("tempdir", "s3://path/for/temp/data") \
    .load()
```

## Using IAM to retrieve credentials and connect to Amazon Redshift
<a name="emr-spark-redshift-iam"></a>

You can use the Amazon Redshift-provided JDBC version 2 driver to connect to Amazon Redshift with the Spark connector. To use AWS Identity and Access Management (IAM), [configure your JDBC URL to use IAM authentication](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-iam-credentials-configure-jdbc-odbc.html). To connect to a Redshift cluster from Amazon EMR, you must give your IAM role permission to retrieve temporary IAM credentials. Assign the following permissions to your IAM role so that it can retrieve credentials and run Amazon S3 operations. 
+  [Redshift:GetClusterCredentials](https://docs.aws.amazon.com/redshift/latest/APIReference/API_GetClusterCredentials.html) (for provisioned Amazon Redshift clusters) 
+  [Redshift:DescribeClusters](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusters.html) (for provisioned Amazon Redshift clusters) 
+ [Redshift:GetWorkgroup](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetWorkgroup.html) (for Amazon Redshift Serverless workgroups)
+  [Redshift:GetCredentials](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetCredentials.html) (for Amazon Redshift Serverless workgroups) 
+  [s3:GetBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetBucket.html) 
+  [s3:GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html) 
+  [s3:GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) 
+  [s3:PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) 
+  [s3:GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html) 

For more information about `GetClusterCredentials`, see [Resource policies for `GetClusterCredentials`](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html#redshift-policy-resources.getclustercredentials-resources).

You also must make sure that Amazon Redshift can assume the IAM role during `COPY` and `UNLOAD` operations.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowSTSAssumerole",
      "Effect": "Allow",
      "Principal": {
        "Service": "redshift.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{123456789012}}"
        }
      }
    }
  ]
}
```

------

The following example uses IAM authentication between Spark and Amazon Redshift:

```
from pyspark.sql import SQLContext
import boto3

sc = # existing SparkContext
sql_context = SQLContext(sc)

url = "jdbc:redshift:iam://{{redshift-host}}:{{redshift-port}}/{{db-name}}"
iam_role_arn = "arn:aws:iam::{{account-id}}:role/{{role-name}}"

# Read data from a table
df = sql_context.read \
    .format("io.github.spark_redshift_community.spark.redshift") \
    .option("url", {{url}}) \
    .option("aws_iam_role", {{iam_role_arn}}) \
    .option("dbtable", "{{my_table}}") \
    .option("tempdir", "{{s3a://path/for/temp/data}}") \
    .mode("error") \
    .load()
```