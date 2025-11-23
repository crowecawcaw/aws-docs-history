# Run an ETL/ELT workflow using Step Functions and the Amazon Redshift API

This sample project demonstrates how to use Step Functions and the Amazon Redshift Data API to run an ETL/ELT workflow that loads data into the Amazon Redshift data warehouse.

In this project, Step Functions uses an AWS Lambda function and the Amazon Redshift Data API to create the required database objects and to generate a set of example data,
then executes two jobs in parallel that perform loading dimension tables, followed by a fact table. Once both dimension load jobs end successfully, Step Functions
executes the load job for the fact table, runs the validation job, then pauses the Amazon Redshift cluster.

###### Note

You can modify the ETL logic to receive data from other sources such as Amazon S3, which can use the [COPY](../../../redshift/latest/dg/r_COPY.md "../../../redshift/latest/dg/r_COPY.md") command to copy data from Amazon S3 to an Amazon Redshift table.

For more information about Amazon Redshift and Step Functions service integrations, see the following guides:

- [Integrating services with Step Functions](integrate-services.md "integrate-services.md")
- [Using the Amazon Redshift Data API](../../../redshift/latest/mgmt/data-api.md "../../../redshift/latest/mgmt/data-api.md")
- [Amazon Redshift Data API service](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds-data.html")
- [Creating a Step Functions state machine that uses Lambda](tutorial-creating-lambda-state-machine.md "tutorial-creating-lambda-state-machine.md")
  For more information about IAM policies for Lambda and Amazon Redshift, see the following guides:

- [IAM policies for calling AWS Lambda](connect-lambda.md#lambda-iam "connect-lambda.md#lambda-iam")
- [Authorizing access to the Amazon Redshift Data API](../../../redshift/latest/mgmt/data-api.md#data-api-access "../../../redshift/latest/mgmt/data-api.md#data-api-access")

###### Note

This sample project may incur charges.

For new AWS users, a free usage tier is available. On this tier, services are free below a certain level of usage. For more information about AWS
costs and the Free Tier, see [AWS Step Functions pricing](https://aws.amazon.com/step-functions/pricing/ "https://aws.amazon.com/step-functions/pricing/").

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
