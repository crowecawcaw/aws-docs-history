

# Tutorial: Create a simple function with CloudFront Functions
<a name="functions-tutorial"></a>

This tutorial shows you how to get started with CloudFront Functions. You can create a simple function that redirects the viewer to a different URL, and that also returns a custom response header.

**Contents**
+ [Prerequisites](#functions-tutorial-prerequisites)
+ [Create the function](#functions-tutorial-create)
+ [Verify the function](#functions-tutorial-verify)

## Prerequisites
<a name="functions-tutorial-prerequisites"></a>

To use CloudFront Functions, you need a CloudFront distribution. If you don’t have one, see [Get started with a CloudFront standard distribution](GettingStarted.SimpleDistribution.md).

## Create the function
<a name="functions-tutorial-create"></a>

You can use the CloudFront console to create a simple function that redirects the viewer to a different URL, and also returns a custom response header. 

**To create a CloudFront function**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Functions**, and then choose **Create function**. 

1. On the **Create function** page, for **Name**, enter a function name such as {{MyFunctionName}}.

1. (Optional) For **Description**, enter a description for the function such as **Simple test function**.

1. For **Runtime**, keep the default selected JavaScript version.

1. Choose **Create function**.

1. Copy the following function code. This function code redirects the viewer to a different URL, and also returns a custom response header.

   ```
   function handler(event) {
       // NOTE: This example function is for a viewer request event trigger. 
       // Choose viewer request for event trigger when you associate this function with a distribution. 
       var response = {
           statusCode: 302,
           statusDescription: 'Found',
           headers: {
               'cloudfront-functions': { value: 'generated-by-CloudFront-Functions' },
               'location': { value: 'https://aws.amazon.com/cloudfront/' }
           }
       };
       return response;
   }
   ```

1. For **Function code**, paste the code into the code editor to replace the default code.

1. Choose **Save changes**.

1. (Optional) You can test the function before you publish it. This tutorial doesn’t describe how to test a function. For more information, see [Test functions](test-function.md).

1. Choose the **Publish** tab and then choose **Publish function**. You *must* publish the function before you can associate it with your CloudFront distribution.

1. Next, you can associate the function with a distribution or cache behavior. On the {{MyFunctionName}} page, choose the **Publish** tab. 
**Warning**  
In the following steps, choose a distribution or a cache behavior that’s used for testing. Don’t associate this test function with a distribution or cache behavior that’s used in production.

1. Choose **Add association**. 

1. On the **Associate** dialog box, choose a distribution and/or a cache behavior. For **Event type**, keep the default value.

1. Choose **Add association**.

   The **Associated distributions** table shows the associated distribution. 

1. Wait a few minutes for the associated distribution to finish deploying. To check the distribution’s status, select the distribution in the **Associated distributions** table and then choose **View distribution**.

   When the distribution’s status is **Deployed**, you’re ready to verify that the function works.

## Verify the function
<a name="functions-tutorial-verify"></a>

After you deploy the function, you can verify that it's working for your distribution.

**To verify the function**

1. In your web browser, navigate to your distribution’s domain name (for example, `https://d111111abcdef8.cloudfront.net`).

   The function returns a redirect to the browser, so the browser automatically goes to `https://aws.amazon.com/cloudfront/`.

1. In a command line window, you can use a tool like **curl** to send a request to your distribution’s domain name.

   ```
   curl -v https://d111111abcdef8.cloudfront.net/
   ```

   In the response, you see the redirect response (`302 Found`) and the custom response headers that the function added. Your response might look like the following example.  
**Example**  

   ```
   curl -v https://d111111abcdef8.cloudfront.net/
   > GET / HTTP/1.1
   > Host: d111111abcdef8.cloudfront.net
   > User-Agent: curl/7.64.1
   > Accept: */*
   >
   < HTTP/1.1 302 Found
   < Server: CloudFront
   < Date: Tue, 16 Mar 2021 18:50:48 GMT
   < Content-Length: 0
   < Connection: keep-alive
   < Location: https://aws.amazon.com/cloudfront/
   < Cloudfront-Functions: generated-by-CloudFront-Functions
   < X-Cache: FunctionGeneratedResponse from cloudfront
   < Via: 1.1 3035b31bddaf14eded329f8d22cf188c.cloudfront.net (CloudFront)
   < X-Amz-Cf-Pop: PHX50-C2
   < X-Amz-Cf-Id: ULZdIz6j43uGBlXyob_JctF9x7CCbwpNniiMlmNbmwzH1YWP9FsEHg==
   ```