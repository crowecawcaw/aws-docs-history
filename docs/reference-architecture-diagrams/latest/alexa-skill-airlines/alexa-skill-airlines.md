

# Amazon Alexa Skill for Airlines
<a name="alexa-skill-airlines"></a>

Publication date: **March 10, 2021 ([Diagram history](#alexa-skill-history))**

As conversational AI technology evolves, consumer demands evolve as well. A multi-channel digital strategy is no longer optional for airlines.

This architecture helps airlines deliver a secure, integrated experience for booking and managing air travel seamlessly through Amazon Alexa. The solution integrates with Passenger Service System (PSS) providers like Amadeus, Sabre, and Navitaire.

## Amazon Alexa Skill for airlines diagram
<a name="alexa-skill-diagram"></a>

![Architecture for an airline Alexa Skill using Amazon API Gateway, AWS Lambda, and Amazon Cognito.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/alexa-skill-airlines/images/alexa-skills-airlines-ra.png)


The following steps describe the architecture:

1. A traveler activates the airline's Alexa Skill. During the first interaction, Alexa prompts authentication and pushes a card to the Amazon Alexa App.

1. The authentication flow uses [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), and [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/). Lambda retrieves auth provider information. [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) authenticates the customer. [CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) ensures optimal network latency.

1. Use API Gateway, Application Load Balancer, and [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) to deploy your natural language understanding (NLU) engine at scale. Use [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) and [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/) for low-latency content and conversation state access.

1. [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/), Amazon Data Firehose, and Amazon S3 capture and store application logs. Use Lambda for real-time analytics stored in [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/). Use [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for AI/ML models on conversation trends. Store results in DynamoDB.

1. Use Amazon S3 PUT triggers and [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) to orchestrate a workflow that updates application content and Alexa Skill configuration.

## Further reading
<a name="alexa-skill-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="alexa-skill-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#alexa-skill-history) | Reference architecture diagram first published. | March 10, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.