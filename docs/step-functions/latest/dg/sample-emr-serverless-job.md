# Run an EMR Serverless job

This sample project demonstrates how to create and start an EMR Serverless application and run multiple jobs within it.

This sample project creates the state machine, the supporting AWS resources, and configures the related IAM permissions. Explore this sample project to
learn about running EMR Serverless jobs using Step Functions state machines, or use it as a starting point for your own projects.

###### Important

EMR Serverless does not have a free pricing tier. Running the sample project will incur costs. You can
find pricing information on the [Amazon EMR Serverless pricing](https://aws.amazon.com/emr/pricing/ "https://aws.amazon.com/emr/pricing/") page.

In addition, the availability of EMR Serverless service integration is subject to the
availability of EMR Serverless APIs. Because of this, this sample project might not work correctly or be available in some AWS Regions. See the [Other considerations](../../../emr/latest/EMR-Serverless-UserGuide/considerations.md "../../../emr/latest/EMR-Serverless-UserGuide/considerations.md") topic for information about availability of EMR Serverless in AWS Regions.

## Step 1: Create the state machine

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/") and choose **Create state machine**.
2. Choose **Create from template** and find the related starter template. Choose **Next** to continue.
3. Choose how to use the template:
   1. **Run a demo** – creates a read-only state machine. After review, you can create the workflow and all related resources.
   2. **Build on it** – provides an editable workflow definition that you can review, customize, and deploy with your own resources. (Related resources, such as functions or queues, will **not** be created automatically.)

4. Choose **Use template** to continue with your selection.

###### Note

_Standard charges apply for services deployed to your account._

## Step 2: Run the demo state machine

If you chose the **Run a demo** option, all related resources will be deployed and ready to run. If you chose the **Build on it** option, you might need to set placeholder values and create additional resources before you can run your custom workflow.

1. Choose **Deploy and run**.
2. Wait for the AWS CloudFormation stack to deploy. This can take up to 10 minutes.
3. After the **Start execution** option appears, review the **Input** and choose **Start execution**.

###### Congratulations!

You should now have a running demo of your state machine. You can choose states in the **Graph view** to review input, output, variables, definition, and events.
