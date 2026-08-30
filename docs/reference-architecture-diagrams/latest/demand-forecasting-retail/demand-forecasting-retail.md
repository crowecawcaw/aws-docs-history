# Improve Demand Forecasting to Boost Sales on Amazon.com

Publication date: **April 5, 2022 ([Diagram history](#df-history "#df-history"))**

With this architecture, you can understand prior demand trends and anticipate future
demand. Companies that sell products on Amazon.com as first-party vendors want
to improve On-Time-In-Full (OTIF) metrics and maximize revenue. You programmatically source
vendor performance data from the Amazon.com Selling Partner API and use machine
learning (ML) to create future demand predictions.

## Demand forecasting diagram

![Data flowing from Amazon.com Selling Partner API through Lambda and Amazon Simple Queue Service into Amazon Simple Storage Service, with AWS Glue for processing, Amazon Forecast for predictions managed by AWS Step Functions, and Amazon Quick Sight for visualization.](images/demand-forecasting-retail.png)

The following steps describe the architecture:

1. [Amazon EventBridge](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md") initiates scheduled tasks that
   keep the data fresh with controlled latency.
2. [Lambda](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md") makes API calls
   to the Amazon Selling Partner API. An AWS Identity and Access Management (IAM) role attached
   to the Amazon Vendor Central account entitles access.
3. The Selling Partner API authenticates the calling API and uses the IAM role to
   authorize access to a specific set of vendor codes.
4. Some API responses are stored in [Amazon Simple Queue Service](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide.md") as part of a
   decoupled microservices architecture.
5. Lambda consumes messages from the Amazon SQS queue. It transforms, persists, and creates
   notifications.
6. [Amazon Simple Notification Service](../../../sns/latest/dg.md "../../../sns/latest/dg.md") receives
   notifications on data conditions such as product catalog changes.
7. [Amazon DynamoDB](../../../amazondynamodb/latest/developerguide.md "../../../amazondynamodb/latest/developerguide.md") acts as an intermediate
   database. It accepts create, read, update, and delete (CRUD) operations while
   maintaining data integrity.
8. A scheduled [AWS Glue](../../../glue/latest/dg.md "../../../glue/latest/dg.md") job
   publishes data to a serverless data lake for long-term persistence.
9. [Amazon Simple Storage Service](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md") is the persistence tier for the
   serverless data lake. It serves time-series data at any scale.
10. EventBridge triggers a recurring [Amazon Forecast](../../../forecast/latest/dg.md "../../../forecast/latest/dg.md") routine. [AWS Step Functions](../../../step-functions/latest/dg.md "../../../step-functions/latest/dg.md") manages the workflow that sources
    demand history to generate future predictions.
11. Amazon S3 data is syndicated to consuming applications. [Amazon Quick Sight](../../../quicksight/latest/developerguide/welcome.md "../../../quicksight/latest/developerguide/welcome.md") and [Amazon Athena](../../../athena/latest/ug.md "../../../athena/latest/ug.md") provide business intelligence and SQL
    capabilities.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date          |
| ------------------- | ----------------------------------------------- | ------------- |
| Initial publication | Reference architecture diagram first published. | April 5, 2022 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you
are using.
