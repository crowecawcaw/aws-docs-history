

# Tune the hyperparameters of a machine learning model in SageMaker AI
<a name="sample-hyper-tuning"></a>

This sample project demonstrates using SageMaker AI to tune the hyperparameters of a machine learning model, and to batch transform a test dataset.

In this project, Step Functions uses a Lambda function to seed an Amazon S3 bucket with a test dataset. It then creates a hyperparameter tuning job using the [SageMaker AI service integration](connect-sagemaker.md). It then uses a Lambda function to extract the data path, saves the tuning model, extracts the model name, and then runs a batch transform job to perform inference in SageMaker AI.

For more information about SageMaker AI and Step Functions service integrations, see the following:
+ [Integrating services with Step Functions](integrate-services.md)
+ [Create and manage Amazon SageMaker AI jobs with Step Functions](connect-sagemaker.md)

**Note**  
This sample project may incur charges.  
For new AWS users, a free usage tier is available. On this tier, services are free below a certain level of usage. For more information about AWS costs and the Free Tier, see [SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/).

## Step 1: Create the state machine
<a name="sample-hyper-tuning-create"></a>

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/) and choose **Create state machine**.

1. Choose **Create from template** and find the related starter template. Choose **Next** to continue.

1. Choose how to use the template:

   1. **Run a demo** – creates a read-only state machine. After review, you can create the workflow and all related resources.

   1. **Build on it** – provides an editable workflow definition that you can review, customize, and deploy with your own resources. (Related resources, such as functions or queues, will **not** be created automatically.)

1. Choose **Use template** to continue with your selection.
**Note**  
*Standard charges apply for services deployed to your account.*

## Step 2: Run the demo state machine
<a name="sample-hyper-tuning-start-execution"></a>

If you chose the **Run a demo** option, all related resources will be deployed and ready to run. If you chose the **Build on it** option, you might need to set placeholder values and create additional resources before you can run your custom workflow.

1. Choose **Deploy and run**.

1. Wait for the CloudFormation stack to deploy. This can take up to 10 minutes.

1. After the **Start execution** option appears, review the **Input** and choose **Start execution**.

**Congratulations\!**  
You should now have a running demo of your state machine. You can choose states in the **Graph view** to review input, output, variables, definition, and events.