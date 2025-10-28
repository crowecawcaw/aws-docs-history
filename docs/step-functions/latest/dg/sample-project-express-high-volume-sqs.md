# Process high-volume messages from Amazon SQS

with Step Functions Express workflows

This sample project demonstrates how to use an AWS Step Functions Express Workflow to process
messages or data from a high-volume event source, such as Amazon Simple Queue Service (Amazon SQS). Because Express
Workflows can be started at a very high rate, they are ideal for high-volume event processing or
streaming data workloads.

Here are two commonly used methods to execute your state machine from an event
source:

- **Configure an Amazon CloudWatch Events rule to start a state machine execution
  whenever the event source emits an event.** For more information, see [Creating a
  CloudWatch Events Rule That Triggers on an Event](../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md "../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md").
- **Map the event source to a Lambda function, and write function code
  to execute your state machine.** The AWS Lambda function is invoked each time your
  event source emits an event, in turn starting a state machine execution. For more
  information see [Using
  AWS Lambda with Amazon SQS](../../../lambda/latest/dg/with-sqs.md "../../../lambda/latest/dg/with-sqs.md").
  This sample project uses the second method to start an execution each time the Amazon SQS queue
  sends a message. You can use a similar configuration to trigger Express Workflows execution from
  other event sources, such as Amazon Simple Storage Service (Amazon S3), Amazon DynamoDB, and Amazon Kinesis.

For more information about Express Workflows and Step Functions service integrations, see the
following:

- [Choosing workflow type in Step Functions](choosing-workflow-type.md "choosing-workflow-type.md")
- [Integrating services with Step Functions](integrate-services.md "integrate-services.md")
- [Step Functions service quotas](service-quotas.md "service-quotas.md")

## Step 1: Create the state machine

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/") and choose **Create state machine**.
2. Choose **Create from template** and find the related starter template. Choose **Next** to continue.
3. Choose how to use the template:
   1. **Run a demo** – creates a read-only state machine. After review, you can create the workflow and all related resources.
   2. **Build on it** – provides an editable workflow definition that you can review, customize, and deploy with your own resources. (Related resources, such as functions or queues, will **not** be created automatically.)

4. Choose **Use template** to continue with your selection.

###### Note

_Standard charges apply for services deployed to your account._

## Step 2: Trigger the state machine execution

1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs "https://console.aws.amazon.com/sqs").
2. Select the queue that was created by the sample project.

The name will be similar to
**Example-SQSQueue-wJalrXUtnFEMI**. 3. In the **Queue Actions** list, select **Send a
Message**. 4. Use the copy button to copy the following message, and on the **Send a
Message** window, enter it, and choose **Send
Message**.

###### Note

In this sample message, the `input:` line has been formatted with line
breaks to fit the page. Use the copy button or otherwise ensure that it is entered as a
single line with no breaks.

```
{
      "input": "QW5kIGxpa2UgdGhlIGJhc2VsZXNzIGZhYnJpYyBvZiB0aGlzIHZpc2lvbiwgVGhlIGNsb3VkLWNhcHBlZCB0b3dlcnMsIHRoZSBnb3JnZW91cyBwYWxhY2VzLCBUaGUgc29sZW1uIHRlbXBsZXMsIHRoZSBncmVhdCBnbG9iZSBpdHNlbGbigJQgWWVhLCBhbGwgd2hpY2ggaXQgaW5oZXJpdOKAlHNoYWxsIGRpc3NvbHZlLCBBbmQgbGlrZSB0aGlzIGluc3Vic3RhbnRpYWwgcGFnZWFudCBmYWRlZCwgTGVhdmUgbm90IGEgcmFjayBiZWhpbmQuIFdlIGFyZSBzdWNoIHN0dWZmIEFzIGRyZWFtcyBhcmUgbWFkZSBvbiwgYW5kIG91ciBsaXR0bGUgbGlmZSBJcyByb3VuZGVkIHdpdGggYSBzbGVlcC4gU2lyLCBJIGFtIHZleGVkLiBCZWFyIHdpdGggbXkgd2Vha25lc3MuIE15IG9sZCBicmFpbiBpcyB0cm91YmxlZC4gQmUgbm90IGRpc3R1cmJlZCB3aXRoIG15IGluZmlybWl0eS4gSWYgeW91IGJlIHBsZWFzZWQsIHJldGlyZSBpbnRvIG15IGNlbGwgQW5kIHRoZXJlIHJlcG9zZS4gQSB0dXJuIG9yIHR3byBJ4oCZbGwgd2FsayBUbyBzdGlsbCBteSBiZWF0aW5nIG1pbmQu"
}
```

5. Choose **Close**.
6. Open the Step Functions console.
7. Go to your [Amazon CloudWatch Logs log group](https://console.aws.amazon.com/cloudwatch/home?#logs: "https://console.aws.amazon.com/cloudwatch/home?#logs:") and inspect the logs. The name of the log group will look
   like **example-ExpressLogGroup-wJalrXUtnFEMI**.
