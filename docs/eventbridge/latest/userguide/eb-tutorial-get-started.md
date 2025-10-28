# Tutorial: Create a sample Amazon EventBridge application

You can use EventBridge to route [events](eb-events.md "eb-events.md") to specific Lambda functions using [rules](eb-rules.md "eb-rules.md").

In this tutorial, you’ll use the AWS CLI, Node.js, and the code in the [GitHub
repo](https://github.com/aws-samples/amazon-eventbridge-producer-consumer-example "https://github.com/aws-samples/amazon-eventbridge-producer-consumer-example") to create the following:

- An [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md")
  function that produces events for bank ATM transactions.
- Three Lambda functions to use as [targets](eb-targets.md "eb-targets.md") of an EventBridge rule.
- and the rule that routes the created
  events to the correct downstream function based on an [event
  pattern](eb-event-patterns.md "eb-event-patterns.md").
  This example uses AWS SAM templates to define the EventBridge rules. To learn more about using AWS SAM
  templates with EventBridge see [Using AWS Serverless Application Model templates to deploy Amazon EventBridge resources](eb-use-sam.md "eb-use-sam.md").

In the repo, the _atmProducer_ subdirectory contains `handler.js`, which represents the ATM service producing events.
This code is a Lambda handler written in Node.js, and publishes events to EventBridge via the [AWS SDK](https://www.npmjs.com/package/aws-sdk "https://www.npmjs.com/package/aws-sdk") using
this line of JavaScript code.

```
const result = await eventbridge.putEvents(params).promise()
```

This directory also contains `events.js`, listing several test transactions in an Entries array. A single event is defined in JavaScript as follows:

```
{
  // Event envelope fields
  Source: 'custom.myATMapp',
  EventBusName: 'default',
  DetailType: 'transaction',
  Time: new Date(),

  // Main event body
  Detail: JSON.stringify({
    action: 'withdrawal',
    location: 'MA-BOS-01',
    amount: 300,
    result: 'approved',
    transactionId: '123456',
    cardPresent: true,
    partnerBank: 'Example Bank',
    remainingFunds: 722.34
  })
}
```

The _Detail_ section of the event specifies transaction attributes. These include the location of the ATM, the amount, the partner bank,
and the result of the transaction.

The `handler.js` file in the _atmConsumer_ subdirectory contains three functions:

```
exports.case1Handler = async (event) => {
  console.log('--- Approved transactions ---')
  console.log(JSON.stringify(event, null, 2))
}

exports.case2Handler = async (event) => {
  console.log('--- NY location transactions ---')
  console.log(JSON.stringify(event, null, 2))
}

exports.case3Handler = async (event) => {
  console.log('--- Unapproved transactions ---')
  console.log(JSON.stringify(event, null, 2))
}
```

Each function receives transaction events, which are logged via the `console.log` statements
to [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md"). The consumer functions operate independently of the producer and are unaware of the source
of the events.

The routing logic is contained in the EventBridge rules that are deployed by the application’s AWS SAM template. The rules evaluate the incoming stream of events, and
route matching events to the target Lambda functions.

The rules use event patterns that are JSON objects with the same structure as the events they match. Here's the event pattern for the one of the rules.

```
{
  "detail-type": ["transaction"],
  "source": ["custom.myATMapp"],
  "detail": {
    "location": [{
      "prefix": "NY-"
    }]
  }
}
```

###### Steps:

- [Prerequisites](#eb-gs-prereqs "#eb-gs-prereqs")
- [Step 1: Create application](#eb-gs-create-application "#eb-gs-create-application")
- [Step 2: Run application](#eb-gs-run-application "#eb-gs-run-application")
- [Step 3: Check the logs and verify the application works](#eb-gs-check-logs "#eb-gs-check-logs")
- [Step 4: Clean up your resources](#cleanup "#cleanup")

## Prerequisites

To complete this tutorial, you'll need the following resources:

- An AWS account. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")
  if you don't already have one.
- AWS CLI installed. To install the AWS CLI, see the [Installing, updating, and uninstalling the AWS CLI version 2](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md").
- Node.js 12.x installed. To install Node.js, see [Downloads](https://nodejs.org/en/download/ "https://nodejs.org/en/download/").

## Step 1: Create application

To set up the example application, you'll use the AWS CLI and Git to create the AWS resources you'll need.

###### To create the application

1. [Sign in to
   AWS](https://console.aws.amazon.com/console/home "https://console.aws.amazon.com/console/home").
2. [Install
   Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "https://git-scm.com/book/en/v2/Getting-Started-Installing-Git") and [install the AWS Serverless Application Model CLI](../../../serverless-application-model/latest/developerguide/serverless-sam-cli-install.md "../../../serverless-application-model/latest/developerguide/serverless-sam-cli-install.md") on your local machine.
3. Create a new directory, and then navigate to that directory in a terminal.
4. At the command line, enter `git clone
https://github.com/aws-samples/amazon-eventbridge-producer-consumer-example`.
5. At the command line run the following command:

```
cd ./amazon-eventbridge-producer-consumer-example
sam deploy --guided
```

6. In the terminal, do the following:
   1. For `**Stack Name**`, enter a name for the stack. For example, name
      the stack `Test`.
   2. For `**AWS Region**`, enter the Region. For example,
      `us-west-2`.
   3. For `**Confirm changes before deploy**`, enter
      `Y`.
   4. For `**Allow SAM CLI IAM role creation**`, enter
      `Y`
   5. For `**Save arguments to configuration file**`, enter
      `Y`
   6. For `**SAM configuration file**`, enter
      `samconfig.toml`.
   7. For `**SAM configuration environment**`, enter
      `default`.

## Step 2: Run application

Now that you've set up the resources, you'll use the console to test the functions.

###### To run the application

1. Open the [Lambda console](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/") in the same Region where you deployed the AWS SAM application.
2. There are four Lambda functions with the prefix **atm-demo**. Select the **atmProducerFn** function, then choose
   **Actions**, **Test**.
3. Enter `Test` for the **Name**.
4. Choose **Test**.

## Step 3: Check the logs and verify the application works

Now that you've run the application, you'll use the console to check the CloudWatch Logs.

###### To check the logs

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/") in the same Region where you ran the AWS SAM application.
2. Choose **Logs**, and then choose **Log groups**.
3. Select the log group containing **atmConsumerCase1**. You see two streams representing the two transactions approved by the ATM. Choose a
   log stream to view the output.
4. Navigate back to the list of log groups, and then select the log group containing
   **atmConsumerCase2**. You'll see two streams representing the two
   transactions matching the _New York_ location filter.
5. Navigate back to the list of log groups, and select the log group containing
   **atmConsumerCase3**. Open the stream to see the denied
   transactions.

## Step 4: Clean up your resources

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you are no longer using, you prevent unnecessary charges to your AWS account.

###### To delete the EventBridge rule(s)

1. Open the [Rules page](https://console.aws.amazon.com/events/home#/rules "https://console.aws.amazon.com/events/home#/rules") of the EventBridge console.
2. Select the rule(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.

###### To delete the Lambda function(s)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Select the function(s) that you created.
3. Choose **Actions**, **Delete**.
4. Choose **Delete**.

###### To delete the CloudWatch Logs log group(s)

1. Open the [Cloudwatch console](https://console.aws.amazon.com/Cloudwatch/home "https://console.aws.amazon.com/Cloudwatch/home").
2. Choose **Logs**, **Log groups**.
3. Select the log group(s) that were created in this tutorial.
4. Choose **Actions**, **Delete log group(s)**.
5. Choose **Delete**.
