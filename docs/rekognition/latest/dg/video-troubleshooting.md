# Troubleshooting Amazon Rekognition Video

The following covers troubleshooting information for working with Amazon Rekognition Video and stored
videos.

## I never receive the completion status that's

sent to the Amazon SNS topic

Amazon Rekognition Video publishes status information to an Amazon SNS topic when video analysis
completes. Typically, you get the completion status message by subscribing to the
topic with an Amazon SQS queue or Lambda function. To help your investigation, subscribe
to the Amazon SNS topic by email so you receive the messages that are sent to your Amazon SNS
topic in your email inbox. For more information, see [Subscribing to an Amazon SNS topic](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md").

If you don't receive the message in your application, consider the
following:

- Verify that the analysis has completed. Check the `JobStatus`
  value in the Get operation response (`GetLabelDetection`, for
  example). If the value is `IN_PROGRESS`, the analysis isn't
  complete, and the completion status hasn't yet been published to the Amazon SNS
  topic.
- Verify that you have an IAM service role that gives Amazon Rekognition Video permissions
  to publish to your Amazon SNS topics. For more information, see [Configuring Amazon Rekognition Video](api-video-roles.md "api-video-roles.md").
- Confirm that the IAM service role that you're using can publish to the
  Amazon SNS topic by using role credentials and that your service role's
  permissions are securely scoped to the resources you are using. Carry out the
  following steps:

      + Get the user Amazon Resource Name (ARN):



      ```
      aws sts get-caller-identity --profile `RekognitionUser`
      ```
      + Add the user ARN to the role trust relationship. For more information,
       see [Modifying a role](../../../IAM/latest/UserGuide/id_roles_manage_modify.md "../../../IAM/latest/UserGuide/id_roles_manage_modify.md"). The following example trust policy
       specifies the user's role credentials and restricts the service
       role's permissions to just the resources you are using (for more
       information on securely limiting the scope of a service role's
       permissions, see [Cross-service confused deputy
       prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")):
      + Assume the role: `aws sts assume-role --role-arn
       arn:`Role ARN` --role-session-name
       `SessionName` --profile
       RekognitionUser`
      + Publish to the Amazon SNS topic: `aws sns publish --topic-arn
       arn:`Topic ARN` --message "Hello
       World!" --region us-east-1 --profile
       RekognitionUser`

  If the AWS CLI command works, you receive the message (in your email
  inbox, if you've subscribed to the topic by email). If you don't receive the
  message:

      + Check that you've configured Amazon Rekognition Video. For more information, see
       [Configuring Amazon Rekognition Video](api-video-roles.md "api-video-roles.md").
      + Check the other tips for this troubleshooting question.

- Check that you're using the correct Amazon SNS topic:
  - If you use an IAM service role to give Amazon Rekognition Video access to a
    single Amazon SNS topic, check that you've given permissions to the
    correct Amazon SNS topic. For more information, see [Giving access to an existing Amazon SNS
    topic](api-video-roles.md#api-video-roles-single-topics "api-video-roles.md#api-video-roles-single-topics").
  - If you use an IAM service role to give Amazon Rekognition Video access to
    multiple SNS topics, verify that you're using the correct topic and
    that the topic name is prepended with
    _AmazonRekognition_. For more information,
    see [Giving access to multiple Amazon SNS
    topics](api-video-roles.md#api-video-roles-all-topics "api-video-roles.md#api-video-roles-all-topics").
  - If you use an AWS Lambda function, confirm that your Lambda function
    is subscribed to the correct Amazon SNS topic. For more information, see
    [Fanout to Lambda functions](../../../sns/latest/dg/sns-lambda.md "../../../sns/latest/dg/sns-lambda.md").

- If you subscribe an Amazon SQS queue to your Amazon SNS topic, confirm that your
  Amazon SNS topic has permissions to send messages to the Amazon SQS queue. For more
  information, see [Give permission to the Amazon SNS topic to send messages to the Amazon SQS
  queue](../../../sns/latest/dg/subscribe-sqs-queue-to-sns-topic.md#SendMessageToSQS.sqs.permissions "../../../sns/latest/dg/subscribe-sqs-queue-to-sns-topic.md#SendMessageToSQS.sqs.permissions").

## I need additional help troubleshooting the Amazon SNS topic

You can use AWS X-Ray with Amazon SNS to trace and analyze the messages that travel through your application.
For more information, see [Amazon SNS and AWS X-Ray](../../../xray/latest/devguide/xray-services-sns.md "../../../xray/latest/devguide/xray-services-sns.md").

For additional help, you can post your question to the [Amazon Rekognition forum](http://forums.aws.amazon.com/forum.jspa?forumID=234 "http://forums.aws.amazon.com/forum.jspa?forumID=234")
or consider signing up for [AWS technical support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
