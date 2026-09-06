

# Poll for job status with Lambda and AWS Batch
<a name="sample-project-job-poller"></a>

This sample project creates an AWS Batch job poller. It implements an AWS Step Functions state machine that uses AWS Lambda to create a `Wait` state loop that checks on an AWS Batch job. 

This sample project creates and configures all resources so that your Step Functions workflow will submit an AWS Batch job, and will wait for that job to complete before ending successfully. 

**Note**  
You can also implement this pattern without using a Lambda function. For information about controlling AWS Batch directly, see [Integrating services with Step Functions](integrate-services.md). 

This sample project creates the state machine, two Lambda functions, and an AWS Batch queue, and configures the related IAM permissions. 

For more information about how AWS Step Functions can control other AWS services, see [Integrating services with Step Functions](integrate-services.md).

## Step 1: Create the state machine
<a name="sample-project-job-poller-create"></a>

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/) and choose **Create state machine**.

1. Choose **Create from template** and find the related starter template. Choose **Next** to continue.

1. Choose how to use the template:

   1. **Run a demo** – creates a read-only state machine. After review, you can create the workflow and all related resources.

   1. **Build on it** – provides an editable workflow definition that you can review, customize, and deploy with your own resources. (Related resources, such as functions or queues, will **not** be created automatically.)

1. Choose **Use template** to continue with your selection.
**Note**  
*Standard charges apply for services deployed to your account.*

## Step 2: Run the demo state machine
<a name="job-status-poller-start-execution"></a>

If you chose the **Run a demo** option, all related resources will be deployed and ready to run. If you chose the **Build on it** option, you might need to set placeholder values and create additional resources before you can run your custom workflow.

1. Choose **Deploy and run**.

1. Wait for the CloudFormation stack to deploy. This can take up to 10 minutes.

1. After the **Start execution** option appears, review the **Input** and choose **Start execution**.

**Congratulations\!**  
You should now have a running demo of your state machine. You can choose states in the **Graph view** to review input, output, variables, definition, and events.