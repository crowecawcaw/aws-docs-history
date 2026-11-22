

# Contract pricing for AMI products on AWS Marketplace

Contract pricing for Amazon Machine Image (AMI)-based products means that the buyer pays an upfront fee for a single AMI product or single AMI with AWS CloudFormation stack. For AMI-based products with contract pricing, AWS Marketplace bills your customers upfront or by the payment schedule that you define, based on the contract between you and your customer. After that point, they're entitled to use those resources. This topic provides more information about contract pricing.

To set your pricing, choose one or more contract durations that you offer customers. You can enter different prices for each contract duration. Your options are 1-month, 12-months, 24-month, and 36-month durations. For private offers, you can specify a custom duration in months (up to 144 months). 

**Note**  
Free trials are not available for AMI products with contract pricing.

You set contract pricing when you create your product's public offer. You can add up to 200 dimensions to the offer. The display name and description of each dimension appear to customers on the product detail and procurement pages of the AWS Marketplace website.

**To start a public offer**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

   The product must have Limited or Public visibility. To create one, see [Create the listing](ami-single-ami-products.md#ami-create-product).

1. Choose the **Procurement** tab.

1. On the **Public offer** card, choose **Create public offer**.

   The **Create public offer** page opens. Continue with the following procedures.

**To set the pricing model and dimensions**

1. On the **Set pricing model and dimensions** step, for **Pricing model**, choose **Contract pricing**.

   You can't change the pricing model later. To use a different pricing model, create a new product.

1. For **Dimension unit type**, choose the unit that describes how you price your product.

   The options are **Gbps**, **Mbps**, **GB**, **MB**, **TB**, **Requests**, **Units**, **Hosts**, and **Users**. You can't change the unit type later. If the unit differs between dimensions, choose **Units**.

1. Choose **Add contract dimension**.

1. In the panel, enter the **API identifier**, **Display name**, and **Description**, and then choose **Add dimensions**.

   The API identifier is the entitlement name in the license that AWS Marketplace creates in the buyer's AWS License Manager account. Your software passes it as `Name` in the `CheckoutLicense` call. Use up to 36 letters, numbers, and underscores, and don't start with a number. You can't change the API identifier later. The display name can have up to 80 characters, and the description can have up to 1,000. To add more than one dimension, choose **Add new dimension** before you choose **Add dimensions**.

1. Choose **Next**.

**To set prices and create the public offer**

1. On the **Configure pricing details and duration** step, under **Purchasing options**, choose **Multiple dimensions per contract** or **Single dimension per contract**.

   With multiple dimensions, buyers choose a quantity of each dimension. With a single dimension, buyers choose one tier from your dimensions, with no quantity.

1. For **Contract duration options**, select the durations that buyers can choose, and then enter the price of each dimension for each duration.

   Prices can have up to 3 decimal places. With multiple dimensions per contract, the price applies to each unit that the buyer buys.

1. Complete the **Specify refund policy**, **Configure legal terms and offer documents**, and **Configure offer availability** steps.

1. On the **Review and create** step, choose **Create public offer**.

AWS Partner Central returns you to the **Procurement** tab while AWS Marketplace processes the request. When the request succeeds, your public offer appears on the **Public offer** card. To add dimensions or change a dimension's display name or description later, choose **Update** in the **Pricing dimensions** section of the **Procurement** tab.


**Example: Data storage application**  

|   | 1-month price | 12-month price  | 24-month price  | 36-month price  | 
| --- | --- | --- | --- | --- | 
| Unencrypted data (GB)  |  $1.50/GB  |  $16.00/GB  |  $30.00/GB  |  $60.00/GB  | 
| Encrypted data (GB)  |  $1.55/GB  |  $16.60/GB  |  $31.20/GB  |  $61.20/GB  | 


**Example: Log monitoring product**  

|   | 1-month price | 12-month price  | 24-month price | 36-month price | 
| --- | --- | --- | --- | --- | 
| Basic (10 hosts monitored, 5 containers monitored)  |  $100  |  $1000  | $2000  | $4000 | 
| Standard (20 hosts monitored, 10 containers monitored)  |  $200  |  $2000  | $4000  | $8000 | 
| Pro (40 hosts monitored, 20 containers monitored)  |  $400  |  $4000  | $8000  | $16,000 | 
| Additional hosts monitored per hour  | $10  | $100  |  $200 | $400 | 
| Additional containers monitored per hour  | $10  | $100  |  $200 | $400 | 

**Note**  
The prices can be for the following durations: 1 month, 12 months, 24 months, or 36 months. You can choose to offer one or more of these options for your product. The durations must be the same across each dimension.   

**Example**  
For example, in a case where you have `ReadOnlyUsers` and `AdminUsers` dimensions, if you offer a yearly price for ReadOnlyUsers, you must offer a yearly price for `AdminUsers`, too.

## Automatic renewals
<a name="ami-contracts-automatic-renewals"></a>

 When customers purchase your product through AWS Marketplace using AMI contracts, they can agree to automatically renew the contract terms. Customers continue to pay for the entitlements every month or for 1, 2, or 3 years. 

Customers can modify their renewal settings at any time. For more information, see [Modifying an existing contract](https://docs.aws.amazon.com/marketplace/latest/buyerguide/modify-existing-contract.html) in the *AWS Marketplace Buyer Guide*.