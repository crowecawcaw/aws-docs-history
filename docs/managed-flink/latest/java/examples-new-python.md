Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Python examples for Managed Service for Apache Flink

The following examples demonstrate how to create applications written in Python.

###### Note

Most of the examples are designed to run both locally, on your development machine
and your IDE of choice, and on Amazon Managed Service for Apache Flink. They demonstrate the simple mechanism that
you can use to pass application parameters, and how to set the dependency correctly
to run the application in both environments with no changes.

**Project dependencies**

Most PyFlink examples require one or more dependencies as JAR files, for example
for Flink connectors. These dependencies must then be packaged with the application
when deployed on Amazon Managed Service for Apache Flink.

The following examples already include the tooling that lets you run the application
locally for development and testing, and to package the required dependencies correctly.
This tooling requires using Java JDK11 and Apache Maven. Refer to the README contained
in each example for the specific instructions.

**Examples**

This example demonstrates the basic structure of a PyFlink application using
SQL embedded in Python code. This project also provides a skeleton for any
PyFlink application that includes JAR dependencies such as connectors. The
README section provides detailed guidance about how to run your Python
application locally for development. The example also shows how to include a
single JAR dependency, the Kinesis SQL connector in this example, in your PyFlink
application.

Code example: [GettingStarted](https://github.com/dzikosc/amazon-managed-service-for-apache-flink-examples/tree/main/python/GettingStarted "https://github.com/dzikosc/amazon-managed-service-for-apache-flink-examples/tree/main/python/GettingStarted")

This example shows how to add Python dependencies to your PyFlink application
in the most general way. This method works for simple dependencies, like Boto3,
or complex dependencies containing C libraries such as PyArrow.

Code example: [PythonDependencies](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/PythonDependencies "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/PythonDependencies")

This example demonstrates four types of the windowing aggregation in SQL
embedded in a Python application.

1. Sliding Window based on processing time
2. Sliding Window based on event time
3. Tumbling Window based on processing time
4. Tumbling Window based on event time
   Code example: [Windowing](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/Windowing "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/Windowing")

This example shows how to write your output to Amazon S3 as JSON files, using SQL
embedded in a Python application. You must enable checkpointing for the S3 sink
to write and rotate files to Amazon S3.

Code example: [S3Sink](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/S3Sink "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/S3Sink")

This example demonstrates how to define a User Defined Function, implement it
in Python, and use it in SQL code that runs in a Python application.

Code example: [UDF](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/UDF "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/UDF")

This example demonstrates how to send data to Amazon Data Firehose using SQL.

Code example: [FirehoseSink](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/FirehoseSink "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/FirehoseSink")
