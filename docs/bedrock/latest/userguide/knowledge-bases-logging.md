# Monitor knowledge bases using CloudWatch Logs

Amazon Bedrock supports a monitoring system to help you understand the execution of any data
ingestion jobs for your knowledge bases. The following sections cover how to enable and
configure the logging system for
Amazon Bedrock knowledge bases using both the AWS Management Console and CloudWatch API. You can gain
visibility into the data ingestion of your knowledge base resources with this logging system.

## Knowledge bases logging using the console

To enable logging for an Amazon Bedrock knowledge base using the AWS Management Console:

1. **Create a knowledge base**: Use the AWS Management Console for Amazon Bedrock to [create a new knowledge
   base](knowledge-base-create.md "knowledge-base-create.md").
2. **Add a log delivery option**: After creating the knowledge
   base, edit or update your knowledge base to add a log delivery option.

###### Note

Log deliveries are not supported when creating a knowledge base with a structured data
store, or for a Kendra GenAI Index.

**Configure log delivery details**: Enter the details for
the log delivery, including:

    * Logging destination (either CloudWatch Logs, Amazon S3, Amazon Data Firehose)
    * (If using CloudWatch Logs as the logging destination) Log group name
    * (If using Amazon S3 as the logging destination) Bucket name
    * (If using Amazon Data Firehose as the logging destination) Firehose stream

3. **Include access permissions**: The user who
   is signed into the console must have the necessary permissions to
   write the collected logs to the chosen destination.

The following example IAM policy can be attached to the user signed into
the console to grant the necessary permissions when using CloudWatch Logs

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

4. **Confirm delivery status**: Verify that the
   log delivery status is "Delivery active" in the console.

## Knowledge bases logging using the CloudWatch API

To enable logging for an Amazon Bedrock knowledge base using the CloudWatch API:

1. **Get the ARN of your knowledge base**: After
   [creating a knowledge base](knowledge-base-create.md "knowledge-base-create.md") using either the Amazon Bedrock API or the Amazon Bedrock console,
   get the Amazon Resource Name of the knowledge base. You can get the Amazon Resource
   Name by calling [GetKnowledgeBase](../APIReference/API_agent_GetKnowledgeBase.md "../APIReference/API_agent_GetKnowledgeBase.md") API. A knowledge base Amazon Resource Name follows this
   format:
   `arn:aws:bedrock:your-region:your-account-id:knowledge-base/knowledge-base-id`
2. **Call `PutDeliverySource`**: Use the [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") API provided by Amazon CloudWatch to create a delivery source for the
   knowledge base. Pass the knowledge base Amazon Resource Name as the `resourceArn`.
   `logType` specifies `APPLICATION_LOGS` as the type of logs
   that are collected. `APPLICATION_LOGS` track the current status of files
   during an ingestion job.

```
{
    "logType": "APPLICATION_LOGS",
    "name": "my-knowledge-base-delivery-source",
    "resourceArn": "arn:aws:bedrock:your-region:your-account-id:knowledge-base/knowledge_base_id"
}

```

3. **Call `PutDeliveryDestination`**: Use the
   [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") API provided by Amazon CloudWatch to configure where the logs
   will be stored. You can choose either CloudWatch Logs, Amazon S3, or Amazon Data Firehose as the destination
   for storing logs. You must specify the Amazon Resource Name of one of the destination
   options for where your logs will be stored. You can choose the `outputFormat`
   of the logs to be one of the following: `json`, `plain`,
   `w3c`, `raw`, `parquet`. The following is an example
   of configuring logs to be stored in an Amazon S3 bucket and in JSON format.

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

Note that if you are delivering logs cross-account, you must use the
`PutDeliveryDestinationPolicy` API to assign an AWS Identity and Access Management (IAM)
policy to the destination account. The IAM policy allows delivery from
one account to another account. 4. **Call `CreateDelivery`**: Use the
[CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") API call to link the delivery source to the destination
that you created in the previous steps. This API operation associates the
delivery source with the end destination.

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

If you want to use AWS CloudFormation, you can use the following:

- [Delivery](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md")
- [DeliveryDestination](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md")
- [DeliverySource](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md")
  The `ResourceArn` is the `KnowledgeBaseARN`, and
  `LogType` must be `APPLICATION_LOGS` as the supported
  log type.

## Supported log types

Amazon Bedrock knowledge bases support the following log types:

- `APPLICATION_LOGS`: Logs that track the current status of a
  specific file during a data ingestion job.

## User permissions and limits

To enable logging for an Amazon Bedrock knowledge base, the following permissions are
required for the user account signed into the console:

1. `bedrock:AllowVendedLogDeliveryForResource` – Required
   to allow logs to be delivered for the knowledge base resource.

You can view an example IAM role/permissions policy with all the required
permissions for your specific logging destination. See [Vended logs permissions for different delivery destinations](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-vended-logs-permissions-V2"),
and follow the IAM role/permission policy example for your logging destination,
including allowing updates to your specific logging destination resource (whether
CloudWatch Logs, Amazon S3, or Amazon Data Firehose).

You can also check if there are any quota limits for making CloudWatch logs delivery-related
API calls in the [CloudWatch
Logs service quotas documentation](../../../general/latest/gr/cwl_region.md "../../../general/latest/gr/cwl_region.md"). Quota limits set a maximum number of
times you can call an API or create a resource. If you exceed a limit, it will result in
a `ServiceQuotaExceededException` error.

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
