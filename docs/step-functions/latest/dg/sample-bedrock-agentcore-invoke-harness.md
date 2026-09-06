

# Triage support tickets with Amazon Bedrock AgentCore invokeHarness
<a name="sample-bedrock-agentcore-invoke-harness"></a>

This sample project demonstrates how you can use Amazon Bedrock AgentCore invokeHarness to triage customer-support tickets with AI. The state machine issues two invokeHarness calls with role-specific system prompts. First, an analyst prompt analyzes the ticket for category, sentiment, and urgency. Then, a triage director prompt recommends an action. The workflow records the final triage decision to an Amazon DynamoDB table.

This sample project creates the state machine, the supporting AWS resources, and configures the related IAM permissions. The template provisions a Bedrock AgentCore Harness that uses the Amazon Nova Lite model, a Standard Step Functions state machine, and a DynamoDB table. Explore this sample project to learn about using Bedrock AgentCore service integration with Step Functions state machines, or use it as a starting point for your own projects.

## Prerequisites
<a name="sample-bedrock-agentcore-invoke-harness-prerequisites"></a>

This sample project uses the Amazon Nova Lite large language model (LLM). To successfully run this sample project, you must add access to this LLM from the Amazon Bedrock console. To add the model access, do the following:

1. Open the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock).

1. On the navigation pane, choose **Model access**.

1. Choose **Manage model access**.

1. Select the check box next to **Amazon Nova Lite**.

1. Choose **Request access**. The **Access status** for the **Amazon Nova Lite** model shows as **Access granted**.

## Step 1: Create the state machine
<a name="sample-bedrock-agentcore-invoke-harness-create"></a>

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/) and choose **Create state machine**.

1. Choose **Create from template** and find the related starter template. Choose **Next** to continue.

1. Choose how to use the template:

   1. **Run a demo** – creates a read-only state machine. After review, you can create the workflow and all related resources.

   1. **Build on it** – provides an editable workflow definition that you can review, customize, and deploy with your own resources. (Related resources, such as functions or queues, will **not** be created automatically.)

1. Choose **Use template** to continue with your selection.
**Note**  
*Standard charges apply for services deployed to your account.*

## Step 2: Run the demo state machine
<a name="sample-bedrock-agentcore-invoke-harness-run"></a>

If you chose the **Run a demo** option, all related resources will be deployed and ready to run. If you chose the **Build on it** option, you might need to set placeholder values and create additional resources before you can run your custom workflow.

1. Choose **Deploy and run**.

1. Wait for the CloudFormation stack to deploy. This can take up to 10 minutes.

1. After the **Start execution** option appears, review the **Input** and choose **Start execution**.

**Congratulations\!**  
You should now have a running demo of your state machine. You can choose states in the **Graph view** to review input, output, variables, definition, and events.