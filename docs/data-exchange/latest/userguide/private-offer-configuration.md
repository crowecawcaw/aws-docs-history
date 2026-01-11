# Creating private offers in AWS Data Exchange

AWS Data Exchange gives providers the option to create custom offers, such as private offers. For more information on private offers, see [Creating an offer for AWS Data Exchange products](prepare-offers.md "prepare-offers.md").

As a data provider, you can provide your data product to a subscriber at terms that are different from the offer terms available to the general public. For products that are not publicly visible, your private offers are the only terms available to customers, and only customers you create private offers for can see the product. Private offers allow you to create a custom offer for one or more AWS accounts. A private offer can be different from other offers in any dimension, including price, duration, payment schedule, data subscription agreement, or refund policy.

As a provider, after you have created a product, you can then create a private offer and make it available to a group of subscribers of your choosing. For publicly visible products, you must create a public offer before you can create a private offer.

To create a private offer for a data product:

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/").
2. Go to the **Data Products** page and select your product.
3. On the **Getting started** tab, select **Create offer** and **Private offer**.
4. On the **Offer details** page, do the following:
   1. Enter the offer name and description.
   2. Select the renewal option.
   3. Set the offer expiration date. Offers expire at 23:59:59 UTC on the set date.

5. Choose **Next** twice.
6. On the **Configure offer pricing and duration** page, specify the following:
   1. Pricing option
   2. Contract duration
   3. Offer currency
   4. Product dimension – The dimension is called `ProductAccess` and is automatically created during the product creation flow.

7. Choose **Next**.
8. On the **Add buyers** page, enter the AWS account IDs for your buyers.
9. Choose **Next**.

###### Important

For linked accounts to benefit from a private offer:

- Include the payer AWS account ID.
- The payer account must accept the hourly terms of the private offer first.
- After the payer account accepts, linked accounts can then accept the private offer.

89. On the **Configure legal terms and offer documents** page, add Data Subcription Agreement or use Data Exchange default, then choose **Next**.

###### Note

You can add up to five files (legal terms, statement of work, bill of materials, pricing sheet, or addendums). The system combines these into one document.

90. On the **Specify refund policy**, add the refund policy.
91. On the **Review and create** page, verify the offer details and choose **Create offer**.
92. After the offer appears on the **Manage private offers** page, open the **Actions** menu, choose **Copy offer URL**, and email it to the buyer.
