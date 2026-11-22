

# Creating a free trial

As an AWS Marketplace seller, you can create free trial offers for your RTB Fabric module products in AWS Partner Central. With a free trial, buyers can use your product for a limited time before they pay. Each AWS account can use one free trial per product.

To find out whether a new agreement is a free trial, call the `DescribeAgreement` API operation when you receive the `Purchase Agreement Created - Proposer` event. For a free trial, the response includes `freeTrialSummary.trialEndTime`, which tells you when the free trial ends.

## How free trials end
<a name="additional-product-types-free-trials-end"></a>

You set the length of a free trial, from 7 to 90 days. RTB Fabric module products are contract priced, so the free trial expires when it ends and doesn't convert to a paid agreement. To continue, the buyer accepts your public offer or a private offer.

## Creating a free trial offer
<a name="additional-product-types-free-trials-create"></a>

You create free trial offers for your RTB Fabric module products in AWS Partner Central.

**To create a free trial offer**

1. Sign in to AWS Partner Central.

1. Choose **Offers**, and then choose the **Public free trials** tab.

1. Choose **Create free trial**. You can create one free trial for each public product.

1. For **Offer fundamentals**, select your **Product**, and then choose **Next**.

1. In **Free trial settings**, enter the **Free trial length (days)**. Free trials can last from 7 to 90 days.

1. Review the **Product dimensions**. You can set quantity limits for each dimension, and remove or add dimensions.

1. View the **Service agreement** and select the EULA version. Then go to the review page.

1. Verify the information, and then submit the free trial.

AWS Marketplace creates a separate free trial offer that doesn't convert.

## Canceling a free trial offer
<a name="additional-product-types-free-trials-cancel"></a>

You can cancel a free trial offer at any time in AWS Partner Central.

**To cancel a free trial offer**

1. Sign in to AWS Partner Central.

1. Choose **Offers**, and then choose the **Public free trials** tab.

1. Select the offer.

1. Choose **View offer**.

1. Choose **Cancel offer**.

After you cancel an offer, active agreements for the offer stay active until they expire. Buyers can't create new agreements for a canceled offer.

## Telling a trial from a paid agreement
<a name="additional-product-types-free-trials-identify"></a>

You can tell a trial agreement from a paid agreement in the following ways:
+ `DescribeAgreement` returns a `freeTrialSummary` block (with a `trialEndTime`) for a trial agreement, and `endTimeBehavior` is `EXPIRE` with reason code `NO_RENEWAL_TERM`. A paid agreement has no `freeTrialSummary`, and `endTimeBehavior` is `RENEW` with the renewal offer. The `freeTrialSummary` field is a reliable trial indicator.
+ `GetAgreementTerms` returns a `freeTrialPricingTerm` for a trial agreement.