# Deploying and testing

the Amazon SNS event fork pipelines sample application

To accelerate the development of your event-driven applications, you can subscribe
event-handling pipelines—powered by AWS Event Fork Pipelines—to Amazon SNS topics. AWS Event Fork Pipelines is a suite of open-source
[nested applications](../../../serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.md"), based on the [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/ "https://aws.amazon.com/serverless/sam/") (AWS
SAM), which you can deploy directly from the [AWS Event Fork Pipelines suite](https://serverlessrepo.aws.amazon.com/applications?query=aws-event-fork-pipelines "https://serverlessrepo.aws.amazon.com/applications?query=aws-event-fork-pipelines") (choose **Show apps that create custom IAM roles or resource policies**) into your AWS account. For more information, see [How AWS Event Fork Pipelines works](sns-fork-pipeline-as-subscriber.md#how-sns-fork-works "sns-fork-pipeline-as-subscriber.md#how-sns-fork-works").

This page shows how you can use the AWS Management Console to deploy and test the AWS Event Fork Pipelines
sample application.

###### Important

To avoid incurring unwanted costs after you finish deploying the AWS Event Fork Pipelines
sample application, delete its CloudFormation stack. For more information, see [Deleting a Stack on the CloudFormation
Console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.md") in the _AWS CloudFormation User Guide_.
