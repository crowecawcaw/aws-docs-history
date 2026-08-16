# Monitor knowledge bases using CloudWatch Logs

Amazon Bedrock supports a monitoring system to help you understand the execution of any data
ingestion jobs for your knowledge bases. The following sections cover how to enable and
configure the logging system for
Amazon Bedrock knowledge bases using both the AWS Management Console and CloudWatch API. You can gain
visibility into the data ingestion of your knowledge base resources with this logging system.

## Prerequisites

Before you enable logging for an Amazon Bedrock knowledge base, confirm the following:

- The user account signed into the console has the
  `bedrock:AllowVendedLogDeliveryForResource` permission. This
  permission allows logs to be delivered for the knowledge base resource.
  For an example IAM policy with all the required permissions, see [Vended logs permissions for different delivery destinations](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2").
  Follow the IAM role/permission policy example for your logging destination,
  including allowing updates to your specific logging destination resource (whether
  CloudWatch Logs, Amazon S3, or Amazon Data Firehose).
- Check whether there are quota limits for CloudWatch Logs delivery-related
  API calls. For more information, see the [CloudWatch
  Logs service quotas documentation](../../../general/latest/gr/cwl_region.md "../../../general/latest/gr/cwl_region.md"). If you exceed a limit, it results in
  a `ServiceQuotaExceededException` error.

### Supported log types

Amazon Bedrock knowledge bases support the following log types:

- `APPLICATION_LOGS`: Logs that track the current status of a
  specific file during a data ingestion job.

## Enabling logging for an Amazon Bedrock knowledge base (console)

###### To enable logging using the console

1. Create a knowledge base. For instructions, see [Create a knowledge
   base](knowledge-base-create.md "knowledge-base-create.md").
2. Edit your knowledge base to add a log delivery option.

###### Note

Log deliveries are not supported when creating a knowledge base with a structured data
store, or for a Kendra GenAI Index. 3. Configure the log delivery details, including:

    * **Logging destination** (CloudWatch Logs, Amazon S3, or Amazon Data Firehose)
    * (If using CloudWatch Logs) **Log group name**
    * (If using Amazon S3) **Bucket name**
    * (If using Amazon Data Firehose) **Firehose stream**

4. Attach an IAM policy to your account to grant permissions to write logs to the destination.

The following example IAM policy grants the necessary permissions when using CloudWatch Logs:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "logs:CreateDelivery",
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:delivery-source:*",
 "arn:aws:logs:`us-east-1`:`123456789012`:delivery:*",
 "arn:aws:logs:`us-east-1`:`123456789012`:delivery-destination:*"
 ]
 }
 ]
}`

```

5. Verify that the log delivery status shows **Delivery active** in the console.

## Enabling logging for an Amazon Bedrock knowledge base (CloudWatch API)

###### To enable logging using the CloudWatch API

1. Create a knowledge base using the Amazon Bedrock API or the Amazon Bedrock console. For instructions, see [Create a knowledge
   base](knowledge-base-create.md "knowledge-base-create.md").
2. Get the ARN of your knowledge base. Call the [GetKnowledgeBase](../APIReference/API_agent_GetKnowledgeBase.md "../APIReference/API_agent_GetKnowledgeBase.md") API to retrieve the ARN. A knowledge base ARN follows this
   format:
   `arn:aws:bedrock:your-region:your-account-id:knowledge-base/knowledge-base-id`
3. Call the [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") API to create a delivery source for the
   knowledge base. Pass the knowledge base ARN as the `resourceArn`.
   Set `logType` to `APPLICATION_LOGS`, which tracks the
   status of files during an ingestion job.

```
{
    "logType": "APPLICATION_LOGS",
    "name": "my-knowledge-base-delivery-source",
    "resourceArn": "arn:aws:bedrock:your-region:your-account-id:knowledge-base/knowledge_base_id"
}

```

4. Call the [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") API to configure where the logs
   are stored.

   1. Choose CloudWatch Logs, Amazon S3, or Amazon Data Firehose as the destination.
   2. Specify the ARN of your chosen destination.
   3. Set `outputFormat`
      to one of the following: `json`, `plain`,
      `w3c`, `raw`, `parquet`.The following example stores logs in an Amazon S3 bucket in JSON format:

```
{
   "deliveryDestinationConfiguration": {
      "destinationResourceArn": "arn:aws:s3:::bucket-name"
   },
   "name": "string",
   "outputFormat": "json",
   "tags": {
      "key" : "value"
   }
}
```

To deliver logs cross-account, use the
`PutDeliveryDestinationPolicy` API to assign an IAM
policy to the destination account. The policy allows delivery from
one account to another. 5. Call the [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") API to link the delivery source to the destination.
This associates the delivery source with the end destination.

```
{
   "deliveryDestinationArn": "string",
   "deliverySourceName": "string",
   "tags": {
      "string" : "string"
   }
}

```

###### Note

If you want to use CloudFormation, you can use the following:

- [Delivery](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md")
- [DeliveryDestination](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md")
- [DeliverySource](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md")
  The `ResourceArn` is the `KnowledgeBaseARN`, and
  `LogType` must be `APPLICATION_LOGS` as the supported
  log type.

## Examples of knowledge base logs

There are data ingestion level logs and resource level logs for Amazon Bedrock knowledge bases.

The following is an example of a data ingestion job log.

```
{
    "event_timestamp": 1718683433639,
    "event": {
        "ingestion_job_id": "<IngestionJobId>",
        "data_source_id": "<IngestionJobId>",
        "ingestion_job_status": "INGESTION_JOB_STARTED" | "STOPPED" | "COMPLETE" | "FAILED" | "CRAWLING_COMPLETED"
        "knowledge_base_arn": "arn:aws:bedrock:<region>:<accountId>:knowledge-base/<KnowledgeBaseId>",
        "resource_statistics": {
            "number_of_resources_updated": int,
            "number_of_resources_ingested": int,
            "number_of_resources_scheduled_for_update": int,
            "number_of_resources_scheduled_for_ingestion": int,
            "number_of_resources_scheduled_for_metadata_update": int,
            "number_of_resources_deleted": int,
            "number_of_resources_with_metadata_updated": int,
            "number_of_resources_failed": int,
            "number_of_resources_scheduled_for_deletion": int
        }
    },
    "event_version": "1.0",
    "event_type": "StartIngestionJob.StatusChanged",
    "level": "INFO"
}
```

The following is an example of a resource level log.

```
{
    "event_timestamp": 1718677342332,
    "event": {
        "ingestion_job_id": "<IngestionJobId>",
        "data_source_id": "<IngestionJobId>",
        "knowledge_base_arn": "arn:aws:bedrock:<region>:<accountId>:knowledge-base/<KnowledgeBaseId>",
        "document_location": {
            "type": "S3",
            "s3_location": {
                "uri": "s3:/<BucketName>/<ObjectKey>"
            }
        },
        "status": "<ResourceStatus>"
        "status_reasons": String[],
        "chunk_statistics": {
            "ignored": int,
            "created": int,
            "deleted": int,
            "metadata_updated": int,
            "failed_to_create": int,
            "failed_to_delete": int,
            "failed_to_update_metadata": int
        },
    },
    "event_version": "1.0",
    "event_type": "StartIngestionJob.ResourceStatusChanged",
    "level": "INFO" | "WARN" | "ERROR"
}
```

The `status` for the resource can be one of the following:

- `SCHEDULED_FOR_INGESTION`, `SCHEDULED_FOR_DELETION`,
  `SCHEDULED_FOR_UPDATE`, `SCHEDULED_FOR_METADATA_UPDATE`:
  These status values indicate that the resource is scheduled for processing after
  calculating the difference between the current state of the knowledge base and the
  changes made in the data source.
- `RESOURCE_IGNORED`: This status value indicates that the resource was
  ignored for processing, and the reason is detailed inside `status_reasons`
  property.
- `EMBEDDING_STARTED` and `EMBEDDING_COMPLETED`: These status
  values indicate when the vector embedding for a resource started and completed.
- `INDEXING_STARTED` and `INDEXING_COMPLETED`: These status values
  indicate when the indexing for a resource started and completed.
- `DELETION_STARTED` and `DELETION_COMPLETED`: These status
  values indicate when the deletion for a resource started and completed.
- `METADATA_UPDATE_STARTED` and `METADATA_UPDATE_COMPLETED`:
  These status values indicate when the metadata update for a resource started and
  completed.
- `EMBEDDING_FAILED`, `INDEXING_FAILED`, `DELETION_FAILED`,
  and `METADATA_UPDATE_FAILED`: These status values indicate that the processing
  of a resource failed, and the reasons are detailed inside `status_reasons` property.
- `INDEXED`, `DELETED`, `PARTIALLY_INDEXED`,
  `METADATA_PARTIALLY_INDEXED`, `FAILED`: Once the processing of a document
  is finalized, a log is published with the final status of the document, and the summary of the
  processing inside `chunk_statistics` property.
- `CRAWLED`, `RESOURCE_CRAWLED`, `RESOURCE_FETCHED`,
  `CRAWLING_COMPLETED`, `CONNECTOR_CRAWLING_COMPLETED`: These status
  values indicate that the resource was crawled or fetched from the data source connector.
- `PENDING`, `STARTING`, `IN_PROGRESS`: These status
  values indicate that the resource is queued or currently being processed.
- `DELETE_IN_PROGRESS`, `DELETING`: These status values indicate
  that the resource is in the process of being deleted.
- `INGESTION_JOB_STARTED`, `INGESTION_JOB_FAILED`: These status
  values indicate the start or failure of the overall ingestion job for the resource.
- `GRAPH_ENTITY_EXTRACTION_STARTED`, `GRAPH_ENTITY_EXTRACTION_COMPLETED`,
  `GRAPH_ENTITY_EXTRACTION_FAILED`: These status values indicate the progress of
  graph entity extraction for knowledge bases that use a graph data store.

## Examples of common queries to debug knowledge base logs

You can interact with logs using queries. For example, you can query for all documents with the event status
`RESOURCE_IGNORED` during ingestion of documents or data.

The following are some common queries that can be used to debug the logs generated using CloudWatch Logs Insights:

- Query for all the logs generated for a specific S3 document.

`filter event.document_location.s3_location.uri = "s3://<bucketName>/<objectKey>"`

- Query for all documents ignored during the data ingestion job.

`filter event.status = "RESOURCE_IGNORED"`

- Query for all the exceptions that occurred while vector embedding documents.

`filter event.status = "EMBEDDING_FAILED"`

- Query for all the exceptions that occurred while indexing documents into the vector database.

`filter event.status = "INDEXING_FAILED"`

- Query for all the exceptions that occurred while deleting documents from the vector database.

`filter event.status = "DELETION_FAILED"`

- Query for all the exceptions that occurred while updating the metadata of your document in the vector database.

`filter event.status = "DELETION_FAILED"`

- Query for all the exceptions that occurred during the execution of a data ingestion job.

`filter level = "ERROR" or level = "WARN"`
