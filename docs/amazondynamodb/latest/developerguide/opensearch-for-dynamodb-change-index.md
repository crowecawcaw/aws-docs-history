# Handling breaking changes to your

index

OpenSearch can dynamically add new attributes to your index. However, after your mapping
template has been set for a given key, you’ll need to take additional action to change it.
Additionally, if your change requires you to reprocess all the data in your DynamoDB table,
you’ll need to take steps to initiate a fresh export.

###### Note

In all these options, you might still run into issues if your DynamoDB table has type
conflicts with the mapping template you’ve specified. Ensure that you have a dead-letter
queue (DLQ) enabled (even in development). This makes it easier to understand what might be
wrong with the record that causes a conflict when it's being indexed into your index on
OpenSearch.

###### Topics

- [How it works](#opensearch-for-dynamodb-change-index-howitworks "#opensearch-for-dynamodb-change-index-howitworks")
- [Delete your index and reset
  the pipeline (pipeline-centric option)](#opensearch-for-dynamodb-change-index-delete "#opensearch-for-dynamodb-change-index-delete")
- [Recreate your index and
  reset the pipeline (index-centric option)](#opensearch-for-dynamodb-change-index-recreate "#opensearch-for-dynamodb-change-index-recreate")
- [Create a new index and sink
  (online option)](#opensearch-for-dynamodb-change-index-create "#opensearch-for-dynamodb-change-index-create")
- [Best practices for avoiding and
  debugging type conflicts](#opensearch-for-dynamodb-change-index-bp "#opensearch-for-dynamodb-change-index-bp")

## How it works

Here's a quick overview of the actions taken when handling breaking changes to your
index. See the step-by-step procedures in the sections that follow.

- **Stop and start the pipeline**: This option resets the
  pipeline’s state, and the pipeline will restart with a new full export. It is
  non-destructive, so it does **not** delete your index or
  any data in DynamoDB. If you don’t create a fresh index before you do this, you might see a
  high number of errors from version conflicts because the export tries to insert older
  documents than the current `_version` in the index. You can safely ignore
  these errors. You will not be billed for the pipeline while it is stopped.
- **Update the pipeline**: This option updates the
  configuration in the pipeline with a [blue/green](../../../whitepapers/latest/overview-deployment-options/bluegreen-deployments.md "../../../whitepapers/latest/overview-deployment-options/bluegreen-deployments.md") approach, without losing any state. If you make significant
  changes to your pipeline (such as adding new routes, indexes, or keys to existing
  indexes), you might need to do a full reset of the pipeline and recreate your index.
  This option does **not** perform a full export.
- **Delete and recreate the index**: This option removes
  your data and mapping settings on your index. You should do this before making any
  breaking changes to your mappings. It will break any applications that rely on the index
  until the index is recreated and synchronized. Deleting the index does **not** initiate a fresh export. You should delete your index only
  after you’ve updated your pipeline. Otherwise, your index might be recreated before you
  update your settings.

## Delete your index and reset

the pipeline (pipeline-centric option)

This method is often the fastest option if you’re still in development. You’ll delete
your index in OpenSearch Service, and then [stop and
start](../../../opensearch-service/latest/developerguide/pipeline--stop-start.md "../../../opensearch-service/latest/developerguide/pipeline--stop-start.md") your pipeline to initiate a fresh export of all your data. This ensures that
there are no mapping template conflicts with existing indexes, and no loss of data from an
incomplete processed table.

1. Stop the pipeline either through the AWS Management Console, or by using the
   StopPipeline API operation with the AWS CLI or an SDK.
2. [Update your
   pipeline configuration](../../../opensearch-service/latest/developerguide/update-pipeline.md "../../../opensearch-service/latest/developerguide/update-pipeline.md") with your new changes.
3. Delete your index in OpenSearch Service, either through a `REST` API call or your
   OpenSearch Dashboard.
4. Start the pipeline either through the console, or by using the
   `StartPipeline` API operation with the AWS CLI or an SDK.

###### Note

This initiates a fresh full export, which will incur additional costs. 5. Monitor for any unexpected issues because a fresh export is generated to create the
new index. 6. Confirm that the index matches your expectations in OpenSearch Service.

After the export has completed and it resumes reading from the stream, your DynamoDB table
data will now be available in the index.

## Recreate your index and

reset the pipeline (index-centric option)

This method works well if you need to do a lot of iterations on the index design in
OpenSearch Service before resuming the pipeline from DynamoDB. This can be useful for development when you
want to iterate very quickly on your search patterns, and want to avoid waiting on fresh
exports to complete between each iteration.

1. Stop the pipeline either through the AWS Management Console, or by calling the
   StopPipeline API operation with the AWS CLI or an SDK.
2. Delete and recreate your index in OpenSearch with the mapping template you want to
   use. You can manually insert some sample data to confirm that your searches are working
   as intended. If your sample data might conflict with any data from DynamoDB, be sure to
   delete it before moving onto the next step.
3. If you have an indexing template in your pipeline, remove it or replace it with the
   one you’ve created already in OpenSearch Service. Ensure that the name of your index matches the name
   in the pipeline.
4. Start the pipeline either through console, or by calling the
   `StartPipeline` API operation with the AWS CLI or an SDK.

###### Note

This will initiate a fresh full export, which will incur additional costs. 5. Monitor for any unexpected issues because a fresh export is generated to create the
new index.

After the export has completed and it resumes reading from the stream, you should be
your DynamoDB table data will now be available in the index.

## Create a new index and sink

(online option)

This method works well if you need to update your mapping template but are currently
using your index in production. This creates a brand new index, which you’ll need to move
your application over to after it’s synchronized and validated.

###### Note

This will create another consumer on the stream. This can be an issue if you also have
other consumers like AWS Lambda or global tables. You might need to pause updates to your
existing pipeline to create capacity to load the new index.

1. [Create a new pipeline](OpenSearchIngestionForDynamoDB.md#opensearch-for-dynamodb-console-create "OpenSearchIngestionForDynamoDB.md#opensearch-for-dynamodb-console-create")
   with new settings and a different index name.
2. Monitor the new index for any unexpected issues.
3. Swap the application over to the new index.
4. Stop and delete the old pipeline after validating that everything is working
   correctly.

## Best practices for avoiding and

debugging type conflicts

- Always use a dead-letter queue (DLQ) to make it easier to debug when there are type
  conflicts.
- Always use an index template with mappings and set `include_keys`. While
  OpenSearch Service dynamically maps new keys, this can cause issues with unexpected behaviors (such
  as expecting something to be a `GeoPoint`, but it’s created as a
  `string` or `object`) or errors (such as having a
  `number` that is a mix of `long` and `float`
  values).
- If you need to keep your existing index working in production, you can also replace
  any of the previous [delete
  index steps](#opensearch-for-dynamodb-change-index-delete "#opensearch-for-dynamodb-change-index-delete") with just renaming your index in your pipeline config file. This
  creates a brand new index. Your application will then need to be updated to point to the
  new index after it's complete.
- If you have a type conversion issue that you fix with a processor, you can test this
  with `UpdatePipeline`. To do this, you’ll need to do a stop and start or
  [process
  your dead-letter queues](https://opensearch.org/docs/latest/data-prepper/pipelines/dlq/ "https://opensearch.org/docs/latest/data-prepper/pipelines/dlq/") to fix any previously skipped documents that had
  errors.
