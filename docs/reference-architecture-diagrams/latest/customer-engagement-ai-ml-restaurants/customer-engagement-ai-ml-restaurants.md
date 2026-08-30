# Customer Engagement Using AI/ML for Restaurants

Publication date: **2020 ([Diagram history](#cerest-history "#cerest-history"))**

With this architecture, you can enhance the customer experience and increase brand loyalty
for restaurant companies. Personalize guest interactions and improve contact center response
time. Quickly recognize guests and their needs, and optimize interactions. The solution uses
[Connect Customer](../../../connect/latest/adminguide.md "../../../connect/latest/adminguide.md"), [Amazon Lex](../../../lexv2/latest/dg.md "../../../lexv2/latest/dg.md"), and [Amazon Comprehend](../../../comprehend/latest/dg.md "../../../comprehend/latest/dg.md").

Restaurant companies face barriers to delivering high levels of customer service. Customers
communicate on multiple channels such as chat, SMS, social media, and telephone. This increases
operational costs from multiple technology integrations. On-premises telephony technologies do
not help brands reduce costs or scale with demand. Building on the foundation of the Guest 360° Data
Platform for Restaurants, you can reduce costs and call times. You can also add
automation, self-service, and personalized interactions.

## Customer engagement AI/ML for restaurants diagram

![How to personalize customer interactions for restaurants by using Connect Customer, Amazon Lex, and Amazon Comprehend.](images/customer-engagement-ai-ml-restaurants-ra.png)

The following steps describe the architecture:

1. Use Connect Customer to implement call center capabilities in the cloud. Use serverless
   functions such as [AWS Lambda](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md") with your operational data platform for
   improved customer interactions. Connect Customer provides skill-based call routing and workflows to
   streamline call center operations.
2. Use Amazon Lex to build conversational chatbots that automate user interactions.
3. Integrate the Connect Customer Contact Control Panel (CCP) with order management, loyalty, and
   case management. Improve call handling times for complex scenarios.
4. Use [Amazon Transcribe](../../../transcribe/latest/dg.md "../../../transcribe/latest/dg.md") and Amazon Comprehend to perform sentiment analysis.
   Identify frequent customer intents and adjust call center operations and
   automation.
5. Use Contact Lens for Connect Customer to understand the sentiment, trends, and compliance of
   customer conversations. Train agents, replicate successful interactions, and identify
   company and product feedback.
6. (Optional) Improve customer interaction effectiveness by integrating the Master Data
   Management (MDM) system.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [AWS
  Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date            |
| ------------------- | ----------------------------------------------- | --------------- |
| Initial publication | Reference architecture diagram first published. | January 1, 2020 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you
are using.
