# Private offer FAQ

This FAQ answers commonly asked questions about creating, managing, and troubleshooting private offers.

###### Topics

- [What is the Private Offer Success Team (POST), and how can sellers contact them?](#what-is-post "#what-is-post")
- [How can a seller resolve errors when accessing the Offers tab?](#resolve-offers-tab-errors "#resolve-offers-tab-errors")
- [What is an installment plan or flexible payment schedule?](#faq-installment-plans "#faq-installment-plans")
- [How can I help a buyer who receives a 404 Error when accessing a private offer?](#troubleshoot-404-errors "#troubleshoot-404-errors")
- [Why do customers see a "You already have an active contract" error when trying to accept a private offer?](#active-contract-error "#active-contract-error")
- [Can a seller or buyer cancel a private offer?](#cancel-private-offer "#cancel-private-offer")
- [How do I request a refund or contract cancellation?](#request-refund-cancellation "#request-refund-cancellation")
- [When is a buyer invoiced?](#buyer-invoicing "#buyer-invoicing")
- [What steps should a seller take once an offer is accepted?](#seller-steps-after-acceptance "#seller-steps-after-acceptance")
- [How does AWS pay sellers and partners?](#aws-payment-process "#aws-payment-process")
- [How does AWS assess tax?](#aws-tax-assessment "#aws-tax-assessment")
- [Resources and support](#resources-and-support "#resources-and-support")
- [Multi-currency support for private offers](#multi-currency-support-faq "#multi-currency-support-faq")

## What is the Private Offer Success Team (POST), and how can sellers contact them?

The POST enables external audiences on the AWS Marketplace Private Offer experience.
Sellers can us the [Support Form](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") in the AWS Marketplace Management Portal. For help with the support form, download and refer to the [Private offers support form guide](https://d1.awsstatic.com/awsmp/solutions/mk-sol-files/private-offers/Private%20Offer%20Support%20Form%20Guide.pdf "https://d1.awsstatic.com/awsmp/solutions/mk-sol-files/private-offers/Private%20Offer%20Support%20Form%20Guide.pdf") PDF.

## How can a seller resolve errors when accessing the Offers tab?

If you encounter an error when choosing the **Offers** tab in the AWS Marketplace Management Portal, ensure that you meet the following prerequisites:

### Prerequisites for creating private offers to sell software or services directly

1. Verify that your AWS account has the appropriate Identity and Access Management (IAM) policies.
   For more information about required policies, see [IAM policies for private offers](detailed-management-portal-permissions.md "detailed-management-portal-permissions.md").

###### Note

If you need help modifying your IAM policies or permissions, contact your internal AWS administrator.
AWS cannot assist with IAM policies or permissions, as access is managed by customers according to the
[Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model "https://aws.amazon.com/compliance/shared-responsibility-model"). 2. Have at least one non-zero publicly listed product. You can verify this by searching for your vendor on AWS Marketplace.
If no products appear, you may not have listed a product publicly or you have a limited listing.

### Prerequisites for creating channel partner private offers (CPPOs) to resell software or services

- Meet the geographic prerequisites to become a "seller" in AWS Marketplace:
  - Use a legal entity from an [eligible jurisdiction](user-guide-for-sellers.md#eligible-jurisdictions "user-guide-for-sellers.md#eligible-jurisdictions"),
    or a business entity incorporated in one of those areas.
  - Provide the required information about your bank account. You can provide one or more bank accounts, including:
    - A US Automated Clearing House (ACH) account
    - A Society for Worldwide Interbank Financial Telecommunication (SWIFT) bank account from an eligible jurisdiction
    - A [Hyperwallet](https://wssellers.hyperwallet.com/ "https://wssellers.hyperwallet.com/") account

## What is an installment plan or flexible payment schedule?

Installment plans, also known as flexible payment schedules (FPS), allow you to extend private offers with a custom payment schedule.
These plans are available for private offers on certain product and pricing types. For more information, refer to
[Product types eligible for private offers](../buyerguide/buyer-private-offers.md#buyer-private-offers-types "../buyerguide/buyer-private-offers.md#buyer-private-offers-types").

The payment schedule can be spread over the accepted contract duration, with the buyer making payments in regular installments.
After subscribing, your customers can view all payments on the schedule and on their AWS invoice, helping them track their spending.

Installment plans and FPSs allow sellers to specify:

- The number of units per dimension or per instance type
- The payment terms for the contract (upfront, delayed, or multiple invoices)

### Creating an installment plan

###### Note

In software resale scenarios, the independent software vendor (ISV) determines the installment plan.

To create an installment plan

1. On the **Configure offer pricing and duration** page, for **Product pricing**, choose **Contract pricing with installment plan**.
2. Choose the contract duration and specify the offer details.
3. Under **Buyer installment plan**, enter the desired parameters:
   - For upfront invoicing upon acceptance, enter the dollar amount and set the invoice date to the date you are creating the private offer.
   - For delayed invoicing, enter the dollar amount and set a future invoice date.
   - For installment invoicing, choose **Add Payment** to enter multiple payment line items with dollar amounts and invoice dates.

For more information, see [Creating an installment plan](installment-plans.md "installment-plans.md"). You can also watch a [video tutorial on Installment Plans](https://www.youtube.com/watch?v=cgxDVAo336I "https://www.youtube.com/watch?v=cgxDVAo336I").

### Setting a fixed SKU or instance type

In the Dimensions section of the offer creation page:

1. Choose "Buyer can choose one or more options offered."
2. Input the different dimensions along with the quantity for each.
3. Choose "Add dimension" to include multiple dimensions or "Create and add new dimension" to create a custom dimension for this private offer.

## How can I help a buyer who receives a 404 Error when accessing a private offer?

Here are common reasons for 404 errors and their resolutions:

### Incorrect account association

1. Ask the buyer to access the [Private Offers](https://us-east-1.console.aws.amazon.com/marketplace/home?region=us-east-1#/private-offers "https://us-east-1.console.aws.amazon.com/marketplace/home?region=us-east-1#/private-offers") tab in their
   [AWS Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. If the offer isn't visible in **Available private offers** or **Accepted and expired offers** tabs:
   - Verify the buyer is signed into the correct account. They can confirm their account ID in the top right corner of the AWS Console.
   - If signed into the correct account, ensure the private offer is for an Amazon Machine Image (AMI) limited listing (see AMI limited listing section below).

**Resolution:** The buyer needs to sign in to the correct account, or you need to issue the private offer to the correct AWS account ID.

### Expired private offer

- If the offer appears in the **Accepted and expired offers** tab, it has expired.

**Resolution:** Extend the expiration date or issue a new private offer.

### AMI limited listing product

- If the offer isn't visible in either tab and the buyer is signed into the correct account, the product may be in limited listing status.

**Resolution:**

- For Single AMI limited listings: Allow-list the buyer's account by following the instructions for
  [allow-listing buyer accounts](ami-single-ami-products.md#single-ami-updating-allowlist "ami-single-ami-products.md#single-ami-updating-allowlist").
- For other server type limited listings: Contact the
  [Private Offer Success Team (POST)](https://aws.amazon.com/marketplace/management/contact-us/? "https://aws.amazon.com/marketplace/management/contact-us/?")
  to allow-list the buyer's account.

###### Note

Allow-listing is a one-time activity per product.

### Private marketplace restrictions

- If the buyer has a private marketplace, they may see an error stating the product is not available in their private catalog.

**Resolution:** The buyer needs to add the product to their allow list.
see [Adding products to a private marketplace](../buyerguide/private-catalog-administration.md#add-products-to-your-private-marketplace "../buyerguide/private-catalog-administration.md#add-products-to-your-private-marketplace").

If the issue persists, ask the buyer to try the following:

- Sign out and back in
- Clear their browser cache
- Delete cookies
- Sign in to an incognito window
- Use a different browser (not Internet Explorer)

## Why do customers see a "You already have an active contract" error when trying to accept a private offer?

This error occurs when a buyer account already has an active subscription to a product. The resolution depends on the product type:

### For Software as a Service (SaaS) contracts

Each buyer account can only have one active subscription to a SaaS contract or contract with consumption product. To update or expand an active subscription:

1. Create an agreement-based offer from the **Agreements** tab in the
   [AWS Marketplace Management Portal (AMMP)](https://aws.amazon.com/marketplace/management/homepage "https://aws.amazon.com/marketplace/management/homepage").
2. Include any pending payment terms from the original offer in the agreement-based offer, as it will override remaining payments not yet invoiced.

#### Creating agreement-based offers

**For Marketplace Private Offer (MPPO):**

1. Navigate to the Agreements tab in [AMMP](https://aws.amazon.com/marketplace/management/homepage "https://aws.amazon.com/marketplace/management/homepage").
2. Search for the buyer's account ID.
3. Select the buyer's current agreement.
4. Choose "Create Agreement Based Offer."

**For Channel Partner Private Offer (CPPO):**

1. The ISV grants a selling authorization to the channel partner with new pricing from their Partners tab, including the number of license units, payment terms to CP, and contract duration.
2. The channel partner navigates to the Agreements tab in [AMMP](https://aws.amazon.com/marketplace/management/homepage "https://aws.amazon.com/marketplace/management/homepage").
3. Search for the buyer's account ID.
4. Select the buyer's current agreement.
5. Choose **Create Agreement Based Offer**.
6. Open the **Selling Authorization** list and select the new opportunity from step 1. This enables the channel partner to input terms for the agreement-based offer.

For more information, see [Creating agreement-based offers](private-offers-upgrades-and-renewals.md "private-offers-upgrades-and-renewals.md").

**Other options for SaaS contracts and contracts with consumption pricing (CCPs):**

- Create a new private offer for the same product ID targeting a different buyer account.
- Issue a new private offer for a different product ID to the same buyer account.
- Request cancellation of the active contract, then issue a new private offer for the same product ID and buyer ID.

### For AMI hourly and annual

Each buyer account can only have one active subscription. To update or expand:

1. Issue a new offer from the **Offers** tab.
2. When the buyer accepts, the new terms override previous contract terms.
3. Pending charges from the previous offer's payment schedule will continue unless cancelled.

### For AMI contracts and professional services

The buyer's current subscription must be cancelled before accepting a new private offer.
Use the [refund/cancellation form](https://aws.amazon.com/marketplace/management/support/refund-request "https://aws.amazon.com/marketplace/management/support/refund-request") to initiate a cancellation request.

## Can a seller or buyer cancel a private offer?

- **If the buyer hasn't subscribed:** The seller can cancel by navigating to the **Offers**
  tab in the AWS Marketplace Management Portal, selecting the offer, and choosing **Cancel**.
- **If the buyer has subscribed:** The seller of record must initiate a cancellation request by using the
  [refund/cancellation form](https://aws.amazon.com/marketplace/management/support/refund-request "https://aws.amazon.com/marketplace/management/support/refund-request") in the AWS Marketplace Management Portal.
  For detailed instructions, refer to this [video tutorial](https://www.youtube.com/watch?v=eQpadPl0ROs "https://www.youtube.com/watch?v=eQpadPl0ROs").

## How do I request a refund or contract cancellation?

Refunds and contract cancellations are handled by the AWS Customer Service team.

Sellers—ISVs for Marketplace private offers, channel partners for channel partner private offers—must use the
[refund/cancellation form](https://aws.amazon.com/marketplace/management/support/refund-request "https://aws.amazon.com/marketplace/management/support/refund-request") to initiate the refund or cancellation.

[This video](https://www.youtube.com/watch?v=eQpadPl0ROs "https://www.youtube.com/watch?v=eQpadPl0ROs") explains the entire process.

Sellers must enter the following data.

- **Buyer account ID**: This information can be found in the offer detail or on Billed Revenue Dashboard. This must be the subscriber account ID.
- **Seller account ID**: This is the seller's AWS account ID used to create the private offer.
- **Product ID**: You can find this information in the offer details or on the
  [Billed revenue dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md") in the **Legacy Product ID** column.
- **Billing date**: You can find this information in the offer details or on the
  [Billed revenue dashboard](billed-revenue-dashboard.md "billed-revenue-dashboard.md") in the **Usage Begin Period** column.
- **Refund amount**: If a refund is not required, the seller can set this to $0.
- **Additional details**: See the following notes.

###### Important

    + For requests that include a contract cancellation, include the following text"


    Please cancel *account X's* subscription to *offer-X*.


    For refunds, specifying the buyer's AWS invoice ID in this section helps but is not mandatory.
    + Save the reference ID provided after submission for future reference in case of follow-ups.

After you submit the request, check the [AWS Support Console](https://support.console.aws.amazon.com/support/home? "https://support.console.aws.amazon.com/support/home?") for status updates.

## When is a buyer invoiced?

- **Upon acceptance:** The invoice is created in the billing console immediately upon subscription.
- **Flexible payment schedule:** The invoice is based on a custom payment schedule negotiated between seller and buyer.
- **AWS consolidated bill (2nd/3rd of the month):** Can include public offer purchases and products with metering.

## What steps should a seller take once an offer is accepted?

1. Track offer acceptance.
2. **For finance teams:** Standard practice is for sellers to handle tracking purchases by creating
   an open payable and suppressing invoice creation to the customer for AWS Marketplace orders.

## How does AWS pay sellers and partners?

- **Disbursements are initiated** only after funds have been successfully collected from subscribers.
- **Disbursements occur on** the default disbursement cadence is monthly between the 7th and 10th of each month.
  Alternatively, ISV and channel partners can select a disbursement schedule—daily or monthly. If an ISV or channel partner selects the monthly option, they can select the day of the
  month they want to receive their disbursements.
- **Disbursements are deposited** to a US bank account on the ISV or channel partner's account minus the listing fees.
  Funds can take 1-3 business days to land with general bank ACH SLAs. If you do not have a US bank account, you can use
  [Hyperwallet](https://sellercentral-europe.amazon.com/help/hub/reference/external/G7S55VWDZ9SQCUEX?ref=efph_G7S55VWDZ9SQCUEX_cont_G521&locale=en-GB "https://sellercentral-europe.amazon.com/help/hub/reference/external/G7S55VWDZ9SQCUEX?ref=efph_G7S55VWDZ9SQCUEX_cont_G521&locale=en-GB")
  to receive disbursements of your Amazon sales into a deposit account and transfer them directly to your local bank in your local currency.

## How does AWS assess tax?

AWS Marketplace charges tax based on:

- The [product subscriber's tax address](https://aws.amazon.com/tax-help/location/ "https://aws.amazon.com/tax-help/location/")
- Product type
- Marketplace Facilitator laws

**Marketplace Facilitator:** Requires the marketplace operator to charge, collect, and remit tax to taxing authorities.

**Non-Marketplace Facilitator:** Responsibility falls on the seller.

For more information about tax obligations, refer to
[AWS Marketplace – Tax Help for Sellers](https://aws.amazon.com/tax-help/marketplace-sellers/ "https://aws.amazon.com/tax-help/marketplace-sellers/").

## Resources and support

If you have a specific request, reach out to one of the following AWS Marketplace teams through the AWS Marketplace Management Portal.

**Private Offers Success Team (POST):** The team supports sellers (ISV and Channel Partners) and buyers with private offer
operational enablement and support. Contact us via the [Support Form](https://aws.amazon.com/marketplace/management/contact-us/? "https://aws.amazon.com/marketplace/management/contact-us/?").

**Vendor Finance Success Team (VFS):** The team improves processes that impact Vendor Finance cash application,
reconciliation and related reporting, and support onboarding sellers (ISV and Channel Partners) with finance specific questions regarding MPPOs and CPPOs not public offers.
Contact us via the [Support Form](https://aws.amazon.com/marketplace/management/contact-us/%22 "https://aws.amazon.com/marketplace/management/contact-us/%22").

**Managed Catalog Operations (MCO):** The team is responsible for onboarding 3rd party sellers of software onto the AWS Marketplace
platform, reviewing and processing their software products for policy compliance and buyer experience, and managing the operational relationship with sellers.
Contact us via the [Support Form](https://aws.amazon.com/marketplace/management/contact-us/%22 "https://aws.amazon.com/marketplace/management/contact-us/%22").

If you are new to the private offer process, use this [video library](https://youtube.com/playlist?list=PLhr1KZpdzukc8sIMVYRmxXt3cpfsXz61q "https://youtube.com/playlist?list=PLhr1KZpdzukc8sIMVYRmxXt3cpfsXz61q")
to help you get started with introductions, overviews, and answers to the most common questions. You can also find the answers to questions about
[buyer invoicing](https://youtu.be/vKzo7FINzss "https://youtu.be/vKzo7FINzss"), [disbursements](https://youtu.be/uevtix9nhsY "https://youtu.be/uevtix9nhsY"),
or [AWS tax rules](https://youtu.be/MyhJZRiYBR0 "https://youtu.be/MyhJZRiYBR0") in the linked videos or in the
[AWS Marketplace Vendor Finance Success](https://d1.awsstatic.com/awsmp/solutions/mk-sol-files/private-offers/Success-guide.pdf "https://d1.awsstatic.com/awsmp/solutions/mk-sol-files/private-offers/Success-guide.pdf") PDF.

## Multi-currency support for private offers

###### Topics

- [Which currencies are supported for private offers?](#which-currencies-supported "#which-currencies-supported")
- [Can I create pay-as-you-go offers in non-USD currencies?](#payg-non-usd-currencies "#payg-non-usd-currencies")
- [How often are foreign exchange rates updated?](#fx-rates-update-frequency "#fx-rates-update-frequency")
- [Can buyers pay in different currencies for different offers?](#buyers-different-currencies "#buyers-different-currencies")
- [How is the listing fee calculated for non-USD offers?](#listing-fee-non-usd "#listing-fee-non-usd")

### Which currencies are supported for private offers?

Private offers support USD, EUR, GBP, AUD, and JPY. All pricing models (contract, contract with consumption, and pay-as-you-go) support these currencies.

### Can I create pay-as-you-go offers in non-USD currencies?

Yes. PAYG private offers support all five currencies. Foreign exchange rates are updated monthly to maintain consistent local currency pricing.

### How often are foreign exchange rates updated?

For consumption and PAYG pricing, FX rates are refreshed monthly before billing runs. Contract pricing uses fixed rates for the entire contract duration.

### Can buyers pay in different currencies for different offers?

Yes. Buyers can accept private offers in different currencies, but they will receive separate invoices for each currency.

### How is the listing fee calculated for non-USD offers?

The listing fee is calculated and deducted in the offer currency. Sellers also receive disbursements in the offer currency. For example, if the offer currency is EUR, the listing fee is deducted in EUR and seller disbursements are made in EUR.
