# Considerations and limitations

when using the Spark connector

The Spark connector supports a variety of ways to manage credentials, to configure security, and to connect with other AWS services. Get familiar with the recommendations in this
list in order to configure a functional and resilient connection.

- We recommend that you activate SSL for the JDBC connection from Spark on
  Amazon EMR to Amazon Redshift.
- We recommend that you manage the credentials for the Amazon Redshift cluster in
  AWS Secrets Manager as a best practice. See [Using AWS Secrets Manager to
  retrieve credentials for connecting to Amazon Redshift](../ReleaseGuide/emr-spark-redshift-secrets.md "../ReleaseGuide/emr-spark-redshift-secrets.md") for an
  example.
- We recommend that you pass an IAM role with the parameter
  `aws_iam_role` for the Amazon Redshift authentication parameter.
- The parameter `tempformat` currently doesn't support the
  Parquet format.
- The `tempdir` URI points to an Amazon S3 location. This temp
  directory isn't cleaned up automatically and therefore could add additional
  cost.
- Consider the following recommendations for Amazon Redshift:
  - We recommend that you block public access to the Amazon Redshift
    cluster.
  - We recommend that you turn on [Amazon Redshift audit
    logging](../../../redshift/latest/mgmt/db-auditing.md "../../../redshift/latest/mgmt/db-auditing.md").
  - We recommend turn on [Amazon Redshift at-rest encryption](../../../redshift/latest/mgmt/security-server-side-encryption.md "../../../redshift/latest/mgmt/security-server-side-encryption.md").

- Consider the following recommendations for Amazon S3:

      + We recommend [blocking public access to Amazon S3 buckets](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md").
      + We recommend that you use [Amazon S3
       server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") to encrypt the S3 buckets that
       you use.
      + We recommend that you use [Amazon S3
       lifecycle policies](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to define the retention rules for the
       S3 bucket.
      + Amazon EMR always verifies code imported from open-source into the
       image. For security, we don't support encoding AWS access
       keys in the `tempdir` URI as an authentication method
       from Spark to Amazon S3.

  For more information on using the connector and its supported parameters, see the
  following resources:

- [Amazon Redshift integration for Apache Spark](../../../redshift/latest/mgmt/spark-redshift-connector.md "../../../redshift/latest/mgmt/spark-redshift-connector.md") in the
  _Amazon Redshift Management Guide_
- The [`spark-redshift` community repository](https://github.com/spark-redshift-community/spark-redshift#readme "https://github.com/spark-redshift-community/spark-redshift#readme") on
  Github
