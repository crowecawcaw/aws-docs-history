

# Tutorial: Create a REST API with a cross-account Lambda proxy integration
<a name="apigateway-cross-account-lambda-integrations"></a>

You can now use an AWS Lambda function from a different AWS account as your API integration backend. Each account can be in any region where Amazon API Gateway is available. This makes it easy to centrally manage and share Lambda backend functions across multiple APIs.

In this section, we show how to configure cross-account Lambda proxy integration using the Amazon API Gateway console.

## Create API for API Gateway cross-account Lambda integration
<a name="apigateway-cross-account-lambda-integrations-create-api"></a>

**To create an API**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. If this is your first time using API Gateway, you see a page that introduces you to the features of the service. Under **REST API**, choose **Build**. When the **Create Example API** popup appears, choose **OK**.

   If this is not your first time using API Gateway, choose **Create API**. Under **REST API**, choose **Build**.

1.  For **API name**, enter **CrossAccountLambdaAPI**.

1. (Optional) For **Description**, enter a description.

1. Keep **API endpoint type** set to **Regional**.

1. For **IP address type**, select **IPv4**.

1. Choose **Create API**.

## Create Lambda integration function in another account
<a name="apigateway-cross-account-lambda-integrations-create-lambda-function"></a>

Now you'll create a Lambda function in a different account from the one in which you created the example API.

**Creating a Lambda function in another account**

1. Log in to the Lambda console in a different account from the one where you created your API Gateway API.

1. Choose **Create function**.

1. Choose **Author from scratch**.

1. Under **Author from scratch**, do the following:

   1. For **Function name**, enter a name.

   1. From the **Runtime** drop-down list, choose a supported Node.js runtime.

   1. For **Architecture**, keep the default setting.

   1. Under **Permissions**, expand **Choose or create an execution role**. You can create a role or choose an existing role.

   1. Choose **Create function** to continue.

1. Scroll down to the **Function code** pane.

1. Enter the Node.js function implementation from [Tutorial: Create a REST API with a Lambda proxy integration](api-gateway-create-api-as-simple-proxy-for-lambda.md).

1. Choose **Deploy**.

1. Note the full ARN for your function (in the upper right corner of the Lambda function pane). You'll need it when you create your cross-account Lambda integration.

## Configure cross-account Lambda integration
<a name="apigateway-cross-account-lambda-integrations-create-integration2"></a>

Once you have a Lambda integration function in a different account, you can use the API Gateway console to add it to your API in your first account.

**Note**  
If you are configuring a cross-region, cross-account authorizer, the `sourceArn` that is added to the target function should use the region of the function, not the region of the API.

After you create an API, you create a resource. Typically, API resources are organized in a resource tree according to the application logic. For this example, you create a **/helloworld** resource. 

**To create a resource**

1. Choose **Create resource**.

1. Keep **Proxy resource** turned off. 

1. Keep **Resource path** as `/`.

1. For **Resource name**, enter **helloworld**.

1. Keep **CORS (Cross Origin Resource Sharing)** turned off.

1. Choose **Create resource**.

After you create an resource, you create a `GET` method. You integrate the `GET` method with a Lambda function in another account. 

**To create a `GET` method**

1. Select the **/helloworld** resource, and then choose **Create method**.

1. For **Method type**, select **GET**.

1. For **Integration type**, select **Lambda function**.

1. Turn on **Lambda proxy integration**.

1. For **Lambda function**, enter the full ARN of your Lambda function from Step 1. 

   In the Lambda console, you can find the ARN for your function in the upper right corner of the console window.

1. When you enter the ARN, a `aws lambda add-permission` command string will appear. This policy grants your first account access to your second account's Lambda function. Copy and paste the `aws lambda add-permission` command string into an AWS CLI window that is configured for your second account.

1. Choose **Create method**.

You can see your updated policy for your function in the Lambda console.

**(Optional) To see your updated policy**

1. Sign in to the AWS Management Console and open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/).

1. Choose your Lambda function.

1. Choose **Permissions**.

   You should see an `Allow` policy with a `Condition` clause in which the in the `AWS:SourceArn` is the ARN for your API's `GET` method.