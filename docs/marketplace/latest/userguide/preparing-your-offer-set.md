# Preparing your offer set

## What are offer sets?

Offer sets enable you to combine multiple private offers into a single-click purchase experience, simplifying procurement for customers purchasing your multi-product solution.

## Understanding offer sets

An offer set is a container that groups multiple private offers together. Key features:

- **Multiple offers**: Combine up to 7 private offers in a single offer set
- **Unified acceptance**: Customers review and accept all offers with one action
- **Flexible terms**: Each offer maintains distinct pricing, payment terms, duration, and EULA
- **Separate agreements**: Each product creates its own agreement. This allows you to manage each product independently after purchase

## Getting Started

1. Sign in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/partners/management-tour "https://aws.amazon.com/marketplace/partners/management-tour").
2. Go to **Offers** → **Private Offer Sets**.
3. Choose **Create offer set**.

###### Note

Some accounts show a left navigation bar. If you see this, go to **Sell** → **Private Offers**.

## Step 1: Configure offer set details

Complete the following information:

- **Offer set name**: Create a descriptive name for easy identification.
- **Customer note**: Include relevant information for your customer.
- **Solution ID association**: Optionally link to an existing solution ID.

## Step 2: Create individual private offers

For each product in your solution, create a separate private offer. You'll use different offer types depending on product ownership:

- **Marketplace Private Offer (MPPO)**: Use for products you own directly.
- **Channel Partner Private Offer (CPPO)**: Use for products you are authorized to resell.
  - Requires valid selling authorization from the product owner.
  - Allows you to share revenue between you and the ISV.

## Step 3: Set offer terms

For each private offer in your offer set, configure:

- **Buyer account ID(s)**: Specify the AWS account ID(s) of the buyer who will receive this offer.
- **Pricing**: Set contract amounts, usage rates, or other pricing dimensions.
- **Payment terms**: Define payment schedules and methods.
- **Duration**: Set contract start and end dates.
- **EULA**: Attach appropriate End User License Agreements.
- **Region targeting**: Choose which AWS regions the offer covers.

### Important requirements

- All offers in an offer set must use the same currency.
- All offers must target the same buyer AWS account.
- All offers should have the same offer expiration date.
- All offers must target different product IDs.
- Maximum of 7 private offers per offer set.

## Step 4: Review and publish

1. Verify that all offers are correctly included in the offer set.
2. Review offer set details for accuracy.
3. Publish the offer set.

###### Note

After publishing, we send email notifications to both you and your buyer. This is in addition to the individual offer emails sent for each offer in the set.

## Step 5: After the transaction

After a customer accepts your offer set:

- The seller of record for each product receives notifications for their products.
- For Channel Partner offers (CPPOs), you receive margin payments for resold products.
- Product owners (ISVs) receive wholesale prices for their products.
- We calculate listing fees per product.
- View consolidated reporting in Seller Insights. You can filter by offer set ID.

## Offer types and limitations

### Supported

- Direct private offers (MPPO)
- Channel Partner private offers (CPPO)
- All standard private offer features (flexible payments, local currency, etc.)

### Not supported

- Public offers
- Replacement offers (amendments)
- Free trial offers as part of offer sets
