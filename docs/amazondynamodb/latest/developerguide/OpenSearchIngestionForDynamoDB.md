# DynamoDB zero-ETL integration with Amazon OpenSearch Service

Amazon DynamoDB offers a zero-ETL integration with Amazon OpenSearch Service through the **DynamoDB plugin for OpenSearch Ingestion**. Amazon OpenSearch Ingestion offers a
fully managed, no-code experience for ingesting data into Amazon OpenSearch Service.

With the DynamoDB plugin for OpenSearch Ingestion, you can use one or more DynamoDB tables as a
source for ingestion to one or more OpenSearch Service indexes. You can browse and configure your
OpenSearch Ingestion pipelines with DynamoDB as a source from either OpenSearch Ingestion or
DynamoDB Integrations in the AWS Management Console.

- Get started with OpenSearch Ingestion by following along in the [OpenSearch Ingestion getting started guide](../../../opensearch-service/latest/developerguide/osis-getting-started-tutorials.md "../../../opensearch-service/latest/developerguide/osis-getting-started-tutorials.md").
- Learn about the prerequisites and all the configuration options for the DynamoDB plugin at
  [DynamoDB plugin for
  OpenSearch Ingestion documentation](../../../opensearch-service/latest/developerguide/configure-client-ddb.md "../../../opensearch-service/latest/developerguide/configure-client-ddb.md").

## How it works

The plugin uses [DynamoDB export to Amazon S3](S3DataExport.md "S3DataExport.md") to
create an initial snapshot to load into OpenSearch. After the snapshot has been loaded, the
plugin uses DynamoDB Streams to replicate any further changes in near real time. Every item is
processed as an event in OpenSearch Ingestion and can be modified with processor plugins.
You can drop attributes or create composite attributes and send them to different indexes
through routes.

You must have [point-in-time recovery (PITR)](Point-in-time-recovery.md "Point-in-time-recovery.md")
enabled to use export to Amazon S3. You must also have [DynamoDB
Streams](streamsmain.md "streamsmain.md") enabled (with the **new & old images** option selected)
to be able to use it. It's possible to create a pipeline without taking a snapshot by
excluding export settings.

You can also create a pipeline with only a snapshot and no updates by excluding streams
settings. The plugin does not use read or write throughput on your table, so it is safe to use
without impacting your production traffic. There are limits to the number of parallel
consumers on a stream that you should consider before creating this or other integrations. For
other considerations, see [Best practices for integrating with DynamoDB](bp-integration.md "bp-integration.md").

For simple pipelines, a single OpenSearch Compute Unit (OCU) can process about 1 MB per
second of writes. This is the equivalent of about 1000 write request units (WCU). Depending on
your pipeline's complexity and other factors, you might achieve more or less than this.

OpenSearch Ingestion supports a dead-letter queue (DLQ) for events that cause
unrecoverable errors. Additionally, the pipeline can resume from where it left off without
user intervention even if there's an interruption of service with either DynamoDB, the pipeline,
or Amazon OpenSearch Service.

If interruption goes on for longer than 24 hours, this can cause a loss of updates.
However, the pipeline would continue to process the updates that were still available when
availability is restored. You would need to do a fresh index build to fix any irregularities
due to the dropped events unless they were in the dead-letter queue.

For all the settings and details for the plugin, see [OpenSearch
Ingestion DynamoDB plugin documentation](../../../opensearch-service/latest/developerguide/configure-client-ddb.md "../../../opensearch-service/latest/developerguide/configure-client-ddb.md").

## Integrated create experience through the console

DynamoDB and OpenSearch Service have an integrated experience in the AWS Management Console, which streamlines the
getting started process. When you go through these steps, the service will automatically
select the DynamoDB blueprint and add the appropriate DynamoDB information for you.

To create an integration, follow along in the [OpenSearch Ingestion
getting started guide](../../../opensearch-service/latest/developerguide/osis-get-started.md "../../../opensearch-service/latest/developerguide/osis-get-started.md"). When you get to [Step 3: Create a pipeline](../../../opensearch-service/latest/developerguide/osis-get-started.md#osis-get-started-pipeline "../../../opensearch-service/latest/developerguide/osis-get-started.md#osis-get-started-pipeline"), replace Steps 1 and 2 with the following steps:

1. Navigate to the DynamoDB console.
2. In the left-hand navigation pane, choose **Integration**.
3. Select the DynamoDB table that you'd like to replicate to OpenSearch.
4. Choose **Create**.

From here, you can continue on with the rest of the tutorial.

## Next steps

For a better understanding of how DynamoDB integrates with OpenSearch Service, see the following:

- [Getting started with Amazon OpenSearch Ingestion](../../../opensearch-service/latest/developerguide/osis-getting-started-tutorials.md "../../../opensearch-service/latest/developerguide/osis-getting-started-tutorials.md")
- [DynamoDB plugin
  configuration and requirements](../../../opensearch-service/latest/developerguide/configure-client-ddb.md "../../../opensearch-service/latest/developerguide/configure-client-ddb.md")
