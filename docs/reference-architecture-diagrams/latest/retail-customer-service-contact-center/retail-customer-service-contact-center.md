

# Retail Customer Service Contact Center Using Amazon Connect
<a name="retail-customer-service-contact-center"></a>

Publication date: **December 9, 2021 ([Diagram history](#diagram-history))**

This reference architecture diagram shows how retailers can simplify and transform their customer service channel with NLP and automation by using [Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/what-is-amazon-connect.html).

## Retail Customer Service Contact Center Using Amazon Connect
<a name="diagram1"></a>

![Reference architecture diagram showing a retail customer service contact center by using Amazon Connect, AWS Lambda, Amazon DynamoDB, Amazon Kinesis Data Streams, and Amazon Simple Storage Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/retail-customer-service-contact-center/images/retail-customer-service-contact-center.png)


1. Customers contact a retailer's customer service number. Amazon Connect automatically answers with a natural interactive voice response (IVR) and retrieves customer information for personalized greetings.

1. Agents answer calls routed to them through the Amazon Connect Contact Control Panel (CCP) and soft phone. Agents can answer calls from anywhere, including remote environments.

1. Amazon Connect integrates with a CRM system (such as Salesforce), powered by Amazon AppFlow. This retrieves customer data such as name, membership status, and loyalty points.

1. Amazon Connect manages customer enquiries through skills-based routing and contact flows. Calls route automatically through conversational NLP interactions, database lookups, and transfers to agents when appropriate.

1. Contact Lens, a feature of Amazon Connect, provides agents with real-time insights such as call sentiment analysis, transcripts, and detailed analytics.

1. Amazon Connect stores call metadata (call lengths, wait times, call abandonment, agent activity). Data streams through [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) for near real-time processing.

1. Data stored in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) links to a contact trace record. Ingest into [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html) and visualize on [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) dashboards.

1. Amazon Connect integrates with external systems. Retailers integrate with data lakes, customer data platforms, or order management systems for common enquiries.

1. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) exposes your organization's capabilities as scalable, secure, and standardized API services.

1. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions provide a scalable and serverless method of running business logic. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) provides a lightweight NoSQL datastore for low-latency lookups.

1. Managers monitor live conversations and review recordings. Amazon Connect stores recordings in Amazon Simple Storage Service at the conclusion of each call.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon Connect product page](https://aws.amazon.com/connect/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | December 9, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.