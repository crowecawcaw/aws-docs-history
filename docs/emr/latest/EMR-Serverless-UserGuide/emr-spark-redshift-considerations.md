# Considerations and limitations

when using the Spark connector

- We suggest that you turn on SSL for the JDBC connection from Spark on
  Amazon EMR to Amazon Redshift.
- We suggest that you manage the credentials for the Amazon Redshift cluster in
  AWS Secrets Manager as a best practice. Refer to [Using AWS Secrets Manager to
  retrieve credentials for connecting to Amazon Redshift](../../../redshift/latest/mgmt/redshift-secrets-manager-integration.md "../../../redshift/latest/mgmt/redshift-secrets-manager-integration.md") for an
  example.
- We suggest that you pass an IAM role with the parameter
  `aws_iam_role` for the Amazon Redshift authentication parameter.
- The parameter `tempformat` currently doesn't support the
  Parquet format.
- The `tempdir` URI points to an Amazon S3 location. This temp
  directory isn't cleaned up automatically and therefore could add additional
  cost.
- Consider the following recommendations for Amazon Redshift:
  - We suggest that you block public access to the Amazon Redshift
    cluster.
  - We suggest that you turn on [Amazon Redshift audit
    logging](../../../redshift/latest/mgmt/db-auditing.md "../../../redshift/latest/mgmt/db-auditing.md").
  - We suggest that you turn on [Amazon Redshift at-rest encryption](../../../redshift/latest/mgmt/security-server-side-encryption.md "../../../redshift/latest/mgmt/security-server-side-encryption.md").

- Consider the following recommendations for Amazon S3:

      + We suggest that you [block public access to Amazon S3 buckets](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md").
      + We suggest that you use [Amazon S3
       server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") to encrypt the Amazon S3 buckets
       used.
      + We suggest that you use [Amazon S3
       lifecycle policies](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to define the retention rules for the
       Amazon S3 bucket.
      + Amazon EMR always verifies code imported from open-source into the
       image. For security, we don't support the following
       authentication methods from Spark to Amazon S3:




      	- Setting AWS access keys in the `hadoop-env`
      	 configuration classification
      	- Encoding AWS access keys in the `tempdir`
      	 URI

  For more information on using the connector and its supported parameters, see the
  following resources:

- [Amazon Redshift integration for Apache Spark](../../../redshift/latest/mgmt/spark-redshift-connector.md "../../../redshift/latest/mgmt/spark-redshift-connector.md") in the
  _Amazon Redshift Management Guide_
- The [`spark-redshift` community repository](https://github.com/spark-redshift-community/spark-redshift#readme "https://github.com/spark-redshift-community/spark-redshift#readme") on
  Github
