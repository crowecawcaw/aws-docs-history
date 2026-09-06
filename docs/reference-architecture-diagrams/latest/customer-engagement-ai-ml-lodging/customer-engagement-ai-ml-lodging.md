

# Customer Engagement Using AI/ML for Lodging
<a name="customer-engagement-ai-ml-lodging"></a>

Publication date: **August 25, 2022 ([Diagram history](#celodge-history))**

With this architecture, you can improve customer experience and brand loyalty for lodging companies. Personalize interactions and improve response times by recognizing guest needs and intents. The solution uses [Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/) for cloud-based contact centers, [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/) for chatbots, and [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/) for real-time personalization.

## Customer engagement AI/ML diagram
<a name="celodge-diagram"></a>

![How to personalize customer interactions for lodging by using Connect Customer, Amazon Lex, and Amazon Personalize.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/customer-engagement-ai-ml-lodging/images/customer-engagement-ai-ml-lodging.png)


The following steps describe the architecture:

1. Use Connect Customer to implement call centers in the cloud and eliminate on-premises hardware. Use [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) to access the operational data platform for faster customer interactions. Connect Customer provides skill-based call routing and workflows.

1. Use Amazon Lex to build conversational chatbots that automate user interactions.

1. Use Amazon Personalize to create real-time personalized user experiences at scale.

1. Integrate the Connect Customer Contact Control Panel (CCP) with customer service, loyalty membership, and reservations. Improve call handling times for complex scenarios.

1. Use [Amazon Transcribe](https://docs.aws.amazon.com/transcribe/latest/dg/) and [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/) for sentiment analysis. Identify frequent customer intents and adjust call center operations and automation.

1. (Optional) Improve customer interaction effectiveness by integrating the MDM system.

## Further reading
<a name="celodge-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="celodge-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#celodge-history) | Reference architecture diagram first published. | August 25, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.