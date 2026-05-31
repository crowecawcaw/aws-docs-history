# Monitoring Amazon DocumentDB

Monitoring your AWS services is an important part of keeping your systems
healthy and functioning optimally. It's wise to collect monitoring data from all parts of your
AWS solution so that you can more easily debug and fix failures or
degradations, should they occur. Before you begin monitoring your AWS
solutions, we recommend that you consider and formulate answers for the following
questions:

- What are your monitoring goals?
- What resources are you going to monitor?
- How frequently will you monitor these resources?
- What monitoring tools will you use?
- Who is responsible for doing the monitoring?
- Who is to be notified and by what means if something goes wrong?
  To understand your current performance patterns, identify performance anomalies, and
  formulate methods to address issues, you should establish baseline performance metrics for
  various times and under differing load conditions. As you monitor your AWS
  solution, we recommend that you store your historical monitoring data for future reference and
  for establishing your baselines.

In general, acceptable values for performance metrics depend on what your baseline looks
like and what your application is doing. Investigate consistent or trending variances from
your baseline. The following is advice about specific types of metrics:

- **High CPU or RAM use** — High values for CPU or
  RAM use might be appropriate, provided that they are in keeping with your goals for your
  application (like throughput or concurrency) and are expected.
- **Storage volume consumption** —Investigate
  storage consumption (`VolumeBytesUsed`) if space that is used is consistently
  at or above 85 percent of the total storage volume space. Determine whether you can
  delete data from the storage volume or archive data to a different system to free up
  space. For more information, see [Amazon DocumentDB storage](how-it-works.md#how-it-works.storage "how-it-works.md#how-it-works.storage") and [Amazon DocumentDB Quotas and limits](limits.md "limits.md").
- **Network traffic** — For network traffic, talk
  with your system administrator to understand what the expected throughput is for your
  domain network and internet connection. Investigate network traffic if throughput is
  consistently lower than expected.
- **Database connections** — Consider constraining
  database connections if you see high numbers of user connections in conjunction with
  decreases in instance performance and response time. The best number of user connections
  for your instance will vary based on your instance class and the complexity of the
  operations being performed.
- **IOPS metrics**—The expected values for IOPS
  metrics depend on disk specification and server configuration, so use your baseline to
  know what is typical. Investigate if values are consistently different from your
  baseline. For best IOPS performance, make sure that your typical working set fits into
  memory to minimize read and write operations.
  Amazon DocumentDB (with MongoDB compatibility) provides a variety of Amazon CloudWatch metrics that you can monitor to determine the
  health and performance of your Amazon DocumentDB clusters and instances. You can view Amazon DocumentDB metrics
  using various tools, including the Amazon DocumentDB console, AWS CLI, CloudWatch API, and Performance Insights.

###### Topics

- [Monitoring a cluster's status](monitoring_docdb-cluster_status.md "monitoring_docdb-cluster_status.md")
- [Monitoring an instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md")
- [Viewing Amazon DocumentDB recommendations](view-docdb-recommendations.md "view-docdb-recommendations.md")
- [Event subscriptions](event-subscriptions.md "event-subscriptions.md")
- [Monitoring Amazon DocumentDB with CloudWatch](cloud_watch.md "cloud_watch.md")
- [Logging Amazon DocumentDB API calls with CloudTrail](logging-with-cloudtrail.md "logging-with-cloudtrail.md")
- [Profiling operations](profiling.md "profiling.md")
- [Monitoring with Performance Insights](performance-insights.md "performance-insights.md")
