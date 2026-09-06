

# ReadForMe
<a name="readforme"></a>

Publication date: **January 25, 2022 ([Diagram history](#diagram-history))**

This architecture shows how the ReadForMe web app uses the AWS Cloud to assist the visually impaired with hearing paper documents. With an event-driven serverless architecture and AI services, you can convert images of text into audio output.

## ReadForMe
<a name="diagram1"></a>

![Architecture diagram showing the ReadForMe serverless application with Amazon Textract, Amazon Polly, and AWS Step Functions.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/readforme/images/readforme.png)


The following steps describe the architecture:

1. [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) distributes the ReadForMe web app (HTML, JavaScript, and CSS) to end users' mobile devices.

1. The [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) identity pool grants temporary access to the [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket.

1. The user uploads an image file to the Amazon S3 bucket by using the AWS SDK through the web app.

1. The ReadForMe web app invokes the backend AI services by sending the Amazon S3 object key in the payload to [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html).

1. API Gateway instantiates an [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) workflow. The state machine orchestrates [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html), [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html), [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/what-is.html), and [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/what-is.html) by using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions.

1. The Step Functions workflow creates an audio file as output and stores it in Amazon S3 in MP3 format.

1. A pre-signed URL with the location of the audio file is sent back to the user's browser through API Gateway. The user's mobile device plays the audio file.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Amplify product page](https://aws.amazon.com/amplify/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | January 25, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.