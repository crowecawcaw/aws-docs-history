# Prerequisites for exporting data from Amazon Keyspaces to Amazon S3

###### Confirm the following prerequisites and create the Amazon Keyspaces resources before you begin with the tutorial

1. Before you start this tutorial, follow the AWS setup instructions in [Accessing Amazon Keyspaces (for Apache Cassandra)](accessing.md "accessing.md"). These steps include signing up for
   AWS and creating an AWS Identity and Access Management (IAM) principal with access to Amazon Keyspaces.
2. The scripts in this tutorial use your credentials and default AWS Region stored in a known
   location. For more information, see [Store access keys for programmatic access](aws.credentials.md "aws.credentials.md").

The following example shows how to store the required values as environment variables for the default user.

```
`$` `export AWS_ACCESS_KEY_ID=`AKIAIOSFODNN7EXAMPLE``
`$` `export AWS_SECRET_ACCESS_KEY=`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY``
`$` `export AWS_DEFAULT_REGION=`us-east-1``
```

3.  To run the scripts in this tutorial, you need the following software and tools installed on your machine:

        * [Java](https://openjdk.org/install/ "https://openjdk.org/install/")
        * [Apache Maven](https://maven.apache.org/install.html "https://maven.apache.org/install.html")
        * [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "https://git-scm.com/book/en/v2/Getting-Started-Installing-Git")
        * [AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")

    This tutorial was tested with AWS CLI 2, Java 17.0.13, and Apache Maven 3.8.7.

4.  You need an Amazon Keyspaces table with sample data to export later in this tutorial. You can use your
    own Amazon Keyspaces table or create a sample table following the steps in the [Getting started with Amazon Keyspaces (for Apache Cassandra)](getting-started.md "getting-started.md") tutorial.

        1. To install the `cqlsh-expansion`, follow the steps at [Using the cqlsh-expansion to connect
         to Amazon Keyspaces](programmatic.md#using_cqlsh "programmatic.md#using_cqlsh").
        2. Confirm that the `Murmur3Partitioner` partitioner is the default partitioner for your account. This partitioner
         is compatible with the Apache Spark Cassandra Connector and with AWS Glue. For more information on partitioners,
         see [Working with partitioners in Amazon Keyspaces](working-with-partitioners.md "working-with-partitioners.md").


        To change the partitioner of your account, you can use the following statement.



        ```
        SELECT partitioner FROM system.local;

        UPDATE system.local set partitioner='org.apache.cassandra.dht.Murmur3Partitioner' where key='local';
        ```
        3. To create an Amazon Keyspaces keyspace, follow the steps at
         [Create a keyspace in Amazon Keyspaces](getting-started.md "getting-started.md").
        4. To create the Amazon Keyspaces table, follow the steps at [Create a table in Amazon Keyspaces](getting-started.md "getting-started.md").
        5. To load sample data into the table to export to Amazon S3, follow the steps at [Inserting and loading data into
         an Amazon Keyspaces table](getting-started.dml.md "getting-started.dml.md").

    After completing the prerequisite steps, proceed to [Step 1: Create the Amazon S3 bucket, download the required tools, and configure the environment](S3-tutorial-step1.md "S3-tutorial-step1.md").
