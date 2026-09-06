

AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/). 

# Using AWS Lambda with an AWS Snowball Edge
<a name="using-lambda"></a>

AWS Lambda powered by AWS IoT Greengrass is a compute service that lets you to run serverless code (Lambda functions) locally on Snowball Edge devices. You can use Lambda to invoke Lambda functions on a Snowball Edge device with Message Queuing Telemetry Transport (MQTT) messages, run Python code in Lambda functions, and use them to call public AWS service endpoints in the cloud. To use Lambda functions with Snowball Edge devices, you must create your Snowball Edge jobs in an AWS Region supported by AWS IoT Greengrass. For a list of valid AWS Regions, see [AWS IoT Greengrass](https://docs.aws.amazon.com/general/latest/gr/greengrassv2.html) in the AWS General Reference. Lambda on Snowball Edge is available in Regions where Lambda and Snowball Edge devices are available.

**Note**  
If you allocate the minimum recommendation of 128 MB of memory for each of your functions, you can have up to seven Lambda functions in a single job.

**Topics**
+ [Getting started using Lambda on Snowball Edge](#function-recommendations)
+ [Deploy a Lambda function to a Snowball Edge device](#import-lambda-gg)

## Getting started using Lambda on Snowball Edge
<a name="function-recommendations"></a>

Before you create a Lambda function in the Python language to run on your Snowball Edge, we recommend that you familiarize yourself with the following services, concepts, and related topics.

### Prerequisites for AWS IoT Greengrass on Snowball Edge
<a name="greengrass-rec"></a>

AWS IoT Greengrass is software that extends AWS Cloud capabilities to local devices. AWS IoT Greengrass makes it possible for local devices to collect and analyze data closer to the source of information, while also securely communicating with each other on local networks. More specifically, developers who use AWS IoT Greengrass can author serverless code (Lambda functions) in the AWS Cloud. They can then conveniently deploy this code to devices for local execution of applications.

The following AWS IoT Greengrass concepts are important to understand when using AWS IoT Greengrass with a Snowball Edge:
+ **AWS IoT Greengrass requirements** – For a full list of AWS IoT Greengrass requirements, see [Requirements](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-gs.html#gg-requirements) in the *AWS IoT Greengrass Version 2 Developer Guide*. 
+ **AWS IoT Greengrass core** – Download the AWS IoT Greengrass core software and install it on an EC2 instance running on the device. See [Using AWS IoT Greengrass on Amazon EC2 instances](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-green-grass.html) in this guide.

  To use Lambda functions on a Snowball Edge device, you must first install AWS IoT Greengrass Core software on an Amazon EC2 instance on the device. The Lambda functions you plan to use on the Snowball Edge device must be created by the same account you will use to install AWS IoT Greengrass on the Snowball Edge device. For information about installing AWS IoT Greengrass on your Snowball Edge device, see [Using AWS IoT Greengrass to run pre-installed software on Amazon EC2-compatible instances on Snowball Edge](using-green-grass.md).
+ **AWS IoT Greengrass group** – A Snowball Edge device is part of an AWS IoT Greengrass group as the group's core device. For more information about groups, see [AWS Greengrass IoT Groups](https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html#gg-group) in the *AWS IoT Greengrass Developer Guide*.
+ **MQTT** – AWS IoT Greengrass uses the industry-standard, lightweight MQTT protocol to communicate within a group. Any device or software compatible with MQTT in your AWS IoT Greengrass group can invoke MQTT messages. These messages can invoke Lambda functions, if you define the related MQTT message to do so.

### Prerequisites for AWS Lambda on Snowball Edge
<a name="lambda-rec"></a>

AWS Lambda is a compute service that lets you run code without provisioning or managing servers. The following Lambda concepts are important to understand when using Lambda with a Snowball Edge:
+ **Lambda functions** – Your custom code, uploaded and published to Lambda and used on a Snowball Edge. For more information, see [Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-function) in the *AWS Lambda Developer Guide*.
+ **Lambda console** – The console in which you upload, update, and publish your Python-language Lambda functions for use on a Snowball Edge. For more information about the [Lambda console](https://console.aws.amazon.com/lambda), see [Lambda console](https://docs.aws.amazon.com/lambda/latest/dg/foundation-console.html) in the *AWS Lambda Developer Guide*.
+ **Python** – The high-level programming language used for your Lambda functions powered by AWS IoT Greengrass on a Snowball Edge. AWS IoT Greengrass supports Python version 3.8.x.

## Deploy a Lambda function to a Snowball Edge device
<a name="import-lambda-gg"></a>

To run a Lambda function on a Snowball Edge device in an AWS IoT Greengrass group, import the function as a component. For complete information about importing a function as a component using the AWS IoT Greengrass console, see [Import a Lambda function as a component (console)](https://docs.aws.amazon.com/greengrass/v2/developerguide/import-lambda-function-console.html) in the AWS IoT Greengrass Version 2 Developer Guide.

1. In the AWS IoT console, on the **Greengrass components** page, choose **Create component**.

1. In **Component source**, choose **Import Lambda function**. In **Lambda function**, choose the name of your function. In **Lambda function version**, choose the version of your function.

1. To subscribe the function to messages on which it can act, choose **Add event source** and choose the event. In **Timeout (seconds)**, provide a timeout period in seconds.

1. In **Pinned**, choose whether or not to pin your function.

1. Choose **Create component**

1. Choose **Deploy**.

1. In **Deployment**, choose **Add to existing deployment**, then choose your Greengrass group. Choose **Next**.

1. In **Public components**, choose these components:
   + **aws.greengrass.Cli**
   + **aws.greengrass.LambdaLauncher**
   + **aws.greengrass.LambdaManager**
   + **aws.greengrass.LambdaRuntimes**
   + **aws.greengrass.Nucleus**

1. Choose **Deploy**.