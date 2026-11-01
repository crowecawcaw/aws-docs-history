

# DescribeForMe Web App
<a name="describe-for-me-web-app"></a>

Publication date: **September 1, 2023 ([Diagram history](diagram-history.md))**

The [DescribeForMe](https://www.describeforme.com/) web app uses the AWS Cloud to help the visually impaired review images. Through the use of multiple artificial intelligence and machine learning (AI/ML) services, you can submit a photo and an image caption will be read back to you in a clear, natural-sounding voice in a variety of languages and dialects.

## DescribeForMe Web App diagram
<a name="describe-for-me-web-app-diagram1"></a>

![The DescribeForMe web app uses the AWS Cloud to help the visually impaired review images. Through the use of multiple artificial intelligence and machine learning (AI/ML) services, you can submit a photo and an image caption wi...](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/electronics-hpc/images/describe-for-me-web-app.png)


1. [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/) distributes the DescribeForMe web app, consisting of HTML, JavaScript, and CSS, to your mobile device. 

1.  The [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) identity pool grants temporary access to the [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) bucket. 

1.  The user uploads an image file to the Amazon S3 bucket using an AWS SDK through the web app. 

1.  The DescribeForMe web app invokes the backend AI services by sending the Amazon S3 object key in the payload to [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/).  

1.  API Gateway instantiates an [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) workflow. The state machine orchestrates the AI/ML services [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/), [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/), [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/), and [Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/) using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions.  

1.  The Step Functions workflow creates an audio file as output and stores it in Amazon S3 in MP3 format. 

1.  A pre-signed URL with the location of the audio file stored in Amazon S3 is sent back to your browser through Amazon API Gateway. Your mobile device plays the audio file using the pre-signed URL. 

## Further reading
<a name="describe-for-me-web-app-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [DescribeForMe](https://www.describeforme.com/) 

## Contributors
<a name="describe-for-me-web-app-contributors"></a>

 Contributors to this reference architecture diagram include: 
+  Alak Eswaradass, Senior Solutions Architect, Amazon Web Services 
+  Jack Marchetti, Senior Solutions Architect, Amazon Web Services 
+  Kandyce Bohannon, Senior Solutions Architect, Amazon Web Services 
+  Trac Do, Solutions Architect, Amazon Web Services 