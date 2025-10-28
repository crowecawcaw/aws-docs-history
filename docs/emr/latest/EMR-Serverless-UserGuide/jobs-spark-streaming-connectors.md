# Supported streaming connectors

Streaming connectors facilitate reading data from a streaming source and can also write data to a streaming sink.

The following are the supported streaming connectors:

**Amazon Kinesis Data Streams connector**

The [Amazon Kinesis Data Streams connector](../ReleaseGuide/emr-spark-structured-streaming-kinesis.md "../ReleaseGuide/emr-spark-structured-streaming-kinesis.md") for Apache Spark enables building streaming applications and pipelines
that consume data from and write data to Amazon Kinesis Data Streams. The connector supports enhanced fan-out consumption with a dedicated read throughput rate
of up to 2MB/second per shard. By default, Amazon EMR Serverless 7.1.0 and higher includes the connector, so you don't need to build
or download any additional packages. For more information about the connector, refer to the [spark-sql-kinesis-connector page on GitHub](https://github.com/awslabs/spark-sql-kinesis-connector/ "https://github.com/awslabs/spark-sql-kinesis-connector/").

The following is an example of how to start a job run with the Kinesis Data Streams connector dependency.

```
aws emr-serverless start-job-run \
--application-id `<APPLICATION_ID>` \
--execution-role-arn `<JOB_EXECUTION_ROLE>` \
--mode 'STREAMING' \
--job-driver '{
    "sparkSubmit": {
        "entryPoint": "s3://`<Kinesis-streaming-script>`",
        "entryPointArguments": ["s3://`<DOC-EXAMPLE-BUCKET-OUTPUT>`/output"],
        "sparkSubmitParameters": "--conf spark.executor.cores=4
                --conf spark.executor.memory=16g
                --conf spark.driver.cores=4
                --conf spark.driver.memory=16g
                --conf spark.executor.instances=3
                --jars /usr/share/aws/kinesis/spark-sql-kinesis/lib/spark-streaming-sql-kinesis-connector.jar"
    }
}'
```

To connect to Kinesis Data Streams, configure the EMR Serverless application with VPC access and use a VPC endpoint to allow private access.
or use a NAT Gateway to get public access. For more information, refer to [Configuring VPC access](vpc-access.md "vpc-access.md").
You must also make sure that your job runtime role has the necessary read and write permissions to access the required data streams. To learn more about how to configure a job runtime role,
refer to [Job runtime roles for Amazon EMR Serverless](security-iam-runtime-role.md "security-iam-runtime-role.md"). For a full list of all of the
required permissions, refer to the [spark-sql-kinesis-connector page on GitHub](https://github.com/awslabs/spark-sql-kinesis-connector/?tab=readme-ov-file#how-to-use-it "https://github.com/awslabs/spark-sql-kinesis-connector/?tab=readme-ov-file#how-to-use-it").

**Apache Kafka connector**

The Apache Kafka connector for Spark structured streaming is an open-source connector from the Spark community and is available in a Maven repository. This connector
facilitates Spark structured streaming applications to read data from and write data to self-managed Apache Kafka and Amazon Managed Streaming for Apache Kafka. For more information about the
connector, refer to the [Structured Streaming + Kafka Integration Guide](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html "https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html") in the Apache Spark documentation.

The following example demonstrates how to include the Kafka connector in your job run request.

```
aws emr-serverless start-job-run \
--application-id `<APPLICATION_ID>` \
--execution-role-arn `<JOB_EXECUTION_ROLE>` \
--mode 'STREAMING' \
--job-driver '{
    "sparkSubmit": {
        "entryPoint": "s3://`<Kafka-streaming-script>`",
        "entryPointArguments": ["s3://`<DOC-EXAMPLE-BUCKET-OUTPUT>`/output"],
        "sparkSubmitParameters": "--conf spark.executor.cores=4
                --conf spark.executor.memory=16g
                --conf spark.driver.cores=4
                --conf spark.driver.memory=16g
                --conf spark.executor.instances=3
                --packages org.apache.spark:spark-sql-kafka-0-10_2.12:`<KAFKA_CONNECTOR_VERSION>`"
    }
}'
```

The Apache Kafka connector version depends on your EMR Serverless release version and corresponding Spark version. To find the correct Kafka version, see the
refer to the [Structured Streaming + Kafka Integration Guide](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html "https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html").

To use Amazon Managed Streaming for Apache Kafka with IAM authentication, include another dependency to enable the Kafka connector to connect to Amazon MSK with IAM. For more information,
refer to the [aws-msk-iam-auth repository on GitHub](https://github.com/aws/aws-msk-iam-auth "https://github.com/aws/aws-msk-iam-auth"). You must also make sure that the job runtime role
has the necessary IAM permissions. The following example demonstrates how to use the connector with IAM authentication.

```
aws emr-serverless start-job-run \
--application-id `<APPLICATION_ID>` \
--execution-role-arn `<JOB_EXECUTION_ROLE>` \
--mode 'STREAMING' \
--job-driver '{
    "sparkSubmit": {
        "entryPoint": "s3://`<Kafka-streaming-script>`",
        "entryPointArguments": ["s3://`<DOC-EXAMPLE-BUCKET-OUTPUT>`/output"],
        "sparkSubmitParameters": "--conf spark.executor.cores=4
                --conf spark.executor.memory=16g
                --conf spark.driver.cores=4
                --conf spark.driver.memory=16g
                --conf spark.executor.instances=3
                --packages org.apache.spark:spark-sql-kafka-0-10_2.12:`<KAFKA_CONNECTOR_VERSION>`,software.amazon.msk:aws-msk-iam-auth:`<MSK_IAM_LIB_VERSION>`"
    }
}'
```

To use the Kafka connector and the IAM authentication library from Amazon MSK configure the EMR Serverless application with VPC access. Your subnets
must have Internet access and use a NAT Gateway to access the
the Maven dependencies. For more information, refer to [Configuring VPC access](vpc-access.md "vpc-access.md"). The subnets
must have network connectivity to access the Kafka cluster. This is true regardless of whether your Kafka cluster is self-managed or if you use
Amazon Managed Streaming for Apache Kafka.
