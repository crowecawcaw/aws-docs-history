# Automotive Call Center Architecture

Publication date: **February 28, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture enables you to build an automotive call center solution as part of connected vehicle platform to enhance customer safety with emergency (eCall) and breakdown (bCall) call services using Amazon Connect.

## Automotive Call Center Architecture Diagram

![Reference architecture diagram showing how to build an automotive call center solution as part of connected vehicle platform to enhance customer safety with emergency (eCall) and breakdown (bCall) call services using Amazon Connect.](images/automotive-call-center-architecture.png)

1. Vehicle triggers an eCall or bCall in case of an accident or breakdown to **Amazon Connect**, and sends a snapshot of sensor and location data to the
   connected vehicle backend with **Amazon API Gateway**.
2. **Amazon Connect** triggers an **AWS Lambda** function that assigns a case ID to the call and data received from
   the vehicle by **Amazon Connect**.
3. connected vehicle backend (such as [Connected Mobility Solution (CMS) on AWS](https://aws.amazon.com/automotive/solutions/connected-mobility/ "https://aws.amazon.com/automotive/solutions/connected-mobility/")), snapshot of current vehicle data and location with case ID using call metadata information. This will be pulled by the call center client via an API call.
4. Use contact flows in **Amazon Connect** to automate the entire
   customer experience by dragging and dropping contact blocks onto a canvas.
5. Authenticate real-time callers with the voice ID capability within **Amazon Connect**.
6. Integrate **Amazon Connect** with Customer Relationship Management
   (CRM) to provide unified customer profile to call center agents across multiple sources.
7. Put call in a queue to be picked up by next available call center agent at home office or on-site.
8. Analyze conversations between customer and agents by using speech transcription,
   natural language processing, and intelligent search capabilities with the Contact Lens for
   **Amazon Connect** feature. It performs sentiment analysis, detects
   issues, and enables you to automatically categorize contacts. It provides both real-time
   and post-call analytics of conversations.
9. Notify customers about reminders, vehicle issues, recommendations by emails and text
   with **Amazon Connect**.
10. Identify key parts of the customer conversation, assign a label, and display a summary
    that can be expanded to view the full transcript of the call with the _Call Summary_ feature.
11. Provide call center agent case ID, vehicle, and location data, customer profile,
    **Amazon Connect** Contact Lens insights, and call summary along
    with the call to ensure a personalised experience to customers. Improve customer
    experience with Contact Lens real time analysis to give guidelines to agents in live
    calls.

## Enhanced Automotive Call Center Architecture

Diagram

![Reference architecture diagram showing how to build an automotive call center solution to enhance customer service and loyalty operations, including service (hCall) and concierge (cCall) call services using Amazon Connect.](images/automotive-call-center-architecture-2.png)

1. Trigger hCall and cCall from vehicle with touch button or voice enabled interface
   (such as **Amazon Alexa**).
2. Use **Amazon Connect** to identify hCall and cCall callers from
   the vehicle owner’s associated phone number. Route these calls to the **Amazon Lex** chat bot channel. Push call metrics insights to **Amazon S3** bucket with **Amazon Kinesis Data Streams**.
3. Identify customer intent and provide conversational service with **Amazon Lex**. Integrate **Amazon Lex** with **Amazon DynamoDB** and **AWS Lambda** to
   formulate reply for identified intent.
4. Call connected mobility backend to collect data with **AWS Lambda** to formulate intent reply if required for hCall and cCall.
   Automate conversations which do not need an agent.
5. Query **Amazon S3** sentiment analysis, call matrix, and
   product feedback data with **Amazon Athena**. Visualize
   dashboards that shows business metrics, monitoring of key performance indicators using
   **Quick Suite** to convert data into insights.
6. Monitor customer and product feedback, customer sentiments, and market trends from call center data. Feedback insights go into development and production processes, product roadmap of an original equipment manufacturer (OEM).
7. Forward hCall and cCall to call center agent if customer wants to talk to a human
   agent. Present case ID, vehicle data, customer profile, **Amazon Connect** Contact Lens insights, and call summary, along with voice call to the
   agent to ensure the best customer experience.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/automotive-call-center-architecture.md "samples/automotive-call-center-architecture.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | February 28, 2022 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
