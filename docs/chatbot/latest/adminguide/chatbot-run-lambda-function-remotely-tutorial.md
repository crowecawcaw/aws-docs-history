AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Tutorial: Using Amazon Q Developer in chat applications to run

an AWS Lambda function remotely

In this tutorial you use Amazon Q Developer in chat applications to run a Lambda function remotely and check the status
of the Lambda function using Amazon CloudWatch. A Lambda function is a self contained block of
organized resuable code that you write. Lambda functions are useful because they are run
without provisioning or managing servers. Additionally, they are only invoked when needed
based on your specifications. There are steps at the end of this tutorial to delete the
resources you created.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Step 1: Create a Lambda function](#create-lambda-function "#create-lambda-function")
- [Step 2: Create an SNS topic](#create-sns-topic "#create-sns-topic")
- [Step 3: Configure a CloudWatch alarm](#configure-cloudwatch-alarm "#configure-cloudwatch-alarm")
- [Step 4: Configure a Slack client for
  Amazon Q Developer in chat applications](#create-chatbot-slack-config "#create-chatbot-slack-config")
- [Step 5: Invoke a Lambda function from
  Slack](#invoke-lambda-function "#invoke-lambda-function")
- [Step 6: Test the CloudWatch alarm](#test-cloudwatch-alarm "#test-cloudwatch-alarm")
- [Step 7: Clean up resources](#clean-up-resources "#clean-up-resources")

## Prerequisites

This tutorial assumes that you have some familiarity with the Lambda, Amazon Q Developer in chat applications, and
CloudWatch consoles.

For more information, see the following topics:

- [Getting started with AWS Lambda](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md") in the _AWS Lambda Developer
  Guide_.
- [Setting up Amazon Q Developer in chat applications](setting-up.md "setting-up.md") in the _Amazon Q Developer in chat applications Administrator
  Guide._
- [Understanding Amazon Q Developer in chat applications permissions](understanding-permissions.md "understanding-permissions.md")
  in the _Amazon Q Developer in chat applications Administrator
  Guide._
- [Getting Set Up
  with CloudWatch](../../../AmazonCloudWatch/latest/monitoring/GettingSetup.md "../../../AmazonCloudWatch/latest/monitoring/GettingSetup.md") in the _Amazon CloudWatch User Guide._

The AWS Region that you select while setting up these consoles should be the same
Region you specify in your Slack channel when your first AWS Command Line Interface
(AWS CLI) command in [Step 5: Invoke a Lambda function from
Slack](#invoke-lambda-function "#invoke-lambda-function").

## Step 1: Create a Lambda function

In this procedure you create a Lambda function in the console and test it.

###### To create a Lambda function

1. Sign in to the AWS Management Console and open the Lambda console at [console.aws.amazon.com/lambda](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. Choose **Author From Scratch**.
4. In **Function Name**, enter:
   `myHelloWorld`
5. Choose **Create Function**.
6. Copy and paste the following example code into
   `index.js`.

```
export const handler = async (event) => {
  // TODO implement
  const response = 'Hello World!'
  return response;
};
   };
```

7. Choose **Deploy**.
8. Choose **Test**.
9. In **Event Name**, enter:
   `myHelloWorld`
10. Choose **Save**.
11. Choose **Test** and then verify that the **Execution
    results** tab displays Response: "Hello World!"

## Step 2: Create an SNS topic

CloudWatch uses Amazon SNS to send notifications. First, you create an SNS topic and subscribe to
it using your email. Later in the tutorial you use this SNS topic to configure
Amazon Q Developer in chat applications.

###### To create an SNS topic

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/ "https://console.aws.amazon.com/sns/").
2. In the left navigation pane, choose **Topics**.
3. Choose **Create Topic**.
4. Create a topic with the following settings:
   1. **Type** – Standard
   2. **Name** –
      `myHelloWorldNotifications`
   3. **Display name** –
      `myHelloWorld`

5. Choose **Create topic**.
6. Choose **Create subscription**.
7. Create a subscription with the following settings:
   1. **Protocol** –
      `Email`
   2. **Endpoint** – Your email address

8. Confirm subscription to the SNS by checking your email and choosing the
   link.

## Step 3: Configure a CloudWatch alarm

A CloudWatch alarm monitors your Lambda function and sends a notification if an error
occurs.

###### To create a CloudWatch alarm

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**.
5. Choose **Lambda**.
6. Choose **By Function Name**.
7. Choose **myHelloWorld errors**.
8. Change the following settings:
   1. **Period** – **1
      minute**
   2. **Whenever Errors is**
      `Greater`
      **than**
      `0`
   3. **Send notifications to** –
      `myHelloWorldNotifications`
   4. **Alarm name** –
      `myHelloWorld-alarm`
   5. **Alarm description** – `Lambda
myHelloWorld alarm`

9. Choose **Create alarm**.

## Step 4: Configure a Slack client for

Amazon Q Developer in chat applications

You can configure a Slack client using Amazon Q Developer in chat applications to to run different commands in Slack
using the AWS CLI. In this tutorial you use AWS CLI to invoke your Lambda function from
Slack.

###### To create a Slack client

1. Open the [Amazon Q Developer in chat applications
   console](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. Under **Configure a Chat client** choose
   **Slack**, and then choose
   **Configure**.

###### Important

When you choose **Configure**, you are momentarily
navigated away from the Amazon Q Developer in chat applications console. 3. In the upper right corner, choose the dropdown list, and then choose the Slack
workspace that you want to use with Amazon Q Developer in chat applications.

###### Note

There's no limit to the number of workspaces that you can set up for
Amazon Q Developer in chat applications, but you must set up each workspace one at a time. 4. Choose **Allow**. 5. Choose **Configure new channel**. 6. Under **Configuration details**, for
**Name**, enter `myHelloWorld`. 7. Under **Channel type**, choose
**Private**.

    1. Navigate to Slack and create a private channel by choosing the
     **+** button to the right of
     **Channels**.
    2. Choose **Create a channel**.
    3. Name the channel `myHelloWorld`.
    4. Choose to make the channel private.
    5. Choose **Create**.
    6. When prompted to add people, choose **x**.
    7. Navigate back to the Amazon Q Developer in chat applications console and enter the private channel
     ID.

8. Define the **Permissions** that the chatbot uses for
   messaging your Slack chat room as shown following:
   1. For **Role settings**, choose **Channel role**.
   2. For **Channel role**, choose **Create an IAM role using a template**.
   3. For **Role name**, enter
      `myHelloWorldRole`.
   4. For **Policy Templates**, select **Read-only
      command permissions** and **Lambda-invoke command
      permissions.**
   5. For **Channel guardrail policies**, select
      **AWS-Chatbot-LambdaInvoke-Policy-e4aef1dc-0da7-4ac5-b506-d282beac41ae**.

9. In the SNS topics section, choose the appropriate AWS Region under
   **Region**.
10. Under **Topics**, select the
    **myHelloWorldNotifcations** topic.
11. Choose **Configure**.

## Step 5: Invoke a Lambda function from

Slack

After you configure a chatbot in Amazon Q Developer in chat applications, you can invoke Lambda functions from Slack
using AWS CLI syntax. To interact with Amazon Q Developer in chat applications in Slack, enter
`@Amazon Q` followed by an AWS CLI command. For more information, see
[Running AWS CLI commands from chat channels using Amazon Q Developer in chat applications](chatbot-cli-commands.md "chatbot-cli-commands.md") in the
_Amazon Q Developer in chat applications Administrator Guide._

###### To invoke a Lambda function

1. Invite Amazon Q Developer in chat applications to your channel by doing the following in Slack:
   1. Enter `@Amazon Q`.
   2. Choose **Invite to Channel.**

   ###### Tip

   You only have to invite Amazon Q Developer in chat applications to the channel once.

   If AWS is not listed as a valid member of the channel, you need to add the Amazon Q Developer in chat applications app to the Slack workspace. For more information, see the [Getting started guide for
   Amazon Q Developer in chat applications](getting-started.md "getting-started.md").

2. Enter the following command in Slack:

```
@Amazon Q lambda invoke --function-name myHelloWorld --region `<your region>`
```

###### Important

Replace `<your region>` with the same AWS
Region you set while using the Lambda, CloudWatch, and Amazon Q Developer in chat applications consoles. You only
need to specify the AWS Region in the channel once when you type your first
AWS CLI command in Slack.

###### Tip

Amazon Q Developer in chat applications also supports certain simplified AWS CLI syntaxes. For example, the
simplified version of the previous command is shown following:

```
@Amazon Q invoke myHelloWorld --region `<your region>`
```

3. Choose **Yes**.
4. The following output is shown:

```
ExecutedVersion: $LATEST
Payload: \"Hello World\"
StatusCode: 200
```

###### Troubleshooting

If you try to run your Lambda function in Slack and you encounter errors referring
to the following permissions, revisit step 8 of the [Step 4: Configure a Slack client for
Amazon Q Developer in chat applications](#create-chatbot-slack-config "#create-chatbot-slack-config") procedure and verify that you have
the correct permissions assigned to your role:

- **Lambda-invoke command permissions**
- **Read-only command permissions**

## Step 6: Test the CloudWatch alarm

In this step, you update the myHelloWorld function so that it returns an error, which
triggers the CloudWatch alarm. By testing the alarm you can confirm that it's configured
correctly and that you can view CloudWatch alarms in Slack (in addition to logs).

###### To test the CloudWatch alarm

1. Open the Lambda console [Functions
   page](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **myHelloWorld**.
3. Copy and paste the following example code into the Lambda function code:

```
exports.handler = async (event) => {
    throw new Error('this is an error');
};
```

4. Choose **Deploy** and confirm your changes have been deployed
   by viewing the label next to the **Deploy** button.
5. Return to your Slack channel and then enter the following command:

```
@Amazon Q invoke myHelloWorld
```

6. An error appears in your output, and you receive a CloudWatch alarm notification in
   Slack and an email. It might take a few minutes for you to receive the
   notifications.
7. To view logs, choose **Show logs** or **Show error
   logs**.

###### Troubleshooting

If you don't receive a notification in Slack or an email from CloudWatch, navigate to
the CloudWatch console and on the left of the screen. Under **Alarms**,
choose **In alarm** to confirm that your alarm has triggered. Your
alarm name should appear on this page if it has been triggered successfully.

## Step 7: Clean up resources

You can remove any resources created for this tutorial that you don't want to keep by
navigating to the specific service’s console and deleting the resource. Removing
unwanted or unused resources is beneficial because it lowers overall costs to
you.

###### To delete the Lambda function

1. Open the [Lambda console](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **myHelloWordFunction**.
3. Choose **Actions** and then choose
   **delete**.

###### To delete the CloudWatch alarm

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Insufficient**.
3. Choose myHelloWorld-alarm by selecting the check box.
4. Choose **Actions** and then choose
   **delete**.

###### To delete the Amazon Q Developer in chat applications configuration

1. Open the [Amazon Q Developer in chat applications
   console](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. Choose **Slack.**
3. Choose the radio button next to the channel you created and then choose
   **Delete**.
