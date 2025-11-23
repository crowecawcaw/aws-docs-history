# Create a task timer with Lambda and Amazon SNS

This sample project creates a task timer. It implements an AWS Step Functions state machine that
implements a `Wait` state, and uses an AWS Lambda function that sends an Amazon Simple Notification Service
(Amazon SNS) notification. A [Wait workflow state](state-wait.md "state-wait.md") state is a state type that waits for a trigger to
perform a single unit of work.

###### Note

This sample project implements an AWS Lambda function to send an Amazon Simple Notification Service (Amazon SNS)
notification. You can also send an Amazon SNS notification directly from the Amazon States Language. See [Integrating services with Step Functions](integrate-services.md "integrate-services.md").

This sample project creates the state machine, a Lambda function, and an Amazon SNS topic, and
configures the related AWS Identity and Access Management (IAM) permissions. For more information about the resources
that are created with the **Task Timer** sample project, see the
following:

For more information about how AWS Step Functions can control other AWS services, see
[Integrating services with Step Functions](integrate-services.md "integrate-services.md").

- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide.md "../../../AWSCloudFormation/latest/UserGuide.md")
- [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md")
- [AWS Lambda Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md")
- [IAM Getting Started Guide](../../../IAM/latest/GettingStartedGuide.md "../../../IAM/latest/GettingStartedGuide.md")

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
2. Wait for the CloudFormation stack to deploy. This can take up to 10 minutes.
3. After the **Start execution** option appears, review the **Input** and choose **Start execution**.

###### Congratulations!

You should now have a running demo of your state machine. You can choose states in the **Graph view** to review input, output, variables, definition, and events.
