# Tutorial: Integrate with Apache Spark to import or export data

Apache Spark is an open-source engine for large-scale data analytics. Apache Spark enables
you to perform analytics on data stored in Amazon Keyspaces more efficiently. You can also use Amazon Keyspaces to
provide applications with consistent, single-digit-millisecond read access to analytics data
from Spark. The open-source Spark Cassandra Connector simplifies reading and writing data
between Amazon Keyspaces and Spark.

Amazon Keyspaces support for the Spark Cassandra Connector streamlines running Cassandra workloads in
Spark-based analytics pipelines by using a fully managed and serverless database service.
With Amazon Keyspaces, you don’t need to worry about Spark competing for the same underlying
infrastructure resources as your tables. Amazon Keyspaces tables scale up and down automatically based
on your application traffic.

The following tutorial walks you through steps and best practices required to read and
write data to Amazon Keyspaces using the Spark Cassandra Connector. The tutorial demonstrates how to
migrate data to Amazon Keyspaces by loading data from a file with the Spark Cassandra Connector and
writing it to an Amazon Keyspaces table. Then, the tutorial shows how to read the data back from Amazon Keyspaces
using the Spark Cassandra Connector. You would do this to run Cassandra workloads in
Spark-based analytics pipelines.

###### Topics

- [Prerequisites for establishing
  connections to Amazon Keyspaces with the Spark Cassandra Connector](spark-tutorial-prerequisites.md "spark-tutorial-prerequisites.md")
- [Step 1: Configure Amazon Keyspaces for integration with the
  Apache Cassandra Spark Connector](spark-tutorial-step1.md "spark-tutorial-step1.md")
- [Step 2: Configure the Apache Cassandra Spark
  Connector](spark-tutorial-step2.md "spark-tutorial-step2.md")
- [Step 3: Create the application configuration
  file](spark-tutorial-step3.md "spark-tutorial-step3.md")
- [Step 4: Prepare the source data and the target
  table in Amazon Keyspaces](spark-tutorial-step4.md "spark-tutorial-step4.md")
- [Step 5: Write and read Amazon Keyspaces data using the
  Apache Cassandra Spark Connector](spark-tutorial-step5.md "spark-tutorial-step5.md")
- [Troubleshooting common errors when using the
  Spark Cassandra Connector with Amazon Keyspaces](spark-tutorial-step6.md "spark-tutorial-step6.md")
