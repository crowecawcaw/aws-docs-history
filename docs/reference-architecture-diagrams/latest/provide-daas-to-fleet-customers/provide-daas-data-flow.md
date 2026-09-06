

# Provide DaaS to Fleet Customers: Data flow
<a name="provide-daas-data-flow"></a>

Publication date: **February 16, 2023 ([Diagram history](#daas-flow-history))**

With this architecture, you can build a serverless Data as a Service (DaaS) platform. Ingest, process, and deliver vehicle data to fleet owner applications. Use a data API subscription model for customer-specific delivery. The solution uses [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/) for ingestion, [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) for event routing, and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for processing.

## DaaS data flow diagram
<a name="daas-flow-diagram"></a>

![Reference architecture diagram showing DaaS data flow for fleet customers by using Amazon Kinesis, Amazon EventBridge, and Lambda.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/provide-daas-to-fleet-customers/images/provide-daas-data-flow.png)


The following steps describe the data ingestion and delivery pipeline for this architecture:

1. Stream vehicle telemetry and diagnostic events into Amazon Kinesis Data Streams or [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/). Store raw events in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for long-term retention.

1. Process streaming events with Lambda or [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html). Perform event validation, transformation, and filtering. Use [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) for reference data such as subscription status and event schema.

1. Store processed events in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/). Use DynamoDB as the data layer for on-demand request APIs.

1. Send transformed events to the Amazon EventBridge default event bus.

1. Retrieve events from the default event bus with Lambda. Enrich events with customer-specific data from Amazon RDS. Send enriched events to a delivery event bus.

1. Process matching telemetry events with Amazon EventBridge rules. Route them to customer-specific [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/) queues for buffering until consumed.

1. Make API calls to [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) from fleet applications. Invoke Lambda to process requests.

1. Pull events from Amazon SQS queues for streaming data. Read events from DynamoDB for on-demand requests.

1. Route alerts and time-sensitive events to customer-specific HTTP endpoints by using an Amazon EventBridge API target.

## Further reading
<a name="daas-flow-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="daas-flow-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#daas-flow-history) | Reference architecture diagram first published. | February 16, 2023 | 
| [Initial publication](provide-daas-subscription.md#daas-sub-history) | Reference architecture diagram first published. | February 16, 2023 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.