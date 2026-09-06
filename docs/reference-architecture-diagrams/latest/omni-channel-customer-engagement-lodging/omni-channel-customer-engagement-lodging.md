

# Omni-channel Customer Engagement for Lodging
<a name="omni-channel-customer-engagement-lodging"></a>

Publication date: **August 15, 2022 ([Diagram history](#oce-history))**

With this architecture, you can provide a unified interface for customer service teams at travel and hospitality companies. Deliver personalized service across all channels at every stage of the guest journey. The solution uses [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/) for chatbot interactions, [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) for product search, and [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/) for notifications.

## Omni-channel customer engagement diagram
<a name="oce-diagram"></a>

![How to provide personalized customer service across all channels by using Amazon Lex, Amazon OpenSearch Service, and Amazon Pinpoint.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/omni-channel-customer-engagement-lodging/images/omni-channel-customer-engagement-lodging.png)


The following steps describe the architecture:

1. Use [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) to store website and configuration files. Serve the unified user interface through [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/).

1. Invoke [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) to provide personalized recommendations for guests through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/). Control API access through [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/).

1. Run a serverless database architecture on [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/). Collect key guest 360-degree data from several sources, including data processing workload outputs and systems of record.

1. Use a chatbot powered by Amazon Lex to collect guest input data. Automate the delivery of personalized user interactions and recommendations.

1. Use a search service powered by Amazon OpenSearch Service to recommend available products in the data bank index.

1. Use Amazon Pinpoint to send recommendations to guests through email or mobile push notifications. Schedule the notifications based on guest preferences.

## Further reading
<a name="oce-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="oce-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#oce-history) | Reference architecture diagram first published. | August 15, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.