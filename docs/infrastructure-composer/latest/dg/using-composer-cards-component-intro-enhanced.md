# Enhanced component cards in Infrastructure Composer

Enhanced component cards are created and managed by Infrastructure Composer. Each card contains AWS CloudFormation resources that are commonly used together when building applications on AWS. Their
infrastructure code is created by Infrastructure Composer following AWS best practices. Enhanced component cards are a great way to start designing your application.

Enhanced component cards are available from the _Resources_ palette, under
the _Enhanced components_ section.

_Enhanced component cards_ can be fully configured and used within
Infrastructure Composer to design and build your serverless applications. We recommend using enhanced component cards when designing your applications with no existing code.

This table displays our enhanced components with links to the AWS CloudFormation or AWS Serverless Application Model (AWS SAM) template specification of the card’s featured resource:

| Card                                                  | Reference                                                                                                                                                                                                            |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon API Gateway                                    | [AWS::Serverless::API](../../../serverless-application-model/latest/developerguide/sam-resource-api.md "../../../serverless-application-model/latest/developerguide/sam-resource-api.md")                            |
| Amazon Cognito UserPool                               | [AWS::Cognito::UserPool](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.md")                                |
| Amazon Cognito UserPoolClient                         | [AWS::Cognito::UserPoolClient](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.md")              |
| Amazon DynamoDB Table                                 | [AWS::DynamoDB::Table](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md")                                      |
| Amazon EventBridge Event rule                         | [AWS::Events::Rule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.md")                                               |
| EventBridge Schedule                                  | [AWS::Scheduler::Schedule](../../../AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.md")                          |
| Amazon Kinesis Stream                                 | [AWS::Kinesis::Stream](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.md")                                      |
| AWS Lambda Function                                   | [AWS::Serverless::Function](../../../serverless-application-model/latest/developerguide/sam-resource-function.md "../../../serverless-application-model/latest/developerguide/sam-resource-function.md")             |
| Lambda Layer                                          | [AWS::Serverless::LayerVersion](../../../serverless-application-model/latest/developerguide/sam-resource-layerversion.md "../../../serverless-application-model/latest/developerguide/sam-resource-layerversion.md") |
| Amazon Simple Storage Service (Amazon S3) Bucket      | [AWS::S3::Bucket](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.md")                                                 |
| Amazon Simple Notification Service (Amazon SNS) Topic | [AWS::SNS::Topic](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.md")                                                     |
| Amazon Simple Queue Service (Amazon SQS) Queue        | [AWS::SQS::Queue](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.md")                                                     |
| AWS Step Functions State machine                      | [AWS::Serverless::StateMachine](../../../serverless-application-model/latest/developerguide/sam-resource-statemachine.md "../../../serverless-application-model/latest/developerguide/sam-resource-statemachine.md") |

## Example

The following is an example of an **S3 Bucket** enhanced component:

![An S3 Bucket enhanced component card.](images/aac_cards_07.png)

When you drag an **S3 Bucket** component card onto the canvas and view your template, you will see the following two AWS CloudFormation resources added to your
template:

- `AWS::S3::Bucket`
- `AWS::S3::BucketPolicy`

The **S3 Bucket** enhanced component card represents two AWS CloudFormation resources that are both required for an Amazon Simple Storage Service (Amazon S3) bucket to interact with
other services in your application.
