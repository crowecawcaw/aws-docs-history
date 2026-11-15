

# Automotive Call Center Architecture
<a name="automotive-call-center-architecture"></a>

Publication date: **February 28, 2022 ([Diagram history](diagram-history.md))**

With this architecture, you can build an automotive call center solution as part of a connected vehicle platform to enhance customer safety with emergency (eCall) and breakdown (bCall) call services using [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/).

## Automotive Call Center Architecture diagram
<a name="automotive-call-center-architecture-diagram1"></a>

The following diagram shows the call flow. The vehicle places an eCall or bCall to Connect Customer and sends sensor and location data to the connected vehicle backend through API Gateway. An Lambda function assigns a case ID, contact flows route the call, and Voice ID authenticates callers. Agents receive a unified CRM customer profile and Connect Customer Contact Lens insights along with the call.

![Diagram of the automotive call center architecture, from vehicle eCall or bCall through Amazon Connect Customer to the call center agent.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/automotive/images/automotive-call-center-architecture.png)


1. Trigger an eCall or bCall from the vehicle to Connect Customer in case of an accident or breakdown, and send a snapshot of sensor and location data to the connected vehicle backend with [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/). 

1. Use Connect Customer to trigger an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function that assigns a case ID to the call and data received from the vehicle by Connect Customer. 

1. Store a snapshot of current vehicle data and location with the case ID in the connected vehicle backend (such as [Connected Mobility Solution (CMS) on AWS](https://aws.amazon.com/automotive/solutions/connected-mobility/)), using call metadata. The call center client retrieves this snapshot through an API call. 

1. Use contact flows in Connect Customer to automate the entire customer experience by dragging and dropping contact blocks onto a canvas. 

1. Authenticate real-time callers with the voice ID capability within Connect Customer. 

1. Integrate Connect Customer with Customer Relationship Management (CRM) to provide unified customer profile to call center agents across multiple sources. 

1. Put call in a queue to be picked up by next available call center agent at home office or on-site. 

1. Analyze conversations between customer and agents by using speech transcription, natural language processing, and intelligent search capabilities with the Contact Lens for Connect Customer feature. It performs sentiment analysis, detects issues, and enables you to automatically categorize contacts. It provides both real-time and post-call analytics of conversations. 

1. Notify customers about reminders, vehicle issues, recommendations by emails and text with Connect Customer. 

1. Identify key parts of the customer conversation, assign a label, and display a summary that can be expanded to view the full transcript of the call with the *Call Summary* feature. 

1. Provide call center agent case ID, vehicle, and location data, customer profile, Connect Customer Contact Lens insights, and call summary along with the call to ensure a personalized experience to customers. Improve customer experience with Contact Lens real time analysis to give guidelines to agents in live calls. 

## Enhanced Automotive Call Center Architecture diagram
<a name="automotive-call-center-architecture-diagram2"></a>

![Reference architecture diagram showing how to build an automotive call center solution to enhance customer service and loyalty operations, including service (hCall) and concierge (cCall) call services using Amazon Connect Customer.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/automotive/images/automotive-call-center-architecture-2.png)


1. Trigger hCall and cCall from vehicle with touch button or voice enabled interface (such as Amazon Alexa). 

1. Use Connect Customer to identify hCall and cCall callers from the vehicle owner's associated phone number. Route these calls to the [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/) chat bot channel. Push call metrics insights to [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket with [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/). 

1. Identify customer intent and provide conversational service with Amazon Lex. Integrate Amazon Lex with [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) and AWS Lambda to formulate reply for identified intent. 

1. Call connected mobility backend to collect data with AWS Lambda to formulate intent reply if required for hCall and cCall. Automate conversations which do not need an agent. 

1. Query Amazon S3 sentiment analysis, call metrics, and product feedback data with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/). Visualize dashboards that show business metrics, monitoring of key performance indicators using [Quick](https://docs.aws.amazon.com/quick/latest/userguide/) to convert data into insights. 

1. Monitor customer and product feedback, customer sentiments, and market trends from call center data. Feedback insights go into development and production processes, product roadmap of an original equipment manufacturer (OEM). 

1. Forward hCall and cCall to call center agent if customer wants to talk to a human agent. Present case ID, vehicle data, customer profile, Connect Customer Contact Lens insights, and call summary, along with voice call to the agent to ensure the best customer experience. 

## Further reading
<a name="automotive-call-center-architecture-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 