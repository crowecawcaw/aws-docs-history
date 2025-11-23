# Using AWS SAM with the AWS Serverless Application Repository

The AWS Serverless Application Model (AWS SAM) is an open-source framework that you can use to build [serverless applications](https://aws.amazon.com/serverless/ "https://aws.amazon.com/serverless/") on
AWS. For more information about using AWS SAM to build your serverless application,
see the [_AWS Serverless Application Model Developer Guide_](../../../serverless-application-model/latest/developerguide.md "../../../serverless-application-model/latest/developerguide.md").

When building applications that will be published to the AWS Serverless Application Repository, you must consider the
set of
supported
AWS Resources and Policy Templates available to use. The sections
below describe these topics in more detail.

## Supported AWS Resources in

the AWS Serverless Application Repository

The AWS Serverless Application Repository supports serverless applications that are composed of many AWS SAM and
CloudFormation resources. To see the complete list of AWS resources that are supported by
AWS Serverless Application Repository, see [List of Supported AWS Resources](list-supported-resources.md "list-supported-resources.md").

If you want to request support for an additional AWS resource, contact [AWS Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

###### Important

If your application template contains one of the following custom IAM roles or
resource policies, your application doesn't show up in search results by
default. Also, customers need to acknowledge the application's custom IAM roles
or resource policies before they can deploy the application. For more
information, see [Acknowledging Application Capabilities](acknowledging-application-capabilities.md "acknowledging-application-capabilities.md").

The list of resources that this applies to are:

- **IAM roles:** [AWS::IAM::Group](../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.md"), [AWS::IAM::InstanceProfile](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.md"), [AWS::IAM::Policy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md"), and [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md").
- **Resource policies:**
  [AWS::Lambda::LayerVersionPermission](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.md"), [AWS::Lambda::Permission](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md"), [AWS::Events::EventBusPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md"), [AWS::IAM:Policy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md"), [AWS::ApplicationAutoScaling::ScalingPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.md"), [AWS::S3::BucketPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.md"), [AWS::SQS::QueuePolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.md"), and [AWS::SNS:TopicPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.md").
  If your application contains the [AWS::Serverless::Application](../../../serverless-application-model/latest/developerguide/serverless-sam-template.md#serverless-sam-template-application "../../../serverless-application-model/latest/developerguide/serverless-sam-template.md#serverless-sam-template-application") resource, customers need to
  acknowledge that the application contains a **nested
  application** before they can deploy the application. For more
  information about nested applications, see [Nested Applications](../../../serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.md") in the _AWS Serverless Application Model Developer
  Guide_. For more information about acknowledging capabilities, see
  [Acknowledging
  Application Capabilities](acknowledging-application-capabilities.md "acknowledging-application-capabilities.md").

## Policy Templates

AWS SAM provides you with a list of policy templates to scope the permissions of
your Lambda functions to the resources that are used by your application. Using
policy templates don't require additional customer acknowledgments to search,
browse, or deploy the application.

For the list of standard AWS SAM policy templates, see [AWS SAM Policy
Templates](../../../serverless-application-model/latest/developerguide/serverless-policy-templates.md "../../../serverless-application-model/latest/developerguide/serverless-policy-templates.md") in the _[AWS Serverless Application Model Developer Guide](../../../serverless-application-model/latest/developerguide.md "../../../serverless-application-model/latest/developerguide.md")_.
