# Streaming jobs for processing continuously streamed data

A streaming job in EMR Serverless is a job mode that lets you analyze and process streaming data in near real-time. These long-running jobs
poll streaming data and continuously process results as data arrives. Streaming jobs are best suited for tasks that require real-time data processing, such as
near real-time analytics, fraud detection, and recommendations engines. EMR Serverless streaming jobs provide optimizations, such as built-in job resiliency, real-time monitoring, enhanced log management, and integration with streaming connectors.

The following are some use cases with streaming jobs:

- **Near real-time analytics** – streaming jobs in Amazon EMR Serverless let you process streaming data in near real-time, so you can perform real-time analytics on continuous
  data streams, such as log data, sensor data, or clickstream data to derive insights and make timely decisions based on the latest information.
- **Fraud detection** – use streaming jobs to run near real-time fraud detection in financial transactions, credit card operations, or online activities when you analyze data streams
  and identify suspicious patterns or anomalies as they occur.
- **Recommendation engines** – streaming jobs can process user-activity data and update recommendations models. Doing so opens up possibilities for personalized and real-time recommendations
  based on behaviors and preferences.
- **Social media analytics** – streaming jobs can process social media data, such as tweets, comments, and posts, so organizations can monitor trends, sentiment analysis, and manage brand
  reputation in near real-time.
- **Internet of Things (IoT) analytics** – streaming jobs can handle and analyze high-velocity streams of data from IoT devices, sensors, and connected machinery, so run
  anomaly detection, predictive maintenance, and other IoT analytics use cases.
- **Clickstream analysis** – streaming jobs can process and analyze clickstream data from websites or mobile applications. Businesses that use such data can run analytics
  to learn more about user behavior, personalize user experiences, and optimize marketing campaigns.
- **Log monitoring and analysis** – streaming jobs can also process log data from servers, applications, and network devices. This provides you with anomaly detection, troubleshooting, and
  system health and performance.
  **Key benefits**

Streaming jobs in EMR Serverless automatically provide _job-resiliency_, which is a combination of the following factors:

- **Auto-retry** – EMR Serverless automatically retries any jobs that failed without any manual input from you.
- **Availability Zone (AZ) resiliency** – EMR Serverless automatically switches streaming jobs to a healthy AZ if the original AZ experiences issues.
- **Log management:**

      + **Log rotation** – for more efficient disk storage management, EMR Serverless
       periodically rotates logs for long streaming jobs. Doing so prevents log accumulation that might consume all of the disk space.
      + **Log compaction** – helps you efficiently manage and optimize log files in
       managed-persistence. Compaction also improves the debug experience when you use the managed spark history server.

  **Supported data sources and data sinks**

EMR Serverless works with a number of input data sources and output data sinks:

- Supported input data sources – Amazon Kinesis Data Streams, Amazon Managed Streaming for Apache Kafka, and self-managed Apache Kafka clusters. By default, Amazon EMR releases 7.1.0 and higher
  include the [Amazon Kinesis Data Streams connector](../ReleaseGuide/emr-spark-structured-streaming-kinesis.md "../ReleaseGuide/emr-spark-structured-streaming-kinesis.md"),
  so you don't need to build or download any additional packages.
- Supported output data sinks – AWS Glue Data Catalog tables, Amazon S3, Amazon Redshift, MySQL, PostgreSQL Oracle, Oracle, Microsoft SQL, Apache Iceberg, Delta Lake, and Apache Hudi.

## Considerations and limitations

When you use streaming jobs, keep in mind the following considerations and limitations.

- Streaming jobs are supported with [Amazon EMR releases 7.1.0 and higher](../ReleaseGuide/emr-710-release.md "../ReleaseGuide/emr-710-release.md").
- EMR Serverless expects streaming jobs to run for a long time, so you can't set execution
  timeout to limit the runtime of the job.
- Streaming jobs are only compatible with the Spark engine, which is built on the [structured streaming framework](https://spark.apache.org/streaming/ "https://spark.apache.org/streaming/").
- EMR Serverless indefinitely retries streaming jobs, and you can't customize the number of maximum attempts. Thrash prevention is automatically included
  to stop the job retry if the amount of failed attempts has surpassed a threshold set over an hourly window. The default threshold
  is five failed attempts over one hour. You can configure this threshold to be between 1 and 10 attempts. For more information,
  refer to [Job resiliency](SECTION-jobs-resiliency.md "SECTION-jobs-resiliency.md").
- Streaming jobs have checkpoints to save runtime state and progress, so EMR Serverless can resume the streaming job
  from the latest checkpoint. For more information, refer to [Recovering from failures with Checkpointing](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing "https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#recovering-from-failures-with-checkpointing") in the Apache Spark documentation.
