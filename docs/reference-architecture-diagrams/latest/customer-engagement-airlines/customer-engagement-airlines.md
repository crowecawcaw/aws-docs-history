

# Customer Engagement Using AI/ML for Airlines
<a name="customer-engagement-airlines"></a>

Publication date: **November 14, 2020 ([Diagram history](#engagement-airlines-history))**

With this architecture, you can improve customer experience and brand loyalty for airlines. Personalize interactions and improve call and response times. This workflow quickly recognizes the customer, customer needs, intents, and optimizes the interactions.

Airlines face barriers in time and costs when building and upgrading call center applications. Customers communicate on multiple channels such as chat, SMS, and social media. This increases costs due to the need to integrate multiple technologies. Airlines have reduced costs through automation and improved customer experience by reducing call times. However, the general lack of airline knowledge with call center developers and redundancy in custom development contributes to increasing complexity and cost.

This architecture builds upon the [Traveler 360 Data Platform for Airlines](../traveler-360-airlines/traveler-360-airlines.html) by adding personalized interactions with the customer.

## Customer engagement AI/ML for airlines diagram
<a name="engagement-airlines-diagram"></a>

![Architecture for airline customer engagement using Amazon Connect Customer, Amazon Lex, and AWS Lambda.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/customer-engagement-airlines/images/customer_engagement_travel_ra.png)


The following steps describe the architecture:

1. Use [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/) for cloud call centers. Use [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for operational data platform integration. Configure skills-based routing and workflows.

1. Use [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/) for conversational chatbots. Use Lambda for data platform access.

1. Integrate the Connect Customer Contact Control Panel with customer service, Passenger Service System (PSS), loyalty, and World Tracer user interfaces.

1. Use [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/) and [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/) for sentiment analysis. Identify customer intents and adjust operations accordingly.

1. (Optional) Improve effectiveness with master data management (MDM) integration. MDM provides a unified traveler profile for accurate engagement.

## Further reading
<a name="engagement-airlines-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="engagement-airlines-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#engagement-airlines-history) | Reference architecture diagram first published. | November 14, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.