

# Creating a SaaS free trial offer in AWS Marketplace

As an AWS Marketplace seller, you can create software as a service (SaaS) free trial offers in AWS Partner Central. With a free trial, you let buyers evaluate your product before they buy it. After a buyer subscribes to your product, your product performs entitlement checks the same way it does for paid buyers.

**Note**  
Agentic Commerce products don't support free trials. For more information, see [Requirements and limitations](agentic-commerce-products.md#agentic-commerce-requirements).

Each AWS account can use one free trial per product. The free usage amount granted during a free trial is not shared across linked accounts in an AWS organization. Different linked accounts within a single main payer account can create their own individual free trials.

**Note**  
If you use the Seller Data Delivery Service (SDDS), you receive an [Agreement details trial report](https://docs.aws.amazon.com/marketplace/latest/userguide/supplementary-reports.html) in your Amazon Simple Storage Service bucket. The report includes agreement details such as the subscriber name and ID, offer ID, and agreement start and end dates.
You also receive [Amazon EventBridge events](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-eventbridge-integration.html) when new subscriptions are created. On the conversion date, AWS Marketplace sends you the `Purchase Agreement Free Trial Converted - Manufacturer` event. AWS Marketplace also emails you when a buyer's free trial converts.  
To check whether a buyer is in a free trial, call `DescribeAgreement` and read `freeTrialSummary.trialEndTime`, or call `SearchAgreements` and read `freeTrialEndTime`. If the time is in the future, the buyer is in the free trial. If you registered your seller account on or before July 15, 2026, you can also receive [Amazon SNS notifications](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-notification.html), which include an `isFreeTrialTermPresent` flag. Amazon SNS doesn't send a message when a free trial converts.
Buyers who subscribe to your free trial go to your registration URL with an additional token, `x-amzn-marketplace-offer-type=free-trial`. You can use the token to create a unique registration experience for free trial buyers.

## How free trials work for SaaS subscription products
<a name="saas-free-trials-auto-conversion"></a>

For SaaS subscription (usage-based) products, a free trial converts automatically to a paid subscription when it ends. Your public offer includes the free trial and your pricing. The buyer stays subscribed to the same offer during the free trial and after it ends, so the buyer keeps access to your product.
+ You set the free trial length, from 7 to 90 days.
+ AWS Marketplace doesn't bill usage during the free trial.
+ AWS Marketplace emails the buyer 3 days and 1 day before the conversion date. For free trials longer than 15 days, the buyer also gets an email 15 days before conversion.
+ On the conversion date, AWS Marketplace starts to bill usage at your pricing.
+ The buyer can cancel at any time before the conversion date. A buyer who cancels during the free trial pays nothing.

**Note**  
SaaS contract free trials don't convert automatically and expire when they end.

## How your integration works with a free trial
<a name="saas-free-trials-integration"></a>

The free trial and the paid period are one subscription to your public offer. At conversion, the buyer doesn't get a new offer or a new subscription. This affects your integration in the following ways.

Metering  
Send metering records with `BatchMeterUsage` for all usage from the buyer's first day. AWS Marketplace doesn't bill usage during the free trial.

Access  
The subscription continues after the free trial. Keep the buyer's access until the buyer cancels.

Conversion  
To know when a free trial converts, use the conversion event. You can also call `DescribeAgreement` and check `freeTrialSummary.trialEndTime`.

Offer  
Don't use the offer to decide whether a buyer is in a free trial. All buyers subscribe to the same offer.

Notifications  
Use Amazon EventBridge to receive the conversion event. Amazon SNS doesn't send a conversion message.

## Creating a SaaS free trial offer
<a name="creating-saas-free-trial"></a>

You can create SaaS free trial offers in AWS Partner Central.

**To create a SaaS free trial offer**

1. Open the [**Offers**](https://us-east-1.console.aws.amazon.com/partnercentral/offers) page in AWS Partner Central, and sign in to your seller account.

1. On the **Public offers** tab, choose **Create free trial**.

1. Under **Offer fundamentals**, for **Product**, choose your product, and then choose **Next**.

   You can create one free trial for each product. A SaaS subscription product must already have a public offer.

1. Under **Free trial settings**, for **Free trial length (days)**, enter a number from 7 to 90.

   For a SaaS subscription product, the **Usage dimensions** table shows the rates that buyers pay after the free trial ends.

1. For a SaaS contract product, complete the following:
   + Under **Free trial settings**, enter a **Quantity** for each dimension. To leave a dimension out of the free trial, choose **Remove**.
   + Under **Legal terms and offer documents**, choose the legal terms that buyers accept for the free trial.

1. Choose **Review changes**.

1. Choose **Create free trial offer**.

AWS Partner Central returns you to the **Offers** page while AWS Marketplace processes the request.

For SaaS subscription products, AWS Marketplace adds the free trial to your public offer. There's no separate free trial offer, and the free trial converts automatically. For SaaS contract products, AWS Marketplace creates a separate free trial offer that doesn't convert.

## Updating an existing free trial offer
<a name="enabling-saas-free-trial-auto-conversion"></a>

A free trial offer that you created before automatic conversion was available doesn't convert. To make it convert, update the offer one time. Before you update it, make sure that your integration works as described in [How your integration works with a free trial](#saas-free-trials-integration).

**Important**  
You can't undo this update.

**To update an existing free trial offer**

1. Open the [**Offers**](https://us-east-1.console.aws.amazon.com/partnercentral/offers) page in AWS Partner Central, and sign in with the AWS account that manages the offer.

1. Choose the **Public offers** tab.

1. Select your free trial offer, and then choose **View details**.

1. Choose **Auto-convert free trials**.

1. In the confirmation dialog, choose **Enable**.

The request takes a few minutes. After the update, AWS Marketplace moves your free trial to your public offer and expires the separate free trial offer. New subscribers convert automatically. Buyers already in a free trial finish on their current terms. Their free trials then expire.

**Note**  
After you update the offer, the standalone free trial offer expires. Update any links that use its offer ID, such as links on your website and Buy with AWS buttons. A link that uses the ID of the expired offer shows buyers an Offer not found page.

## Metering during a free trial
<a name="saas-free-trial-metering"></a>

Send metering records for all usage during the free trial, at your usual hourly cadence. AWS Marketplace doesn't bill usage that happens before the conversion date. AWS Marketplace bills usage after the conversion date at your pricing.

If a buyer cancels, you have 1 hour after the `License Deprovisioned - Manufacturer` event to send remaining usage records.

## Canceling a SaaS free trial offer
<a name="cancelling-saas-free-trial"></a>

You can cancel free trial offers at any time from AWS Partner Central. This procedure applies to SaaS contract free trial offers and to free trial offers that you haven't updated to convert automatically.

**To cancel a SaaS free trial offer**

1. Open the [**Offers**](https://us-east-1.console.aws.amazon.com/partnercentral/offers) page in AWS Partner Central, and sign in to your seller account.

1. Choose the **Public offers** tab.

1. Select the offer.

1. Choose **View details**.

1. Choose **Cancel offer**.

After an offer is canceled, active agreements for this offer are active until expiration. New agreements for a canceled offer can't be created.

For SaaS subscription products, the free trial is part of your public offer, so you don't cancel a separate offer. To change the duration of the free trial or remove it, use the `UpdatePricingTerms` change type in the AWS Marketplace Catalog API. For more information, see [Working with change sets](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html#working-with-change-sets) in the *AWS Marketplace API Reference*.