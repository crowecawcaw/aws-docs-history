# Prevent Amazon S3 throttling

Throttling is the process of limiting the rate at which you use a service, an application,
or a system. In AWS, you can use throttling to prevent overuse of the Amazon S3 service and
increase the availability and responsiveness of Amazon S3 for all users. However, because
throttling limits the rate at which the data can be transferred to or from Amazon S3, it's
important to consider preventing your interactions from being throttled.

As pointed out in the [performance tuning](performance-tuning.md "performance-tuning.md") chapter, optimizations can
depend on your service level decisions, on how you structure your tables and data, and on
how you write your queries.

###### Topics

- [Reduce throttling at the service level](performance-tuning-s3-throttling-reduce-throttling-at-the-service-level.md "performance-tuning-s3-throttling-reduce-throttling-at-the-service-level.md")
- [Optimize your tables](performance-tuning-s3-throttling-optimizing-your-tables.md "performance-tuning-s3-throttling-optimizing-your-tables.md")
- [Optimize your queries](performance-tuning-s3-throttling-optimizing-queries.md "performance-tuning-s3-throttling-optimizing-queries.md")
