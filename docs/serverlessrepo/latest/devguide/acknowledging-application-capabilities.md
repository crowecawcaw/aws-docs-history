# Application Capabilities: IAM

Roles, Resource Policies, and Nested Applications

Before you can deploy an application, the AWS Serverless Application Repository checks the application’s template for
IAM roles, AWS resource policies, and nested applications that the template specifies that
it should create. IAM resources, such as an IAM role with full access, can modify any
resource in your AWS account. Therefore, we recommend that you review the permissions
associated with the application before proceeding so that you don't unintentionally create
resources with escalated permissions. To ensure that you've done so, you must acknowledge
that the application contains capabilities before the AWS Serverless Application Repository can deploy the application on
your behalf.

Applications can contain any of the following four capabilities:
`CAPABILITY_IAM`, `CAPABILITY_NAMED_IAM`,
`CAPABILITY_RESOURCE_POLICY`, and `CAPABILITY_AUTO_EXPAND`.

The following resources require you to specify `CAPABILITY_IAM` or
`CAPABILITY_NAMED_IAM`: [AWS::IAM::Group](../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.md"), [AWS::IAM::InstanceProfile](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.md"), [AWS::IAM::Policy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md"), and [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md"). If the
application contains IAM resources with custom names, you must specify
`CAPABILITY_NAMED_IAM`. For an example of how to specify capabilities, see
[Finding and
Acknowledging Application Capabilities (AWS CLI)](serverlessrepo-how-to-consume.md#acknowledging-application-capabilities-api "serverlessrepo-how-to-consume.md#acknowledging-application-capabilities-api").

The following resources require you to specify `CAPABILITY_RESOURCE_POLICY`:
[AWS::Lambda::LayerVersionPermission](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.md"), [AWS::Lambda::Permission](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.md"),
[AWS::Events::EventBusPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.md"), [AWS::IAM:Policy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.md"), [AWS::ApplicationAutoScaling::ScalingPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.md"), [AWS::S3::BucketPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.md"), [AWS::SQS::QueuePolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.md"), and
[AWS::SNS::TopicPolicy](../../../AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.md").

Applications that contain one or more nested applications require you to specify
`CAPABILITY_AUTO_EXPAND`. For more information about nested applications, see
[Nested Applications](../../../serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.md") in the _AWS Serverless Application Model Developer
Guide_.

## Finding and Acknowledging

Application Capabilities (Console)

You can find applications available in the AWS Serverless Application Repository on the [AWS Serverless Application Repository website](https://aws.amazon.com/serverless/serverlessrepo/ "https://aws.amazon.com/serverless/serverlessrepo/"), or
through the [Lambda console (on the **Create Function** page under the AWS Serverless Application Repository
tab)](https://console.aws.amazon.com/lambda/home?region=us-east-1#/create?tab=serverlessApps "https://console.aws.amazon.com/lambda/home?region=us-east-1#/create?tab=serverlessApps").

Applications that require acknowledgment of capabilities for creating custom IAM roles
or resource policies aren't shown in search results by default. To search for
applications that contain these capabilities, you must select the **Show apps
that create custom IAM roles or resource policies** check box.

You can review the capabilities of an application under the
**Permissions** tab when you select the application. To deploy the
application, you need to select the **I acknowledge this application creates
custom IAM roles or resource policies** check box. If you don’t acknowledge
these capabilities, you see this error message: **Acknowledgement required. To
deploy, check the box in Configure application parameters section**.

## Viewing Application

Capabilities (AWS CLI)

To view an application's capabilities using the AWS CLI, you first need the
application's Amazon Resource Name (ARN). You can then execute the following
command:

```
aws serverlessrepo get-application \
--application-id `application-arn`
```

The [requiredCapabilities](applications-applicationid.md#applications-applicationid-prop-version-requiredcapabilities "applications-applicationid.md#applications-applicationid-prop-version-requiredcapabilities") response property contains the list of application
capabilities that you need to acknowledge before you can deploy the application. Note
that if the [requiredCapabilities](applications-applicationid.md#applications-applicationid-prop-version-requiredcapabilities "applications-applicationid.md#applications-applicationid-prop-version-requiredcapabilities") property is empty, the application has no required
capabilities.
