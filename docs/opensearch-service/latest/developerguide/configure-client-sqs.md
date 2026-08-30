# Using an OpenSearch Ingestion pipeline with Amazon Simple Queue Service

You can use the Amazon Simple Queue Service (Amazon SQS) source plugin to ingest data directly from Amazon SQS queue
messages into Amazon OpenSearch Service domains and Amazon OpenSearch Serverless collections. The pipeline polls messages from
one or more Amazon SQS queues, parses the message body as structured data, and indexes the
content into OpenSearch – no intermediate storage such as Amazon S3 is required.

This source is ideal for event-driven architectures where applications publish structured
messages (JSON, plaintext, or other formats) directly to Amazon SQS queues and you want to index
and search that data in near real time.

###### Topics

- [Prerequisites](#sqs-prereqs "#sqs-prereqs")
- [Step 1: Configure the pipeline role](#sqs-pipeline-role "#sqs-pipeline-role")
- [Step 2: Create the pipeline](#sqs-pipeline "#sqs-pipeline")
- [Configuration options](#sqs-config-options "#sqs-config-options")
- [Data consistency](#sqs-pipeline-consistency "#sqs-pipeline-consistency")
- [Cross-account Amazon Simple Queue Service as a source](#sqs-cross-account "#sqs-cross-account")
- [Recommended CloudWatch Alarms for Amazon SQS](#sqs-pipeline-metrics "#sqs-pipeline-metrics")
- [Limitations](#sqs-pipeline-limitations "#sqs-pipeline-limitations")
- [Troubleshooting](#sqs-pipeline-troubleshooting "#sqs-pipeline-troubleshooting")

## Prerequisites

Before you create your OpenSearch Ingestion pipeline with an Amazon SQS source, you must have the
following:

1. **An Amazon Simple Queue Service queue** – One or more
   standard Amazon SQS queues containing messages you want to ingest. The pipeline reads
   the message body directly and treats it as the event payload. For more
   information, see [Creating a queue](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/step-create-queue.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/step-create-queue.md") in the _Amazon Simple Queue Service Developer
   Guide_.

###### Note

FIFO queues are not supported. Use standard Amazon SQS queues. 2. **An Amazon OpenSearch Service domain or Amazon OpenSearch Serverless
collection** – The destination for your ingested data. For
more information, see [Getting started with OpenSearch Ingestion](osis-getting-started-tutorials.md "osis-getting-started-tutorials.md").

## Step 1: Configure the pipeline role

The Amazon SQS source plugin uses a pull-based architecture in which the pipeline polls
messages directly from the Amazon SQS queue. You must [configure the pipeline role](pipeline-security-overview.md#pipeline-security-sink "pipeline-security-overview.md#pipeline-security-sink") with permissions to read from the Amazon SQS queue
and write to the OpenSearch sink.

###### Note

You must use the same `sts_role_arn` in all pipeline components.

### Amazon SQS source permissions

Add the following permissions to allow the pipeline to poll and manage messages on
the queue:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "allowReadFromSQS",
      "Effect": "Allow",
      "Action": [
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:DeleteMessageBatch",
        "sqs:ChangeMessageVisibility"
      ],
      "Resource": "arn:aws:sqs:`region`:`account-id`:`queue-name`"
    }
  ]
}
```

### (Optional) AWS KMS decryption permissions

If your Amazon SQS queue is encrypted with an AWS KMS customer managed key, add the following
permissions:

```
{
  "Sid": "allowKMSDecryptSQS",
  "Effect": "Allow",
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey"
  ],
  "Resource": "arn:aws:kms:`region`:`account-id`:key/`key-id`"
}
```

### OpenSearch sink permissions

Add the following permissions for writing to your OpenSearch domain or
collection:

```
{
  "Sid": "allowAccessToOpenSearch",
  "Effect": "Allow",
  "Action": [
    "es:DescribeDomain",
    "es:ESHttp*"
  ],
  "Resource": [
    "arn:aws:es:`region`:`account-id`:domain/`domain-name`",
    "arn:aws:es:`region`:`account-id`:domain/`domain-name`/*"
  ]
}
```

### Pipeline role trust policy

The pipeline role must have a trust relationship with
`osis-pipelines.amazonaws.com`:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "osis-pipelines.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`account-id`"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:osis:`region`:`account-id`:pipeline/*"
        }
      }
    }
  ]
}
```

### Domain access policy

If you're writing to an OpenSearch Service domain, configure the [domain
access policy](ac.md#ac-types-resource "ac.md#ac-types-resource") to allow the pipeline role:

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::`account-id`:role/`pipeline-role`"
      },
      "Action": ["es:DescribeDomain", "es:ESHttp*"],
      "Resource": "arn:aws:es:`region`:`account-id`:domain/`domain-name`/*"
    }
  ]
}
```

## Step 2: Create the pipeline

After configuring the pipeline role, create your OpenSearch Ingestion pipeline specifying
`sqs` as the source. You can use a preconfigured **Amazon Simple Queue Service** blueprint available on the OpenSearch Ingestion console.

### Basic pipeline configuration

The following example reads JSON messages from a single Amazon SQS queue and indexes
them into OpenSearch:

```
version: "2"
sqs-pipeline:
  source:
    sqs:
      queues:
        - url: "https://sqs.`region`.amazonaws.com/`account-id`/`queue-name`"
          codec:
            json:
          workers: 2
          maximum_messages: 10
          poll_delay: "0s"
          wait_time: "20s"
          visibility_timeout: "60s"
      acknowledgments: true
      aws:
        sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
        region: "`region`"
  processor:
    - date:
        destination: "@timestamp"
        from_time_received: true
  sink:
    - opensearch:
        hosts: ["https://search-`domain-name`.`region`.es.amazonaws.com"]
        index: "sqs-events"
        aws:
          region: "`region`"
          sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
          serverless: false
        dlq:
          s3:
            bucket: "`dlq-bucket-name`"
            key_path_prefix: "sqs-pipeline/dlq"
            region: "`region`"
            sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
```

### Pipeline configuration with multiple queues

Each queue is configured as its own entry in the `queues` list with
independent settings:

```
version: "2"
multi-queue-pipeline:
  source:
    sqs:
      queues:
        - url: "https://sqs.`region`.amazonaws.com/`account-id`/`queue-1`"
          codec:
            json:
          workers: 2
          maximum_messages: 10
          poll_delay: "0s"
          wait_time: "20s"
        - url: "https://sqs.`region`.amazonaws.com/`account-id`/`queue-2`"
          codec:
            ndjson:
          workers: 3
          maximum_messages: 5
          poll_delay: "5s"
          wait_time: "20s"
      acknowledgments: true
      aws:
        sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
        region: "`region`"
  sink:
    - opensearch:
        hosts: ["https://search-`domain-name`.`region`.es.amazonaws.com"]
        index: "sqs-events"
        aws:
          region: "`region`"
          sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
          serverless: false
```

### Pipeline configuration with newline-delimited messages

For queues where each message contains multiple log lines separated by
newlines:

```
version: "2"
log-pipeline:
  source:
    sqs:
      queues:
        - url: "https://sqs.`region`.amazonaws.com/`account-id`/`queue-name`"
          codec:
            newline:
          workers: 2
          maximum_messages: 10
          poll_delay: "0s"
          wait_time: "20s"
          on_error: "retain_messages"
      acknowledgments: true
      aws:
        sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
        region: "`region`"
  processor:
    - grok:
        match:
          message:
            - "%{COMMONAPACHELOG}"
    - date:
        destination: "@timestamp"
        from_time_received: true
  sink:
    - opensearch:
        hosts: ["https://search-`domain-name`.`region`.es.amazonaws.com"]
        index: "sqs-logs"
        aws:
          region: "`region`"
          sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
          serverless: false
```

### Pipeline configuration with visibility duplication protection

For high-throughput queues where processing time may exceed the visibility
timeout:

```
version: "2"
protected-pipeline:
  source:
    sqs:
      queues:
        - url: "https://sqs.`region`.amazonaws.com/`account-id`/`queue-name`"
          codec:
            json:
          workers: 4
          maximum_messages: 10
          poll_delay: "0s"
          wait_time: "20s"
          visibility_timeout: "60s"
          visibility_duplication_protection: true
          visibility_duplicate_protection_timeout: "2h"
      acknowledgments: true
      aws:
        sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
        region: "`region`"
  sink:
    - opensearch:
        hosts: ["https://search-`domain-name`.`region`.es.amazonaws.com"]
        index: "sqs-events"
        aws:
          region: "`region`"
          sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
          serverless: false
```

### Pipeline configuration with Amazon OpenSearch Serverless

```
version: "2"
serverless-sqs-pipeline:
  source:
    sqs:
      queues:
        - url: "https://sqs.`region`.amazonaws.com/`account-id`/`queue-name`"
          codec:
            json:
          workers: 2
          maximum_messages: 10
          poll_delay: "0s"
          wait_time: "20s"
      acknowledgments: true
      aws:
        sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
        region: "`region`"
  sink:
    - opensearch:
        hosts: ["https://`collection-id`.`region`.aoss.amazonaws.com"]
        index: "sqs-events"
        aws:
          region: "`region`"
          sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
          serverless: true
          serverless_options:
            network_policy_name: "`network-policy-name`"
```

## Configuration options

### Amazon SQS source top-level options

Each entry in `queues` configures a single Amazon SQS queue with the
following parameters:

| Option            | Required | Type     | Description                                                                                                                                                                                                                                                   |
| ----------------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `queues`          | Yes      | List     | A list of queue configurations. Each entry defines a single Amazon SQS<br>queue and its independent polling settings.                                                                                                                                         |
| `acknowledgments` | No       | Boolean  | Enables end-to-end delivery acknowledgment. When<br>`true`, messages are deleted from the queue only<br>after the sink confirms successful delivery. When `false`,<br>messages are deleted immediately after buffering (risks data loss).<br>Default: `true`. |
| `buffer_timeout`  | No       | Duration | Time to wait for buffer space before timing out. Default:<br>`10s`.                                                                                                                                                                                           |
| `aws`             | Yes      | Object   | AWS authentication configuration (see below).                                                                                                                                                                                                                 |

### Queue configuration options

| Option                                    | Required | Type       | Description                                                                                                                                                                                                                                                      |
| ----------------------------------------- | -------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `url`                                     | Yes      | String     | The Amazon SQS queue URL to poll. Each queue must be its own entry in<br>the `queues` list.                                                                                                                                                                      |
| `codec`                                   | No       | InputCodec | The codec used to parse the Amazon SQS message body. Supported codecs<br>include `json`, `ndjson`, and<br>`newline`. When not specified, the raw message body is<br>used as a single event.                                                                      |
| `workers`                                 | No       | Integer    | The number of worker threads to use for polling and processing<br>messages from this queue. Default: `1`.                                                                                                                                                        |
| `maximum_messages`                        | No       | Integer    | The maximum number of messages to receive per<br>`ReceiveMessage` API call. Valid range: 1–10.<br>Default: uses the Amazon SQS queue's configured value (typically<br>10).                                                                                       |
| `poll_delay`                              | No       | Duration   | The delay between polling cycles when messages were received in<br>the previous cycle. Default: `0s` (no delay between<br>polls).                                                                                                                                |
| `wait_time`                               | No       | Duration   | The wait time for Amazon SQS long polling. Setting this to a value<br>greater than 0 enables long polling, reducing empty responses and API<br>costs. Valid range: 0–20s. Default: uses the Amazon SQS queue's<br>configured value.                              |
| `visibility_timeout`                      | No       | Duration   | The visibility timeout applied to messages received from the<br>queue. Set this to be longer than expected processing time to avoid<br>duplicate processing. Valid range: 0–43200s (12h). Default:<br>uses the Amazon SQS queue's configured visibility timeout. |
| `visibility_duplication_protection`       | No       | Boolean    | When `true`, the pipeline progressively extends the<br>visibility timeout for messages still being processed, preventing<br>them from becoming visible to other consumers before acknowledgment.<br>Default: `false`.                                            |
| `visibility_duplicate_protection_timeout` | No       | Duration   | The maximum total time a message's visibility timeout can be<br>extended when `visibility_duplication_protection` is<br>enabled. Valid range: 30s–24h. Default:<br>`2h`.                                                                                         |
| `on_error`                                | No       | String     | Controls behavior when a message fails processing.<br>`retain_messages` keeps the message in the queue for<br>redelivery. `delete_messages` deletes the message even on<br>failure. Default: `retain_messages`.                                                  |

### AWS configuration options

| Option                 | Required | Type   | Description                                                                                                                                                    |
| ---------------------- | -------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sts_role_arn`         | Yes      | String | The IAM role ARN that the pipeline assumes to access the Amazon SQS<br>queue. This role must have a trust relationship with<br>`osis-pipelines.amazonaws.com`. |
| `region`               | Yes      | String | The AWS Region of the Amazon SQS queues.                                                                                                                       |
| `sts_external_id`      | No       | String | An external ID for cross-account STS role assumption. Length:<br>2–1224 characters.                                                                            |
| `sts_header_overrides` | No       | Map    | A map of header overrides for STS requests. Maximum 5<br>entries.                                                                                              |

### Available metadata attributes

The following metadata attributes are available from Amazon SQS messages and can be
referenced in the pipeline configuration using `getMetadata()`:

| Attribute       | Description                                                           |
| --------------- | --------------------------------------------------------------------- |
| `messageId`     | The unique Amazon SQS message ID.                                     |
| `receiptHandle` | The receipt handle for the message (used internally for<br>deletion). |

## Data consistency

OpenSearch Ingestion supports end-to-end acknowledgment to ensure data durability when using
the Amazon SQS source. The plugin supports multi-node deployments and back-off
mechanisms:

1. The pipeline polls messages from the Amazon SQS queue using the
   `ReceiveMessage` API with the configured
   `maximum_messages` count.
2. Received messages become invisible to other consumers for the duration of the
   `visibility_timeout`.
3. The plugin uses configurable worker threads (`workers`) to process
   messages concurrently from each queue.
4. A back-off mechanism is triggered when the pipeline encounters errors, using
   exponential backoff to prevent overwhelming the Amazon SQS service.
5. After all events from a message are successfully ingested into the
   OpenSearch domain or collection, the pipeline deletes the message from the
   queue using `DeleteMessageBatch`.
6. If processing fails or the pipeline crashes, the visibility timeout expires and
   the message becomes available again for reprocessing.
7. When `visibility_duplication_protection` is enabled, the pipeline
   progressively extends the visibility timeout for in-flight messages, preventing
   duplicate processing for long-running operations.
8. The plugin supports multi-node deployment, allowing multiple pipeline
   instances to poll from the same queue for horizontal scalability.

To handle messages that repeatedly fail processing, configure a [dead-letter queue (DLQ)](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.md") on the source Amazon SQS queue. Messages that exceed the
maximum receive count are automatically moved to the DLQ by Amazon Simple Queue Service.

## Cross-account Amazon Simple Queue Service as a source

You can configure cross-account access so that an OpenSearch Ingestion pipeline in one
AWS account can read messages from an Amazon SQS queue in another account.

### Step 1: Configure Amazon SQS queue resource policy (source account)

In the account that owns the Amazon SQS queue, add the following to the queue's access
policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCrossAccountPipelineAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::`pipeline-account-id`:role/`pipeline-role`"
      },
      "Action": [
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:DeleteMessageBatch",
        "sqs:ChangeMessageVisibility"
      ],
      "Resource": "arn:aws:sqs:`region`:`source-account-id`:`queue-name`"
    }
  ]
}
```

### Step 2: Pipeline configuration for cross-account

Specify the full queue URL from the source account in your pipeline
configuration:

```
version: "2"
cross-account-sqs-pipeline:
  source:
    sqs:
      queues:
        - url: "https://sqs.`region`.amazonaws.com/`source-account-id`/`queue-name`"
          codec:
            json:
          workers: 2
          maximum_messages: 10
          poll_delay: "0s"
          wait_time: "20s"
      acknowledgments: true
      aws:
        sts_role_arn: "arn:aws:iam::`pipeline-account-id`:role/`pipeline-role`"
        region: "`region`"
        sts_external_id: "`external-id`"
  sink:
    - opensearch:
        hosts: ["https://search-`domain-name`.`region`.es.amazonaws.com"]
        index: "cross-account-events"
        aws:
          region: "`region`"
          sts_role_arn: "arn:aws:iam::`pipeline-account-id`:role/`pipeline-role`"
          serverless: false
```

## Recommended CloudWatch Alarms for Amazon SQS

The following CloudWatch metrics are emitted by the Amazon SQS source plugin and can be used for
monitoring pipeline health:

| Metric name                               | Full CloudWatch metric name                                         | Description                                                                                                               |
| ----------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `sqsMessagesReceived`                     | `<pipeline-name>.sqs.sqsMessagesReceived.count`                     | Number of messages successfully received from the Amazon SQS<br>queue.                                                    |
| `sqsMessagesDeleted`                      | `<pipeline-name>.sqs.sqsMessagesDeleted.count`                      | Number of messages successfully deleted after processing.                                                                 |
| `sqsMessagesFailed`                       | `<pipeline-name>.sqs.sqsMessagesFailed.count`                       | Number of messages that failed to process.                                                                                |
| `sqsMessagesDeleteFailed`                 | `<pipeline-name>.sqs.sqsMessagesDeleteFailed.count`                 | Number of messages that failed to delete from the queue.                                                                  |
| `sqsVisibilityTimeoutChangedCount`        | `<pipeline-name>.sqs.sqsVisibilityTimeoutChangedCount.count`        | Number of times visibility timeout was successfully extended (when<br>`visibility_duplication_protection` is<br>enabled). |
| `sqsVisibilityTimeoutChangeFailedCount`   | `<pipeline-name>.sqs.sqsVisibilityTimeoutChangeFailedCount.count`   | Number of times visibility timeout extension failed.                                                                      |
| `sqsMessageDelay`                         | `<pipeline-name>.sqs.sqsMessageDelay.*`                             | Timer measuring the delay between when a message was sent and when it<br>was first received by the pipeline.              |
| `acknowledgementSetCallbackCounter`       | `<pipeline-name>.sqs.acknowledgementSetCallbackCounter.count`       | Number of acknowledgment callbacks processed.                                                                             |
| `sqsMessagesDeletedWithoutAcknowledgment` | `<pipeline-name>.sqs.sqsMessagesDeletedWithoutAcknowledgment.count` | Number of messages deleted without end-to-end acknowledgment (when<br>`acknowledgments` is `false`).                      |
| `sqsMessagesAccessDenied`                 | `<pipeline-name>.sqs.sqsMessagesAccessDenied.count`                 | Number of access denied (403) errors when polling the<br>queue.                                                           |
| `sqsMessagesThrottled`                    | `<pipeline-name>.sqs.sqsMessagesThrottled.count`                    | Number of throttling errors when polling the queue.                                                                       |
| `sqsResourceNotFound`                     | `<pipeline-name>.sqs.sqsResourceNotFound.count`                     | Number of resource not found (404) errors – typically indicates<br>the queue does not exist.                              |

### Recommended alarm configurations

| Alarm                       | Metric                          | Threshold             | Description                                                                                                                              |
| --------------------------- | ------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Message processing failures | `sqsMessagesFailed.count`       | > 0 for 5 minutes     | Messages are failing to process. Check message format and codec<br>configuration.                                                        |
| Message delete failures     | `sqsMessagesDeleteFailed.count` | > 0 for 5 minutes     | Messages processed successfully but cannot be deleted. Check IAM<br>permissions for `sqs:DeleteMessage` and<br>`sqs:DeleteMessageBatch`. |
| Access denied errors        | `sqsMessagesAccessDenied.count` | > 0 for 1 minute      | Pipeline cannot access the Amazon SQS queue. Verify IAM role<br>permissions and trust policy.                                            |
| Queue not found             | `sqsResourceNotFound.count`     | > 0 for 1 minute      | The configured Amazon SQS queue does not exist or was<br>deleted.                                                                        |
| Throttling                  | `sqsMessagesThrottled.count`    | > 10 for 5 minutes    | Amazon SQS is throttling the pipeline. Reduce `workers` or<br>increase `poll_delay`.                                                     |
| Stalled ingestion           | `sqsMessagesReceived.count`     | = 0 for 15 minutes    | Pipeline is not receiving messages. Verify queue has messages and<br>IAM permissions.                                                    |
| High message delay          | `sqsMessageDelay.avg`           | > 300s for 10 minutes | Messages are sitting in the queue too long before being processed.<br>Consider increasing `workers`.                                     |

## Limitations

Consider the following limitations when setting up an OpenSearch Ingestion pipeline with an
Amazon SQS source:

- **FIFO queues are not supported** – Only
  standard Amazon SQS queues can be used.
- **Message size limit** – Amazon SQS messages
  have a maximum body size of 256 KB. Messages exceeding this limit must use the
  [Amazon SQS Extended Client Library](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-s3-messages.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-s3-messages.md"), which stores the payload in
  Amazon S3 – this is not supported by the Amazon SQS source plugin.
- **At-least-once delivery** – Standard Amazon SQS
  queues provide at-least-once delivery. Combined with the visibility timeout
  mechanism, this means rare duplicate processing is possible. Use
  `document_id` in the sink configuration to ensure idempotent
  writes.
- **Regional constraints** – The Amazon SQS queue
  and OpenSearch Ingestion pipeline must be in the same AWS Region.
- **Ordering** – Standard Amazon SQS queues do not
  guarantee message ordering. If your use case requires strict ordering, consider
  Amazon Kinesis Data Streams as the source instead.

## Troubleshooting

| Issue                                          | Possible cause                                       | Resolution                                                                                                                                                                          |
| ---------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pipeline is not receiving messages             | Queue is empty or permissions are insufficient       | Verify the queue has messages available (not in-flight) and that the<br>pipeline role has `sqs:ReceiveMessage` permission.                                                          |
| `AccessDenied` errors in pipeline logs         | IAM role lacks required Amazon SQS permissions       | Verify the pipeline role has `sqs:ReceiveMessage`,<br>`sqs:DeleteMessage`, `sqs:DeleteMessageBatch`,<br>and `sqs:ChangeMessageVisibility` permissions on the queue<br>ARN.          |
| Duplicate documents in OpenSearch              | Visibility timeout is too short causing reprocessing | Increase `visibility_timeout` in the queue configuration or<br>enable `visibility_duplication_protection`. Use<br>`document_id` with `messageId` metadata for<br>idempotent writes. |
| Messages going to Amazon SQS dead-letter queue | Repeated processing failures                         | Check pipeline logs for codec parsing errors. Verify the message body<br>format matches the configured `codec`.                                                                     |
| High latency                                   | Large message volume or insufficient compute         | Increase pipeline OCUs (Ingestion OpenSearch Compute Units). For<br>multiple high-volume queues, consider separate pipelines or increase<br>`workers` per queue.                    |
| `KMS.AccessDeniedException` errors             | Encrypted queue without AWS KMS permissions          | Add `kms:Decrypt` permission to the pipeline role for the<br>AWS KMS key used to encrypt the queue.                                                                                 |
| Messages retained in queue despite errors      | `on_error` is set to `retain_messages`               | This is the default safe behavior. Messages will be retried until the<br>DLQ threshold is reached. Set `on_error: "delete_messages"`<br>only if data loss on error is acceptable.   |
