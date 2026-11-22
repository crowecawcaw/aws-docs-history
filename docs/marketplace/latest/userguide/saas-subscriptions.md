

# Pricing for SaaS subscriptions

For software as a service (SaaS) subscriptions, AWS Marketplace bills your customers based on the metering records that you send to us. All charges must be measured and reported every hour from the software deployed in the customer's account. All usage is then calculated monthly and billed monthly using the same mechanism as AMI based AWS Marketplace offerings. Our ability to bill customers for usage of your product is dependent upon receiving metering records from you. You are responsible for ensuring that your product’s metering records are successfully transmitted and received. 

Before you can publish a SaaS product with subscription pricing, you must do the following:

**To create a SaaS subscription product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

   The product must have Limited or Public visibility. To create one, see [Creating an initial SaaS product page on AWS Marketplace](saas-create-product-page.md).

1. Choose the **Procurement** tab.

1. In the **Public offer** section, choose **Create public offer**.

**To complete the public offer for a SaaS subscription product**

1. On the **Set pricing model and dimensions** step, for **Pricing model**, choose **Usage-based pricing**.

   You can't change the pricing model later. To use a different pricing model, create a new product.

1. For **Dimension unit type**, choose the unit that describes how you price your product.

   You can't change the unit type later. If the unit differs between dimensions, choose **Units**.

1. Add your usage dimensions. For each dimension, enter the **API identifier**, **Display name**, and **Description**.

   The API identifier is the dimension name that your metering records use, and you can't change it after you create the dimension. Use up to 60 letters, numbers, and underscores, and don't start with a number. The display name can have up to 80 characters, and the description can have up to 90.

1. Complete the **Configure pricing details and duration**, **Specify refund policy**, **Configure legal terms and offer documents**, and **Configure offer availability** steps.

1. On the **Review and create** step, choose **Create public offer**.

AWS Partner Central returns you to the **Procurement** tab while AWS Marketplace processes the request. When the request succeeds, your public offer appears in the **Public offer** section.

To find the product code that your integration uses, choose **Show more** in the product's **Product summary**.

## When a SaaS subscription ends
<a name="saas-subscription-ends"></a>

**Amazon SNS notifications aren't available to new sellers**  
If you registered your seller account after July 15, 2026, use Amazon EventBridge to receive events. If you registered on or before that date, you can continue to use Amazon SNS. For more information, see [Managing SaaS subscription events with Amazon EventBridge](saas-eventbridge-integration.md).

 A customer can unsubscribe from your SaaS subscription product through the AWS Management Console. Key points of the SaaS subscription ending process include the following: 

1. Your default Amazon EventBridge bus will receive a purchase agreement ended event for that customer.

1.  You have one hour to meter any remaining usage for the customer. 

1. After this hour, you receive a license deprovisioned - manufacturer event. At this point, you can no longer send metering records for this customer. 

 It’s up to you to decide how you want to disable functionality in your SaaS product for unsubscribed customers. For example, your product might complete the customer's existing work but prevent them from creating work. You might want to display a message to the customer that their usage has been disabled. Customers can resubscribe to your product through AWS Marketplace. 

## When a SaaS subscription is cancelled
<a name="saas-subscription-cancellations"></a>

Key points of the SaaS subscription cancellation process include the following: 

1. A customer can cancel their subscription to your SaaS subscription product the **Your Marketplace Software** page of the AWS Marketplace website. 

   Your default Amazon EventBridge bus will receive a purchase agreement ended event for that customer.

1.  You have one hour to meter any remaining usage for the customer. 

1. You notify the customer from your product that the cancellation is in progress. If a customer indicates that they want to cancel through your product, direct the customer to AWS Marketplace. To guarantee that there will be no future charges, customers should conﬁrm the cancellation with AWS Marketplace. 