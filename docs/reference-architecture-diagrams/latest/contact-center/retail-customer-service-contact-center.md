

# Retail Customer Service Contact Center Using Amazon Connect Customer
<a name="retail-customer-service-contact-center"></a>

Publication date: **December 9, 2021 ([Diagram history](diagram-history.md))**

This reference architecture diagram shows how retailers can simplify and transform their customer service channel with NLP and automation by using [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/).

## Retail Customer Service Contact Center Using Amazon Connect Customer diagram
<a name="retail-customer-service-contact-center-diagram1"></a>

![Reference architecture diagram showing a retail customer service contact center by using Amazon Connect Customer, AWS Lambda, Amazon DynamoDB, Amazon Kinesis Data Streams, and Amazon Simple Storage Service.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/contact-center/images/retail-customer-service-contact-center.png)


1. Customers contact a retailer's customer service number. Connect Customer automatically answers with a natural interactive voice response (IVR) and retrieves customer information for personalized greetings.

1. Agents answer calls routed to them through the Connect Customer Contact Control Panel (CCP) and softphone. Agents can answer calls from anywhere, including remote environments.

1. Connect Customer integrates with a CRM system (such as Salesforce), powered by [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/). This retrieves customer data such as name, membership status, and loyalty points.

1. Connect Customer manages customer inquiries through skills-based routing and contact flows. Calls route automatically through conversational NLP interactions, database lookups, and transfers to agents when appropriate.

1. Contact Lens, a feature of Connect Customer, provides agents with real-time insights such as call sentiment analysis, transcripts, and detailed analytics.

1. Connect Customer stores call metadata (call lengths, wait times, call abandonment, agent activity). Data streams through [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/) for near real-time processing.

1. Data stored in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) links to a contact trace record. Ingest into [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) and visualize on [Quick](https://docs.aws.amazon.com/quick/latest/userguide/) dashboards.

1. Connect Customer integrates with external systems. Retailers integrate with data lakes, customer data platforms, or order management systems for common inquiries.

1. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) exposes your organization's capabilities as scalable, secure, and standardized API services.

1. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions provide a scalable and serverless method of running business logic. [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) provides a lightweight NoSQL datastore for low-latency lookups.

1. Managers monitor live conversations and review recordings. Connect Customer stores recordings in Amazon Simple Storage Service at the conclusion of each call.

## Further reading
<a name="retail-customer-service-contact-center-further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon Connect Customer product page](https://aws.amazon.com/connect/)