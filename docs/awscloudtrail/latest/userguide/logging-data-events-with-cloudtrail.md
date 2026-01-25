# Logging data events

This section describes how to log data events using the [CloudTrail console](#logging-data-events-console "#logging-data-events-console") and [AWS CLI](#creating-data-event-selectors-with-the-AWS-CLI "#creating-data-event-selectors-with-the-AWS-CLI").

By default, trails and event data stores do not log data events. Additional charges apply for data events. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

Data events provide information about the resource operations performed on or in a
resource. These are also known as _data plane
operations_. Data events are often high-volume activities.

Example data events include:

- [Amazon S3 object-level API activity](../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events "../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events") (for example,
  `GetObject`, `DeleteObject`, and
  `PutObject` API operations) on objects in S3 buckets.
- AWS Lambda function execution activity (the `Invoke`
  API).
- CloudTrail [`PutAuditEvents`](../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md "../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md") activity on a [CloudTrail Lake channel](query-event-data-store-integration.md "query-event-data-store-integration.md")
  that is used to log events from outside AWS.
- Amazon SNS [`Publish`](../../../sns/latest/api/API_Publish.md "../../../sns/latest/api/API_Publish.md") and [`PublishBatch`](../../../sns/latest/api/API_PublishBatch.md "../../../sns/latest/api/API_PublishBatch.md") API operations on topics.
  You can use advanced event selectors to create fine-grained selectors, which help you control costs by only logging the specific events of interest for your use cases.
  For example, you can use advanced event selectors to log specific API calls by adding a filter on the `eventName` field. For more information, see [Filtering data events by using advanced event
  selectors](filtering-data-events.md "filtering-data-events.md").

###### Note

The events that are logged by your trails are available in Amazon EventBridge. For example, if
you choose to log data events for S3 objects but not management events, your
trail processes and logs only data events for the specified S3 objects. The data events
for these S3 objects are available in Amazon EventBridge. For more information, see [AWS service events delivered via CloudTrail](../../../eventbridge/latest/userguide/eb-service-event-cloudtrail.md "../../../eventbridge/latest/userguide/eb-service-event-cloudtrail.md") in the _Amazon EventBridge User Guide_ and the [AWS Events Reference](../../../eventbridge/latest/ref/welcome.md "../../../eventbridge/latest/ref/welcome.md").

###### Contents

- [Data events](logging-data-events-with-cloudtrail.md#logging-data-events "logging-data-events-with-cloudtrail.md#logging-data-events")
  - [Data events supported by AWS CloudTrail](logging-data-events-with-cloudtrail.md#w2aac21c31c19c11 "logging-data-events-with-cloudtrail.md#w2aac21c31c19c11")
  - [Examples: Logging data events for
    Amazon S3 objects](logging-data-events-with-cloudtrail.md#logging-data-events-examples "logging-data-events-with-cloudtrail.md#logging-data-events-examples")
  - [Logging
    data events for S3 objects in other AWS accounts](logging-data-events-with-cloudtrail.md#logging-data-events-for-s3-resources-in-other-accounts "logging-data-events-with-cloudtrail.md#logging-data-events-for-s3-resources-in-other-accounts")

- [Read-only and write-only events](logging-data-events-with-cloudtrail.md#read-write-events-data "logging-data-events-with-cloudtrail.md#read-write-events-data")
- [Logging data events with the AWS Management Console](logging-data-events-with-cloudtrail.md#logging-data-events-console "logging-data-events-with-cloudtrail.md#logging-data-events-console")
- [Logging data events
  with the AWS Command Line Interface](logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI")
  - [Logging data events for
    trails with the AWS CLI](logging-data-events-with-cloudtrail.md#logging-data-events-CLI-trail-examples "logging-data-events-with-cloudtrail.md#logging-data-events-CLI-trail-examples")
    - [Log data events for trails by using
      advanced event selectors](logging-data-events-with-cloudtrail.md#creating-data-event-selectors-advanced "logging-data-events-with-cloudtrail.md#creating-data-event-selectors-advanced")
    - [Log all Amazon S3 events for an Amazon S3
      bucket by using advanced event selectors](logging-data-events-with-cloudtrail.md#creating-data-adv-event-selectors-CLI-s3 "logging-data-events-with-cloudtrail.md#creating-data-adv-event-selectors-CLI-s3")
    - [Log Amazon S3 on AWS Outposts
      events by using advanced event selectors](logging-data-events-with-cloudtrail.md#creating-data-event-selectors-CLI-outposts "logging-data-events-with-cloudtrail.md#creating-data-event-selectors-CLI-outposts")
    - [Log events by using basic
      event selectors](logging-data-events-with-cloudtrail.md#creating-data-event-selectors-basic "logging-data-events-with-cloudtrail.md#creating-data-event-selectors-basic")

  - [Logging data events for event data stores with the AWS CLI](logging-data-events-with-cloudtrail.md#logging-data-events-CLI-eds-examples "logging-data-events-with-cloudtrail.md#logging-data-events-CLI-eds-examples")
    - [Include all Amazon S3
      events for a specific bucket](logging-data-events-with-cloudtrail.md#creating-data-adv-event-selectors-CLI-s3-eds "logging-data-events-with-cloudtrail.md#creating-data-adv-event-selectors-CLI-s3-eds")
    - [Include Amazon S3 on
      AWS Outposts events](logging-data-events-with-cloudtrail.md#creating-data-event-selectors-CLI-outposts-eds "logging-data-events-with-cloudtrail.md#creating-data-event-selectors-CLI-outposts-eds")

- [Filtering data events by using advanced event
  selectors](filtering-data-events.md "filtering-data-events.md")
  - [How CloudTrail evaluates multiple conditions for a field](filtering-data-events.md#filtering-data-events-conditions "filtering-data-events.md#filtering-data-events-conditions")
    - [Example showing multiple conditions for the resources.ARN field](filtering-data-events.md#filtering-data-events-conditions-ex "filtering-data-events.md#filtering-data-events-conditions-ex")

  - [AWS CLI examples for filtering data events](filtering-data-events.md#filtering-data-events-examples "filtering-data-events.md#filtering-data-events-examples")
    - [Example 1: Filtering on the eventName field](filtering-data-events.md#filtering-data-events-eventname "filtering-data-events.md#filtering-data-events-eventname")
    - [Example 2: Filtering on the resources.ARN and userIdentity.arn fields](filtering-data-events.md#filtering-data-events-useridentityarn "filtering-data-events.md#filtering-data-events-useridentityarn")
    - [Example 3: Filtering on
      the resources.type and eventName fields to exclude
      individual objects deleted by an Amazon S3 DeleteObjects event](filtering-data-events.md#filtering-data-events-deleteobjects "filtering-data-events.md#filtering-data-events-deleteobjects")

- [Aggregating data events](aggregating-data-events.md "aggregating-data-events.md")
  - [Enabling aggregations for data events using the console](aggregating-data-events.md#aggregating-data-events-console "aggregating-data-events.md#aggregating-data-events-console")
  - [Enabling aggregations for data events using the AWS CLI](aggregating-data-events.md#aggregating-data-events-cli "aggregating-data-events.md#aggregating-data-events-cli")
    - [Example: API_ACTIVITY aggregated event](aggregating-data-events.md#aggregating-data-events-api-activity-example "aggregating-data-events.md#aggregating-data-events-api-activity-example")
    - [Example: RESOURCE_ACCESS aggregated event](aggregating-data-events.md#aggregating-data-events-resource-access-example "aggregating-data-events.md#aggregating-data-events-resource-access-example")

- [Logging data events for AWS Config
  compliance](logging-data-events-with-cloudtrail.md#config-data-events-best-practices "logging-data-events-with-cloudtrail.md#config-data-events-best-practices")
- [Logging data events with the AWS
  SDKs](logging-data-events-with-cloudtrail.md#logging-data-events-with-the-AWS-SDKs "logging-data-events-with-cloudtrail.md#logging-data-events-with-the-AWS-SDKs")

## Data events

The following table shows the resource types available for trails and event
data stores. The **Resource type (console)** column shows the appropriate selection in the console.
The **resources.type value** column shows the
`resources.type` value that you would specify to include data
events of that type in your trail or event data store using the AWS CLI or CloudTrail APIs.

For trails, you can use basic or advanced event selectors to log data events for Amazon S3 objects in general purpose buckets, Lambda functions, and DynamoDB tables (shown in the first three rows of the table). You can use only advanced event selectors to log the resource types shown in the remaining rows.

For event data stores, you can use only advanced event selectors to include data events.

### Data events supported by AWS CloudTrail

| AWS service                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Resource type (console)                             | resources.type value                               |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------- |
| Amazon RDS                                  | [Amazon RDS API activity](../../../AmazonRDS/latest/AuroraUserGuide/logging-using-cloudtrail-data-api.md#logging-using-cloudtrail-data-api.including-excluding-cloudtrail-events "../../../AmazonRDS/latest/AuroraUserGuide/logging-using-cloudtrail-data-api.md#logging-using-cloudtrail-data-api.including-excluding-cloudtrail-events") on a DB Cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **RDS Data API<br>• DB Cluster**                    | `AWS::RDS::DBCluster`                              |
| Amazon S3                                   | [Amazon S3 object-level API activity](../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events "../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events") (for example, `GetObject`,<br>`DeleteObject`, and `PutObject` API<br>operations) on objects in general purpose buckets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **S3**                                              | `AWS::S3::Object`                                  |
| Amazon S3                                   | [Amazon S3 API activity](../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events "../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events") on access points.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **S3 Access Point**                                 | `AWS::S3::AccessPoint`                             |
| Amazon S3                                   | [Amazon S3 object-level API activity](../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events "../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events") (for example, `GetObject`,<br>`DeleteObject`, and `PutObject` API operations) on objects in directory buckets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **S3 Express**                                      | `AWS::S3Express::Object`                           |
| Amazon S3                                   | [Amazon S3 Object Lambda access points API activity](../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events "../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events"), such as calls to<br>`CompleteMultipartUpload` and<br>`GetObject`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **S3 Object Lambda**                                | `AWS::S3ObjectLambda::AccessPoint`                 |
| Amazon S3                                   | Amazon FSx API activity on volumes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **FSx Volume**                                      | `AWS::FSx::Volume`                                 |
| Amazon S3 Tables                            | Amazon S3 API activity on [tables](../../../AmazonS3/latest/userguide/s3-tables-create.md "../../../AmazonS3/latest/userguide/s3-tables-create.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **S3 table**                                        | `AWS::S3Tables::Table`                             |
| Amazon S3 Tables                            | Amazon S3 API activity on [table buckets](../../../AmazonS3/latest/userguide/s3-tables-buckets.md "../../../AmazonS3/latest/userguide/s3-tables-buckets.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **S3 table bucket**                                 | `AWS::S3Tables::TableBucket`                       |
| Amazon S3 Vectors                           | Amazon S3 API activity on [vector buckets](../../../AmazonS3/latest/userguide/s3-vectors-buckets.md "../../../AmazonS3/latest/userguide/s3-vectors-buckets.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **S3 vector bucket**                                | `AWS::S3Vectors::VectorBucket`                     |
| Amazon S3 Vectors                           | Amazon S3 API activity on [vector indexes](../../../AmazonS3/latest/userguide/s3-vectors-indexes.md "../../../AmazonS3/latest/userguide/s3-vectors-indexes.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **S3 vector index**                                 | `AWS::S3Vectors::Index`                            |
| Amazon S3 on Outposts                       | [Amazon S3 on Outposts object-level API activity](../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events "../../../AmazonS3/latest/userguide/cloudtrail-logging-s3-info.md#cloudtrail-data-events").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **S3 Outposts**                                     | `AWS::S3Outposts::Object`                          |
| Amazon SNS                                  | Amazon SNS [`Publish`](../../../sns/latest/api/API_Publish.md "../../../sns/latest/api/API_Publish.md") API operations on platform endpoints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **SNS platform endpoint**                           | `AWS::SNS::PlatformEndpoint`                       |
| Amazon SNS                                  | Amazon SNS [`Publish`](../../../sns/latest/api/API_Publish.md "../../../sns/latest/api/API_Publish.md") and [`PublishBatch`](../../../sns/latest/api/API_PublishBatch.md "../../../sns/latest/api/API_PublishBatch.md") API operations on topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **SNS topic**                                       | `AWS::SNS::Topic`                                  |
| Amazon SQS                                  | [Amazon SQS API activity](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-logging-using-cloudtrail.md#sqs-data-events-in-cloud-trail "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-logging-using-cloudtrail.md#sqs-data-events-in-cloud-trail") on messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **SQS**                                             | `AWS::SQS::Queue`                                  |
| AWS Supply Chain                            | AWS Supply Chain API activity on an instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Supply Chain**                                    | `AWS::SCN::Instance`                               |
| Amazon SWF                                  | [Amazon SWF API activity](../../../amazonswf/latest/developerguide/ct-logging.md#cloudtrail-data-events "../../../amazonswf/latest/developerguide/ct-logging.md#cloudtrail-data-events") on [domains](../../../amazonswf/latest/developerguide/swf-dev-domains.md "../../../amazonswf/latest/developerguide/swf-dev-domains.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **SWF domain**                                      | `AWS::SWF::Domain`                                 |
| AWS AppConfig                               | [AWS AppConfig API activity](../../../appconfig/latest/userguide/logging-using-cloudtrail.md#appconfig-data-events-cloudtrail "../../../appconfig/latest/userguide/logging-using-cloudtrail.md#appconfig-data-events-cloudtrail") for configuration operations such as calls to `StartConfigurationSession` and `GetLatestConfiguration`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **AWS AppConfig**                                   | `AWS::AppConfig::Configuration`                    |
| AWS AppSync                                 | [AWS AppSync API activity](../../../appsync/latest/devguide/cloudtrail-logging.md#cloudtrail-data-events "../../../appsync/latest/devguide/cloudtrail-logging.md#cloudtrail-data-events") on AppSync GraphQL APIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **AppSync GraphQL**                                 | `AWS::AppSync::GraphQLApi`                         |
| Amazon Aurora DSQL                          | Amazon Aurora DSQL API activity on cluster resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Amazon Aurora DSQL**                              | `AWS::DSQL::Cluster`                               |
| AWS B2B Data Interchange                    | B2B Data Interchange API activity for Transformer operations such as calls to `GetTransformerJob` and `StartTransformerJob`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **B2B Data Interchange**                            | `AWS::B2BI::Transformer`                           |
| AWS Backup                                  | AWS Backup Search Data API activity on search jobs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **AWS Backup Search Data APIs**                     | `AWS::Backup::SearchJob`                           |
| Amazon Bedrock                              | [Amazon Bedrock API activity](../../../bedrock/latest/userguide/logging-using-cloudtrail.md#service-name-data-events-cloudtrail "../../../bedrock/latest/userguide/logging-using-cloudtrail.md#service-name-data-events-cloudtrail") on an agent alias.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Bedrock agent alias**                             | `AWS::Bedrock::AgentAlias`                         |
| Amazon Bedrock                              | Amazon Bedrock API activity on async invocations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Bedrock async invoke**                            | `AWS::Bedrock::AsyncInvoke`                        |
| Amazon Bedrock                              | Amazon Bedrock API activity on a flow alias.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **Bedrock flow alias**                              | `AWS::Bedrock::FlowAlias`                          |
| Amazon Bedrock                              | Amazon Bedrock API activity on guardrails.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Bedrock guardrail**                               | `AWS::Bedrock::Guardrail`                          |
| Amazon Bedrock                              | Amazon Bedrock API activity on inline agents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Bedrock Invoke Inline-Agent**                     | `AWS::Bedrock::InlineAgent`                        |
| Amazon Bedrock                              | [Amazon Bedrock API activity](../../../bedrock/latest/userguide/logging-using-cloudtrail.md#service-name-data-events-cloudtrail "../../../bedrock/latest/userguide/logging-using-cloudtrail.md#service-name-data-events-cloudtrail") on a knowledge base.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **Bedrock knowledge base**                          | `AWS::Bedrock::KnowledgeBase`                      |
| Amazon Bedrock                              | Amazon Bedrock API activity on models.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Bedrock model**                                   | `AWS::Bedrock::Model`                              |
| Amazon Bedrock                              | Amazon Bedrock API activity on prompts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Bedrock prompt**                                  | `AWS::Bedrock::PromptVersion`                      |
| Amazon Bedrock                              | Amazon Bedrock API activity on sessions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Bedrock session**                                 | `AWS::Bedrock::Session`                            |
| Amazon Bedrock                              | Amazon Bedrock API activity on flow executions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Bedrock flow execution**                          | `AWS::Bedrock::FlowExecution`                      |
| Amazon Bedrock                              | Amazon Bedrock API activity on an automated reasoning policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Bedrock automated reasoning policy**              | `AWS::Bedrock::AutomatedReasoningPolicy`           |
| Amazon Bedrock                              | Amazon Bedrock API activity on an automated reasoning policy version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Bedrock automated reasoning policy version**      | `AWS::Bedrock::AutomatedReasoningPolicyVersion`    |
| Amazon Bedrock                              | Amazon Bedrock data automation project API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Bedrock Data Automation project**                 | `AWS::Bedrock::DataAutomationProject`              |
| Amazon Bedrock                              | Bedrock data automation invocation API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Bedrock Data Automation invocation**              | `AWS::Bedrock::DataAutomationInvocation`           |
| Amazon Bedrock                              | Amazon Bedrock data automation profile API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Bedrock Data Automation profile**                 | `AWS::Bedrock::DataAutomationProfile`              |
| Amazon Bedrock                              | Amazon Bedrock blueprint API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Bedrock blueprint**                               | `AWS::Bedrock::Blueprint`                          |
| Amazon Bedrock                              | Amazon Bedrock Code-Interpreter API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Bedrock-AgentCore Code-Interpreter**              | `AWS::BedrockAgentCore::CodeInterpreter`           |
| Amazon Bedrock                              | Amazon Bedrock Browser API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Bedrock-AgentCore Browser**                       | `AWS::BedrockAgentCore::Browser`                   |
| Amazon Bedrock                              | Amazon Bedrock Workload Identity API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Bedrock-AgentCore Workload Identity**             | `AWS::BedrockAgentCore::WorkloadIdentity`          |
| Amazon Bedrock                              | Amazon Bedrock Workload Identity Directory API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Bedrock-AgentCore Workload Identity Directory**   | `AWS::BedrockAgentCore::WorkloadIdentityDirectory` |
| Amazon Bedrock                              | Amazon Bedrock Token Vault API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Bedrock-AgentCore Token Vault**                   | `AWS::BedrockAgentCore::TokenVault`                |
| Amazon Bedrock                              | Amazon Bedrock APIKey CredentialProvider API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Bedrock-AgentCore APIKey CredentialProvider**     | `AWS::BedrockAgentCore::APIKeyCredentialProvider`  |
| Amazon Bedrock                              | Amazon Bedrock Runtime API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Bedrock-AgentCore Runtime**                       | `AWS::BedrockAgentCore::Runtime`                   |
| Amazon Bedrock                              | Amazon Bedrock Runtime-Endpoint API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Bedrock-AgentCore Runtime-Endpoint**              | `AWS::BedrockAgentCore::RuntimeEndpoint`           |
| Amazon Bedrock                              | Amazon Bedrock Gateway API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Bedrock-AgentCore Gateway**                       | `AWS::BedrockAgentCore::Gateway`                   |
| Amazon Bedrock                              | Amazon Bedrock Memory API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Bedrock-AgentCore Memory**                        | `AWS::BedrockAgentCore::Memory`                    |
| Amazon Bedrock                              | Amazon Bedrock Oauth2 CredentialProvider API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Bedrock-AgentCore Oauth2 CredentialProvider**     | `AWS::BedrockAgentCore::OAuth2CredentialProvider`  |
| Amazon Bedrock                              | Amazon Bedrock Browser-Custom API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Bedrock-AgentCore Browser-Custom**                | `AWS::BedrockAgentCore::BrowserCustom`             |
| Amazon Bedrock                              | Amazon Bedrock Code-Interpreter-Custom API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Bedrock-AgentCore Code-Interpreter-Custom**       | `AWS::BedrockAgentCore::CodeInterpreterCustom`     |
| Amazon Bedrock                              | Amazon Bedrock Tool API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Bedrock Tool**                                    | `AWS::Bedrock::Tool`                               |
| AWS Cloud Map                               | [AWS Cloud Map API activity](../../../cloud-map/latest/dg/cloudtrail-data-events.md "../../../cloud-map/latest/dg/cloudtrail-data-events.md") on a [namespace](../../../cloud-map/latest/api/API_Namespace.md "../../../cloud-map/latest/api/API_Namespace.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **AWS Cloud Map namespace**                         | `AWS::ServiceDiscovery::Namespace`                 |
| AWS Cloud Map                               | [AWS Cloud Map API activity](../../../cloud-map/latest/dg/cloudtrail-data-events.md "../../../cloud-map/latest/dg/cloudtrail-data-events.md") on a [service](../../../cloud-map/latest/api/API_Service.md "../../../cloud-map/latest/api/API_Service.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **AWS Cloud Map service**                           | `AWS::ServiceDiscovery::Service`                   |
| Amazon CloudFront                           | CloudFront API activity on a [KeyValueStore](../../../cloudfront/latest/APIReference/API_KeyValueStore.md "../../../cloudfront/latest/APIReference/API_KeyValueStore.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **CloudFront KeyValueStore**                        | `AWS::CloudFront::KeyValueStore`                   |
| AWS CloudTrail                              | CloudTrail [`PutAuditEvents`](../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md "../../../awscloudtraildata/latest/APIReference/API_PutAuditEvents.md") activity on a [CloudTrail Lake<br>channel](query-event-data-store-integration.md "query-event-data-store-integration.md") that is used to log events from outside<br>AWS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **CloudTrail channel**                              | `AWS::CloudTrail::Channel`                         |
| Amazon CloudWatch                           | [Amazon CloudWatch API activity](../../../AmazonCloudWatch/latest/monitoring/logging_cw_api_calls.md#CloudWatch-data-plane-events "../../../AmazonCloudWatch/latest/monitoring/logging_cw_api_calls.md#CloudWatch-data-plane-events") on metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **CloudWatch metric**                               | `AWS::CloudWatch::Metric`                          |
| Amazon CloudWatch Network Flow Monitor      | Amazon CloudWatch Network Flow Monitor API activity on monitors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Network Flow Monitor monitor**                    | `AWS::NetworkFlowMonitor::Monitor`                 |
| Amazon CloudWatch Network Flow Monitor      | Amazon CloudWatch Network Flow Monitor API activity on scopes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Network Flow Monitor scope**                      | `AWS::NetworkFlowMonitor::Scope`                   |
| Amazon CloudWatch RUM                       | Amazon CloudWatch RUM API activity on app monitors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **RUM app monitor**                                 | `AWS::RUM::AppMonitor`                             |
| Amazon CodeGuru Profiler                    | CodeGuru Profiler API activity on profiling groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **CodeGuru Profiler profiling group**               | `AWS::CodeGuruProfiler::ProfilingGroup`            |
| Amazon CodeWhisperer                        | Amazon CodeWhisperer API activity on a customization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **CodeWhisperer customization**                     | `AWS::CodeWhisperer::Customization`                |
| Amazon CodeWhisperer                        | Amazon CodeWhisperer API activity on a profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **CodeWhisperer**                                   | `AWS::CodeWhisperer::Profile`                      |
| Amazon Cognito                              | Amazon Cognito API activity on Amazon Cognito [identity pools](../../../cognito/latest/developerguide/amazon-cognito-info-in-cloudtrail.md#identity-pools-cloudtrail-events "../../../cognito/latest/developerguide/amazon-cognito-info-in-cloudtrail.md#identity-pools-cloudtrail-events").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **Cognito Identity Pools**                          | `AWS::Cognito::IdentityPool`                       |
| AWS Data Exchange                           | AWS Data Exchange API activity on assets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **Data Exchange asset**                             | `AWS::DataExchange::Asset`                         |
| Amazon Data Firehose                        | Amazon Data Firehose delivery stream API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Amazon Data Firehose**                            | `AWS::KinesisFirehose::DeliveryStream`             |
| AWS Deadline Cloud                          | [Deadline Cloud](../../../deadline-cloud/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../deadline-cloud/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events") API activity on fleets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Deadline Cloud fleet**                            | `AWS::Deadline::Fleet`                             |
| AWS Deadline Cloud                          | [Deadline Cloud](../../../deadline-cloud/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../deadline-cloud/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events") API activity on jobs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Deadline Cloud job**                              | `AWS::Deadline::Job`                               |
| AWS Deadline Cloud                          | [Deadline Cloud](../../../deadline-cloud/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../deadline-cloud/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events") API activity on queues.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Deadline Cloud queue**                            | `AWS::Deadline::Queue`                             |
| AWS Deadline Cloud                          | [Deadline Cloud](../../../deadline-cloud/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../deadline-cloud/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events") API activity on workers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Deadline Cloud worker**                           | `AWS::Deadline::Worker`                            |
| Amazon DynamoDB                             | [Amazon DynamoDB item-level API activity](../../../amazondynamodb/latest/developerguide/logging-using-cloudtrail.md#ddb-data-plane-events-in-cloudtrail "../../../amazondynamodb/latest/developerguide/logging-using-cloudtrail.md#ddb-data-plane-events-in-cloudtrail") on tables (for example,<br>`PutItem`, `DeleteItem`, and `UpdateItem`<br>API operations).<br>NoteFor tables with streams enabled, the `resources` field in the data event contains both `AWS::DynamoDB::Stream` and `AWS::DynamoDB::Table`. If you specify `AWS::DynamoDB::Table`<br>for the `resources.type`, it will log both DynamoDB table and DynamoDB streams events by default.<br>To exclude [streams events](../../../amazondynamodb/latest/developerguide/logging-using-cloudtrail.md#ddb-data-plane-events-in-cloudtrail "../../../amazondynamodb/latest/developerguide/logging-using-cloudtrail.md#ddb-data-plane-events-in-cloudtrail"), add a filter on the `eventName` field. | **DynamoDB**                                        | `AWS::DynamoDB::Table`                             |
| Amazon DynamoDB                             | [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/logging-using-cloudtrail.md#ddb-data-plane-events-in-cloudtrail "../../../amazondynamodb/latest/developerguide/logging-using-cloudtrail.md#ddb-data-plane-events-in-cloudtrail") API activity on streams.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **DynamoDB Streams**                                | `AWS::DynamoDB::Stream`                            |
| Amazon Elastic Block Store                  | [Amazon Elastic Block Store (EBS)](../../../ebs/latest/userguide/logging-ebs-apis-using-cloudtrail.md "../../../ebs/latest/userguide/logging-ebs-apis-using-cloudtrail.md") direct APIs, such as<br>`PutSnapshotBlock`, `GetSnapshotBlock`, and<br>`ListChangedBlocks` on Amazon EBS snapshots.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Amazon EBS direct APIs**                          | `AWS::EC2::Snapshot`                               |
| Amazon Elastic Compute Cloud                | Amazon EC2 instance connect endpoint API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **EC2 instance connect endpoint**                   | `AWS::EC2::InstanceConnectEndpoint`                |
| Amazon Elastic Container Service            | Amazon Elastic Container Service API activity on a container instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **ECS container instance**                          | `AWS::ECS::ContainerInstance`                      |
| Amazon Elastic Kubernetes Service           | Amazon Elastic Kubernetes Service API activity on dashboards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Amazon Elastic Kubernetes Service dashboard**     | `AWS::EKS::Dashboard`                              |
| Amazon EMR                                  | [Amazon EMR API activity](../../../emr/latest/ManagementGuide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../emr/latest/ManagementGuide/logging-using-cloudtrail.md#cloudtrail-data-events") on a write-ahead log workspace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **EMR write-ahead log workspace**                   | `AWS::EMRWAL::Workspace`                           |
| AWS End User Messaging SMS                  | [AWS End User Messaging SMS](../../../sms-voice/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../sms-voice/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events") API activity on origination identities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **SMS Voice origination identity**                  | `AWS::SMSVoice::OriginationIdentity`               |
| AWS End User Messaging SMS                  | [AWS End User Messaging SMS](../../../sms-voice/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../sms-voice/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events") API activity on messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **SMS Voice message**                               | `AWS::SMSVoice::Message`                           |
| AWS End User Messaging Social               | [AWS End User Messaging Social](../../../social-messaging/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../social-messaging/latest/userguide/logging-using-cloudtrail.md#cloudtrail-data-events") API activity on phone number IDs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Social-Messaging Phone Number Id**                | `AWS::SocialMessaging::PhoneNumberId`              |
| AWS End User Messaging Social               | AWS End User Messaging Social API activity on Waba IDs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Social-Messaging Waba ID**                        | `AWS::SocialMessaging::WabaId`                     |
| Amazon FinSpace                             | [Amazon FinSpace](../../../finspace/latest/userguide/logging-cloudtrail-events.md#finspace-dataplane-events "../../../finspace/latest/userguide/logging-cloudtrail-events.md#finspace-dataplane-events") API activity on environments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **FinSpace**                                        | `AWS::FinSpace::Environment`                       |
| Amazon GameLift Streams                     | Amazon GameLift Streams [streaming API activity](../../../gameliftstreams/latest/developerguide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../gameliftstreams/latest/developerguide/logging-using-cloudtrail.md#cloudtrail-data-events") on applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **GameLift Streams application**                    | `AWS::GameLiftStreams::Application`                |
| Amazon GameLift Streams                     | Amazon GameLift Streams [streaming API activity](../../../gameliftstreams/latest/developerguide/logging-using-cloudtrail.md#cloudtrail-data-events "../../../gameliftstreams/latest/developerguide/logging-using-cloudtrail.md#cloudtrail-data-events") on stream groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **GameLift Streams stream group**                   | `AWS::GameLiftStreams::StreamGroup`                |
| AWS Glue                                    | AWS Glue API activity on tables that were created by Lake Formation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Lake Formation**                                  | `AWS::Glue::Table`                                 |
| Amazon GuardDuty                            | Amazon GuardDuty API activity for a [detector](../../../guardduty/latest/ug/logging-using-cloudtrail.md#guardduty-data-events-in-cloudtrail "../../../guardduty/latest/ug/logging-using-cloudtrail.md#guardduty-data-events-in-cloudtrail").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **GuardDuty detector**                              | `AWS::GuardDuty::Detector`                         |
| AWS HealthImaging                           | AWS HealthImaging API activity on data stores.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **MedicalImaging data store**                       | `AWS::MedicalImaging::Datastore`                   |
| AWS HealthImaging                           | AWS HealthImaging image set API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **MedicalImaging image set**                        | `AWS::MedicalImaging::Imageset`                    |
| AWS IoT                                     | [AWS IoT API activity](../../../greengrass/v2/developerguide/logging-using-cloudtrail.md#greengrass-data-events-cloudtrail "../../../greengrass/v2/developerguide/logging-using-cloudtrail.md#greengrass-data-events-cloudtrail") on [certificates](../../../iot/latest/developerguide/x509-client-certs.md "../../../iot/latest/developerguide/x509-client-certs.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **IoT certificate**                                 | `AWS::IoT::Certificate`                            |
| AWS IoT                                     | [AWS IoT API activity](../../../greengrass/v2/developerguide/logging-using-cloudtrail.md#greengrass-data-events-cloudtrail "../../../greengrass/v2/developerguide/logging-using-cloudtrail.md#greengrass-data-events-cloudtrail") on [things](../../../iot/latest/developerguide/thing-registry.md "../../../iot/latest/developerguide/thing-registry.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **IoT thing**                                       | `AWS::IoT::Thing`                                  |
| AWS IoT Greengrass Version 2                | [Greengrass API activity](../../../greengrass/v2/developerguide/logging-using-cloudtrail.md#greengrass-data-events-cloudtrail "../../../greengrass/v2/developerguide/logging-using-cloudtrail.md#greengrass-data-events-cloudtrail") from a Greengrass core device on a component version.<br>NoteGreengrass doesn't log access denied events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **IoT Greengrass component version**                | `AWS::GreengrassV2::ComponentVersion`              |
| AWS IoT Greengrass Version 2                | [Greengrass API activity](../../../greengrass/v2/developerguide/logging-using-cloudtrail.md#greengrass-data-events-cloudtrail "../../../greengrass/v2/developerguide/logging-using-cloudtrail.md#greengrass-data-events-cloudtrail") from a Greengrass core device on a deployment.<br>NoteGreengrass doesn't log access denied events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **IoT Greengrass deployment**                       | `AWS::GreengrassV2::Deployment`                    |
| AWS IoT SiteWise                            | [IoT SiteWise API activity](../../../iot-sitewise/latest/userguide/logging-using-cloudtrail.md#service-name-data-events-cloudtrail "../../../iot-sitewise/latest/userguide/logging-using-cloudtrail.md#service-name-data-events-cloudtrail") on [assets](../../../iot-sitewise/latest/APIReference/API_CreateAsset.md "../../../iot-sitewise/latest/APIReference/API_CreateAsset.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **IoT SiteWise asset**                              | `AWS::IoTSiteWise::Asset`                          |
| AWS IoT SiteWise                            | [IoT SiteWise API activity](../../../iot-sitewise/latest/userguide/logging-using-cloudtrail.md#service-name-data-events-cloudtrail "../../../iot-sitewise/latest/userguide/logging-using-cloudtrail.md#service-name-data-events-cloudtrail") on [time series](../../../iot-sitewise/latest/APIReference/API_DescribeTimeSeries.md "../../../iot-sitewise/latest/APIReference/API_DescribeTimeSeries.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **IoT SiteWise time series**                        | `AWS::IoTSiteWise::TimeSeries`                     |
| AWS IoT SiteWise Assistant                  | Sitewise Assistant API activity on conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Sitewise Assistant conversation**                 | `AWS::SitewiseAssistant::Conversation`             |
| AWS IoT TwinMaker                           | IoT TwinMaker API activity on an [entity](../../../iot-twinmaker/latest/apireference/API_CreateEntity.md "../../../iot-twinmaker/latest/apireference/API_CreateEntity.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **IoT TwinMaker entity**                            | `AWS::IoTTwinMaker::Entity`                        |
| AWS IoT TwinMaker                           | IoT TwinMaker API activity on a [workspace](../../../iot-twinmaker/latest/apireference/API_CreateWorkspace.md "../../../iot-twinmaker/latest/apireference/API_CreateWorkspace.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **IoT TwinMaker workspace**                         | `AWS::IoTTwinMaker::Workspace`                     |
| Amazon Kendra Intelligent Ranking           | Amazon Kendra Intelligent Ranking API activity on [rescore execution plans](../../../kendra/latest/dg/cloudtrail-intelligent-ranking.md#cloud-trail-intelligent-ranking-log-entry "../../../kendra/latest/dg/cloudtrail-intelligent-ranking.md#cloud-trail-intelligent-ranking-log-entry").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Kendra Ranking**                                  | `AWS::KendraRanking::ExecutionPlan`                |
| Amazon Keyspaces (for Apache Cassandra)     | [Amazon Keyspaces API activity](../../../keyspaces/latest/devguide/logging-using-cloudtrail.md#keyspaces-in-cloudtrail-dml "../../../keyspaces/latest/devguide/logging-using-cloudtrail.md#keyspaces-in-cloudtrail-dml") on a table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Cassandra table**                                 | `AWS::Cassandra::Table`                            |
| Amazon Keyspaces (for Apache Cassandra)     | Amazon Keyspaces (for Apache Cassandra) API activity on Cassandra CDC streams.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Cassandra CDC streams**                           | `AWS::Cassandra::Stream`                           |
| Amazon Kinesis Data Streams                 | Kinesis Data Streams API activity on [streams](../../../streams/latest/dev/working-with-streams.md "../../../streams/latest/dev/working-with-streams.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Kinesis stream**                                  | `AWS::Kinesis::Stream`                             |
| Amazon Kinesis Data Streams                 | Kinesis Data Streams API activity on [stream consumers](../../../streams/latest/dev/building-consumers.md "../../../streams/latest/dev/building-consumers.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Kinesis stream consumer**                         | `AWS::Kinesis::StreamConsumer`                     |
| Amazon Kinesis Video Streams                | Kinesis Video Streams API activity on video streams, such as calls to `GetMedia` and `PutMedia`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Kinesis video stream**                            | `AWS::KinesisVideo::Stream`                        |
| Amazon Kinesis Video Streams                | Kinesis Video Streams video signaling channel API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Kinesis video signaling channel**                 | `AWS::KinesisVideo::SignalingChannel`              |
| AWS Lambda                                  | AWS Lambda function execution activity (the `Invoke` API).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Lambda**                                          | `AWS::Lambda::Function`                            |
| Amazon Location Maps                        | Amazon Location Maps API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Geo Maps**                                        | `AWS::GeoMaps::Provider`                           |
| Amazon Location Places                      | Amazon Location Places API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Geo Places**                                      | `AWS::GeoPlaces::Provider`                         |
| Amazon Location Routes                      | Amazon Location Routes API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Geo Routes**                                      | `AWS::GeoRoutes::Provider`                         |
| Amazon Machine Learning                     | Machine Learning API activity on ML models.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Maching Learning MlModel**                        | `AWS::MachineLearning::MlModel`                    |
| Amazon Managed Blockchain                   | Amazon Managed Blockchain API activity on a network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Managed Blockchain network**                      | `AWS::ManagedBlockchain::Network`                  |
| Amazon Managed Blockchain                   | [Amazon Managed Blockchain](../../../managed-blockchain/latest/ethereum-dev/logging-using-cloudtrail.md#ethereum-jsonrpc-logging "../../../managed-blockchain/latest/ethereum-dev/logging-using-cloudtrail.md#ethereum-jsonrpc-logging") JSON-RPC calls on Ethereum nodes, such as<br>`eth_getBalance` or<br>`eth_getBlockByNumber`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Managed Blockchain**                              | `AWS::ManagedBlockchain::Node`                     |
| Amazon Managed Blockchain Query             | Amazon Managed Blockchain Query API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Managed Blockchain Query**                        | `AWS::ManagedBlockchainQuery::QueryAPI`            |
| Amazon Managed Workflows for Apache Airflow | Amazon MWAA API activity on environments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **Managed Apache Airflow**                          | `AWS::MWAA::Environment`                           |
| Amazon Neptune Graph                        | Data API activities, for example queries, algorithms, or vector search, on a Neptune Graph.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Neptune Graph**                                   | `AWS::NeptuneGraph::Graph`                         |
| Amazon One Enterprise                       | Amazon One Enterprise API activity on a UKey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Amazon One UKey**                                 | `AWS::One::UKey`                                   |
| Amazon One Enterprise                       | Amazon One Enterprise API activity on users.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **Amazon One User**                                 | `AWS::One::User`                                   |
| AWS Payment Cryptography                    | AWS Payment Cryptography API activity on aliases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Payment Cryptography Alias**                      | `AWS::PaymentCryptography::Alias`                  |
| AWS Payment Cryptography                    | AWS Payment Cryptography API activity on keys.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Payment Cryptography Key**                        | `AWS::PaymentCryptography::Key`                    |
| Amazon Pinpoint                             | Amazon Pinpoint API activity on mobile targeting applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Mobile Targeting Application**                    | `AWS::Pinpoint::App`                               |
| AWS Private CA                              | AWS Private CA Connector for Active Directory API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **AWS Private CA Connector for Active Directory**   | `AWS::PCAConnectorAD::Connector`                   |
| AWS Private CA                              | AWS Private CA Connector for SCEP API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **AWS Private CA Connector for SCEP**               | `AWS::PCAConnectorSCEP::Connector`                 |
| Amazon Q Apps                               | Data API activity on [Amazon Q Apps](../../../amazonq/latest/qbusiness-ug/purpose-built-qapps.md "../../../amazonq/latest/qbusiness-ug/purpose-built-qapps.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Amazon Q Apps**                                   | `AWS::QApps::QApp`                                 |
| Amazon Q Apps                               | Data API activity on Amazon Q App sessions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Amazon Q App Session**                            | `AWS::QApps::QAppSession`                          |
| Amazon Q Business                           | [Amazon Q Business API activity](../../../amazonq/latest/business-use-dg/logging-using-cloudtrail.md#service-name-data-plane-events-cloudtrail "../../../amazonq/latest/business-use-dg/logging-using-cloudtrail.md#service-name-data-plane-events-cloudtrail") on an application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Amazon Q Business application**                   | `AWS::QBusiness::Application`                      |
| Amazon Q Business                           | [Amazon Q Business API activity](../../../amazonq/latest/business-use-dg/logging-using-cloudtrail.md#service-name-data-plane-events-cloudtrail "../../../amazonq/latest/business-use-dg/logging-using-cloudtrail.md#service-name-data-plane-events-cloudtrail") on a data source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Amazon Q Business data source**                   | `AWS::QBusiness::DataSource`                       |
| Amazon Q Business                           | [Amazon Q Business API activity](../../../amazonq/latest/business-use-dg/logging-using-cloudtrail.md#service-name-data-plane-events-cloudtrail "../../../amazonq/latest/business-use-dg/logging-using-cloudtrail.md#service-name-data-plane-events-cloudtrail") on an index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **Amazon Q Business index**                         | `AWS::QBusiness::Index`                            |
| Amazon Q Business                           | [Amazon Q Business API activity](../../../amazonq/latest/business-use-dg/logging-using-cloudtrail.md#service-name-data-plane-events-cloudtrail "../../../amazonq/latest/business-use-dg/logging-using-cloudtrail.md#service-name-data-plane-events-cloudtrail") on a web experience.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Amazon Q Business web experience**                | `AWS::QBusiness::WebExperience`                    |
| Amazon Q Business                           | Amazon Q Business integration API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Amazon Q Business integration**                   | `AWS::QBusiness::Integration`                      |
| Amazon Q Developer                          | Amazon Q Developer API activity on an integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Q Developer integration**                         | `AWS::QDeveloper::Integration`                     |
| Amazon Q Developer                          | [Amazon Q Developer API activity](../../../AmazonCloudWatch/latest/monitoring/logging_cw_api_calls.md#Q-Developer-Investigations-Cloudtrail "../../../AmazonCloudWatch/latest/monitoring/logging_cw_api_calls.md#Q-Developer-Investigations-Cloudtrail") on operational investigations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **AIOps Investigation Group**                       | `AWS::AIOps::InvestigationGroup`                   |
| Amazon Quick Suite                          | Amazon Quick Suite API activity on an action connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **AWS QuickSuite Actions**                          | `AWS::Quicksight::ActionConnector`                 |
| Amazon Quick Suite                          | Amazon Quick Suite Flow API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **AWS::QuickSight::Flow**                           | `AWS::QuickSight::Flow`                            |
| Amazon Quick Suite                          | Amazon Quick Suite FlowSession API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **AWS::QuickSight::FlowSession**                    | `AWS::QuickSight::FlowSession`                     |
| Amazon SageMaker AI                         | Amazon SageMaker AI [`InvokeEndpointWithResponseStream`](../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpointWithResponseStream.md "../../../sagemaker/latest/APIReference/API_runtime_InvokeEndpointWithResponseStream.md") activity on endpoints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **SageMaker AI endpoint**                           | `AWS::SageMaker::Endpoint`                         |
| Amazon SageMaker AI                         | Amazon SageMaker AI API activity on feature stores.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **SageMaker AI feature store**                      | `AWS::SageMaker::FeatureGroup`                     |
| Amazon SageMaker AI                         | Amazon SageMaker AI API activity on [experiment trial components](../../../sagemaker/latest/dg/experiments-monitoring.md "../../../sagemaker/latest/dg/experiments-monitoring.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **SageMaker AI metrics experiment trial component** | `AWS::SageMaker::ExperimentTrialComponent`         |
| Amazon SageMaker AI                         | Amazon SageMaker AI MLflow API activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **SageMaker MLflow**                                | `AWS::SageMaker::MlflowTrackingServer`             |
| AWS Signer                                  | Signer API activity on signing jobs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Signer signing job**                              | `AWS::Signer::SigningJob`                          |
| AWS Signer                                  | Signer API activity on signing profiles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Signer signing profile**                          | `AWS::Signer::SigningProfile`                      |
| Amazon Simple Email Service                 | Amazon Simple Email Service (Amazon SES) API activity on configuration sets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **SES configuration set**                           | `AWS::SES::ConfigurationSet`                       |
| Amazon Simple Email Service                 | Amazon Simple Email Service (Amazon SES) API activity on email identities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **SES identity**                                    | `AWS::SES::EmailIdentity`                          |
| Amazon Simple Email Service                 | Amazon Simple Email Service (Amazon SES) API activity on templates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **SES template**                                    | `AWS::SES::Template`                               |
| Amazon SimpleDB                             | Amazon SimpleDB API activity on domains.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **SimpleDB domain**                                 | `AWS::SDB::Domain`                                 |
| AWS Step Functions                          | [Step Functions API activity](../../../step-functions/latest/dg/procedure-cloud-trail.md#cloudtrail-data-events "../../../step-functions/latest/dg/procedure-cloud-trail.md#cloudtrail-data-events") on activities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Step Functions**                                  | `AWS::StepFunctions::Activity`                     |
| AWS Step Functions                          | [Step Functions API activity](../../../step-functions/latest/dg/procedure-cloud-trail.md#cloudtrail-data-events "../../../step-functions/latest/dg/procedure-cloud-trail.md#cloudtrail-data-events") on state machines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Step Functions state machine**                    | `AWS::StepFunctions::StateMachine`                 |
| AWS Systems Manager                         | [Systems Manager API activity](../../../systems-manager/latest/userguide/monitoring-cloudtrail-logs.md#cloudtrail-data-events "../../../systems-manager/latest/userguide/monitoring-cloudtrail-logs.md#cloudtrail-data-events") on control channels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Systems Manager**                                 | `AWS::SSMMessages::ControlChannel`                 |
| AWS Systems Manager                         | Systems Manager API activity on impact assessments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **SSM Impact Assessment**                           | `AWS::SSM::ExecutionPreview`                       |
| AWS Systems Manager                         | [Systems Manager API activity](../../../systems-manager/latest/userguide/monitoring-cloudtrail-logs.md#cloudtrail-data-events "../../../systems-manager/latest/userguide/monitoring-cloudtrail-logs.md#cloudtrail-data-events") on managed nodes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Systems Manager managed node**                    | `AWS::SSM::ManagedNode`                            |
| Amazon Timestream                           | Amazon Timestream [`Query`](../../../timestream/latest/developerguide/API_query_Query.md "../../../timestream/latest/developerguide/API_query_Query.md") API activity on databases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Timestream database**                             | `AWS::Timestream::Database`                        |
| Amazon Timestream                           | Amazon Timestream API activity on regional endpoints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Timestream regional endpoint**                    | `AWS::Timestream::RegionalEndpoint`                |
| Amazon Timestream                           | Amazon Timestream [`Query`](../../../timestream/latest/developerguide/API_query_Query.md "../../../timestream/latest/developerguide/API_query_Query.md") API activity on tables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Timestream table**                                | `AWS::Timestream::Table`                           |
| Amazon Verified Permissions                 | Amazon Verified Permissions API activity on a policy store.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Amazon Verified Permissions**                     | `AWS::VerifiedPermissions::PolicyStore`            |
| Amazon WorkSpaces Thin Client               | WorkSpaces Thin Client API activity on a Device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Thin Client Device**                              | `AWS::ThinClient::Device`                          |
| Amazon WorkSpaces Thin Client               | WorkSpaces Thin Client API activity on an Environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Thin Client Environment**                         | `AWS::ThinClient::Environment`                     |
| AWS X-Ray                                   | [X-Ray API activity](../../../xray/latest/devguide/xray-api-cloudtrail.md#cloudtrail-data-events "../../../xray/latest/devguide/xray-api-cloudtrail.md#cloudtrail-data-events") on [traces](../../../xray/latest/devguide/xray-concepts.md#xray-concepts-traces "../../../xray/latest/devguide/xray-concepts.md#xray-concepts-traces").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **X-Ray trace**                                     | `AWS::XRay::Trace`                                 |
| Amazon AIDevOps                             | AIDevOps API activity on agent spaces.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Agent Space**                                     | `AWS::AIDevOps::AgentSpace`                        |
| Amazon AIDevOps                             | AIDevOps API activity on associations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **AIDevOps association**                            | `AWS::AIDevOps::Association`                       |
| Amazon AIDevOps                             | AIDevOps API activity on operator app teams.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **AIDevOps operator app team**                      | `AWS::AIDevOps::OperatorAppTeam`                   |
| Amazon AIDevOps                             | AIDevOps API activity on pipeline metadata.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **AIDevOps Pipelines Metadata**                     | `AWS::AIDevOps::PipelineMetadata`                  |
| Amazon AIDevOps                             | AIDevOps API activity on services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **AIDevOps service**                                | `AWS::AIDevOps::Service`                           |
| Amazon Bedrock                              | Bedrock API activity on advanced optimize prompt jobs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **AdvancedOptimizePromptJob**                       | `AWS::Bedrock::AdvancedOptimizePromptJob`          |
| Amazon Bedrock AgentCore                    | Bedrock AgentCore API activity on evaluators.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Bedrock-AgentCore Evaluator**                     | `AWS::BedrockAgentCore::Evaluator`                 |
| Amazon Cost Optimization                    | CloudOptimization API activity on profiles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **CloudOptimization Profile**                       | `AWS::CloudOptimization::Profile`                  |
| Amazon Cost Optimization                    | CloudOptimization API activity on recommendations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **CloudOptimization Recommendation**                | `AWS::CloudOptimization::Recommendation`           |
| Amazon GuardDuty                            | GuardDuty API activity on malware scans.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **GuardDuty malware scan**                          | `AWS::GuardDuty::MalwareScan`                      |
| Amazon NovaAct                              | Amazon NovaAct API activity on workflow definitions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Workflow definition**                             | `AWS::NovaAct::WorkflowDefinition`                 |
| Amazon NovaAct                              | Amanzon NovaAct API activity on workflow runs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | **Workflow run**                                    | `AWS::NovaAct::WorkflowRun`                        |
| Amazon Redshift                             | Redshift API activity on clusters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Amazon Redshift Cluster**                         | `AWS::Redshift::Cluster`                           |
| Amazon Support                              | SupportAccess API activity on tenants.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **SupportAccess tenant**                            | `AWS::SupportAccess::Tenant`                       |
| Amazon Support                              | SupportAccess API activity on trusting accounts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | **SupportAccess trusting account**                  | `AWS::SupportAccess::TrustingAccount`              |
| Amazon Support                              | SupportAccess API activity on trusting roles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **SupportAccess trusting role**                     | `AWS::SupportAccess::TrustingRole`                 |
| Amazon Transform                            | Transform API activity on agent instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Transform agent instance**                        | `AWS::Transform::AgentInstance`                    |
| Amazon Transform Custom                     | Transform Custom API activity on campaigns.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **Transform-Custom campaign**                       | `AWS::TransformCustom::Campaign`                   |
| Amazon Transform Custom                     | Transform Custom API activity on conversations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Transform-Custom conversation**                   | `AWS::TransformCustom::Conversation`               |
| Amazon Transform Custom                     | Transform Custom API activity on knowledge items.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | **Transform-Custom knowledge item**                 | `AWS::TransformCustom::KnowledgeItem`              |
| Amazon Transform Custom                     | Transform Custom API activity on packages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **Transform-Custom package**                        | `AWS::TransformCustom::Package`                    |

To record CloudTrail data
events, you must explicitly add each resource type for which you
want to collect activity. For more information, see [Creating a trail with the CloudTrail console](cloudtrail-create-a-trail-using-the-console-first-time.md "cloudtrail-create-a-trail-using-the-console-first-time.md") and [Create an event data store for CloudTrail
events with the console](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md").

On a single-Region trail or event data store, you can log data events only for resources that you can
access in that Region. Though S3 buckets are global, AWS Lambda functions and DynamoDB
tables are regional.

Additional charges apply for logging data events. For CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

### Examples: Logging data events for

Amazon S3 objects

###### Logging data

events for all S3 objects in an S3 bucket

The following example demonstrates how logging works when you configure
logging of all data events for an S3 bucket named
`amzn-s3-demo-bucket`. In this example, the CloudTrail user
specified an empty prefix, and the option to log both **Read**
and **Write** data events.

1. A user uploads an object to `amzn-s3-demo-bucket`.
2. The `PutObject` API operation is an Amazon S3 object-level API. It
   is recorded as a data event in CloudTrail. Because the CloudTrail user specified an S3
   bucket with an empty prefix, events that occur on any object in that bucket
   are logged. The trail or event data store processes and logs the
   event.
3. Another user uploads an object to `amzn-s3-demo-bucket2`.
4. The `PutObject` API operation occurred on an object in an S3
   bucket that wasn't specified for the trail or event data store. The trail or
   event data store doesn't log the event.

###### Logging

data events for specific S3 objects

The following example demonstrates how logging works when you configure a
trail or event data store to log events for specific S3 objects. In this
example, the CloudTrail user specified an S3 bucket named
`amzn-s3-demo-bucket3`, with the prefix
`my-images`, and the option to log only
**Write** data events.

1. A user deletes an object that begins with the `my-images`
   prefix in the bucket, such as
   `arn:aws:s3:::amzn-s3-demo-bucket3/my-images/example.jpg`.
2. The `DeleteObject` API operation is an Amazon S3 object-level API.
   It is recorded as a **Write** data event in CloudTrail. The event
   occurred on an object that matches the S3 bucket and prefix specified in the
   trail or event data store. The trail or event data store processes and logs
   the event.
3. Another user deletes an object with a different prefix in the S3 bucket,
   such as `arn:aws:s3:::amzn-s3-demo-bucket3/my-videos/example.avi`.
4. The event occurred on an object that doesn't match the prefix specified in
   your trail or event data store. The trail or event data store doesn't log
   the event.
5. A user calls the `GetObject` API operation for the object,
   `arn:aws:s3:::amzn-s3-demo-bucket3/my-images/example.jpg`.
6. The event occurred on a bucket and prefix that are specified in the trail
   or event data store, but `GetObject` is a read-type Amazon S3
   object-level API. It is recorded as a **Read**
   data event in CloudTrail, and the trail or event data store is not configured to
   log **Read** events. The trail or event data
   store doesn't log the event.

###### Note

For trails, if you are logging data events for specific Amazon S3 buckets, we
recommend you do not use an Amazon S3 bucket for which you are logging data events to
receive log files that you have specified in the data events section for your
trail. Using the same Amazon S3 bucket causes your trail to log a data event each
time log files are delivered to your Amazon S3 bucket. Log files are aggregated
events delivered at intervals, so this is not a 1:1 ratio of event to log file;
the event is logged in the next log file. For example, when CloudTrail delivers logs,
the `PutObject` event occurs on the S3 bucket. If the S3 bucket is
also specified in the data events section, the trail processes and logs the
`PutObject` event as a data event. That action is another
`PutObject` event, and the trail processes and logs the event
again.

To avoid logging data events for the Amazon S3 bucket where you receive log files
if you configure a trail to log all Amazon S3 data events in your AWS account,
consider configuring delivery of log files to an Amazon S3 bucket that belongs to
another AWS account. For more information, see [Receiving CloudTrail log files from multiple accounts](cloudtrail-receive-logs-from-multiple-accounts.md "cloudtrail-receive-logs-from-multiple-accounts.md").

### Logging

data events for S3 objects in other AWS accounts

When you configure your trail to log data events, you can also specify S3 objects
that belong to other AWS accounts. When an event occurs on a specified object,
CloudTrail evaluates whether the event matches any trails in each account. If the event
matches the settings for a trail, the trail processes and logs the event for that
account. Generally, both API callers and resource owners can receive events.

If you own an S3 object and you specify it in your trail, your trail logs events
that occur on the object in your account. Because you own the object, your trail
also logs events when other accounts call the object.

If you specify an S3 object in your trail, and another account owns the object,
your trail only logs events that occur on that object in your account. Your trail
doesn't log events that occur in other accounts.

###### Example: Logging data events for an Amazon S3 object for two AWS

accounts

The following example shows how two AWS accounts configure CloudTrail to log
events for the same S3 object.

1. In your account, you want your trail to log data events for all objects in
   your S3 bucket named `amzn-s3-demo-bucket`. You configure the trail by
   specifying the S3 bucket with an empty object prefix.
2. Bob has a separate account that has been granted access to the S3 bucket.
   Bob also wants to log data events for all objects in the same S3 bucket. For
   his trail, he configures his trail and specifies the same S3 bucket with an
   empty object prefix.
3. Bob uploads an object to the S3 bucket with the `PutObject` API
   operation.
4. This event occurred in his account and it matches the settings for his
   trail. Bob's trail processes and logs the event.
5. Because you own the S3 bucket and the event matches the settings for your
   trail, your trail also processes and logs the same event. Because there are
   now two copies of the event (one logged in Bob's trail, and one logged in
   yours), CloudTrail charges for two copies of the data event.
6. You upload an object to the S3 bucket.
7. This event occurs in your account and it matches the settings for your
   trail. Your trail processes and logs the event.
8. Because the event didn't occur in Bob's account, and he doesn't own the S3
   bucket, Bob's trail doesn't log the event. CloudTrail charges for only one copy of
   this data event.

###### Example: Logging data events for all buckets, including an S3 bucket used by

two AWS accounts

The following example shows the logging behavior when **Select all S3
buckets in your account** is enabled for trails that collect data
events in an AWS account.

1. In your account, you want your trail to log data events for all S3
   buckets. You configure the trail by choosing **Read**
   events, **Write** events, or both for **All current
   and future S3 buckets** in **Data
   events**.
2. Bob has a separate account that has been granted access to an S3 bucket in
   your account. He wants to log data events for the bucket to which he has
   access. He configures his trail to get data events for all S3
   buckets.
3. Bob uploads an object to the S3 bucket with the `PutObject` API
   operation.
4. This event occurred in his account and it matches the settings for his
   trail. Bob's trail processes and logs the event.
5. Because you own the S3 bucket and the event matches the settings for your
   trail, your trail also processes and logs the event. Because there are now
   two copies of the event (one logged in Bob's trail, and one logged in
   yours), CloudTrail charges each account for a copy of the data event.
6. You upload an object to the S3 bucket.
7. This event occurs in your account and it matches the settings for your
   trail. Your trail processes and logs the event.
8. Because the event didn't occur in Bob's account, and he doesn't own the S3
   bucket, Bob's trail doesn't log the event. CloudTrail charges for only one copy of
   this data event in your account.
9. A third user, Mary, has access to the S3 bucket, and runs a
   `GetObject` operation on the bucket. She has a trail
   configured to log data events on all S3 buckets in her account. Because she
   is the API caller, CloudTrail logs a data event in her trail. Though Bob has
   access to the bucket, he is not the resource owner, so no event is logged in
   his trail this time. As the resource owner, you receive an event in your
   trail about the `GetObject` operation that Mary called. CloudTrail
   charges your account and Mary's account for each copy of the data event: one
   in Mary's trail, and one in yours.

## Read-only and write-only events

When you configure your trail or event data store to log data and management events, you can specify
whether you want read-only events, write-only events, or both.

- **Read**

**Read** events include API operations that read your
resources, but don't make changes. For example, read-only events include the
Amazon EC2 `DescribeSecurityGroups` and `DescribeSubnets` API
operations. These operations return only information about your Amazon EC2 resources
and don't change your configurations.

- **Write**

**Write** events include API operations that modify (or might
modify) your resources. For example, the Amazon EC2 `RunInstances` and
`TerminateInstances` API operations modify your instances.

###### Example: Logging read and write events for separate trails

The following example shows how you can configure trails to split log activity for
an account into separate S3 buckets: one bucket named amzn-s3-demo-bucket1 receives read-only events and a
second amzn-s3-demo-bucket2 receives write-only events.

1. You create a trail and choose the S3 bucket named `amzn-s3-demo-bucket1`
   to receive log files. You then update the trail to specify that you want
   **Read** management events and data events.
2. You create a second trail and choose the S3 bucket the
   `amzn-s3-demo-bucket2` to receive log files. You then update the
   trail to specify that you want **Write** management events and
   data events.
3. The Amazon EC2 `DescribeInstances` and `TerminateInstances`
   API operations occur in your account.
4. The `DescribeInstances` API operation is a read-only event and it
   matches the settings for the first trail. The trail logs and delivers the event
   to the `amzn-s3-demo-bucket1`.
5. The `TerminateInstances` API operation is a write-only event and it
   matches the settings for the second trail. The trail logs and delivers the event
   to the `amzn-s3-demo-bucket2` .

## Logging data events with the AWS Management Console

The following procedures describe how to an update existing event data store or trail
to log data events by using the AWS Management Console. For information about how to create an
event data store to log data events, see [Create an event data store for CloudTrail
events with the console](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md"). For information about how to
create a trail to log data events, see [Creating a trail with the console](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console").

For trails, the steps for logging data events differ based on whether you're using
advanced event selectors or basic event selectors. You can log data events for all
resource types using advanced event selectors, but if you use basic event
selectors you're limited to logging data events for Amazon S3 buckets and bucket objects,
AWS Lambda functions, and Amazon DynamoDB tables.

Use the following procedure to update an existing event data store to log data events. For more
information about using advanced event selectors, see [Filtering data events by using advanced event
selectors](filtering-data-events.md "filtering-data-events.md") in this
topic.

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, under **Lake**, choose **Event data stores**.
3. On the **Event data stores**
   page, choose the event data store you want to update.

###### Note

You can only enable data events on event data stores that contain CloudTrail events. You cannot enable data events
on CloudTrail event data stores for AWS Config configuration items, CloudTrail Insights events, or non-AWS events. 4. On the details page, in **Data events**,
choose **Edit**. 5. If you are not already logging data events, choose the **Data
events** check box. 6. For **Resource type**, choose the resource type on
which you want to log data events. 7. Choose a log selector template. You can choose a predefined template, or choose **Custom**
to define your own event collection conditions.

You can choose from the following predefined
templates:

    * **Log all events** –
     Choose this template to log all events.
    * **Log only read events** –
     Choose this template to log only read events.
     Read-only events are events that do not change the
     state of a resource, such as `Get*` or `Describe*`
     events.
    * **Log only write events** – Choose this template to log only write events.
     Write events add, change, or delete resources, attributes, or artifacts,
     such as `Put*`, `Delete*`, or `Write*` events.
    * **Log only AWS Management Console events** –
     Choose this template to log only events originating from the AWS Management Console.
    * **Exclude AWS service initiated events** – Choose this template to exclude
     AWS service events, which have an `eventType` of `AwsServiceEvent`,
     and events initiated with AWS service-linked roles (SLRs).

8. (Optional) In **Selector name**, enter a name to identify your selector. The selector name is a
   descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets". The selector name is listed as `Name` in the
   advanced event selector and is viewable if you expand the
   **JSON view**.
9. If you selected **Custom**, in **Advanced event selectors** build an expression based on the values of advanced event selector fields.

###### Note

Selectors don't support the use of wildcards like `*` . To match multiple values with a single condition,
you may use `StartsWith`, `EndsWith`, `NotStartsWith`, or `NotEndsWith` to explicitly match the beginning or end of the event field.

    1. Choose from the following fields.




    	* **`readOnly`**
    	 - `readOnly` can be set to
    	 **equals** a value of
    	 `true` or `false`. Read-only
    	 data events are events that do not change the state of a
    	 resource, such as `Get*` or
    	 `Describe*` events. Write events add,
    	 change, or delete resources, attributes, or artifacts,
    	 such as `Put*`, `Delete*`, or
    	 `Write*` events. To log both
    	 `read` and `write` events,
    	 don't add a `readOnly` selector.
    	* **`eventName`** -
    	 `eventName` can use any operator. You can
    	 use it to include or exclude any data event logged to
    	 CloudTrail, such as `PutBucket`,
    	 `GetItem`, or
    	 `GetSnapshotBlock`.
    	* **`eventSource`** – The event source to include or exclude. This field can use any operator.
    	* **eventType** – The event type to include or exclude. For example, you can set this field to
    	 **not equals** `AwsServiceEvent` to exclude
    	 [AWS service events](non-api-aws-service-events.md "non-api-aws-service-events.md"). For a list of event types,
    	 see [eventType](cloudtrail-event-reference-record-contents.md#ct-event-type "cloudtrail-event-reference-record-contents.md#ct-event-type") in
    	 [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").
    	* **sessionCredentialFromConsole** – Include or exclude events originating from an AWS Management Console session. This field can be set to **equals** or **not equals** with a value of
    	 `true`.
    	* **userIdentity.arn** – Include or exclude events for actions taken by specific IAM identities. For more information, see [CloudTrail userIdentity element](cloudtrail-event-reference-user-identity.md "cloudtrail-event-reference-user-identity.md").
    	* **`resources.ARN`** - You can use
    	 any operator with `resources.ARN`, but if you
    	 use **equals** or
    	 **does not equal**, the value must
    	 exactly match the ARN of a valid resource of the type
    	 you've specified in the template as the value of
    	 `resources.type`.


    	###### Note

    	You can't use the `resources.ARN` field to filter resource types that do not have ARNs.


    	For more information about the ARN formats of data event
    	 resources, see [Actions, resources, and condition
    	 keys for AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") in the *Service Authorization Reference*.
    2. For each field, choose **+ Condition** to
     add as many conditions as you need, up to a maximum of 500
     specified values for all conditions. For example, to exclude
     data events for two S3 buckets from data events that are logged
     on your event data store, you can set the field to
     **resources.ARN**, set the operator for
     **does not start with**, and then paste in
     an S3 bucket ARN for which you do
     not want to log events.


    To add the second S3 bucket, choose **+
     Condition**, and then repeat the preceding
     instruction, pasting in the ARN for or browsing for a different
     bucket.


    For information about how CloudTrail evaluates multiple conditions, see
     [How CloudTrail evaluates multiple conditions for a field](filtering-data-events.md#filtering-data-events-conditions "filtering-data-events.md#filtering-data-events-conditions").


    ###### Note

    You can have a maximum of 500 values for all selectors on
     an event data store. This includes arrays of multiple values for a
     selector such as `eventName`. If you have single
     values for all selectors, you can have a maximum of 500
     conditions added to a selector.
    3. Choose **+ Field** to add additional fields
     as required. To avoid errors, do not set conflicting or
     duplicate values for fields. For example, do not specify an ARN
     in one selector to be equal to a value, then specify that the
     ARN not equal the same value in another selector.

10. To add another resource type on which to log data events, choose
    **Add data event type**. Repeat steps 6 through
    this step to configure advanced event selectors for another resource type.
11. After you've reviewed and verified your choices, choose
    **Save changes**.

In the AWS Management Console, if your trail is using advanced event selectors, you can
choose from predefined templates that log all data events on a selected
resource. After you choose a log selector template, you can customize the
template to include only the data events you most want to see. For more
information about using advanced event selectors, see [Filtering data events by using advanced event
selectors](filtering-data-events.md "filtering-data-events.md") in this
topic.

1. On the **Dashboard** or **Trails**
   pages of the CloudTrail console, choose the trail you want to update.
2. On the details page, in **Data events**,
   choose **Edit**.
3. If you are not already logging data events, choose the **Data
   events** check box.
4. For **Resource type**, choose the resource type on
   which you want to log data events.
5. Choose a log selector template. You can choose a predefined template, or choose **Custom**
   to define your own event collection conditions.

You can choose from the following predefined
templates:

    * **Log all events** –
     Choose this template to log all events.
    * **Log only read events** –
     Choose this template to log only read events.
     Read-only events are events that do not change the
     state of a resource, such as `Get*` or `Describe*`
     events.
    * **Log only write events** – Choose this template to log only write events.
     Write events add, change, or delete resources, attributes, or artifacts,
     such as `Put*`, `Delete*`, or `Write*` events.
    * **Log only AWS Management Console events** –
     Choose this template to log only events originating from the AWS Management Console.
    * **Exclude AWS service initiated events** – Choose this template to exclude
     AWS service events, which have an `eventType` of `AwsServiceEvent`,
     and events initiated with AWS service-linked roles (SLRs).

###### Note

Choosing a predefined template for S3 buckets enables data event
logging for all buckets currently in your AWS account and any
buckets you create after you finish creating the trail. It also
enables logging of data event activity performed by any user or role
in your AWS account, even if that activity is performed on a
bucket that belongs to another AWS account.

If the trail applies only to one Region, choosing a predefined
template that logs all S3 buckets enables data event logging for all
buckets in the same Region as your trail and any buckets you create
later in that Region. It will not log data events for Amazon S3 buckets
in other Regions in your AWS account.

If you are creating a trail for all Regions, choosing a predefined
template for Lambda functions enables data event logging for all
functions currently in your AWS account, and any Lambda functions
you might create in any Region after you finish creating the trail.
If you are creating a trail for a single Region (for trails, this only can be done by using the
AWS CLI), this selection enables data event logging for all functions
currently in that Region in your AWS account, and any Lambda
functions you might create in that Region after you finish creating
the trail. It does not enable data event logging for Lambda functions
created in other Regions.

Logging data events for all functions also enables logging of data
event activity performed by any user or role in your AWS account,
even if that activity is performed on a function that belongs to
another AWS account. 6. (Optional) In **Selector name**, enter a name to identify your selector. The selector name is a
descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets". The selector name is listed as `Name` in the
advanced event selector and is viewable if you expand the
**JSON view**. 7. If you selected **Custom**, in **Advanced event selectors** build an expression based on the values of advanced event selector fields.

###### Note

Selectors don't support the use of wildcards like `*` . To match multiple values with a single condition,
you may use `StartsWith`, `EndsWith`, `NotStartsWith`, or `NotEndsWith` to explicitly match the beginning or end of the event field.

    1. Choose from the following fields.




    	* **`readOnly`**
    	 - `readOnly` can be set to
    	 **equals** a value of
    	 `true` or `false`. Read-only
    	 data events are events that do not change the state of a
    	 resource, such as `Get*` or
    	 `Describe*` events. Write events add,
    	 change, or delete resources, attributes, or artifacts,
    	 such as `Put*`, `Delete*`, or
    	 `Write*` events. To log both
    	 `read` and `write` events,
    	 don't add a `readOnly` selector.
    	* **`eventName`** -
    	 `eventName` can use any operator. You can
    	 use it to include or exclude any data event logged to
    	 CloudTrail, such as `PutBucket`,
    	 `GetItem`, or
    	 `GetSnapshotBlock`.
    	* **`eventSource`** – The event source to include or exclude. This field can use any operator.
    	* **eventType** – The event type to include or exclude. For example, you can set this field to
    	 **not equals** `AwsServiceEvent` to exclude
    	 [AWS service events](non-api-aws-service-events.md "non-api-aws-service-events.md"). For a list of event types,
    	 see [eventType](cloudtrail-event-reference-record-contents.md#ct-event-type "cloudtrail-event-reference-record-contents.md#ct-event-type") in
    	 [CloudTrail record contents for management, data, and network activity events](cloudtrail-event-reference-record-contents.md "cloudtrail-event-reference-record-contents.md").
    	* **sessionCredentialFromConsole** – Include or exclude events originating from an AWS Management Console session. This field can be set to **equals** or **not equals** with a value of
    	 `true`.
    	* **userIdentity.arn** – Include or exclude events for actions taken by specific IAM identities. For more information, see [CloudTrail userIdentity element](cloudtrail-event-reference-user-identity.md "cloudtrail-event-reference-user-identity.md").
    	* **`resources.ARN`** - You can use
    	 any operator with `resources.ARN`, but if you
    	 use **equals** or
    	 **does not equal**, the value must
    	 exactly match the ARN of a valid resource of the type
    	 you've specified in the template as the value of
    	 `resources.type`.


    	###### Note

    	You can't use the `resources.ARN` field to filter resource types that do not have ARNs.


    	For more information about the ARN formats of data event
    	 resources, see [Actions, resources, and condition
    	 keys for AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") in the *Service Authorization Reference*.
    2. For each field, choose **+ Condition** to
     add as many conditions as you need, up to a maximum of 500
     specified values for all conditions. For example, to exclude
     data events for two S3 buckets from data events that are logged
     on your event data store, you can set the field to
     **resources.ARN**, set the operator for
     **does not start with**, and then paste in
     an S3 bucket ARN for which you do
     not want to log events.


    To add the second S3 bucket, choose **+
     Condition**, and then repeat the preceding
     instruction, pasting in the ARN for or browsing for a different
     bucket.


    For information about how CloudTrail evaluates multiple conditions, see
     [How CloudTrail evaluates multiple conditions for a field](filtering-data-events.md#filtering-data-events-conditions "filtering-data-events.md#filtering-data-events-conditions").


    ###### Note

    You can have a maximum of 500 values for all selectors on
     an event data store. This includes arrays of multiple values for a
     selector such as `eventName`. If you have single
     values for all selectors, you can have a maximum of 500
     conditions added to a selector.
    3. Choose **+ Field** to add additional fields
     as required. To avoid errors, do not set conflicting or
     duplicate values for fields. For example, do not specify an ARN
     in one selector to be equal to a value, then specify that the
     ARN not equal the same value in another selector.

8. To add another resource type on which to log data events, choose
   **Add data event type**. Repeat steps 4 through
   this step to configure advanced event selectors for the resource type.
9. After you've reviewed and verified your choices, choose
   **Save changes**.

Use the following procedure to update an existing trail to log data events using basic event selectors.

1. Sign in to the AWS Management Console and open the CloudTrail console at
   [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. Open the **Trails** page of the CloudTrail console and
   choose the trail name.

###### Note

While you can edit an existing trail to log data events,
as a best practice, consider creating a separate trail specifically
for logging data events. 3. For **Data events**, choose
**Edit**. 4. For Amazon S3 buckets:

    1. For **Data event source**, choose
     **S3**.
    2. You can choose to log **All current and future S3
     buckets**, or you can specify individual buckets or
     functions. By default, data events are logged for all current
     and future S3 buckets.


    ###### Note

    Keeping the default **All current and future S3
     buckets** option enables data event logging for
     all buckets currently in your AWS account and any buckets
     you create after you finish creating the trail. It also
     enables logging of data event activity performed by any user
     or role in your AWS account, even if that activity is
     performed on a bucket that belongs to another AWS
     account.

    If you are creating a trail for a single Region (done by
     using the AWS CLI), selecting the **Select all S3
     buckets in your account** option enables data
     event logging for all buckets in the same Region as your
     trail and any buckets you create later in that Region. It
     will not log data events for Amazon S3 buckets in other Regions
     in your AWS account.
    3. If you leave the default, **All current and future S3
     buckets**, choose to log **Read**
     events, **Write** events, or both.
    4. To select individual buckets, empty the
     **Read** and **Write**
     check boxes for **All current and future S3
     buckets**. In **Individual bucket
     selection**, browse for a bucket on which to log
     data events. To find specific buckets, type a bucket prefix for
     the bucket you want. You can select multiple buckets in this
     window. Choose **Add bucket** to log data
     events for more buckets. Choose to log **Read**
     events, such as `GetObject`,
     **Write** events, such as
     `PutObject`, or both.


    This setting takes precedence over individual settings you
     configure for individual buckets. For example, if you specify
     logging **Read** events for all S3 buckets, and
     then choose to add a specific bucket for data event logging,
     **Read** is already selected for the bucket
     you added. You cannot clear the selection. You can only
     configure the option for **Write**.


    To remove a bucket from logging, choose
     **X**.

5. To add another resource type on which to log data events, choose
   **Add data event type**.
6. For Lambda functions:
   1. For **Data event source**, choose
      **Lambda**.
   2. In **Lambda function**, choose **All
      regions** to log all Lambda functions, or
      **Input function as ARN** to log data
      events on a specific function.

   To log data events for all Lambda functions in your AWS
   account, select **Log all current and future
   functions**. This setting takes precedence over
   individual settings you configure for individual functions. All
   functions are logged, even if all functions are not
   displayed.

   ###### Note

   If you
   are creating a trail for all Regions, this selection enables
   data event logging for all functions currently in your AWS
   account, and any Lambda functions you might create in any
   Region after you finish creating the trail. If you are
   creating a trail for a single Region (done by using the
   AWS CLI), this selection enables data event logging for all
   functions currently in that Region in your AWS account,
   and any Lambda functions you might create in that Region
   after you finish creating the trail. It does not enable data
   event logging for Lambda functions created in other
   Regions.

   Logging data events for all functions also enables logging
   of data event activity performed by any user or role in your
   AWS account, even if that activity is performed on a
   function that belongs to another AWS account. 3. If you choose **Input function as ARN**,
   enter the ARN of a Lambda function.

   ###### Note

   If you have more than 15,000 Lambda functions in your
   account, you cannot view or select all functions in the CloudTrail
   console when creating a trail. You can still select the
   option to log all functions, even if they are not displayed.
   If you want to log data events for specific functions, you
   can manually add a function if you know its ARN. You can
   also finish creating the trail in the console, and then use
   the AWS CLI and the **put-event-selectors**
   command to configure data event logging for specific Lambda
   functions. For more information, see [Managing trails with the AWS CLI](cloudtrail-additional-cli-commands.md "cloudtrail-additional-cli-commands.md").

7. To add another resource type on which to log data events, choose
   **Add data event type**.
8. For DynamoDB tables:
   1. For **Data event source**, choose
      **DynamoDB**.
   2. In **DynamoDB table selection**, choose
      **Browse** to select a table, or paste in
      the ARN of a DynamoDB table to which you have access. A DynamoDB table
      ARN uses the following format:

   ```
   arn:`partition`:dynamodb:`region`:`account_ID`:table/`table_name`
   ```

   To add another table, choose **Add row**, and
   browse for a table or paste in the ARN of a table to which you
   have access.

9. Choose **Save changes**.

## Logging data events

with the AWS Command Line Interface

You can configure your trails or event data stores to log data events using the AWS CLI.

###### Topics

- [Logging data events for
  trails with the AWS CLI](#logging-data-events-CLI-trail-examples "#logging-data-events-CLI-trail-examples")
- [Logging data events for event data stores with the AWS CLI](#logging-data-events-CLI-eds-examples "#logging-data-events-CLI-eds-examples")

### Logging data events for

trails with the AWS CLI

You can configure your trails to log management and data events using the AWS CLI.

###### Note

- Be aware that if your account is logging more than one copy of management events,
  you incur charges. There is always a charge for logging data events. For more
  information, see [AWS CloudTrail
  Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").
- You can use either advanced event selectors or basic event selectors, but not both.
  If you apply advanced event selectors to a trail, any existing basic event selectors are overwritten.
- If your trail uses basic event selectors, you can only log the following
  resource types:

      + `AWS::DynamoDB::Table`
      + `AWS::Lambda::Function`
      + `AWS::S3::Object`

  To log additional resource types, you'll need to use advanced event
  selectors. To convert a trail to advanced event selectors, run the **get-event-selectors** command to confirm the
  current event selectors, and then configure the advanced event selectors
  to match the coverage of the previous event selectors, then add
  selectors for any resource types for which you want to log data events.

- You can use advanced event selectors to filter based
  on the value of the [supported advanced event selector fields](filtering-data-events.md "filtering-data-events.md")supported advanced event selector fields, giving you the ability to log only the
  data events of interest. For more information about configuring these
  fields, see [AdvancedFieldSelector](../APIReference/API_AdvancedFieldSelector.md "../APIReference/API_AdvancedFieldSelector.md") in the _AWS CloudTrail API Reference_ and [Filtering data events by using advanced event
  selectors](filtering-data-events.md "filtering-data-events.md") in this
  guide.

To
see whether your trail is logging management and data events, run the [`get-event-selectors`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-selectors.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-selectors.html") command.

```
aws cloudtrail get-event-selectors --trail-name `TrailName`
```

The command returns the event selectors for the trail.

###### Topics

- [Log data events for trails by using
  advanced event selectors](#creating-data-event-selectors-advanced "#creating-data-event-selectors-advanced")
- [Log all Amazon S3 events for an Amazon S3
  bucket by using advanced event selectors](#creating-data-adv-event-selectors-CLI-s3 "#creating-data-adv-event-selectors-CLI-s3")
- [Log Amazon S3 on AWS Outposts
  events by using advanced event selectors](#creating-data-event-selectors-CLI-outposts "#creating-data-event-selectors-CLI-outposts")
- [Log events by using basic
  event selectors](#creating-data-event-selectors-basic "#creating-data-event-selectors-basic")

#### Log data events for trails by using

advanced event selectors

###### Note

If you apply advanced event selectors to a trail, any existing basic event selectors are overwritten. Before configuring advanced event selectors, run the
**get-event-selectors** command to confirm the
current event selectors, and then configure the advanced event selectors
to match the coverage of the previous event selectors, then add
selectors for any additional data events you want to log.

The following example creates custom advanced event selectors for a trail
named `TrailName` to include read and write management
events (by omitting the `readOnly` selector), `PutObject`
and `DeleteObject` data events for all Amazon S3 bucket/prefix
combinations except for a bucket named `amzn-s3-demo-bucket` and data
events for an AWS Lambda function named `MyLambdaFunction`. Because
these are custom advanced event selectors, each set of selectors has a
descriptive name. Note that a trailing slash is part of the ARN value for S3
buckets.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --advanced-event-selectors
'[
  {
    "Name": "Log readOnly and writeOnly management events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Management"] }
    ]
  },
  {
    "Name": "Log PutObject and DeleteObject events for all but one bucket",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventName", "Equals": ["PutObject","DeleteObject"] },
      { "Field": "resources.ARN", "NotStartsWith": ["arn:aws:s3:::amzn-s3-demo-bucket/"] }
    ]
  },
  {
    "Name": "Log data plane actions on MyLambdaFunction",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::Lambda::Function"] },
      { "Field": "resources.ARN", "Equals": ["arn:aws:lambda:us-east-2:111122223333:function/MyLambdaFunction"] }
    ]
  }
]'
```

The example returns the advanced event selectors that are configured for the
trail.

```
{
  "AdvancedEventSelectors": [
    {
      "Name": "Log readOnly and writeOnly management events",
      "FieldSelectors": [
        {
          "Field": "eventCategory",
          "Equals": [ "Management" ]
        }
      ]
    },
    {
      "Name": "Log PutObject and DeleteObject events for all but one bucket",
      "FieldSelectors": [
        {
          "Field": "eventCategory",
          "Equals": [ "Data" ]
        },
        {
          "Field": "resources.type",
          "Equals": [ "AWS::S3::Object" ]
        },
        {
          "Field": "resources.ARN",
          "NotStartsWith": [ "arn:aws:s3:::amzn-s3-demo-bucket/" ]
        },
      ]
    },
{
      "Name": "Log data plane actions on MyLambdaFunction",
      "FieldSelectors": [
        {
          "Field": "eventCategory",
          "Equals": [ "Data" ]
        },
        {
          "Field": "resources.type",
          "Equals": [ "AWS::Lambda::Function" ]
        },
        {
          "Field": "eventName",
          "Equals": [ "Invoke" ]
        },
        {
          "Field": "resources.ARN",
          "Equals": [ "arn:aws:lambda:us-east-2:111122223333:function/MyLambdaFunction" ]
        }
      ]
    }
  ],
  "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName`"
}
```

#### Log all Amazon S3 events for an Amazon S3

bucket by using advanced event selectors

###### Note

If you apply advanced event selectors to a trail, any existing basic event selectors are overwritten.

The following example shows how to configure your trail to include all data events
for all Amazon S3 objects in a specific S3 bucket. The value for S3 events for the
`resources.type` field is `AWS::S3::Object`. Because the
ARN values for S3 objects and S3 buckets are slightly different, you must add the
`StartsWith` operator for `resources.ARN` to capture all
events.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --region `region` \
--advanced-event-selectors \
'[
    {
            "Name": "S3EventSelector",
            "FieldSelectors": [
                { "Field": "eventCategory", "Equals": ["Data"] },
                { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
                { "Field": "resources.ARN", "StartsWith": ["arn:`partition`:s3:::`amzn-s3-demo-bucket`/"] }
            ]
        }
]'

```

The command returns the following example output.

```
{
    "TrailARN": "arn:aws:cloudtrail:`region`:`account_ID`:trail/`TrailName`",
    "AdvancedEventSelectors": [
        {
            "Name": "S3EventSelector",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::S3::Object"
                    ]
                },
                {
                    "Field": "resources.ARN",
                    "StartsWith": [
                        "arn:`partition`:s3:::`amzn-s3-demo-bucket`/"
                    ]
                }
            ]
        }
    ]
}
```

#### Log Amazon S3 on AWS Outposts

events by using advanced event selectors

###### Note

If you apply advanced event selectors to a trail, any existing basic event selectors are overwritten.

The following example shows how to configure your trail to include all data events
for all Amazon S3 on Outposts objects in your outpost.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --region `region` \
--advanced-event-selectors \
'[
    {
            "Name": "OutpostsEventSelector",
            "FieldSelectors": [
                { "Field": "eventCategory", "Equals": ["Data"] },
                { "Field": "resources.type", "Equals": ["AWS::S3Outposts::Object"] }
            ]
    }
]'
```

The command returns the following example output.

```
{
    "TrailARN": "arn:aws:cloudtrail:`region`:`account_ID`:trail/`TrailName`",
    "AdvancedEventSelectors": [
        {
            "Name": "OutpostsEventSelector",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::S3Outposts::Object"
                    ]
                }
            ]
        }
    ]
}
```

#### Log events by using basic

event selectors

The following is an example result of the **get-event-selectors**
command showing basic event selectors. By default, when you create a trail by using
the AWS CLI, a trail logs all management events. By default, trails do not log data
events.

```
{
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/TrailName",
    "EventSelectors": [
        {
            "IncludeManagementEvents": true,
            "DataResources": [],
            "ReadWriteType": "All"
        }
    ]
}
```

To configure your trail to log management and data events, run the [`put-event-selectors`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-event-selectors.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-event-selectors.html") command.

The following example shows how to use basic event selectors to configure your
trail to include all management and data events for the S3 objects in two S3 bucket prefixes. You can specify
from 1 to 5 event selectors for a trail. You can specify from 1 to 250 data
resources for a trail.

###### Note

The maximum number of S3 data resources is 250, if you choose to limit data
events by using basic event selectors.

```
aws cloudtrail put-event-selectors --trail-name `TrailName` --event-selectors '[{ "ReadWriteType": "All", "IncludeManagementEvents":true, "DataResources": [{ "Type": "AWS::S3::Object", "Values": ["arn:aws:s3:::`amzn-s3-demo-bucket1`/prefix", "arn:aws:s3:::`amzn-s3-demo-bucket2`;/prefix2"] }] }]'
```

The command returns the event selectors that are configured for the trail.

```
{
    "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/`TrailName`",
    "EventSelectors": [
        {
            "IncludeManagementEvents": true,
            "DataResources": [
                {
                    "Values": [
                        "arn:aws:s3:::`amzn-s3-demo-bucket1`/prefix",
                        "arn:aws:s3:::`amzn-s3-demo-bucket2`/prefix2",
                    ],
                    "Type": "AWS::S3::Object"
                }
            ],
            "ReadWriteType": "All"
        }
    ]
}
```

### Logging data events for event data stores with the AWS CLI

You can configure your event data stores to include data events using the AWS CLI. Use the [`create-event-data-store`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-event-data-store.html") command to create a new event data store to
log data events. Use the [`update-event-data-store`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-event-data-store.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-event-data-store.html") command to update the advanced event selectors for an existing event data store.

You configure advanced event selectors to log data events on an event data store. For a list of supported fields,
see [Filtering data events by using advanced event
selectors](filtering-data-events.md "filtering-data-events.md").

To
see whether your event data store includes data events, run the [`get-event-data-store`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-data-store.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-data-store.html") command.

```
aws cloudtrail get-event-data-store --event-data-store `EventDataStoreARN`
```

The command returns the settings for the event data store.

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLE492-301f-4053-ac5e-EXAMPLE6441aa",
    "Name": "ebs-data-events",
    "Status": "ENABLED",
    "AdvancedEventSelectors": [
        {
            "Name": "Log all EBS direct APIs on EBS snapshots",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::EC2::Snapshot"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": false,
    "BillingMode": "EXTENDABLE_RETENTION_PRICING",
    "RetentionPeriod": 366,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-11-04T15:57:33.701000+00:00",
    "UpdatedTimestamp": "2023-11-20T20:37:34.228000+00:00"
}
```

###### Topics

- [Include all Amazon S3
  events for a specific bucket](#creating-data-adv-event-selectors-CLI-s3-eds "#creating-data-adv-event-selectors-CLI-s3-eds")
- [Include Amazon S3 on
  AWS Outposts events](#creating-data-event-selectors-CLI-outposts-eds "#creating-data-event-selectors-CLI-outposts-eds")

#### Include all Amazon S3

events for a specific bucket

The following example shows how to create an event data store to include all data events
for all Amazon S3 objects in a specific general purpose S3 bucket and exclude AWS service events and events generated by the `bucket-scanner-role` `userIdentity`.
The value for S3 events for the
`resources.type` field is `AWS::S3::Object`. Because the
ARN values for S3 objects and S3 buckets are slightly different, you must add the
`StartsWith` operator for `resources.ARN` to capture all
events.

```
aws cloudtrail create-event-data-store --name "`EventDataStoreName`" --multi-region-enabled \
--advanced-event-selectors \
'[
    {
        "Name": "S3EventSelector",
        "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Data"] },
            { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
            { "Field": "resources.ARN", "StartsWith": ["arn:`partition`:s3:::`amzn-s3-demo-bucket`/"] },
            { "Field": "userIdentity.arn", "NotStartsWith": ["arn:aws:sts::123456789012:assumed-role/bucket-scanner-role"]},
            { "Field": "eventType","NotEquals": ["AwsServiceEvent"]}
        ]
    }
]'

```

The command returns the following example output.

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLE492-301f-4053-ac5e-EXAMPLE441aa",
    "Name": "EventDataStoreName",
    "Status": "ENABLED",
    "AdvancedEventSelectors": [
        {
            "Name": "S3EventSelector",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "resources.ARN",
                    "StartsWith": [
                        "arn:`partition`:s3:::`amzn-s3-demo-bucket`/"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::S3::Object"
                    ]
                },
                {
                    "Field": "userIdentity.arn",
                    "NotStartsWith": [
                        "arn:aws:sts::123456789012:assumed-role/bucket-scanner-role"
                     ]
                },
                {
                    "Field": "eventType",
                    "NotEquals": [
                        "AwsServiceEvent"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": false,
    "BillingMode": "EXTENDABLE_RETENTION_PRICING",
    "RetentionPeriod": 366,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2024-11-04T15:57:33.701000+00:00",
    "UpdatedTimestamp": "2024-11-20T20:49:21.766000+00:00"
}
```

#### Include Amazon S3 on

AWS Outposts events

The following example shows how to create an event data store that includes all data events
for all Amazon S3 on Outposts objects in your outpost.

```
aws cloudtrail create-event-data-store --name `EventDataStoreName` \
--advanced-event-selectors \
'[
    {
            "Name": "OutpostsEventSelector",
            "FieldSelectors": [
                { "Field": "eventCategory", "Equals": ["Data"] },
                { "Field": "resources.type", "Equals": ["AWS::S3Outposts::Object"] }
            ]
        }
]'
```

The command returns the following example output.

```
{
    "EventDataStoreArn": "arn:aws:cloudtrail:us-east-1:111122223333:eventdatastore/EXAMPLEb4a8-99b1-4ec2-9258-EXAMPLEc890",
    "Name": "EventDataStoreName",
    "Status": "CREATED",
    "AdvancedEventSelectors": [
        {
            "Name": "OutpostsEventSelector",
            "FieldSelectors": [
                {
                    "Field": "eventCategory",
                    "Equals": [
                        "Data"
                    ]
                },
                {
                    "Field": "resources.type",
                    "Equals": [
                        "AWS::S3Outposts::Object"
                    ]
                }
            ]
        }
    ],
    "MultiRegionEnabled": true,
    "OrganizationEnabled": false,
    "BillingMode": "EXTENDABLE_RETENTION_PRICING",
    "RetentionPeriod": 366,
    "TerminationProtectionEnabled": true,
    "CreatedTimestamp": "2023-02-20T21:00:17.673000+00:00",
    "UpdatedTimestamp": "2023-02-20T21:00:17.820000+00:00"
}
```

## Logging data events for AWS Config

compliance

If you are using AWS Config conformance packs to help your enterprise maintain compliance
with formalized standards such as those required by Federal Risk and Authorization
Management Program (FedRAMP) or National Institute of Standards and Technology (NIST),
conformance packs for compliance frameworks generally require you to log data events for
Amazon S3 buckets, at minimum. Conformance packs for compliance frameworks include a [managed rule](../../../config/latest/developerguide/evaluate-config_use-managed-rules.md "../../../config/latest/developerguide/evaluate-config_use-managed-rules.md") called [`cloudtrail-s3-dataevents-enabled`](../../../config/latest/developerguide/cloudtrail-s3-dataevents-enabled.md "../../../config/latest/developerguide/cloudtrail-s3-dataevents-enabled.md") that
checks for S3 data event logging in your account. Many conformance packs that are not
associated with compliance frameworks also require S3 data event logging. The following
are examples of conformance packs that include this rule.

- [Operational Best Practices for AWS Well-Architected
  Framework Security Pillar](../../../config/latest/developerguide/operational-best-practices-for-wa-Security-Pillar.md "../../../config/latest/developerguide/operational-best-practices-for-wa-Security-Pillar.md")
- [Operational Best Practices for FDA Title 21 CFR Part
  11](../../../config/latest/developerguide/operational-best-practices-for-FDA-21CFR-Part-11.md "../../../config/latest/developerguide/operational-best-practices-for-FDA-21CFR-Part-11.md")
- [Operational Best Practices for FFIEC](../../../config/latest/developerguide/operational-best-practices-for-ffiec.md "../../../config/latest/developerguide/operational-best-practices-for-ffiec.md")
- [Operational Best Practices for
  FedRAMP(Moderate)](../../../config/latest/developerguide/operational-best-practices-for-fedramp-moderate.md "../../../config/latest/developerguide/operational-best-practices-for-fedramp-moderate.md")
- [Operational Best Practices for HIPAA
  Security](../../../config/latest/developerguide/operational-best-practices-for-hipaa_security.md "../../../config/latest/developerguide/operational-best-practices-for-hipaa_security.md")
- [Operational Best Practices for K-ISMS](../../../config/latest/developerguide/operational-best-practices-for-k-isms.md "../../../config/latest/developerguide/operational-best-practices-for-k-isms.md")
- [Operational Best Practices for Logging](../../../config/latest/developerguide/operational-best-practices-for-logging.md "../../../config/latest/developerguide/operational-best-practices-for-logging.md")

For a full list of sample conformance packs available in AWS Config, see [Conformance pack sample templates](../../../config/latest/developerguide/conformancepack-sample-templates.md "../../../config/latest/developerguide/conformancepack-sample-templates.md") in the _AWS Config
Developer Guide._

## Logging data events with the AWS

SDKs

Run the [GetEventSelectors](../APIReference/API_GetEventSelectors.md "../APIReference/API_GetEventSelectors.md")
operation to see whether your trail is logging data events. You can
configure your trails to log data events by running the [PutEventSelectors](../APIReference/API_PutEventSelectors.md "../APIReference/API_PutEventSelectors.md") operation.
For more information, see the [AWS CloudTrail API Reference](../APIReference.md "../APIReference.md").

Run the [GetEventDataStore](../APIReference/API_GetEventDataStore.md "../APIReference/API_GetEventDataStore.md")
operation to see whether your event data store is logging data events. You can
configure your event data stores to include data events by running the [CreateEventDataStore](../APIReference/API_CreateEventDataStore.md "../APIReference/API_CreateEventDataStore.md") or [UpdateEventDataStore](../APIReference/API_UpdateEventDataStore.md "../APIReference/API_UpdateEventDataStore.md") operations and specifying advanced event selectors.
For more information, see [Create, update, and manage event data stores with the AWS CLI](lake-eds-cli.md "lake-eds-cli.md") and the [AWS CloudTrail API Reference](../APIReference.md "../APIReference.md").
