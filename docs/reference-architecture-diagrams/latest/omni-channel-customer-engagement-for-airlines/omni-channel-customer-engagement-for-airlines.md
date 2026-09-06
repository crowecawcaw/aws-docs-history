

# Omni-channel Customer Engagement for Airlines
<a name="omni-channel-customer-engagement-for-airlines"></a>

Publication date: **August 15, 2022 ([Diagram history](#diagram-history))**

This reference architecture provides a unified user interface for customer service teams (both centralized and on location) at Travel and Hospitality companies to provide personalized customer service across all channels at every stage of their customer's journey.

## Omni-channel Customer Engagement for Airlines Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how you can use AWS services together to create a user interface to provide a personalized customer experience.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/omni-channel-customer-engagement-for-airlines/images/omni-channel-customer-engagement-for-airlines.png)


1. Use **Amazon Simple Storage Service** (Amazon S3) to store website, configuration files, and **Amazon CloudFront** to serve a unified user interface. 

1. Invoke **AWS Lambda** to provide personalized recommendations for travelers and generate data through **Amazon API Gateway**. API access is controlled through **Amazon Cognito**. 

1. Serverless database architecture runs on **Amazon DynamoDB** to collect key Traveler 360 data from several sources, personalization data processing workload outputs, and systems of records. 

1. A chatbot powered by **Amazon Lex** asks for traveler input data and automates the delivery of personalized user interactions and recommendations. 

1. Use a search service for available products to recommend in the data bank index by using **Amazon OpenSearch Service**. 

1. Use a mail or mobile push notification service to send recommendations to travelers, scheduled through **Amazon Pinpoint**. 

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | August 15, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.