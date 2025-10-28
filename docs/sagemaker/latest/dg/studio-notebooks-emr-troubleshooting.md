# Troubleshooting

When working with Amazon EMR clusters from Studio or Studio Classic notebooks, you may
encounter various potential issues or challenges during the connection or usage process.
To help you troubleshoot and resolve these errors, this section provides guidance on
common problems that can arise.

The following are common errors that might occur while connecting or using Amazon EMR
clusters from Studio or Studio Classic notebooks.

## Troubleshoot Livy

connections hanging or failing

The following are Livy connectivity issues that might occur while using Amazon EMR
clusters from Studio or Studio Classic notebooks.

- Your Amazon EMR cluster encountered an out-of-memory
  error.

A possible reason for a Livy connection via `sparkmagic`
hanging or failing is if your Amazon EMR cluster encountered an out-of-memory
error.

By default, the Java configuration parameter of the Apache Spark driver,
`spark.driver.defaultJavaOptions`, is set to
`-XX:OnOutOfMemoryError='kill -9 %p'`. This means that the
default action taken when the driver program encounters an
`OutOfMemoryError` is to terminate the driver program by
sending a SIGKILL signal. When the Apache Spark driver is terminated, any
Livy connection via `sparkmagic` that depends on that driver
hangs or fails. This is because the Spark driver is responsible for managing
the Spark application's resources, including task scheduling and execution.
Without the driver, the Spark application cannot function, and any attempts
to interact with it fails.

If you suspect that your Spark cluster is experiencing memory issues, you
can check [Amazon EMR logs](../../../emr/latest/ManagementGuide/emr-manage-view-web-log-files.md "../../../emr/latest/ManagementGuide/emr-manage-view-web-log-files.md"). Containers killed due to out-of-memory errors
typically exit with a code of `137`. In such cases, you need to
restart the Spark application and establish a new Livy connection to resume
interaction with the Spark cluster.

You can refer to the knowledge base article [How do I resolve the error "Container killed by YARN for exceeding
memory limits" in Spark on Amazon EMR?](https://repost.aws/knowledge-center/emr-spark-yarn-memory-limit "https://repost.aws/knowledge-center/emr-spark-yarn-memory-limit") on AWS re:Post to learn about
various strategies and parameters that can be used to address an
out-of-memory issue.

We recommend reviewing the [Amazon EMR Best Practices
Guides](https://aws.github.io/aws-emr-best-practices/ "https://aws.github.io/aws-emr-best-practices/") for best practices and tuning guidance on running Apache
Spark workloads on your Amazon EMR clusters.

- Your Livy session times out when connecting to an
  Amazon EMR cluster for the first time.

When you initially connect to an Amazon EMR cluster using [sagemaker-studio-analytics-extension](https://pypi.org/project/sagemaker-studio-analytics-extension/ "https://pypi.org/project/sagemaker-studio-analytics-extension/"), which enables connection
to a remote Spark (Amazon EMR) cluster via the [SparkMagic](https://github.com/jupyter-incubator/sparkmagic "https://github.com/jupyter-incubator/sparkmagic")
library using [Apache Livy](https://livy.apache.org/ "https://livy.apache.org/"), you
may encounter a connection timeout error:

`An error was encountered: Session 0 did not start up in 60
 seconds.`

If your Amazon EMR cluster requires the initialization of a Spark application
upon establishing a connection, there is an increased chance of seeing
connection timeout errors.

To reduce the chances of getting timeouts when connecting to an Amazon EMR
cluster using Livy through the analytics extension,
`sagemaker-studio-analytics-extension` version
`0.0.19` and later override the default server session
timeout to `120` seconds instead of `sparkmagic`'s
default of `60` seconds.

We recommend upgrading your extension `0.0.18` and sooner by
running the following upgrade command.

```
pip install --upgrade sagemaker-studio-analytics-extension
```

Note that when providing a custom timeout configuration in
`sparkmagic`,
`sagemaker-studio-analytics-extension` honors this override.
However, setting the session timeout to `60` seconds
automatically triggers the default server session timeout of
`120` seconds in
`sagemaker-studio-analytics-extension`.
