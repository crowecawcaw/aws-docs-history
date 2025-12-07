# AWS Glue Spark and PySpark jobs

AWS Glue support Spark and PySpark jobs. A Spark job is run in an Apache Spark environment managed by AWS Glue. It processes data in batches. A streaming ETL job is similar to a Spark job, except that it performs ETL on data streams. It uses the Apache Spark Structured Streaming framework. Some Spark job features are not available to streaming ETL jobs.

The following sections provide information on AWS Glue Spark and PySpark jobs.

###### Topics

- [Configuring job properties for Spark jobs in AWS Glue](add-job.md "add-job.md")
- [Editing Spark scripts in the AWS Glue console](edit-script-spark.md "edit-script-spark.md")
- [Jobs (legacy)](console-edit-script.md "console-edit-script.md")
- [Tracking processed data using job bookmarks](monitor-continuations.md "monitor-continuations.md")
- [Storing Spark shuffle data](monitor-spark-shuffle-manager.md "monitor-spark-shuffle-manager.md")
- [Monitoring AWS Glue Spark jobs](monitor-spark.md "monitor-spark.md")
- [Generative AI troubleshooting for Apache Spark in AWS Glue](troubleshoot-spark.md "troubleshoot-spark.md")
- [Using materialized views with AWS Glue](materialized-views.md "materialized-views.md")
