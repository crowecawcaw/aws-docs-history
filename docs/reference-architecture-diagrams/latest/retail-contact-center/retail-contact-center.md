

# Retail Customer Service Contact Center
<a name="retail-contact-center"></a>

Publication date: **December 9, 2021 ([Diagram history](#rcc-history))**

With this architecture, you can transform your retail customer service channel by using natural language processing (NLP) and automation. Physical and ecommerce retailers use [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/) to simplify customer interactions across voice, text, and chat channels.

## Retail contact center diagram
<a name="rcc-diagram"></a>

![Amazon Connect Customer routing customer calls through IVR, Amazon AppFlow CRM integration, Amazon Kinesis streaming, and Amazon Quick Sight analytics.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/retail-contact-center/images/retail-contact-center.png)


The following steps describe the architecture:

1. Customers contact the retailer's service number. Connect Customer automatically answers and greets the customer with a natural interactive voice response (IVR).

1. Connect Customer integrates with a customer relationship management (CRM) system such as Salesforce. Amazon AppFlow retrieves customer data such as name, membership status, and loyalty points.

1. Connect Customer manages enquiries through skills-based routing and contact flows. Calls are routed to the appropriate automation or transferred to agents when needed.

1. Agents answer calls through the Connect Customer Contact Control Panel (CCP) and soft phone. Because calls are placed over the internet, agents work from any location.

1. Managers monitor live conversations and review recordings. Connect Customer stores call recordings in Amazon S3 at the conclusion of each call.

1. Contact Lens, a feature of Connect Customer, provides real-time insights such as call sentiment analysis, transcripts, and detailed analytics.

1. Connect Customer stores call metadata such as call lengths, wait times, and agent activity. Connect Customer streams this data through Amazon Kinesis for near real-time processing.

1. Data stored in Amazon S3 is ingested into [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) and visualized on a dashboard by using [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html).

1. Connect Customer integrates with external systems. Retailers connect to their data lake, customer data platform, or order management systems to answer common enquiries.

1. [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) exposes backend services and microservices as scalable, secure APIs for reuse throughout the organization.

1. [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions run business logic such as database lookups. [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) provides low-latency lookups directly from API Gateway.

## Further reading
<a name="rcc-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="rcc-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#rcc-history) | Reference architecture diagram first published. | December 9, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.