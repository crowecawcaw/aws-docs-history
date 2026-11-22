

# Testing your DaaS product in AWS Marketplace

Test the complete buyer journey while your Data as a Service (DaaS) product has the **Limited** status. For paid pricing models, each dimension uses a reduced test price while you test. For more information, see [Creating the public offer](daas-create-product.md#daas-create-product-offer).

## Testing the purchase
<a name="daas-product-testing-purchase"></a>

To test as a buyer, use a second AWS account that isn't your seller account. You allowlist that account so that it can open your **Limited** listing, and then you subscribe with it.

**To test a purchase of your DaaS product**

1. In AWS Partner Central, open your product, and then choose **Request changes**, **Update allowlist**. Enter the test buyer's AWS account ID, and then choose **Submit**.

1. Using the test buyer account, open your product's listing in AWS Marketplace, and then choose **View purchase options**, **Subscribe**.

1. Choose **Launch your software**. On the **Set up your account** page, choose **Set up your account**, and confirm that your fulfillment URL opens and completes registration.

## Verifying the results
<a name="daas-product-testing-results"></a>

After the test purchase, check each of the following results:


**DaaS test checks**  

| Check | Where | Expected result | 
| --- | --- | --- | 
| Buyer registered | Your data store for buyer records | A record with the test account ID and the current license ARN. | 
| Subscription event received | Your Amazon SQS queue | A Purchase Agreement Created - Proposer event. | 
| Buyer activated | Your Amazon SQS queue | A License Updated - Manufacturer event. Activate the buyer only after you receive it. | 
| Entitlement visible | GetEntitlements response in your application logs | The purchased dimension and quantity. | 
| Metering accepted (usage-based pricing) | BatchMeterUsage response in your application logs | Status: Success. | 
| Cancellation | For pay as you go or free products, as the test buyer, cancel the subscription. For the steps, see [Canceling a DaaS subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-daas-products.html#buyer-daas-cancel) in the AWS Marketplace Buyer Guide. | A Purchase Agreement Ended - Proposer event, and your application removes access. | 
| Billing and reports | AWS Partner Central reports | Test usage appears as expected. | 

## Troubleshooting test failures
<a name="daas-product-testing-troubleshooting"></a>

If a check fails, look for the following common causes:
+ **AccessDenied** – Confirm that the IAM role that your integration uses allows the AWS Marketplace API actions that it calls, such as `ResolveCustomer`, `GetEntitlements`, and `BatchMeterUsage`.
+ **InvalidTokenException** – The token isn't valid. Check that you pass the exact `x-amzn-marketplace-token` value, and that you call the API from your seller account.
+ **ExpiredTokenException** – The registration token has expired. As the test buyer, return to the **Set up your account** page and choose **Set up your account** again to get a new token. Resolve it as soon as your fulfillment URL receives it.
+ **No event received** – Confirm that you enabled the EventBridge rule and set your queue as its target. For more information, see [Setting up events for your DaaS product](daas-eventbridge-integration.md#daas-eventbridge-setup).
+ **Reporting or billing discrepancies** – See [Seller reports, data feeds, and dashboards in AWS Marketplace](reports-and-data-feed.md).

When your tests pass, you can make your product public. For more information, see [Making your DaaS product public in AWS Marketplace](daas-make-public.md).