# Manage an Amazon EMR job

This sample project demonstrates Amazon EMR and AWS Step Functions integration. The project creates an Amazon EMR cluster, adds multiple steps and runs them, and then terminate
the cluster.

###### Important

Amazon EMR does not have a free pricing tier. Running the sample project will incur costs. You can
find pricing information on the [Amazon EMR
pricing](https://aws.amazon.com//emr/pricing/ "https://aws.amazon.com//emr/pricing/") page. The availability of Amazon EMR service integration is subject to the
availability of Amazon EMR APIs. Because of this, this sample project might not work correctly in
some AWS Regions. See the [Amazon EMR](../../../govcloud-us/latest/UserGuide/govcloud-emr.md "../../../govcloud-us/latest/UserGuide/govcloud-emr.md") documentation for
limitations in special Regions.

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
