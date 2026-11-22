

# Creating a SaaS product in AWS Marketplace

As an AWS Marketplace seller, you can add your software as a service (SaaS) product to AWS Marketplace. This includes creating your SaaS product and integrating it with the appropriate AWS Marketplace API operations, based on your billing model. To sell software as a SaaS products in AWS Marketplace, you follow these broad steps:
+ Create the SaaS product in AWS Marketplace.
+ Integrate the SaaS [subscription](saas-integrate-subscription.md), [contract](saas-integrate-contract.md), or [contract with pay-as-you-go](saas-integrate-contract-with-pay.md) product with AWS Marketplace. 
+ Test the [subscription](saas-integrate-subscription.md#saas-subscription-integration-testing), [contract](saas-integrate-contract.md#saas-contract-integration-testing), or [contract with pay-as-you-go](saas-integrate-contract-with-pay.md#saas-contract-consumption-integration-testing) product's integration with AWS Marketplace.
+ Submit your product for launch.

The following procedure shows you how to create a SaaS product in AWS Marketplace.

## Create a SaaS product
<a name="saas-creating-self-service"></a>

**To create a SaaS product**

1. **Decide to list a SaaS product**

   Have a SaaS product that you would like to sell in AWS Marketplace. Review and understand how to [Planning your SaaS product](saas-prepare.md).

1. **Determine pricing model**

   There are four pricing models for SaaS products: subscriptions, contracts, contracts with pay-as-you-go, and free. When you create the public offer, you choose **Usage-based pricing**, **Contract-based pricing**, or **Free**. For a contract with pay-as-you-go, you also select **Enable additional usage on top of contract**. Your choice of pricing model affects how you integrate your SaaS product with AWS Marketplace. For more information, see [Plan your pricing](saas-prepare.md#plan-pricing).

1. **Collect assets**

   Collect the assets needed to submit your product. Assets include:
   + Product logo – A PNG or JPG file of up to 5 MB that contains a clear image of your product's logo. The image must be 120 to 640 pixels wide and tall, with a 1:1 or 2:1 (wide) ratio and a transparent or white background. On the **Provide product details** page, you choose **File upload** or **Amazon S3 link**. If you use an Amazon S3 link, the bucket must be publicly accessible. For more information, see [Company and product logo requirements](product-submission.md#seller-and-product-logos).
   + End User License Agreement (EULA) – Your product must have a EULA. You upload it as a .txt or .pdf file when you create the public offer.
   + Product registration URL – This is the URL where buyers are redirected after successfully subscribing to your product in AWS Marketplace.
   + Metadata about your product – You provide the metadata on the **Provide product details** page in AWS Partner Central.
   + Support information for your product – This information includes email addresses and URLs for your product's support channels.

1. **Submit your product for integration**

   Use your seller account and AWS Partner Central to [Creating an initial SaaS product page on AWS Marketplace](saas-create-product-page.md). AWS Marketplace will publish your product as a limited product, which means that it's only available to use for integration and testing. Your product code and Amazon EventBridge event configuration will be available to you on the product overview page.
**Note**  
You set your prices when you create the public offer in **Step 3: Procurement configuration**.

1. **Integrate with AWS Marketplace**

   Your product must support customers onboarding and using your product, including validating their subscription before giving them access, and, in some cases, metering for their usage. How you integrate with AWS Marketplace depends on the pricing model you're using for your product. For more information about integration, based on pricing model, see the following topics:
   + [ Subscription integration](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-integrate-subscription.html)
   + [ Contract integration](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-integrate-contract.html)
   + [ Contract with pay-as-you-go integration](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-integrate-contract-with-pay.html)

   The final step of integrating your product with AWS Marketplace is to test it to ensure that the integration works properly.

1. **Product testing and contract cancellation**

   After you have completed the integration process, we recommend that you subscribe to your own product to evaluate and confirm the customer experience. Creating a test subscription allows you to:
   + Review product information
   + Examine available purchase options
   + Process test payments
   + Verify links to your own product website

   When you finish testing, cancel your test subscription before you change your product's visibility from limited to public. To cancel a pay-as-you-go subscription, follow the instructions at [Canceling your SaaS subscription](https://docs.aws.amazon.com/marketplace/latest/buyerguide/cancel-subscription.html#cancel-saas-subscription). To cancel a contract, request an agreement cancellation from the **Agreements** page in AWS Partner Central. For instructions on canceling an agreement, see [Requesting an agreement cancellation](refunds.md#requesting-cancellation).

1. **Submit your product for launch**

   After you verify your integration and you're ready for the product to be live, submit it for review. Choose **Publish** under **Complete your listing**, and then choose **Submit for review**. AWS Marketplace reviews your listing against its policies before it goes live. Automated checks can approve it within hours. If a check flags your listing, the review usually takes 3 to 5 business days.

   Before you publish, replace any test prices in your public offer with the prices that you want buyers to pay. For more information, see [Update pricing terms](saas-product-settings.md#saas-update-pricing-terms).