# Creating a SaaS product in AWS Marketplace

As an AWS Marketplace seller, you can add your software as a service (SaaS) product to AWS Marketplace.
This includes creating your SaaS product and integrating it with the appropriate AWS Marketplace API
operations, based on your billing model. To sell software as a SaaS products in AWS Marketplace, you
follow these broad steps:

- Create the SaaS product in AWS Marketplace.
- Integrate the SaaS [subscription](saas-integrate-subscription.md "saas-integrate-subscription.md"), [contract](saas-integrate-contract.md "saas-integrate-contract.md"), or
  [contract with
  pay-as-you-go](saas-integrate-contract-with-pay.md "saas-integrate-contract-with-pay.md") product with AWS Marketplace.
- Test the [subscription](saas-integrate-subscription.md#saas-subscription-integration-testing "saas-integrate-subscription.md#saas-subscription-integration-testing"), [contract](saas-integrate-contract.md#saas-contract-integration-testing "saas-integrate-contract.md#saas-contract-integration-testing"), or [contract with
  pay-as-you-go](saas-integrate-contract-with-pay.md#saas-contract-consumption-integration-testing "saas-integrate-contract-with-pay.md#saas-contract-consumption-integration-testing") product's integration with AWS Marketplace.
- Submit your product for launch.
  The following procedure shows you how to create a SaaS product in AWS Marketplace.

## Create a SaaS product

###### To create a SaaS product

1. **Decide to list a SaaS product**

Have a SaaS product that you would like to sell in AWS Marketplace. Review and
understand how to [Planning your SaaS product](saas-prepare.md "saas-prepare.md"). 2. **Determine pricing and offer type**

There are three offer types for SaaS products: subscriptions, contracts, and
contracts with pay-as-you-go. Your choice of offer type affects how you
integrate your SaaS product with AWS Marketplace. For more information, see [Plan your pricing](saas-prepare.md#plan-pricing "saas-prepare.md#plan-pricing"). 3. **Collect assets**

Collect the assets needed to submit your product. Assets include:

    * Product logo URL – A publicly accessible Amazon S3 URL that contains
     a clear image of the logo for the product that you're providing.
    * End User License Agreement (EULA) URL – Your product must have
     a EULA that's available as a PDF file. You must provide a link to an
     Amazon S3 bucket where customers can review the EULA on your product's AWS Marketplace
     page.
    * Product registration URL – This is the URL where buyers are
     redirected after successfully subscribing to your product in
     AWS Marketplace.
    * Metadata about your product – You provide the metadata in the
     product creation wizard of the AWS Marketplace Management Portal.
    * Support information for your product – This information
     includes email addresses and URLs for your product's support
     channels.

4. **Submit your product for integration**

Use your seller account and the AWS Marketplace Management Portal to [Creating an initial SaaS product page on AWS Marketplace](saas-create-product-page.md "saas-create-product-page.md"). AWS Marketplace will publish your product as a limited product, which means that it's
only available to use for integration and testing. Your product code and
Amazon Simple Notification Service (SNS) topics will be available to you on the product overview
page.

###### Note

Your product must remain at a reduced price so you and the AWS Marketplace Seller
Operations team can test your product without incurring a large cost. We'll
ask you for the product’s actual price when you request public visibility
for your product. 5. **Integrate with AWS Marketplace**

Your product must support customers onboarding and using your product,
including validating their subscription before giving them access, and, in some
cases, metering for their usage. How you integrate with AWS Marketplace depends on the
offer type you're using for your product. For more information about
integration, based on offer type, see the following topics:

    * [Subscription integration](saas-integrate-subscription.md "saas-integrate-subscription.md")
    * [Contract integration](saas-integrate-contract.md "saas-integrate-contract.md")
    * [Contract with pay-as-you-go integration](saas-integrate-contract-with-pay.md "saas-integrate-contract-with-pay.md")

The final step of integrating your product with AWS Marketplace is to test it to ensure
that the integration works properly. 6. **Product testing and contract
cancellation**

After you have completed the integration process, we recommend that you
subscribe to your own product to evaluate and confirm the customer experience.
Creating a test subscription allows you to:

    * Review product information
    * Examine available purchase options
    * Process test payments
    * Verify links to your own product website

###### Important

Cancel your pay-as-you-go subscription before changing your product's visibility
from limited to public by following the instructions at [Canceling your SaaS subscription](../buyerguide/cancel-subscription.md#cancel-saas-subscription "../buyerguide/cancel-subscription.md#cancel-saas-subscription"). To cancel contract, contact the AWS Marketplace
Seller Operations team by [submitting a support ticket](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/"). 7. **Submit your product for launch**

After you verify your integration and you’re ready for the product to be live,
choose **Update visibility**. The AWS Marketplace
Seller Operations team will review your product and update the price before the
visibility can be updated to Public.

###### Note

AWS Marketplace Seller Operations uses a manual process to verify and update SaaS products.
The process takes 7–10 business days to update visibility to public, and longer if the team finds errors.
For more information about timing, see [Timing and expectations](product-submission.md#timing-and-expectations "product-submission.md#timing-and-expectations") in this guide.
