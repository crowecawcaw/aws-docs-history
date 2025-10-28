Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Use Python with Managed Service for Apache Flink

###### Note

If you are developing Python Flink application on a new Mac with Apple Silicon chip, you may encounter some [known issues](https://issues.apache.org/jira/browse/FLINK-26981 "https://issues.apache.org/jira/browse/FLINK-26981") with Python dependencies of PyFlink 1.15.
In this case we recommend running the Python interpreter in Docker. For step-by-step instructions, see [PyFlink 1.15 development on Apple Silicon Mac](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/LocalDevelopmentOnAppleSilicon "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/LocalDevelopmentOnAppleSilicon").

Apache Flink version 1.20 includes support for creating applications using Python version
3.11. For more information, see [Flink
Python Docs](https://nightlies.apache.org/flink/flink-docs-release-1.20/api/python/ "https://nightlies.apache.org/flink/flink-docs-release-1.20/api/python/"). You create a Managed Service for Apache Flink application using Python by doing the
following:

- Create your Python application code as a text file with a `main` method.
- Bundle your application code file and any Python or Java dependencies into a zip file, and
  upload it to an Amazon S3 bucket.
- Create your Managed Service for Apache Flink application, specifying your Amazon S3 code location, application properties,
  and application settings.
  At a high level, the Python Table API is a wrapper around the Java Table API. For information about the Python Table API, see the
  [Table API Tutorial](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/table_api_tutorial/ "https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/python/table_api_tutorial/") in the Apache Flink Documentation.
