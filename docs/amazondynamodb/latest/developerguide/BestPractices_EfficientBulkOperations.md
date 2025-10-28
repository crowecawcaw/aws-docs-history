# Efficient bulk operations

###### When to use this pattern

These patterns are useful to efficiently perform bulk updates on DynamoDB items.

- DynamoDB-shell is not a supported for production use case.
- `TransactWriteItems` – up to 100 individual updates with or without conditions, executing as an all or nothing ACID bundle

Trade-off – Additional throughput is consumed, 2 WCUs per 1 KB write.

- PartiQL `BatchExecuteStatement` – up to 25 updates with or without conditions

Trade-off – Additional logic is required to distribute requests in batches of 25.

- AWS Step Functions – rate-limited bulk operations for developers familiar with AWS Lambda.

Trade-off – Execution time is inversely proportional to rate-limit. Limited by the
maximum Lambda function timeout. The functionality entails that data changes that occur
between the read and the write may be overwritten. For more info, see [Backfilling an Amazon DynamoDB Time to Live attribute using Amazon EMR: Part
2](https://aws.amazon.com/blogs/database/part-2-backfilling-an-amazon-dynamodb-time-to-live-attribute-using-amazon-emr/ "https://aws.amazon.com/blogs/database/part-2-backfilling-an-amazon-dynamodb-time-to-live-attribute-using-amazon-emr/").

- AWS Glue and Amazon EMR – rate-limited bulk operation with managed parallelism. For
  applications or updates that are not time-sensitive, these options can run in the background
  only consuming a small percentage of throughput. Both services uses the emr-dynamodb-connector
  to perform DynamoDB operations. These services perform a big read followed by a big write of
  updated items with an option to rate-limit.

Trade-off – Execution time is inversely proportional to rate-limit. The
functionality includes that data changes occurring between the read and the write can be
overwritten. You can't read from Global Secondary Indexes (GSIs). See, [Backfilling an Amazon DynamoDB Time to Live attribute using Amazon EMR: Part 2](https://aws.amazon.com/blogs/database/part-2-backfilling-an-amazon-dynamodb-time-to-live-attribute-using-amazon-emr/ "https://aws.amazon.com/blogs/database/part-2-backfilling-an-amazon-dynamodb-time-to-live-attribute-using-amazon-emr/").

- DynamoDB Shell – rate-limited bulk operations using SQL-like queries. You can read
  from GSIs for better efficiency.

Trade-off – Execution time is inversely proportional to rate-limit. See [Rate limited bulk operations in DynamoDB Shell](https://aws.amazon.com/blogs/database/rate-limited-bulk-operations-in-dynamodb-shell/ "https://aws.amazon.com/blogs/database/rate-limited-bulk-operations-in-dynamodb-shell/").

## Using the pattern

Bulk updates can have significant cost implications especially if you use the on-demand throughput mode.
There’s a trade-off between speed and cost if you use the provisioned throughput mode. Setting the
rate-limit parameter very strictly can lead to a very large processing time. You can roughly
determine speed of the update using the average item size and the rate limit.

Alternatively, you can determine amount of throughput needed for the process based on the
expected duration of the update process and the average item size. The blog references shared
with each pattern provide details on the strategy, implementation and limitations of using the
pattern. For more information, see [Cost-effective bulk processing with Amazon DynamoDB](https://aws.amazon.com/blogs/database/cost-effective-bulk-processing-with-amazon-dynamodb/ "https://aws.amazon.com/blogs/database/cost-effective-bulk-processing-with-amazon-dynamodb/").

There are multiple approaches to perform bulk-updates against a live DynamoDB table.
The suitable approach depends on factors such as ACID and/or idempotency requirements, number
of items to be updated and familiarity with APIs. It is important to consider the cost versus
time trade-off, most approaches discussed above provide an option to rate-limit the throughput
used by the bulk update job.
