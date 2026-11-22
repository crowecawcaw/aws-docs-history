

# Pricing for SaaS contracts

SaaS contracts allow customers to purchase your software through an upfront agreement. Under the agreement, customers are entitled to a specified quantity of use of your SaaS product. You define the usage categories, dimensions, and the length of the contract. AWS Marketplace bills your customers upfront or by the payment schedule that you define. For additional usage above their contract, your software reports the usage through the AWS Marketplace Metering Service (AWS Marketplace Metering Service).

When using the SaaS Contract pricing model, your application never sends metering records. Instead, it verifies entitlement by calling the AWS Marketplace Entitlement Service (AWS Marketplace Entitlement Service). AWS Marketplace communicates these entitlements to your SaaS application.

## Creating a SaaS contract product
<a name="creating-saas-contract-product"></a>

Before you can publish a SaaS product with contract pricing, create the product and set up its contract pricing.

**To create a SaaS contract product**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

   The product must have Limited or Public visibility. To create one, see [Creating an initial SaaS product page on AWS Marketplace](saas-create-product-page.md).

1. Choose the **Procurement** tab.

1. In the **Public offer** section, choose **Create public offer**.

   The **Create public offer** page opens. Continue with the following procedures.

**To set the pricing model and dimensions**

1. On the **Set pricing model and dimensions** step, for **Pricing model**, choose **Contract-based pricing**.

   You can't change the pricing model later. To use a different pricing model, create a new product.

1. (Optional) To let buyers pay for usage above their contract, select **Enable additional usage on top of contract**.

1. For **Dimension unit type**, choose the unit that describes how you price your product.

   You can't change the unit type later. If the unit differs between dimensions, choose **Units**.

1. Add your contract dimensions. For each dimension, enter the **API identifier**, **Display name**, and **Description**.

   For more information, see [Understanding SaaS contract pricing dimensions](#understanding-saas-contract-pricing-dimensions).

1. Choose **Next**.

**To set prices and create the public offer**

1. On the **Configure pricing details and duration** step, under **Purchasing options**, choose **Multiple dimensions per contract** or **Single dimension per contract**.

   With multiple dimensions, buyers choose a quantity of each dimension. With a single dimension, buyers choose one tier from your dimensions.

1. For **Contract duration options**, select the durations that buyers can choose, and then enter the price of each dimension for each duration.

   You can offer 1, 12, 24, or 36 months. If you enabled additional usage, also enter the hourly price under **Usage dimension pricing**.

1. Complete the **Specify refund policy**, **Configure legal terms and offer documents**, and **Configure offer availability** steps.

1. On the **Review and create** step, choose **Create public offer**.

AWS Partner Central returns you to the **Procurement** tab while AWS Marketplace processes the request. When the request succeeds, your public offer appears in the **Public offer** section.

To find the product code that your integration uses, choose **Show more** in the product's **Product summary**.

## Understanding SaaS contract pricing dimensions
<a name="understanding-saas-contract-pricing-dimensions"></a>

Each pricing dimension represents a feature or service that you can set a per unit price for. Examples of dimensions are users, hosts scanned, and GB of logs ingested. For each dimension you define, you add a name, a description, a price, and an API identifier. The name, price, and description are displayed to customers. You use the API identifier for tracking and reporting with AWS Marketplace as follows:
+ Calling the [AWS Marketplace Entitlement Service](https://docs.aws.amazon.com/marketplaceentitlement/latest/APIReference/Welcome.html) to retrieve the dimensions your customers have purchased.
+ Calling the [AWS Marketplace Metering Service](https://docs.aws.amazon.com/marketplacemetering/latest/APIReference/Welcome.html) to indicate which dimensions customers used.

For each pricing dimension in your contract, you can choose to let customers pay as they go for additional usage of that dimension above their contract. You can also add additional dimensions without contract prices that customers only consume by paying as they go.

When you create the public offer, you define the following fields for each contract dimension:

**API identifier**  
The name that you use when you call the AWS Marketplace Entitlement Service. This name is visible in billing reports and reports that aren't external-facing. It can have 1 to 36 characters: letters, numbers, and underscores. You can't change it after you create the dimension.

**Display name**  
The customer-facing name of the dimension. Use a name that helps buyers understand the dimension. It can have 1 to 80 characters and can't start with a space. You can change it later.

**Description**  
The customer-facing description of the dimension. It can have 1 to 1,000 characters and can't start with a space.

On the **Configure pricing details and duration** step, you enter a price per unit for each dimension in each contract duration that you offer. Each price is a one-time charge for the whole duration, not a monthly charge. Prices support up to 3 decimal places.


**Example: Data storage application**  

|   | Monthly price  | 12-month price  | 24-month price  | Pay-as-you-go price for additional usage  | 
| --- | --- | --- | --- | --- | 
|  Unencrypted data (GB)  |  $1.50/GB  |  $16.00/GB  |  $30.00/GB  |  $0.1/GB per hour  | 
|  Encrypted data (GB)  |  $1.55/GB  |  $16.60/GB  |  $31.20/GB  |  $0.11/GB per hour  | 


**Example: Log monitoring product**  

|   | Monthly price  | 12-month price  | Pay-as-you-go price for additional usage  | 
| --- | --- | --- | --- | 
|  Basic (10 hosts monitored, 5 containers monitored)  |  $100  |  $1000  |   | 
|  Standard (20 hosts monitored, 10 containers monitored)  |  $200  |  $2000  |   | 
|  Pro (40 hosts monitored, 20 containers monitored)  |  $400  |  $4000  |   | 
|  Additional hosts monitored per hour  |   |   |  $0.1  | 
|  Additional containers monitored per hour  |   |   |  $0.2  | 

**Note**  
The prices can be for the following durations: 1 month, 12 months, 24 months, or 36 months. You can choose to offer one or more of these options for your product. The durations must be the same across each dimension. For example, assume that you have `ReadOnlyUsers` and `AdminUsers` dimensions. If you offer a yearly price for `ReadOnlyUsers`, you must offer a yearly price for `AdminUsers`, too.

## SaaS contract upgrades
<a name="upgrades"></a>

 Customers can upgrade a contract to one of a higher value except for longer durations. For example, they can upgrade to higher quantities or higher-value entitlements. Customers are given a prorated credit for their existing contract. Customers can't decrease the size of their existing contract. They can only decrease the size at renewal, or cancel their renewal.

 Entitlements are veriﬁed by your SaaS product, which makes calls to the AWS Marketplace Entitlement Service. 

## Automatic renewals
<a name="automatic-renewals"></a>

 When a customer purchases your product through AWS Marketplace using SaaS contracts, they can agree to automatic renewal of the contract terms. The customer continues to pay for the entitlements every month or for 1, 2, or 3 years. The customer always has the option to modify the renewal settings. They can cancel the renewal or renew the contract for different quantities and durations. 

## When a SaaS contract ends
<a name="saas-contract-ends"></a>

A SaaS contract product has a contract expiry. When a contract ends, the following events occur: 

1.  Your SaaS product receives an `entitlement-updated` notification indicating the buyer's entitlement has changed. The AWS Marketplace Entitlement Service returns an empty response. 

1.  You have 1 hour to meter any remaining usage for the customer. After this time has elapsed, you can no longer send metering records for this customer. 

## When a SaaS contract is canceled
<a name="saas-contract-cancellations"></a>

Key points of the SaaS contract cancellation process include the following: 

1. Customers can request a cancellation and refund for SaaS contract products though AWS Support.

   Customers must request refunds within 48 hours through AWS Support. 

   The full or prorated refund is typically granted in 3–5 business days. 

1. Your SaaS product receives notification through Amazon EventBridge events for that customer.

1. You have one hour to send a ﬁnal metering record for the customer for any additional usage charges. 

1. You notify the customer from your product that the cancellation is in progress. If a customer indicates that they want to cancel through your product, direct the customer to AWS Marketplace. To guarantee that there will be no future charges, customers should conﬁrm the cancellation with AWS Marketplace. 