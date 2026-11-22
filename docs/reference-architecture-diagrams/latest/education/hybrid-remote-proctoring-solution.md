

# Hybrid remote proctoring solution

Publication date: **March 30, 2023 ([Diagram history](diagram-history.md))**

Hybrid remote proctoring supports education use cases where you can monitor students live with AI assistance to highlight prohibited objects and behaviors. This solution uses [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/) for image analysis and the [Amazon Chime SDK](https://docs.aws.amazon.com/chime-sdk/latest/dg/) for video session management. You can apply this solution to in-person exams as well as remote exams.

**Privacy considerations**  
This is a technical diagram only and does not account for possible privacy implications, laws, and regulations that might apply to this scenario, such as just-in-time privacy notices, user consent, and data usage, retention, processing, and deletion of personally identifiable information, including biometric data.

## Hybrid remote proctoring solution diagram
<a name="hybrid-remote-proctoring-solution-diagram"></a>

![During exams, Amazon Rekognition flags prohibited objects while the Amazon Chime SDK manages video sessions.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/education/images/hybrid-remote-proctoring-solution.png)


The following steps describe the architecture:

1. The architecture hosts static web app code in an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) serves this content with low-latency access from edge locations. You can secure content in the Amazon S3 bucket against unintended access by using CloudFront Origin Access Control.

1. [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) serves the REST APIs, and serverless [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions handle requests. [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) provides secure authenticated access to these APIs and manages identities for proctors and students.

1. For the registration flow, an API request registers each student. The request passes the student's photo to a Lambda function. The function calls a Amazon Rekognition API to retrieve a unique **FaceId** based on extracted facial feature vectors. The student's **FaceId** is stored in an [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) serverless database for future matching needs.

1. The proctor starts the exam by calling a Amazon Chime SDK Messaging API. This starts a Amazon Chime SDK session and a Amazon Chime SDK Messaging Channel for chat-based communication between the proctor and each student. The exam workflow captures student consent at the start of the exam with relevant policies.

1. The exam workflow stores exam information in DynamoDB. To stop the exam, a similar request updates the exam status within the database.

1. After the exam starts, the student's web app connects with a separate Amazon Chime SDK session. The web app captures the camera video stream and screen, using media capture pipelines with user consent. It saves these to an Amazon S3 bucket in up to five-second file chunks for internal audit and archiving.

1. For every new video chunk saved, an Amazon S3 PutEvent calls a Lambda function. The function pulls one image frame from the video chunk and stores that image frame in another Amazon S3 bucket as a .jpeg file. This optimizes cost while still allowing use of the full video chunk as needed.

1. Another Lambda function validates the .jpeg file by using Amazon Rekognition with API calls for verifying the student's face, checking how many faces are in the frame, and detecting when no face is present. The Lambda function saves these response alerts in DynamoDB for internal audit purposes.

1. If Amazon Rekognition detects prohibited actions, it sends an alert to the proctor by using [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/). A Lambda function sends an alert to the proctor (and student, if needed) by using the Amazon Chime SDK messaging channel.

## Further reading
<a name="hybrid-remote-proctoring-solution-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 