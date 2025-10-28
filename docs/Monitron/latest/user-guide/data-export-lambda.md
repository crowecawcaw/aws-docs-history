Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Processing data with Lambda

###### Topics

- [Step 1: Create the IAM
  role that gives your function permission to access AWS
  resources](#create-iam-role "#create-iam-role")
- [Step 2: Create the Lambda function](#create-lambda-function "#create-lambda-function")
- [Step 3: Configure the Lambda function](#configure-lambda-function "#configure-lambda-function")
- [Step 4: Enable Kinesis trigger in AWS Lambda console](#enable-lambda-trigger "#enable-lambda-trigger")

## Step 1: Create the [IAM

role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") that gives your function permission to access AWS
resources

1. Open the [roles
   page](https://console.aws.amazon.com/iam/home?#/roles "https://console.aws.amazon.com/iam/home?#/roles") in the IAM console.
2. Choose **Create role**.
3. Create a role with the following properties.
   - Trusted entity: Lambda
   - Permissions: AWSLambdaKinesisExecutionRole (and
     AWSKeyManagementServicePowerUser if the Kinesis stream is
     encrypted)
   - Role name: lambda-kinesis-role

![IAM role creation interface showing name, review, and create steps with role details and permissions.](images/lambda-create-role.png)

## Step 2: Create the Lambda function

1. Open the **Functions** page in the Lambda
   console.
2. Choose **Create function**.
3. Choose **Use a blueprint**.
4. In the **Blueprints** search bar, search and choose
   **kinesis-process-record (nodejs)** or
   **kinesis-process-record-python**.
5. Choose **Configure**.

![Create function interface with options to author from scratch, use a blueprint, or select container image.](images/lambda-create-function.png)

## Step 3: Configure the Lambda function

1. Choose **Function name**
2. Choose the role created in the first step as the **Execution
   role**.
3. Configure Kinesis trigger.
   1. Choose your Kinesis stream.
   2. Click **Create function**.

![Lambda function configuration form with basic information and Kinesis trigger settings.](images/lambda-kinesis-trigger.png)

## Step 4: Enable Kinesis trigger in AWS Lambda console

1. On the **Configuration** tab, choose
   **Triggers**.
2. Check the box next to the name of the Kinesis stream and choose
   **Enable**.

![Lambda function configuration page with Triggers tab and Kinesis stream trigger highlighted.](images/kinesis-process-record-lambda.png)

The blueprint used in this example only consumes log data from the selected
stream. You can further edit Lambda function code later to complete a more
complicated task.
