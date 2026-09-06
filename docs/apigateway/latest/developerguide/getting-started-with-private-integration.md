

# Tutorial: Create a REST API with a private integration
<a name="getting-started-with-private-integration"></a>

In this tutorial, you create a REST API that connects to an Amazon ECS service that runs in an Amazon VPC. Clients outside of your Amazon VPC can use the API to access your Amazon ECS service. 

This tutorial takes approximately an hour to complete. First, you use an CloudFormation template to create a Amazon VPC and Amazon ECS service. Then you use the API Gateway console to create a VPC link V2. The VPC link allows API Gateway to access the Amazon ECS service that runs in your Amazon VPC. Next, you create a REST API that uses the VPC link V2 to connect to your Amazon ECS service. Lastly, you test your API.

When you invoke your REST API, API Gateway routes the request to your Amazon ECS service through your VPC link V2, and then returns the response from the service.

**Note**  
This tutorial was previously supported for HTTP APIs, and now is supported for REST APIs using VPC link V2.

![Overview of the REST API you create in this tutorial.](http://docs.aws.amazon.com/apigateway/latest/developerguide/images/private-integration-rest.png)


To complete this tutorial, you need an AWS account and an AWS Identity and Access Management user with console access. For more information, see [Set up to use API Gateway](setting-up.md).

**Topics**
+ [Step 1: Create an Amazon ECS service](#rest-api-private-integration-create-ecs-service)
+ [Step 2: Create a VPC link](#http-api-private-integration-vpc-link)
+ [Step 3: Create a REST API](#http-api-private-integration-create-api)
+ [Step 4: Test your API](#rest-api-private-integration-test-api)
+ [Step 5: Deploy your API](#rest-api-private-integration-deploy-api)
+ [Step 6: Call your API](#rest-api-private-integration-call)
+ [Step 7: Clean up](#rest-api-private-integration-cleanup)

## Step 1: Create an Amazon ECS service
<a name="rest-api-private-integration-create-ecs-service"></a>

Amazon ECS is a container management service that makes it easy to run, stop, and manage Docker containers on a cluster. In this tutorial, you run your cluster on a serverless infrastructure that's managed by Amazon ECS.

Download and unzip [this CloudFormation template](samples/rest-private-integration-tutorial.zip), which creates all of the dependencies for the service, including an Amazon VPC. You use the template to create an Amazon ECS service that uses an Application Load Balancer.

**To create an CloudFormation stack**

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Choose **Create stack** and then choose **With new resources (standard)**.

1. For **Specify template**, choose **Upload a template file**.

1. Select the template that you downloaded.

1. Choose **Next**. 

1. For **Stack name**, enter **rest-api-private-integrations-tutorial** and then choose **Next**.

1. For **Configure stack options**, choose **Next**.

1. For **Capabilities**, acknowledge that CloudFormation can create IAM resources in your account.

1. Choose **Next**, and then choose **Submit**.

CloudFormation provisions the ECS service, which can take a few minutes. When the status of your CloudFormation stack is **CREATE\_COMPLETE**, you're ready to move on to the next step.

## Step 2: Create a VPC link
<a name="http-api-private-integration-vpc-link"></a>

A VPC link allows API Gateway to access private resources in an Amazon VPC. You use a VPC link to allow clients to access your Amazon ECS service through your REST API.

**To create a VPC link**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. On the main navigation pane, choose **VPC links** and then choose **Create**.

   You might need to choose the menu icon to open the main navigation pane.

1. For **Choose a VPC link version**, select **VPC link V2**.

1. For **Name**, enter **private-integrations-tutorial**.

1. For **VPC**, choose the VPC that you created in step 1. The name should start with **RestApiStack**.

1. For **Subnets**, select the two private subnets in your VPC. Their names end with `PrivateSubnet`.

1. For **Security groups**, select the Group ID that starts with `private-integrations-tutorial` and has the description of `RestApiStack/RestApiTutorialService/Service/SecurityGroup`.

1. Choose **Create**.

After you create your VPC link V2, API Gateway provisions Elastic Network Interfaces to access your VPC. The process can take a few minutes. In the meantime, you can create your API.

## Step 3: Create a REST API
<a name="http-api-private-integration-create-api"></a>

The REST API provides an HTTP endpoint for your Amazon ECS service.



**To create a REST API**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose **Create API**, and then for **REST API**, choose **Build**.

1. For **Name**, enter **private-integration-api**.

1. For **IP address type**, select **IPv4**.

1. Choose **Create API**.

   After you create your API, you create a method.

1. Choose **Create method**, and then do the following:

   1. For **Method type**, select `GET`.

   1. For **Integration type**, select **VPC link**.

   1. Turn on **VPC proxy integration**.

   1. For **HTTP method**, select `GET`.

   1. For **VPC link**, choose the VPC link V2 you created in the previous step.

   1. For **Integration target**, enter the load balancer that you created with the CloudFormation template in Step 1. It's name should start with **rest-**.

   1. For **Endpoint URL**, enter `http://private-integrations-tutorial.com`.

      The URL is used to set the `Host` header of the integration request. In this case, the host header is **private-integrations-tutorial**.

   1. Choose **Create method**.

      With the proxy integration, the API is ready to test.

## Step 4: Test your API
<a name="rest-api-private-integration-test-api"></a>

Next, you test invoking the API method.

**To test your API**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose your API.

1. Choose the **Test** tab. You might need to choose the right arrow button to show the tab.

1. Choose **Test**

   Verify that your API's response is a welcome message that tells you that your app is running on Amazon ECS.

## Step 5: Deploy your API
<a name="rest-api-private-integration-deploy-api"></a>

Next, you deploy your API.

**To deploy your API**

1. Choose **Deploy API**.

1. For **Stage**, select **New stage**.

1. For **Stage name**, enter **Prod**.

1. (Optional) For **Description**, enter a description.

1. Choose **Deploy**.

## Step 6: Call your API
<a name="rest-api-private-integration-call"></a>

After your API is deployed, you can call it.

**To call your API**

1. Enter the invoke URL in a web browser.

   The full URL should look like `https://{{abcd123}}.execute-api.{{us-east-2}}.amazonaws.com/Prod`. 

   Your browser sends a `GET` request to the API.

1. Verify that your API's response is a welcome message that tells you that your app is running on Amazon ECS.

   If you see the welcome message, you successfully created an Amazon ECS service that runs in an Amazon VPC, and you used an API Gateway REST API with a VPC link V2 to access the Amazon ECS service.

## Step 7: Clean up
<a name="rest-api-private-integration-cleanup"></a>

To prevent unnecessary costs, delete the resources that you created as part of this tutorial. The following steps delete your VPC link V2, CloudFormation stack, and REST API.

**To delete a REST API**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. On the **APIs** page, select an API. Choose **Actions**, choose **Delete**, and then confirm your choice.

**To delete a VPC link**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose **VPC link**.

1. Select your VPC link, choose **Delete**, and then confirm your choice.

**To delete an CloudFormation stack**

1. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/).

1. Select your CloudFormation stack.

1. Choose **Delete** and then confirm your choice.