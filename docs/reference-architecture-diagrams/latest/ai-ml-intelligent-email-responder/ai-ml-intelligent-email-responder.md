

# AI/ML Based Intelligent Email Responder
<a name="ai-ml-intelligent-email-responder"></a>

Publication date: **March 10, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to improve customer experience and agent productivity. With [Amazon Simple Email Service](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) (Amazon SES) and AWS ML services, you can comprehend intent and identify next-best-action for email responses.

## AI/ML Based Intelligent Email Responder
<a name="diagram1"></a>

![Architecture diagram showing an AI/ML based intelligent email responder with Amazon SES, SageMaker AI, and Amazon Comprehend.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ai-ml-intelligent-email-responder/images/ai-ml-intelligent-email-responder.png)


The following steps describe the architecture:

1. Amazon SES captures emails received at the corporate email exchange.

1. Amazon SES writes the raw payload to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and triggers a notification through [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/welcome.html). An [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function captures this notification and triggers the email responder workflow.

1. The email responder workflow uses [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) for language, sentiment, and keyword extraction. It uses [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html) for language translation. It calls intent extraction and next-best-action model endpoints deployed on [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) for better routing. It performs data lookups from the enterprise data lake. It updates the transactional data stores by using [Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html).

1. Based on confidence and completeness, the workflow either sends a response through Amazon SES or routes the email to the right queue for an agent.

1. From the data collected, you continuously improve the intent extraction and next-best-action models by using SageMaker AI Ground Truth and SageMaker AI.

1. You can perform personalized email campaigns, additional email analytics, and reporting by using [Amazon Pinpoint](https://docs.aws.amazon.com/pinpoint/latest/userguide/welcome.html), [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html), and [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon SageMaker AI product page](https://aws.amazon.com/sagemaker/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 10, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.