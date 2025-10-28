# Detect people and objects in a video with Amazon Rekognition using an AWS SDK

The following code examples show how to detect people and objects in a video with Amazon Rekognition.

Java

**SDK for Java 2.x**

Shows how to use Amazon Rekognition Java API to create an app to detect faces and objects in videos
located in an Amazon Simple Storage Service (Amazon S3) bucket. The app sends the admin an email notification with the results
using Amazon Simple Email Service (Amazon SES).

For complete source code and instructions on how to set up and run, see the full example on
[GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/video_analyzer_application "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/usecases/video_analyzer_application").

###### Services used in this example

- Amazon Rekognition
- Amazon S3
- Amazon SES
- Amazon SNS
- Amazon SQS

Python

**SDK for Python (Boto3)**

Use Amazon Rekognition to detect faces, objects, and people in videos by starting
asynchronous detection jobs. This example also configures Amazon Rekognition to notify
an Amazon Simple Notification Service (Amazon SNS) topic when jobs complete and subscribes an
Amazon Simple Queue Service (Amazon SQS) queue to the topic. When the queue receives a
message about a job, the job is retrieved and the results are output.

This example is best viewed on GitHub. For complete source code
and instructions on how to set up and run, see the full example on
[GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rekognition "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/rekognition").

###### Services used in this example

- Amazon Rekognition
- Amazon S3
- Amazon SES
- Amazon SNS
- Amazon SQS

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SQS with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
