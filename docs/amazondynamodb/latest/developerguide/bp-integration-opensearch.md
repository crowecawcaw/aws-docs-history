# Best practices for working with DynamoDB zero-ETL integration and OpenSearch Service

DynamoDB has a [DynamoDB zero-ETL integration with](OpenSearchIngestionForDynamoDB.md "OpenSearchIngestionForDynamoDB.md") Amazon OpenSearch Service. For more information, see the [DynamoDB plugin for
OpenSearch Ingestion](../../../opensearch-service/latest/developerguide/configure-client-ddb.md "../../../opensearch-service/latest/developerguide/configure-client-ddb.md") and [specific best practices for
Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/bp.md "../../../opensearch-service/latest/developerguide/bp.md").

## Configuration

- Only index data that you need to perform searches on. Always use a mapping template
  (`template_type: index_template` and `template_content`) and
  `include_keys` to implement this.
- Monitor your logs for errors that are related to type conflicts. OpenSearch Service expects all
  values for a given key to have the same type. It generates exceptions if there's a
  mismatch. If you encounter one of these errors, you can add a processor to catch that a
  given key is always be the same value.
- Generally use the `primary_key` metadata value for the
  `document_id` value. In OpenSearch Service, the document ID is the equivalent of the
  primary key in DynamoDB. Using the primary key will make it easy to find your document and
  ensure that updates are consistently replicated to it without conflicts.

You can use the helper function `getMetadata` to get your primary key
(for example, `document_id: "${getMetadata('primary_key')}"`). If you're
using a composite primary key, the helper function will concatenate them together for
you.

- In general, use the `opensearch_action` metadata value for the
  `action` setting. This will ensure that updates are replicated in such a
  way that the data in OpenSearch Service matches the latest state in DynamoDB.

You can use the helper function `getMetadata` to get your primary key
(for example, `action: "${getMetadata('opensearch_action')}"`). You can also
get the stream event type through `dynamodb_event_name` for use cases like
filtering. However, you should typically not use it for the `action`
setting.

## Observability

- Always use a dead-letter queue (DLQ) on your OpenSearch sinks to handle dropped
  events. DynamoDB is generally less structured than OpenSearch Service, and it's always possible for
  something unexpected to happen. With a dead-letter queue, you can recover individual
  events, and even automate the recovery process. This will help you to avoid needing to
  rebuild your entire index.
- Always set alerts that your replication delay doesn't go over an expected amount. It
  is typically safe to assume one minute without the alert being too noisy. This can vary
  depending on how spiky your write traffic is and your OpenSearch Compute Unit (OCU)
  settings on the pipeline.

If your replication delay goes over 24 hours, your stream will start to drop events,
and you'll have accuracy issues unless you do a full rebuild of your index from
scratch.

## Scaling

- Use auto scaling for pipelines to help scale up or down the OCUs to best fit the
  workload.
- For provisioned throughput tables without auto scaling, we recommend setting OCUs
  based on your write capacity units (WCUs) divided by 1000. Set the minimum to 1 OCU
  below that amount (but at least 1), and set the maximum to at least 1 OCU above that
  amount.
  - **Formula:**

  ```
  OCU_minimum = GREATEST((table_WCU / 1000) - 1, 1)
  OCU_maximum = (table_WCU / 1000) + 1
  ```

  - **Example:** Your table has 25000 WCUs provisioned.
    Your pipeline's OCUs should be set with a minimum of 24 (25000/1000 - 1) and maximum
    of at least 26 (25000/1000 + 1).

- For provisioned throughput tables with auto scaling, we recommend setting OCUs based
  on your minimum and maximum WCUs, divided by 1000. Set the minimum to 1 OCU below the
  minimum from DynamoDB, and set the maximum to at least 1 OCU above the maximum from
  DynamoDB.
  - **Formula:**

  ```
  OCU_minimum = GREATEST((table_minimum_WCU / 1000) - 1, 1)
  OCU_maximum = (table_maximum_WCU / 1000) + 1
  ```

  - **Example:** Your table has an auto scaling policy
    with a minimum of 8000 and maximum of 14000. Your pipeline's OCUs should be set with
    a minimum of 7 (8000/1000 - 1) and a maximum of 15 (14000/1000 + 1).

- For on-demand throughput tables, we recommend setting OCUs based on your typical
  peak and valley for write request units per second. You might need to average over a
  longer time period, depending on the aggregation that's available to you. Set the
  minimum to 1 OCU below the minimum from DynamoDB, and set the maximum to at least 1 OCU
  above the maximum from DynamoDB.
  - **Formula:**

  ```
  # Assuming we have writes aggregated at the minute level
  OCU_minimum = GREATEST((min(table_writes_1min) / (60 * 1000)) - 1, 1)
  OCU_maximum = (max(table_writes_1min) / (60 * 1000)) + 1
  ```

  - **Example:** Your table has an average valley of
    300 write request units per second and an average peak of 4300. Your pipeline's OCUs
    should be set with a minimum of 1 (300/1000 - 1, but at least 1) and a maximum of 5
    (4300/1000 + 1).

- Follow best practices on scaling your destination OpenSearch Service indexes. If your indexes are
  under-scaled, it will slow down ingestion from DynamoDB, and might cause delays.

###### Note

[`GREATEST`](../../../redshift/latest/dg/r_GREATEST_LEAST.md "../../../redshift/latest/dg/r_GREATEST_LEAST.md") is a SQL function that, given a set of arguments,
returns the argument with the greatest value.
