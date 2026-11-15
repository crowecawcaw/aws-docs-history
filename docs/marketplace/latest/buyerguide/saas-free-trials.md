

# Subscribing to SaaS free trials
<a name="saas-free-trials"></a>

Some vendors offer free trials for their SaaS products through AWS Marketplace for evaluation purposes. You can search through SaaS products in AWS Marketplace and filter results to show only those with free trials. All free trial products display the **Free trial** badge next to the product logo. On the product procurement page, you can find the duration of the free trial and what happens when the free trial ends.

What happens when a free trial ends depends on the pricing model:

SaaS subscription (usage-based) free trials  
The free trial converts to a paid subscription when it ends. You keep access to the product, and you don't need to subscribe again. For more information, see [Free trials that convert automatically](#saas-free-trials-auto-conversion).

SaaS contract free trials  
The free trial expires when it ends. To continue to use the product, subscribe to a public offer or negotiate a private offer. If you no longer want the product, you can let the free trial expire.

To view your subscriptions, choose **Manage subscriptions** in the AWS Marketplace console.

**Note**  
Each AWS account can use one free trial per product.

**To subscribe to a SaaS contract free trial offer**

1. Sign in to the AWS Marketplace console, and choose **Discover products** from the AWS Marketplace menu. 

1. In the **Refine results** panel, go to **Free trial** and select **Free trial**.

1.  For **Delivery methods**, select **SaaS**. 

1. For **Pricing model**, select **Upfront Commitment** to view all products that offer free trials. All eligible products display a **Free trial** badge.

1. Select the SaaS product that you want.

1. Choose **Try for free** from the product detail page. 

1. For **Offer type**, select a **Free trial** option. 

1. For **Purchase**, choose **Try for free**.

1. Choose **Set up your account** to complete your registration and start to use your software.

**To subscribe to a SaaS subscription free trial offer**

1.  Sign in to the AWS Marketplace console, and choose **Discover products** from the AWS Marketplace menu. 

1. In the **Refine results** panel, go to **Free trial** and select **Free trial**.

1. For **Delivery methods**, select **SaaS**. 

1. For **Pricing model**, select **Usage Based** to view all products that offer free trials. All eligible products display a **Free trial** badge.

1. Select the SaaS product that you want.

1. Choose **Try for free** from the product detail page. 

1. Review the free trial length, the conversion date, and the pricing after the free trial.

1. Select the acknowledgment check box.

1. Choose **Subscribe**.

## Free trials that convert automatically
<a name="saas-free-trials-auto-conversion"></a>

Before you subscribe, the product procurement page shows the free trial length, the conversion date, and the pricing after the free trial. The page also states that the free trial converts automatically to a paid subscription, and that you can cancel at any time before conversion. To subscribe, you must accept the conversion terms.

You aren't charged for software usage during the free trial. Starting on the conversion date, you're charged for usage at the seller's pricing.

AWS Marketplace sends you an email before your free trial converts:
+ 15 days before the conversion date, for free trials longer than 15 days
+ 3 days before the conversion date
+ 1 day before the conversion date

Each email includes guidance on how to cancel your subscription. For where these emails go and how to add recipients, see [Buyer notifications for AWS Marketplace events](buyer-notifications.md). AWS Marketplace also sends the `Purchase Agreement Free Trial Converting Soon - Acceptor` event to Amazon EventBridge at each reminder.

**Note**  
AWS accounts on the free account plan can't subscribe to free trials that convert automatically.

## Canceling a SaaS free trial
<a name="saas-free-trials-cancel"></a>

You can cancel a free trial at any time. To cancel, cancel your subscription. For instructions, see [Canceling your SaaS subscription](cancel-subscription.md#cancel-saas-subscription). You can also follow the guidance in the reminder email.

If you cancel before the conversion date, you aren't charged for software usage during the free trial. If you cancel after the conversion date, you're charged for usage from the conversion date until you cancel. In both cases, your subscription ends and the seller can end your access to the product.