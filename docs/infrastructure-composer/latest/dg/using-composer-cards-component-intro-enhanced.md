

# Enhanced component cards in Infrastructure Composer
<a name="using-composer-cards-component-intro-enhanced"></a>

Enhanced component cards are created and managed by Infrastructure Composer. Each card contains CloudFormation resources that are commonly used together when building applications on AWS. Their infrastructure code is created by Infrastructure Composer following AWS best practices. Enhanced component cards are a great way to start designing your application.

Enhanced component cards are available from the *Resources* palette, under the *Enhanced components* section.

*Enhanced component cards* can be fully configured and used within Infrastructure Composer to design and build your serverless applications. We recommend using enhanced component cards when designing your applications with no existing code.

This table displays our enhanced components with links to the AWS CloudFormation or AWS Serverless Application Model (AWS SAM) template specification of the card’s featured resource:


| Card | Reference | 
| --- | --- | 
| Amazon API Gateway | [AWS::Serverless::API](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-api.html) | 
| Amazon Cognito UserPool | [AWS::Cognito::UserPool](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html) | 
| Amazon Cognito UserPoolClient | [AWS::Cognito::UserPoolClient](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html) | 
| Amazon DynamoDB Table | [AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html) | 
| Amazon EventBridge Event rule | [AWS::Events::Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html) | 
| EventBridge Schedule | [AWS::Scheduler::Schedule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-scheduler-schedule.html) | 
| Amazon Kinesis Stream | [AWS::Kinesis::Stream](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html) | 
| AWS Lambda Function | [AWS::Serverless::Function](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html) | 
| Lambda Layer | [AWS::Serverless::LayerVersion](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-layerversion.html) | 
| Amazon Simple Storage Service (Amazon S3) Bucket | [AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html) | 
| Amazon Simple Notification Service (Amazon SNS) Topic | [AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-topic.html) | 
| Amazon Simple Queue Service (Amazon SQS) Queue | [AWS::SQS::Queue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html) | 
| AWS Step Functions State machine | [AWS::Serverless::StateMachine](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-statemachine.html) | 

## Example
<a name="w2aab9c21c13"></a>

The following is an example of an **S3 Bucket** enhanced component:

![An S3 Bucket enhanced component card.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac_cards_07.png)


When you drag an **S3 Bucket** component card onto the canvas and view your template, you will see the following two CloudFormation resources added to your template:
+ `AWS::S3::Bucket`
+ `AWS::S3::BucketPolicy`

The **S3 Bucket** enhanced component card represents two CloudFormation resources that are both required for an Amazon Simple Storage Service (Amazon S3) bucket to interact with other services in your application.