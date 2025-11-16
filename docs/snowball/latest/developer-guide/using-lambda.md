AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using AWS Lambda with an AWS Snowball Edge

AWS Lambda powered by AWS IoT Greengrass is a compute service that lets you to run serverless code (Lambda functions) locally on Snowball Edge devices. You can use Lambda to invoke Lambda functions on a Snowball Edge device with Message Queuing Telemetry Transport (MQTT) messages, run Python code in Lambda functions, and use them to call public AWS service endpoints in the cloud. To use Lambda functions with Snowball Edge devices, you must create your Snowball Edge jobs in an AWS Region supported by AWS IoT Greengrass. For a list of valid AWS Regions, see [AWS IoT Greengrass](../../../general/latest/gr/greengrassv2.md "../../../general/latest/gr/greengrassv2.md") in
the AWS General Reference. Lambda on Snowball Edge
is available in Regions where Lambda and Snowball Edge devices are available.

###### Note

If you allocate the minimum recommendation of 128 MB of memory for each of your functions, you can have up to seven Lambda functions in a single job.

###### Topics

- [Getting started using Lambda on Snowball Edge](#function-recommendations "#function-recommendations")
- [Deploy a Lambda function to a Snowball Edge device](#import-lambda-gg "#import-lambda-gg")

## Getting started using Lambda on Snowball Edge

Before you create a Lambda function in the Python language to run on your Snowball Edge, we
recommend that you familiarize yourself with the following services, concepts, and
related topics.

### Prerequisites for AWS IoT Greengrass on Snowball Edge

AWS IoT Greengrass is software that extends AWS Cloud capabilities to local devices.
AWS IoT Greengrass makes it possible for local devices to collect and analyze data closer to
the source of information, while also securely communicating with each other on
local networks. More specifically, developers who use AWS IoT Greengrass can author serverless
code (Lambda functions) in the AWS Cloud. They can then conveniently deploy this code
to devices for local execution of applications.

The following AWS IoT Greengrass concepts are important to understand when using AWS IoT Greengrass with a
Snowball Edge:

- **AWS IoT Greengrass requirements** – For a full list
  of AWS IoT Greengrass requirements, see [Requirements](../../../greengrass/latest/developerguide/gg-gs.md#gg-requirements "../../../greengrass/latest/developerguide/gg-gs.md#gg-requirements") in the _AWS IoT Greengrass Version 2 Developer Guide_.
- **AWS IoT Greengrass core** – Download the AWS IoT Greengrass core software and install it on an EC2 instance running on the device. See [Using AWS IoT Greengrass on Amazon EC2 instances](using-green-grass.md "using-green-grass.md") in this guide.

To use Lambda functions on a Snowball Edge device, you must first install AWS IoT Greengrass Core software on an Amazon EC2 instance on the device. The Lambda functions you plan to use on the Snowball Edge device must be created by the same account you will use to install AWS IoT Greengrass on the Snowball Edge device. For information about installing AWS IoT Greengrass on your Snowball Edge device, see [Using AWS IoT Greengrass to run pre-installed software on Amazon EC2-compatible instances on Snowball Edge](using-green-grass.md "using-green-grass.md").

- **AWS IoT Greengrass group** – A Snowball Edge device is
  part of an AWS IoT Greengrass group as the group's core device. For more information about
  groups, see [AWS Greengrass IoT Groups](../../../greengrass/latest/developerguide/what-is-gg.md#gg-group "../../../greengrass/latest/developerguide/what-is-gg.md#gg-group") in the _AWS IoT Greengrass Developer
  Guide_.
- **MQTT** – AWS IoT Greengrass uses the industry-standard, lightweight MQTT protocol to communicate within a group. Any device or software compatible with MQTT in your AWS IoT Greengrass group can invoke MQTT messages. These messages can invoke Lambda functions, if you define the related MQTT message to do so.

### Prerequisites for AWS Lambda on Snowball Edge

AWS Lambda is a compute service that lets you run code without provisioning or
managing servers. The following Lambda concepts are important to understand when
using Lambda with a Snowball Edge:

- **Lambda functions** – Your custom code,
  uploaded and published to Lambda and used on a Snowball Edge. For more
  information, see [Lambda Functions](../../../lambda/latest/dg/gettingstarted-concepts.md#gettingstarted-concepts-function "../../../lambda/latest/dg/gettingstarted-concepts.md#gettingstarted-concepts-function") in the
  _AWS Lambda Developer Guide_.
- **Lambda console** – The console in
  which you upload, update, and publish your Python-language Lambda functions
  for use on a Snowball Edge. For more information about the [Lambda console](https://console.aws.amazon.com/lambda "https://console.aws.amazon.com/lambda"), see [Lambda console](../../../lambda/latest/dg/foundation-console.md "../../../lambda/latest/dg/foundation-console.md") in the
  _AWS Lambda Developer Guide_.
- **Python** – The high-level programming
  language used for your Lambda functions powered by AWS IoT Greengrass on a Snowball Edge.
  AWS IoT Greengrass supports Python version 3.8.x.

## Deploy a Lambda function to a Snowball Edge device

To run a Lambda function on a Snowball Edge device in an AWS IoT Greengrass group, import the function as a component. For complete information about importing a function as a component using the AWS IoT Greengrass console, see [Import a Lambda function as a component (console)](../../../greengrass/v2/developerguide/import-lambda-function-console.md "../../../greengrass/v2/developerguide/import-lambda-function-console.md") in the AWS IoT Greengrass Version 2 Developer Guide.

1. In the AWS IoT console, on the **Greengrass components** page, choose **Create component**.
2. In **Component source**, choose **Import Lambda function**. In **Lambda function**, choose the name of your function. In **Lambda function version**, choose the version of your function.
3. To subscribe the function to messages on which it can act, choose **Add event source** and choose the event. In **Timeout (seconds)**, provide a timeout period in seconds.
4. In **Pinned**, choose whether or not to pin your function.
5. Choose **Create component**
6. Choose **Deploy**.
7. In **Deployment**, choose **Add to existing deployment**, then choose your Greengrass group. Choose **Next**.
8. In **Public components**, choose these components:
   - **aws.greengrass.Cli**
   - **aws.greengrass.LambdaLauncher**
   - **aws.greengrass.LambdaManager**
   - **aws.greengrass.LambdaRuntimes**
   - **aws.greengrass.Nucleus**

9. Choose **Deploy**.
