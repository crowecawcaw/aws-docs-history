# Add triggers to a Lambda@Edge

function

You can use the AWS Lambda console or Amazon CloudFront console to add a trigger to your
Lambda@Edge function.

###### Important

You can create triggers only for numbered versions of your function (not the
**$LATEST**).

Lambda console

###### To add triggers for

CloudFront events to a Lambda@Edge function

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. In the Region list at the top of the page, choose
   **US East (N. Virginia)**.
3. On the **Functions** page, choose the name of
   the function that you want to add triggers for.
4. On the **Function overview** page, choose the
   **Versions** tab.
5. Choose the version that you want to add triggers to.

After you choose a version, the name of the button changes to
**Version: $LATEST** or
**Version:**
_version number_. 6. Choose the **Triggers** tab. 7. Choose **Add trigger**. 8. For **Trigger configuration**, choose
**Select a source**, enter
`cloudfront`, and then choose
**CloudFront**.

###### Note

If you've already created one or more triggers, CloudFront is
the default service. 9. Specify the following values to indicate when you want the
Lambda function to execute.

    1. **Distribution** – Choose the
     distribution that you want to add the trigger to.
    2. **Cache behavior** – Choose
     the cache behavior that specifies the objects that you
     want to execute the function on.


    ###### Note

    If you specify `*` for the cache
     behavior, the Lambda function deploys to the default
     cache behavior.
    3. **CloudFront event** – Choose the
     CloudFront event that causes the function to execute.
    4. **Include body** – Select this
     check box if you want to access the request body in your
     function.
    5. **Confirm deploy to Lambda@Edge**
     – Select this check box so that AWS Lambda
     replicates the function to AWS Regions
     globally.

10. Choose **Add**.

The function starts to process requests for the specified CloudFront
events when the updated CloudFront distribution is deployed. To
determine whether a distribution is deployed, choose
**Distributions** in the navigation pane.
When a distribution is deployed, the value of the
**Status** column for the distribution
changes from **Deploying** to the date and time
of deployment.

CloudFront console

###### To add triggers for CloudFront events to a Lambda@Edge function

1. Get the ARN of the Lambda function that you want to add
   triggers for:
   1. Sign in to the AWS Management Console and open the AWS Lambda console at
      [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
   2. In the list of Regions at the top of the page, choose
      **US East (N. Virginia)**.
   3. In the list of functions, choose name of the function
      that you want to add triggers to.
   4. On the **Function overview** page,
      choose the **Versions** tab, and choose
      the numbered version that you want to add triggers
      to.
   5. Choose the **Copy ARN** button to
      copy the ARN to your clipboard. The ARN for the Lambda
      function looks something like this:

   `arn:aws:lambda:us-east-1:123456789012:function:TestFunction:2`

   The number at the end (**2** in this
   example) is the version number of the function.

2. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
3. In the list of distributions, choose the ID of the
   distribution that you want to add triggers to.
4. Choose the **Behaviors** tab.
5. Select the cache behavior that you want to add triggers to,
   and then choose **Edit**.
6. For **Function associations**, in the
   **Function type** list, choose
   **Lambda@Edge** for when you want the
   function to execute: for viewer requests, viewer responses,
   origin requests, or origin responses.

For more information, see [Choose the event to trigger the
function](lambda-how-to-choose-event.md "lambda-how-to-choose-event.md"). 7. In the **Function ARN / Name** text box,
paste the ARN of the Lambda function that you want to execute
when the chosen event occurs. This is the value that you copied
from the Lambda console. 8. Select **Include body** if you want to access
the request body in your function.

If you just want to replace the request body, you don't need
to select this option. 9. To execute the same function for more event types, repeat
steps 6 and 7. 10. Choose **Save changes**. 11. To add triggers to more cache behaviors for this distribution,
repeat steps 5 through 10.

The function starts to process requests for the specified CloudFront
events when the updated CloudFront distribution is deployed. To
determine whether a distribution is deployed, choose
**Distributions** in the navigation pane.
When a distribution is deployed, the value of the
**Status** column for the distribution
changes from **Deploying** to the time and date
of deployment.
