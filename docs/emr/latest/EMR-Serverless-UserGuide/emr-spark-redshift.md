# Using Amazon Redshift integration for Apache Spark on

Amazon EMR Serverless

With Amazon EMR release 6.9.0 and later, every release image includes a connector between
[Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/") and Amazon Redshift. With this connector, use Spark on
Amazon EMR Serverless to process data stored in Amazon Redshift. The integration is based on the
[`spark-redshift` open-source connector](https://github.com/spark-redshift-community/spark-redshift#readme "https://github.com/spark-redshift-community/spark-redshift#readme"). For
Amazon EMR Serverless, the [Amazon Redshift integration for Apache Spark](../../../redshift/latest/mgmt/spark-redshift-connector.md "../../../redshift/latest/mgmt/spark-redshift-connector.md") is
included as a native integration.

###### Topics

- [Launching a Spark application with the
  Amazon Redshift integration for Apache Spark](emr-spark-redshift-launch.md "emr-spark-redshift-launch.md")
- [Authenticating with the
  Amazon Redshift integration for Apache Spark](emr-spark-redshift-auth.md "emr-spark-redshift-auth.md")
- [Reading and writing from and to
  Amazon Redshift](emr-spark-redshift-readwrite.md "emr-spark-redshift-readwrite.md")
- [Considerations and limitations
  when using the Spark connector](emr-spark-redshift-considerations.md "emr-spark-redshift-considerations.md")
