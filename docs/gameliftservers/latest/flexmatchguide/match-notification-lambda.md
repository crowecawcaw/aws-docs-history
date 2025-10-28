# Configure a topic subscription to invoke a Lambda

function

You can invoke a Lambda function using event notifications published to your Amazon SNS topic.
When configuring the matchmaker, be sure to set the notification target to your SNS topic's
ARN.

The following AWS CloudFormation template configures a subscription to an SNS topic named
`MyFlexMatchEventTopic` to invoke a Lambda function named
`FlexMatchEventHandlerLambdaFunction`. The template creates an IAM permissions
policy that allows Amazon GameLift Servers to write to the SNS topic. The template then adds permissions for the
SNS topic to invoke the Lambda function.

```
FlexMatchEventTopic:
  Type: "AWS::SNS::Topic"
  Properties:
    KmsMasterKeyId: alias/aws/sns #Enables server-side encryption on the topic using an AWS managed key
    Subscription:
      - Endpoint: !GetAtt FlexMatchEventHandlerLambdaFunction.Arn
        Protocol: lambda
    TopicName: MyFlexMatchEventTopic

FlexMatchEventTopicPolicy:
  Type: "AWS::SNS::TopicPolicy"
  DependsOn: FlexMatchEventTopic
  Properties:
    PolicyDocument:
      Version: "2012-10-17"
      Statement:
        - Effect: Allow
          Principal:
            Service: gamelift.amazonaws.com
          Action:
            - "sns:Publish"
          Resource: !Ref FlexMatchEventTopic
    Topics:
      - Ref: FlexMatchEventTopic

FlexMatchEventHandlerLambdaPermission:
  Type: "AWS::Lambda::Permission"
  Properties:
    Action: "lambda:InvokeFunction"
    FunctionName: !Ref FlexMatchEventHandlerLambdaFunction
    Principal: sns.amazonaws.com
    SourceArn: !Ref FlexMatchEventTopic
```
