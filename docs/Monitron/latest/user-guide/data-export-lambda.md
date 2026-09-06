

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Processing data with Lambda
<a name="data-export-lambda"></a>

**Topics**
+ [Step 1: Create the [IAM role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) that gives your function permission to access AWS resources](#create-iam-role)
+ [Step 2: Create the Lambda function](#create-lambda-function)
+ [Step 3: Configure the Lambda function](#configure-lambda-function)
+ [Step 4: Enable Kinesis trigger in AWS Lambda console](#enable-lambda-trigger)

## Step 1: Create the [IAM role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) that gives your function permission to access AWS resources
<a name="create-iam-role"></a>

1. Open the [roles page](https://console.aws.amazon.com/iam/home?#/roles) in the IAM console.

1. Choose **Create role**.

1. Create a role with the following properties.
   + Trusted entity: Lambda
   + Permissions: AWSLambdaKinesisExecutionRole (and AWSKeyManagementServicePowerUser if the Kinesis stream is encrypted)
   + Role name: lambda-kinesis-role  
![Name, review, and create page showing role name, description, trusted entities policy, and permissions.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/lambda-create-role.png)

## Step 2: Create the Lambda function
<a name="create-lambda-function"></a>

1. Open the **Functions** page in the Lambda console.

1. Choose **Create function**.

1. Choose **Use a blueprint**.

1. In the **Blueprints** search bar, search and choose **kinesis-process-record (nodejs)** or **kinesis-process-record-python**.

1. Choose **Configure**.  
![Create function page with Use a blueprint option selected and kinesis-process-record-python blueprint shown.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/lambda-create-function.png)

## Step 3: Configure the Lambda function
<a name="configure-lambda-function"></a>

1. Choose **Function name**

1. Choose the role created in the first step as the **Execution role**.

1. Configure Kinesis trigger.

   1. Choose your Kinesis stream.

   1. Click **Create function**.  
![Lambda function configuration form with basic information and Kinesis trigger settings.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/lambda-kinesis-trigger.png)

## Step 4: Enable Kinesis trigger in AWS Lambda console
<a name="enable-lambda-trigger"></a>

1. On the **Configuration** tab, choose **Triggers**.

1. Check the box next to the name of the Kinesis stream and choose **Enable**.  
![Configuration tab showing Triggers section with Kinesis bugbash trigger and Enable button.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/kinesis-process-record-lambda.png)

The blueprint used in this example only consumes log data from the selected stream. You can further edit Lambda function code later to complete a more complicated task. 