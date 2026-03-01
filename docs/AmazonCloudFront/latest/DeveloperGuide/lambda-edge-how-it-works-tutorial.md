# Tutorial: Create a basic Lambda@Edge function (console)

This tutorial shows you how to get started with Lambda@Edge by creating and
configuring an example Node.js function that runs in CloudFront. This example adds HTTP
security headers to a response when CloudFront retrieves a file. (This can improve
security and privacy for a website.)

You don't need your own website for this tutorial. However, when you choose to
create your own Lambda@Edge solution, you follow similar steps and select from the
same options.

###### Topics

- [Step 1: Sign up for an AWS account](#lambda-edge-how-it-works-tutorial-AWS "#lambda-edge-how-it-works-tutorial-AWS")
- [Step 2: Create a CloudFront distribution](#lambda-edge-how-it-works-tutorial-cloudfront "#lambda-edge-how-it-works-tutorial-cloudfront")
- [Step 3: Create your function](#lambda-edge-how-it-works-tutorial-create-function "#lambda-edge-how-it-works-tutorial-create-function")
- [Step 4: Add a CloudFront trigger to run the function](#lambda-edge-how-it-works-tutorial-add-trigger "#lambda-edge-how-it-works-tutorial-add-trigger")
- [Step 5: Verify that the function runs](#lambda-edge-how-it-works-tutorial-verify "#lambda-edge-how-it-works-tutorial-verify")
- [Step 6: Troubleshoot issues](#lambda-edge-how-it-works-tutorial-troubleshoot "#lambda-edge-how-it-works-tutorial-troubleshoot")
- [Step 7: Clean up your example resources](#lambda-edge-how-it-works-tutorial-cleanup-resources "#lambda-edge-how-it-works-tutorial-cleanup-resources")
- [Related information](#lambda-edge-how-it-works-tutorial-resources "#lambda-edge-how-it-works-tutorial-resources")

## Step 1: Sign up for an AWS account

If you haven't already done so, sign up for an AWS account. For more
information, see [Sign up for an AWS account](setting-up-cloudfront.md#sign-up-for-aws "setting-up-cloudfront.md#sign-up-for-aws").

## Step 2: Create a CloudFront distribution

Before you create the example Lambda@Edge function, you must have a CloudFront
environment to work with that includes an origin to serve content from.

For this example, you create a CloudFront distribution that uses an Amazon S3 bucket as
the origin for the distribution. If you already have an environment to use, you
can skip this step.

###### To create a CloudFront distribution with an Amazon S3 origin

1. Create an Amazon S3 bucket with a file or two, such as image files, for
   sample content. For help, follow the steps in [Upload your content to Amazon S3](GettingStarted.md#GettingStartedUploadContent "GettingStarted.md#GettingStartedUploadContent"). Make sure that you set
   permissions to grant public read access to the objects in your
   bucket.
2. Create a CloudFront distribution and add your S3 bucket as an origin, by
   following the steps in [Create a CloudFront web distribution](GettingStarted.md#GettingStartedCreateDistribution "GettingStarted.md#GettingStartedCreateDistribution"). If you already have a
   distribution, you can add the bucket as an origin for that distribution
   instead.

###### Tip

Make a note of your distribution ID. Later in this tutorial when
you add a CloudFront trigger for your function, you must choose the ID for
your distribution in a dropdown list—for example,
`E653W22221KDDL`.

## Step 3: Create your function

In this step, you create a Lambda function from a blueprint template in the
Lambda console. The function adds code to update security headers in your CloudFront
distribution.

###### To create a Lambda function

1. Sign in to the AWS Management Console and open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").

###### Important

Make sure that you're in the **US-East-1 (N.
Virginia)** AWS Region
(**us-east-1**). You must be in this Region to
create Lambda@Edge functions. 2. Choose **Create function**. 3. On the **Create function** page, choose **Use
a blueprint**, and then filter for the CloudFront blueprints by
entering `cloudfront` in the search field.

###### Note

CloudFront blueprints are available only in the **US-East-1 (N.
Virginia)** Region
(**us-east-1**). 4. Choose the **Modify HTTP response header** blueprint
as the template for your function. 5. Enter the following information about your function:

    * **Function name** – Enter a name for
     your function.
    * **Execution role** – Choose how to set
     the permissions for your function. To use the recommended basic
     Lambda@Edge permissions policy template, choose **Create
     a new role from AWS policy templates**.
    * **Role name** – Enter a name for the
     role that the policy template creates.
    * **Policy templates** – Lambda
     automatically adds the policy template **Basic
     Lambda@Edge permissions** because you chose a CloudFront
     blueprint as the basis for your function. This policy template
     adds execution role permissions that allow CloudFront to run your
     Lambda function for you in CloudFront locations around the world. For
     more information, see [Set up IAM permissions and roles for Lambda@Edge](lambda-edge-permissions.md "lambda-edge-permissions.md").

6. Choose **Create function** at the bottom of the
   page.
7. In the **Deploy to Lambda@Edge** pane that appears,
   choose **Cancel**. (For this tutorial, you must modify
   the function code before deploying the function to Lambda@Edge.)
8. Scroll down to the **Code source** section of the
   page.
9. Replace the template code with a function that modifies the security
   headers that your origin returns. For example, you could use code
   similar to the following:

```
'use strict';
export const handler = (event, context, callback) => {

    //Get contents of response
    const response = event.Records[0].cf.response;
    const headers = response.headers;

    //Set new headers
    headers['strict-transport-security'] = [{key: 'Strict-Transport-Security', value: 'max-age= 63072000; includeSubdomains; preload'}];
    headers['content-security-policy'] = [{key: 'Content-Security-Policy', value: "default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'"}];
    headers['x-content-type-options'] = [{key: 'X-Content-Type-Options', value: 'nosniff'}];
    headers['x-frame-options'] = [{key: 'X-Frame-Options', value: 'DENY'}];
    headers['x-xss-protection'] = [{key: 'X-XSS-Protection', value: '1; mode=block'}];
    headers['referrer-policy'] = [{key: 'Referrer-Policy', value: 'same-origin'}];

    //Return modified response
    callback(null, response);
};
```

10. Choose **File**, **Save** to save
    your updated code.
11. Choose **Deploy**.

Proceed to the next section to add a CloudFront trigger to run the function.

## Step 4: Add a CloudFront trigger to run the function

Now that you have a Lambda function to update security headers, configure the
CloudFront trigger to run your function to add the headers in any response that CloudFront
receives from the origin for your distribution.

###### To configure the CloudFront trigger for your function

1. In the Lambda console, on the **Function overview**
   page for your function, choose **Add trigger**.
2. For **Trigger configuration**, choose
   **CloudFront**.
3. Choose **Deploy to Lambda@Edge**.
4. In the **Deploy to Lambda@Edge** pane, under
   **Configure CloudFront trigger**, enter the following
   information:
   - **Distribution** – The CloudFront
     distribution ID to associate with your function. In the dropdown
     list, choose the distribution ID.
   - **Cache behavior** – The cache
     behavior to use with the trigger. For this example, leave the
     value set to **\***, which means your
     distribution's default cache behavior. For more information, see
     [Cache behavior settings](DownloadDistValuesCacheBehavior.md "DownloadDistValuesCacheBehavior.md") in the
     [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md")
     topic.
   - **CloudFront event** – The trigger that
     specifies when your function runs. We want the security headers
     function to run whenever CloudFront returns a response from the
     origin. In the dropdown list, choose **Origin
     response**. For more information, see [Add triggers for a Lambda@Edge function](lambda-edge-add-triggers.md "lambda-edge-add-triggers.md").

5. Select the **Confirm deploy to Lambda@Edge** check
   box.
6. Choose **Deploy** to add the trigger and replicate
   the function to AWS locations worldwide.
7. Wait for the function to replicate. This typically takes several
   minutes.

You can check to see if replication is finished by [going to the CloudFront
console](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home") and viewing your distribution. Wait for the
distribution status to change from **Deploying** to a
date and time, which means that your function has been replicated. To
verify that the function works, follow the steps in the next
section.

## Step 5: Verify that the function runs

Now that you've created your Lambda function and configured a trigger to run it
for a CloudFront distribution, check to make sure that the function is accomplishing
what you expect it to. In this example, we check the HTTP headers that CloudFront
returns, to make sure that the security headers are added.

###### To verify that your Lambda@Edge function adds security headers

1. In a browser, enter the URL for a file in your S3 bucket. For example,
   you might use a URL similar to
   `https://d111111abcdef8.cloudfront.net/image.jpg`.

For more information about the CloudFront domain name to use in the file
URL, see [Customize the URL format for files in CloudFront](LinkFormat.md "LinkFormat.md"). 2. Open your browser's Web Developer toolbar. For example, in your
browser window in Chrome, open the context (right-click) menu, and then
choose **Inspect**. 3. Choose the **Network** tab. 4. Reload the page to view your image, and then choose an HTTP request on
the left pane. You see the HTTP headers displayed in a separate
pane. 5. Look through the list of HTTP headers to verify that the expected
security headers are included in the list. For example, you might see
headers similar to those shown in the following screenshot.

![HTTP headers list with the expected security headers highlighted.](images/lambda-at-edge-security-headers-list.png)

If the security headers are included in your headers list, great! You've
successfully created your first Lambda@Edge function. If CloudFront returns errors or
there are other issues, continue to the next step to troubleshoot the
issues.

## Step 6: Troubleshoot issues

If CloudFront returns errors or doesn't add the security headers as expected, you
can investigate your function's execution by looking at CloudWatch Logs. Be sure to
use the logs stored in the AWS location that is closest to the location where
the function is executed.

For example, if you view the file from London, try changing the Region in the
CloudWatch console to Europe (London).

###### To examine CloudWatch logs for your Lambda@Edge function

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Change **Region** to the location that is shown when
   you view the file in your browser. This is where the function is
   executing.
3. In the left pane, choose **Logs** to view the logs
   for your distribution.

For more information, see [Monitor CloudFront metrics with Amazon CloudWatch](monitoring-using-cloudwatch.md "monitoring-using-cloudwatch.md").

## Step 7: Clean up your example resources

If you created an Amazon S3 bucket and CloudFront distribution just for this tutorial,
delete the AWS resources that you allocated so that you no longer accrue
charges. After you delete your AWS resources, any content that you added is no
longer available.

**Tasks**

- [Delete the S3 bucket](#lambda-edge-how-it-works-tutorial-delete-bucket "#lambda-edge-how-it-works-tutorial-delete-bucket")
- [Delete the Lambda function](#lambda-edge-how-it-works-tutorial-delete-function "#lambda-edge-how-it-works-tutorial-delete-function")
- [Delete the CloudFront distribution](#lambda-edge-how-it-works-tutorial-delete-distribution "#lambda-edge-how-it-works-tutorial-delete-distribution")

### Delete the S3 bucket

Before you delete your Amazon S3 bucket, make sure that logging is disabled for
the bucket. Otherwise, AWS continues to write logs to your bucket as you
delete it.

###### To disable logging for a bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select your bucket, and then choose
   **Properties**.
3. From **Properties**, choose
   **Logging**.
4. Clear the **Enabled** check box.
5. Choose **Save**.

Now, you can delete your bucket. For more information, see [Deleting a bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md") in the _Amazon Simple Storage
Service Console User Guide_.

### Delete the Lambda function

For instructions to delete the Lambda function association and optionally
the function itself, see [Delete Lambda@Edge functions and replicas](lambda-edge-delete-replicas.md "lambda-edge-delete-replicas.md").

### Delete the CloudFront distribution

Before you delete a CloudFront distribution, you must disable it. A disabled
distribution is no longer functional and does not accrue charges. You can
enable a disabled distribution at any time. After you delete a disabled
distribution, it's no longer available.

###### To disable and delete a CloudFront distribution

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Select the distribution that you want to disable, and then choose
   **Disable**.
3. When prompted for confirmation, choose **Yes,
   Disable**.
4. Select the disabled distribution, and then choose
   **Delete**.
5. When prompted for confirmation, choose **Yes,
   Delete**.

## Related information

Now that you have a basic idea of how Lambda@Edge functions work, learn more by
reading the following:

- [Lambda@Edge example functions](lambda-examples.md "lambda-examples.md")
- [Lambda@Edge Design Best Practices](https://aws.amazon.com/blogs/networking-and-content-delivery/lambdaedge-design-best-practices/ "https://aws.amazon.com/blogs/networking-and-content-delivery/lambdaedge-design-best-practices/")
- [Reducing Latency and Shifting Compute to the Edge with
  Lambda@Edge](https://aws.amazon.com/blogs/networking-and-content-delivery/reducing-latency-and-shifting-compute-to-the-edge-with-lambdaedge/ "https://aws.amazon.com/blogs/networking-and-content-delivery/reducing-latency-and-shifting-compute-to-the-edge-with-lambdaedge/")
