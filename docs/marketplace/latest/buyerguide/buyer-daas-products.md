

# DaaS products through AWS Marketplace

With Data as a Service (DaaS) products, you subscribe to data and content through AWS Marketplace, and the seller delivers it to you. Depending on the product, the seller might deliver data through an API, a web portal, an Amazon S3 location, or a managed feed. Charges for DaaS products appear on your AWS bill.

DaaS products use the following pricing options:
+ **Pay as you go** – You pay for the data that you use.
+ **Contract** – You pay in advance for a quantity of the product for a set duration.
+ **Contract with consumption** – You pay for a contract, and you also pay for usage beyond what the contract includes.
+ **Free** – You use the product at no cost.
+ **Free trials** – You can try some products at no cost for a limited time.

You can also ask the seller for a private offer with custom pricing and terms. For more information, see [Private offers in AWS Marketplace](buyer-private-offers.md).

## Subscribing to a DaaS product
<a name="buyer-daas-subscribe"></a>

Use the following procedure to subscribe to a DaaS product with a public offer.

**To subscribe to a DaaS product**

1. On the product detail page, choose **View purchase options**.

1. If the product has more than one offer, choose an offer.

1. Review the pricing dimensions and the price for each one. For a contract, choose the quantities, the contract duration, and whether the contract renews automatically.

1. Review the end user license agreement (EULA) for the offer.

1. Choose **Subscribe**.

After you subscribe, you set up your account with the seller to get access to the data. For more information, see [Accessing your data after you subscribe](#buyer-daas-access).

## Accessing your data after you subscribe
<a name="buyer-daas-access"></a>

After you subscribe, you finish setup on the seller's website, where you create an account or sign in. You don't need any additional permissions to do this.

**To access a DaaS product that you subscribed to**

1. On the product's procurement page, choose **Launch your software**.

1. On the **Set up your account** page, review the seller's usage instructions and your agreement details, including the agreement ID and the service start and end dates.

1. Choose **Set up your account**. AWS Marketplace opens the seller's website, where you create an account or sign in.

To return to the **Set up your account** page later, open the product's procurement page, or find the product in your subscriptions in the AWS Marketplace console.

## DaaS free trials
<a name="buyer-daas-free-trials"></a>

Some sellers offer free trials of their DaaS products. Each AWS account can use one free trial per product.

What happens when a free trial ends depends on the pricing model:
+ **Pay as you go** – The free trial converts to a paid subscription when it ends.
+ **Contract** and **contract with consumption** – The free trial doesn't convert. It expires when it ends.

## Canceling a DaaS subscription
<a name="buyer-daas-cancel"></a>

You can cancel a DaaS subscription with pay as you go or free pricing in the AWS Marketplace console. You can't cancel a subscription with contract or contract with consumption pricing in the console. If **Cancel subscription** isn't available, or for information about refunds, see [Canceling product subscriptions](cancel-subscription.md).

**To cancel a pay as you go or free DaaS subscription**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace).

   The **Manage subscriptions** page appears.

1. Choose the subscription that you want to cancel.

1. Under **Agreement**, open the **Actions** list and choose **Cancel subscription**.

1. In the **Cancel subscription** dialog box, enter **confirm**, then choose **Yes, cancel subscription**.

**To cancel auto-renewal for your DaaS contract**

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace).

1. Go to the **Product detail** page.

1. Choose **Continue** to get to the ordering page.

1. Choose the **Modify renewal** tab, then choose **Cancel renewal**.