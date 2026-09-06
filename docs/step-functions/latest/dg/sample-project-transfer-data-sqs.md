

# Transfer data records with Lambda, DynamoDB, and Amazon SQS
<a name="sample-project-transfer-data-sqs"></a>

This sample project demonstrates how to iteratively read items from an Amazon DynamoDB table and send these items to an Amazon SQS queue using a Step Functions state machine. Deploying this sample project will create a Step Functions state machine, a DynamoDB table, an AWS Lambda function, and an Amazon SQS queue. 

In this project, Step Functions uses the Lambda function to populate the DynamoDB table. The state machine also uses a `for` loop to read each of the entries, and then sends each entry to an Amazon SQS queue.

## Step 1: Create the state machine
<a name="sample-project-transfer-data-sqs-create"></a>

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/) and choose **Create state machine**.

1. Choose **Create from template** and find the related starter template. Choose **Next** to continue.

1. Choose how to use the template:

   1. **Run a demo** – creates a read-only state machine. After review, you can create the workflow and all related resources.

   1. **Build on it** – provides an editable workflow definition that you can review, customize, and deploy with your own resources. (Related resources, such as functions or queues, will **not** be created automatically.)

1. Choose **Use template** to continue with your selection.
**Note**  
*Standard charges apply for services deployed to your account.*

## Step 2: Run the demo state machine
<a name="sample-sqs-start-execution"></a>

If you chose the **Run a demo** option, all related resources will be deployed and ready to run. If you chose the **Build on it** option, you might need to set placeholder values and create additional resources before you can run your custom workflow.

1. Choose **Deploy and run**.

1. Wait for the CloudFormation stack to deploy. This can take up to 10 minutes.

1. After the **Start execution** option appears, review the **Input** and choose **Start execution**.

**Congratulations\!**  
You should now have a running demo of your state machine. You can choose states in the **Graph view** to review input, output, variables, definition, and events.