# Configuring delivery status logging using

AWS CloudFormation

To configure `DeliveryStatusLogging` using AWS CloudFormation, use a JSON or YAML
template to create an AWS CloudFormation stack. For more information, see the
`DeliveryStatusLogging` property of the `AWS::SNS::Topic`
resource in the AWS CloudFormation User Guide. Below are examples of AWS CloudFormation templates in JSON and YAML
to create a new topic or update an existing topic with all
`DeliveryStatusLogging` attributes for the Amazon SQS protocol.

Ensure the IAM roles referenced in `SuccessFeedbackRoleArn` and
`FailureFeedbackRoleArn` have the required CloudWatch Logs permissions.

JSON

```
"Resources": {
    "MySNSTopic" : {
        "Type" : "AWS::SNS::Topic",
        "Properties" : {
            "TopicName" : "TestTopic",
            "DisplayName" : "TEST",
            "SignatureVersion" : "2",
            "DeliveryStatusLogging" : [{
                "Protocol": "sqs",
                "SuccessFeedbackSampleRate": "45",
                "SuccessFeedbackRoleArn": "arn:aws:iam::123456789012:role/SNSSuccessFeedback_test1",
                "FailureFeedbackRoleArn": "arn:aws:iam::123456789012:role/SNSFailureFeedback_test2"
            }]
        }
    }
}
```

YAML

```
Resources:
  MySNSTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName:TestTopic
      DisplayName:TEST
      SignatureVersion:2
      DeliveryStatusLogging:
       - Protocol: sqs
         SuccessFeedbackSampleRate: 45
         SuccessFeedbackRoleArn: arn:aws:iam::123456789012:role/SNSSuccessFeedback_test1
         FailureFeedbackRoleArn: arn:aws:iam::123456789012:role/SNSFailureFeedback_test2

```
