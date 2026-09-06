

# Serverless Strategy for Dynamic Pricing
<a name="serverless-dynamic-pricing"></a>

Publication date: **June 28, 2021 ([Diagram history](#diagram-history))**

This architecture shows a serverless strategy for dynamic pricing. For bookings based on date ranges, you can build prices in parallel and dynamically calculate them based on factors such as date, duration, and number of people. You then display sorted comparable products with sub-second response times, and update prices based on current market conditions.

## Serverless Strategy for Dynamic Pricing
<a name="diagram1"></a>

![Architecture diagram showing a serverless dynamic pricing solution using Amazon API Gateway, AWS Lambda, Amazon DynamoDB, Amazon Kinesis, and Amazon SageMaker AI.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/serverless-dynamic-pricing/images/serverless-dynamic-pricing.png)


The following steps describe the architecture:

1. You provide search input to obtain a sorted list of products filtered by price and other attributes. Data is sent through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) which calls multiple [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions to process pricing requests in parallel for real-time price lookups.

1. The batch parallel processor Lambda functions call the rule calculator function to get the latest product rules from [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html). The product is calculated against the search ID and stored in [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html). After the batch functions complete, all results for the search ID are returned from the cache.

1. Historical data from the booking engine and external market data provide information so the pricing engine has sufficient data to update pricing in real time.

1. The booking engine events are captured and monitored on [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html). Amazon Kinesis Data Analytics queries the data stream and triggers the price evaluator Lambda function if a change is detected. Events are stored in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) with supporting historical batch data.

1. An [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) Train model uses historic booking data and augmented historic data to train the model for pricing recommendations.

1. Using an SageMaker AI inference recommender model, the pricing engine gets new price recommendations based on market conditions.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | June 28, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.