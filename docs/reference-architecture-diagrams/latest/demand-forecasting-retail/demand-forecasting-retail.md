

# Improve Demand Forecasting to Boost Sales on Amazon.com
<a name="demand-forecasting-retail"></a>

Publication date: **April 5, 2022 ([Diagram history](#df-history))**

With this architecture, you can understand prior demand trends and anticipate future demand. Companies that sell products on Amazon.com as first-party vendors want to improve On-Time-In-Full (OTIF) metrics and maximize revenue. You programmatically source vendor performance data from the Amazon.com Selling Partner API and use machine learning (ML) to create future demand predictions.

## Demand forecasting diagram
<a name="df-diagram"></a>

![Data flowing from Amazon.com Selling Partner API through Lambda and Amazon Simple Queue Service into Amazon Simple Storage Service, with AWS Glue for processing, Amazon Forecast for predictions managed by AWS Step Functions, and Amazon Quick Sight for visualization.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/demand-forecasting-retail/images/demand-forecasting-retail.png)


The following steps describe the architecture:

1. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) initiates scheduled tasks that keep the data fresh with controlled latency.

1. [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) makes API calls to the Amazon Selling Partner API. An AWS Identity and Access Management (IAM) role attached to the Amazon Vendor Central account entitles access.

1. The Selling Partner API authenticates the calling API and uses the IAM role to authorize access to a specific set of vendor codes.

1. Some API responses are stored in [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/) as part of a decoupled microservices architecture.

1. Lambda consumes messages from the Amazon SQS queue. It transforms, persists, and creates notifications.

1. [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) receives notifications on data conditions such as product catalog changes.

1. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) acts as an intermediate database. It accepts create, read, update, and delete (CRUD) operations while maintaining data integrity.

1. A scheduled [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) job publishes data to a serverless data lake for long-term persistence.

1. [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) is the persistence tier for the serverless data lake. It serves time-series data at any scale.

1. EventBridge triggers a recurring [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) routine. [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) manages the workflow that sources demand history to generate future predictions.

1. Amazon S3 data is syndicated to consuming applications. [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) and [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) provide business intelligence and SQL capabilities.

## Further reading
<a name="df-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="df-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#df-history) | Reference architecture diagram first published. | April 5, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.