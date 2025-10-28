End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Deploy a Lambda function for AWS IoT Events

using AWS CloudFormation

This tutorial uses an AWS CloudFormation template to deploy a Lambda function. This template
automatically creates an IAM role that allows the Lambda function to work with
Amazon SES and Amazon SNS.

The following shows you how to use the AWS Command Line Interface (AWS CLI) to create a
CloudFormation stack.

1. In your device's terminal, run `aws --version` to check if you installed the AWS CLI.
   For more information, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
   in the _AWS Command Line Interface User Guide_.
2. Run `aws configure list` to check if you configured the AWS CLI in the AWS Region
   that has all your AWS resources for this tutorial. For more information, see [Set and view configuration settings using commands](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-methods "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-methods")
   in the _AWS Command Line Interface User Guide_
3. Download the CloudFormation template, [notificationLambda.template.yaml.zip](samples/notificationLambda.template.yaml.md "samples/notificationLambda.template.yaml.md").

###### Note

If you have difficulty downloading the file, the template is also
available in the [CloudFormation template](alarms-create-lambda.md#cfn-template "alarms-create-lambda.md#cfn-template"). 4. Unzip the content and save it locally as
`notificationLambda.template.yaml`. 5. Open a terminal on your device and navigate to the directory where you
downloaded the `notificationLambda.template.yaml`
file. 6. To create a CloudFormation stack, run the following command:

```
aws cloudformation create-stack --stack-name notificationLambda-stack --template-body file://notificationLambda.template.yaml --capabilities CAPABILITY_IAM
```

You might modify this CloudFormation template to customize the Lambda function and
its behavior.

###### Note

AWS Lambda retries function errors twice. If the function doesn't have
enough capacity to handle all incoming requests, events might wait in the
queue for hours or days to be sent to the function. You can configure an
undelivered-message queue (DLQ) on the function to capture events that
weren't successfully processed. For more information, see [Asynchronous invocation](../../../lambda/latest/dg/invocation-async.md "../../../lambda/latest/dg/invocation-async.md")
in the _AWS Lambda Developer Guide_.

You can also create or configure the stack in the CloudFormation console. For more
information, see [Working with
stacks](../../../AWSCloudFormation/latest/UserGuide/stacks.md "../../../AWSCloudFormation/latest/UserGuide/stacks.md"), in the _AWS CloudFormation User Guide_.
