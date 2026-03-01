# Use Apache Spark in Amazon Athena

Amazon Athena makes it easy to interactively run data analytics and exploration using Apache Spark
without the need to plan for, configure, or manage resources. Running Apache Spark applications on Athena means
submitting Spark code for processing and receiving the results directly without the need for additional configuration.
Apache Spark on Amazon Athena is serverless and provides automatic, on-demand scaling that delivers instant-on compute
to meet changing data volumes and processing requirements.

In release version [PySpark engine version 3](notebooks-spark-release-versions.md#notebooks-spark-release-versions-pyspark-3 "notebooks-spark-release-versions.md#notebooks-spark-release-versions-pyspark-3"), you can use the simplified notebook experience in Amazon Athena console to develop Apache Spark applications
using Python or Athena notebook APIs.

In release version [Apache Spark version 3.5](notebooks-spark-release-versions.md#notebooks-spark-release-versions-spark-35 "notebooks-spark-release-versions.md#notebooks-spark-release-versions-spark-35"), you can run Spark code from Amazon SageMaker Unified Studio notebooks or your preferred Spark Connect compatible clients.

Amazon Athena offers the following features:

- Console usage – Submit your Spark
  applications from the Amazon Athena console (Pyspark enginer version 3 only).
- Scripting – Quickly and interactively build
  and debug Apache Spark applications in Python.
- Dynamic scaling – Amazon Athena automatically
  determines the compute and memory resources needed to run a job and continuously
  scales those resources accordingly up to the maximums that you specify. This dynamic
  scaling reduces cost without affecting speed.
- Notebook experience – Use the Amazon SageMaker AI Unified Studio notebooks
  to create, edit, and run computations using a familiar interface. In Pyspark engine version 3, you can use
  Athena in-console notebooks that are compatible with Jupyter notebooks and contain a list of cells that are executed in order
  as calculations. Cell content can include code, text, Markdown, mathematics, plots and rich media.
  For additional information, see [Run Spark SQL on Amazon Athena
  Spark](https://aws.amazon.com/blogs/big-data/run-spark-sql-on-amazon-athena-spark/ "https://aws.amazon.com/blogs/big-data/run-spark-sql-on-amazon-athena-spark/") and [Explore your
  data lake using Amazon Athena for Apache Spark](https://aws.amazon.com/blogs/big-data/explore-your-data-lake-using-amazon-athena-for-apache-spark/ "https://aws.amazon.com/blogs/big-data/explore-your-data-lake-using-amazon-athena-for-apache-spark/") in the _AWS Big Data
  Blog_.

###### Topics

- [Release versions](notebooks-spark-release-versions.md "notebooks-spark-release-versions.md")
- [Considerations and limitations](notebooks-spark-considerations-and-limitations.md "notebooks-spark-considerations-and-limitations.md")
- [Get started](notebooks-spark-getting-started.md "notebooks-spark-getting-started.md")
- [Manage notebook files](notebooks-spark-managing.md "notebooks-spark-managing.md")
- [Notebook editor](notebooks-spark-editor.md "notebooks-spark-editor.md")
- [Non-Hive table formats](notebooks-spark-table-formats.md "notebooks-spark-table-formats.md")
- [Python library support](notebooks-spark-python-library-support.md "notebooks-spark-python-library-support.md")
- [Specify custom configuration](notebooks-spark-custom-jar-cfg.md "notebooks-spark-custom-jar-cfg.md")
- [Supported data and storage formats](notebooks-spark-data-and-storage-formats.md "notebooks-spark-data-and-storage-formats.md")
- [Monitor Apache Spark](notebooks-spark-metrics.md "notebooks-spark-metrics.md")
- [Cost attribution](notebooks-spark-cost-attribution.md "notebooks-spark-cost-attribution.md")
- [Logging and monitoring](notebooks-spark-logging-monitoring.md "notebooks-spark-logging-monitoring.md")
- [Spark UI access](notebooks-spark-ui-access.md "notebooks-spark-ui-access.md")
- [Spark Connect](notebooks-spark-connect.md "notebooks-spark-connect.md")
- [Enable requester pays buckets](notebooks-spark-requester-pays.md "notebooks-spark-requester-pays.md")
- [Lake Formation integration](notebooks-spark-lakeformation.md "notebooks-spark-lakeformation.md")
- [Enable Spark encryption](notebooks-spark-encryption.md "notebooks-spark-encryption.md")
- [Cross-account catalog access](spark-notebooks-cross-account-glue.md "spark-notebooks-cross-account-glue.md")
- [Service quotas](notebooks-spark-quotas.md "notebooks-spark-quotas.md")
- [Athena Spark APIs](notebooks-spark-api-list.md "notebooks-spark-api-list.md")
- [Troubleshoot](notebooks-spark-troubleshooting.md "notebooks-spark-troubleshooting.md")
