

# Process data from a queue with a Map state in Step Functions
<a name="sample-map-state"></a>

In this sample workflow, a [Map workflow state](state-map.md) state processes data from a queue, sending messages to subscribers and storing them in a database.

Step Functions uses an optimized integration to pull messages from an Amazon SQS queue. When messages are available, a [Choice](state-choice.md) state passes an array of JSON messages to a [Map](state-map.md) state for processing. For each message, the state machine writes the message to DynamoDB, removes the message from the queue, and publishes the message to an Amazon SNS topic.

## Step 1: Create the state machine
<a name="sample-map-state-create"></a>

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/) and choose **Create state machine**.

1. Choose **Create from template** and find the related starter template. Choose **Next** to continue.

1. Choose how to use the template:

   1. **Run a demo** – creates a read-only state machine. After review, you can create the workflow and all related resources.

   1. **Build on it** – provides an editable workflow definition that you can review, customize, and deploy with your own resources. (Related resources, such as functions or queues, will **not** be created automatically.)

1. Choose **Use template** to continue with your selection.
**Note**  
*Standard charges apply for services deployed to your account.*

## Step 2: Subscribe to the Amazon SNS topic
<a name="sample-map-subscribe-topic"></a>

**Tip**  
Subscribe to the Amazon SNS topic and add items to the Amazon SQS queue **before** you run your state machine.

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/home).

1. Choose **Topics** and find the topic that was created by the sample project.

1. Choose **Create subscription**, and for **Protocol**, choose **Email**.

1. Under **Endpoint**, enter your email address to subscribe to the topic.

1. Choose **Create subscription**.

1. Confirm the subscription in your email to activate the subscription.

## Step 3: Add messages to the Amazon SQS queue
<a name="sample-map-create-queue"></a>

1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/home).

1. Choose the queue that was created by the sample project.

1. Choose **Send and receive messages**, enter a message and choose **Send message**. Repeat this step to add several messages to the queue.

## Step 4: Run the state machine
<a name="sample-map-start-execution"></a>

**Tip**  
Queues in Amazon SNS are eventually consistent. You may need to wait a few minutes after sending messages to the queue before running your state machine.

If you chose the **Run a demo** option, all related resources will be deployed and ready to run. If you chose the **Build on it** option, you might need to set placeholder values and create additional resources before you can run your custom workflow.

1. Choose **Deploy and run**.

1. Wait for the CloudFormation stack to deploy. This can take up to 10 minutes.

1. After the **Start execution** option appears, review the **Input** and choose **Start execution**.

**Congratulations\!**  
You should now have a running demo of your state machine. You can choose states in the **Graph view** to review input, output, variables, definition, and events.