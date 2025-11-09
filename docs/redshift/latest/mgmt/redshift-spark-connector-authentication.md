Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Authentication with the Spark

connector

The following diagram describes the authentication between Amazon S3, Amazon Redshift, the Spark
driver, and Spark executors.

![This is a diagram of the spark connector authentication.](images/spark-connector-authentication.png)

## Authentication between Redshift and

Spark

You can use the Amazon Redshift provided JDBC driver version 2.x driver to connect to
Amazon Redshift with the Spark connector by specifying sign-in credentials. To use IAM,
[configure your JDBC url to use IAM authentication](generating-iam-credentials-configure-jdbc-odbc.md "generating-iam-credentials-configure-jdbc-odbc.md"). To connect to a
Redshift cluster from Amazon EMR or AWS Glue, make sure that your IAM role has the
necessary permissions to retrieve temporary IAM credentials. The following list
describes all of the permissions that your IAM role needs to retrieve credentials
and run Amazon S3 operations.

- [Redshift:GetClusterCredentials](../APIReference/API_GetClusterCredentials.md "../APIReference/API_GetClusterCredentials.md") (for provisioned Redshift
  clusters)
- [Redshift:DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md") (for provisioned Redshift
  clusters)
- [Redshift:GetWorkgroup](../../../redshift-serverless/latest/APIReference/API_GetWorkgroup.md "../../../redshift-serverless/latest/APIReference/API_GetWorkgroup.md") (for Amazon Redshift Serverless workgroups)
- [Redshift:GetCredentials](../../../redshift-serverless/latest/APIReference/API_GetCredentials.md "../../../redshift-serverless/latest/APIReference/API_GetCredentials.md") (for Amazon Redshift Serverless workgroups)
- [s3:ListBucket](../../../AmazonS3/latest/API/API_ListBuckets.md "../../../AmazonS3/latest/API/API_ListBuckets.md")
- [s3:GetBucket](../../../AmazonS3/latest/API/API_control_GetBucket.md "../../../AmazonS3/latest/API/API_control_GetBucket.md")
- [s3:GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md")
- [s3:PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md")
- [s3:GetBucketLifecycleConfiguration](../../../AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.md "../../../AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.md")

For more information about GetClusterCredentials, see [Resource policies for GetClusterCredentials](redshift-iam-access-control-identity-based.md#redshift-policy-resources.getclustercredentials-resources "redshift-iam-access-control-identity-based.md#redshift-policy-resources.getclustercredentials-resources").

You also must make sure that Amazon Redshift can assume the IAM role during
`COPY` and `UNLOAD` operations.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

If you’re using the latest JDBC driver, the driver will automatically manage the
transition from an Amazon Redshift self-signed certificate to an ACM certificate. However,
you must [specify the SSL options to the JDBC url](jdbc20-configuration-options.md#jdbc20-ssl-option "jdbc20-configuration-options.md#jdbc20-ssl-option").

The following is an example of how to specify the JDBC driver URL and
`aws_iam_role` to connect to Amazon Redshift.

```
df.write \
  .format("io.github.spark_redshift_community.spark.redshift ") \
  .option("url", "jdbc:redshift:iam://<the-rest-of-the-connection-string>") \
  .option("dbtable", "<your-table-name>") \
  .option("tempdir", "s3a://<your-bucket>/<your-directory-path>") \
  .option("aws_iam_role", "<your-aws-role-arn>") \
  .mode("error") \
  .save()

```

## Authentication between Amazon S3 and

Spark

If you’re using an IAM role to authenticate between Spark and Amazon S3, use one of
the following methods:

- The AWS SDK for Java will automatically attempt to find AWS
  credentials by using the default credential provider chain implemented by
  the DefaultAWSCredentialsProviderChain class. For more information, see
  [Using the Default Credential Provider Chain](../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default "../../../sdk-for-java/v1/developer-guide/credentials.md#credentials-default").
- You can specify AWS keys via [Hadoop configuration properties](https://github.com/apache/hadoop/blob/trunk/hadoop-tools/hadoop-aws/src/site/markdown/tools/hadoop-aws/index.md "https://github.com/apache/hadoop/blob/trunk/hadoop-tools/hadoop-aws/src/site/markdown/tools/hadoop-aws/index.md"). For example, if your
  `tempdir` configuration points to a `s3n://`
  filesystem, set the `fs.s3n.awsAccessKeyId` and
  `fs.s3n.awsSecretAccessKey` properties in a Hadoop XML
  configuration file or call `sc.hadoopConfiguration.set()` to
  change Spark's global Hadoop configuration.

For example, if you are using the s3n filesystem, add:

```
sc.hadoopConfiguration.set("fs.s3n.awsAccessKeyId", "YOUR_KEY_ID")
sc.hadoopConfiguration.set("fs.s3n.awsSecretAccessKey", "YOUR_SECRET_ACCESS_KEY")
```

For the s3a filesystem, add:

```
sc.hadoopConfiguration.set("fs.s3a.access.key", "YOUR_KEY_ID")
sc.hadoopConfiguration.set("fs.s3a.secret.key", "YOUR_SECRET_ACCESS_KEY")
```

If you’re using Python, use the following operations:

```
sc._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", "YOUR_KEY_ID")
sc._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey", "YOUR_SECRET_ACCESS_KEY")
```

- Encode authentication keys in the `tempdir` URL. For example,
  the URI `s3n://ACCESSKEY:SECRETKEY@bucket/path/to/temp/dir`
  encodes the key pair (`ACCESSKEY`,
  `SECRETKEY`).

## Authentication between Redshift and

Amazon S3

If you’re using the COPY and UNLOAD commands in your query, you also must grant
Amazon S3 access to Amazon Redshift to run queries on your behalf. To do so, first [authorize Amazon Redshift
to access other AWS services](authorizing-redshift-service.md "authorizing-redshift-service.md"), then authorize the [COPY
and UNLOAD operations using IAM roles](copy-unload-iam-role.md "copy-unload-iam-role.md").

As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

## Integration with

AWS Secrets Manager

You can retrieve your Redshift username and password credentials from a stored
secret in AWS Secrets Manager. To automatically supply Redshift credentials, use the
`secret.id` parameter. For more information about how to create a
Redshift credentials secret, see [Create an
AWS Secrets Manager database secret](../../../secretsmanager/latest/userguide/create_database_secret.md "../../../secretsmanager/latest/userguide/create_database_secret.md").

| GroupID                      | ArtifactID              | Supported Revision(s) | Description                                                                                                                                                        |
| ---------------------------- | ----------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| com.amazonaws.secretsmanager | aws-secretsmanager-jdbc | 1.0.12                | The AWS Secrets Manager SQL Connection Library for Java lets<br>Java Developers to easily connect to SQL databases using secrets<br>stored in AWS Secrets Manager. |

###### Note

Acknowledgement: This documentation contains sample code and language developed
by the [Apache Software Foundation](http://www.apache.org/ "http://www.apache.org/")
licensed under the [Apache
2.0 license](https://www.apache.org/licenses/LICENSE-2.0 "https://www.apache.org/licenses/LICENSE-2.0").
