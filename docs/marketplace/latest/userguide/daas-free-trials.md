

# Creating a DaaS free trial offer in AWS Marketplace

As an AWS Marketplace seller, you can create free trial offers for your Data as a Service (DaaS) products in AWS Partner Central. With a free trial, buyers can use your product for a limited time before they pay. Each AWS account can use one free trial per product.

To find out whether a new agreement is a free trial, call the `DescribeAgreement` API when you receive the **Purchase Agreement Created - Proposer** event. For a free trial, the response includes `freeTrialSummary.trialEndTime`, which tells you when the free trial ends. When a pay as you go free trial converts, AWS Marketplace sends the **Purchase Agreement Free Trial Converted - Manufacturer** event. For more information, see [Managing DaaS subscription events with Amazon EventBridge](daas-eventbridge-integration.md).

## How free trials end
<a name="daas-free-trials-conversion"></a>

You set the length of a free trial, from 7 to 90 days. What happens when the free trial ends depends on your pricing model:
+ **Pay as you go** – The free trial converts automatically to a paid subscription when it ends.
+ **Contract** and **contract with consumption** – The free trial doesn't convert. It expires when it ends. When a free trial expires, remove the buyer's access to your product.

## Creating a DaaS free trial offer
<a name="daas-free-trials-create"></a>

You create DaaS free trial offers in AWS Partner Central.

**To create a DaaS free trial offer**

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Choose **Offers**, and then choose **Public offers**.

1. Choose **Create free trial**. You can create one free trial for each public DaaS product.

1. For **Offer fundamentals**, select your **Product**, and then choose **Next**.

1. In **Free trial settings**, enter the **Free trial length (days)**. Free trials can last from 7 to 90 days.

1. Review the pricing:
   + For pay as you go products, review the **Paid pricing terms**. Buyers pay these rates after the free trial ends.
   + For contract products, review the **Product dimensions**. You can set the quantity limits for each dimension, and **Remove** or **Add dimensions**.

1. For contract products, view the **Service agreement** and select the EULA version. Then go to the review page.

1. Verify the information, and then submit the free trial.

For pay as you go products, AWS Marketplace adds the free trial to your public offer. There's no separate free trial offer, and the free trial converts automatically. For contract products, AWS Marketplace creates a separate free trial offer that doesn't convert.

## Canceling a DaaS free trial offer
<a name="daas-free-trials-cancel"></a>

You can cancel a contract free trial offer at any time in AWS Partner Central.

**To cancel a DaaS free trial offer**

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Choose **Offers**, and then choose **Public offers**.

1. Find the free trial offer.

1. Choose **Cancel**.

After you cancel an offer, active agreements for the offer stay active until they expire. Buyers can't create new agreements for a canceled offer.

For pay as you go products, the free trial is part of your public offer, so there's no separate offer to cancel. To change the length of the free trial or remove it, use the `UpdatePricingTerms` change type in the AWS Marketplace Catalog API. For more information, see [Working with change sets](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets) in the *AWS Marketplace API Reference*.