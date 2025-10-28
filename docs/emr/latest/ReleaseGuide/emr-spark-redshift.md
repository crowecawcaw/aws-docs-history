# Using Amazon Redshift integration for Apache Spark with Amazon EMR

With Amazon EMR release 6.4.0 and later, every release image includes a connector between
[Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/") and Amazon Redshift. With this connector, you can use Spark on Amazon EMR to process
data stored in Amazon Redshift. For Amazon EMR releases 6.4.0 through 6.8.0, the integration is based on
the [`spark-redshift` open-source connector](https://github.com/spark-redshift-community/spark-redshift#readme "https://github.com/spark-redshift-community/spark-redshift#readme"). For Amazon EMR releases
6.9.0 and later, the [Amazon Redshift integration for Apache Spark](../../../redshift/latest/mgmt/spark-redshift-connector.md "../../../redshift/latest/mgmt/spark-redshift-connector.md")
has been migrated from the community version to a native integration.

###### Topics

- [Launching a Spark application using the Amazon Redshift integration for Apache Spark](emr-spark-redshift-launch.md "emr-spark-redshift-launch.md")
- [Authenticating with
  Amazon Redshift integration for Apache Spark](emr-spark-redshift-auth.md "emr-spark-redshift-auth.md")
- [Reading and writing from and to
  Amazon Redshift](emr-spark-redshift-readwrite.md "emr-spark-redshift-readwrite.md")
- [Considerations and limitations
  when using the Spark connector](emr-spark-redshift-considerations.md "emr-spark-redshift-considerations.md")
