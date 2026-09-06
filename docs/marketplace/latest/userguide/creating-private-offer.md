

# Creating and managing private offers
<a name="creating-private-offer"></a>

As an AWS Marketplace seller, you can create and manage private offers. Private offers are negotiated terms used to purchase a product from AWS Marketplace. This can involve a custom pricing plan, end user license agreement (EULA), or custom solutions. The following sections describe how to create and manage private offers.

**Note**  
To be eligible to issue private offers, you must have at least one active public listing. If you have a public listing, and you don't have access to the Private Offers tab, see [IAM Permissions](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html) or [contact AWS Marketplace support](https://aws.amazon.com/marketplace/management/contact-us).

**Topics**
+ [Starting a new private offer](#starting-new-private-offer)
+ [Understanding offer statuses](#understanding-offer-statuses)
+ [Drafting and publishing the private offer](#drafting-and-publishing-private-offer)
+ [Adding private offer and demo request buttons](#private-offer-requests-demos)
+ [Sending a private offer to a buyer](#send-private-offer)
+ [Cloning your private offer](#cloning-your-private-offer)
+ [Downloading offer details](#download-offer-details)
+ [Saving your private offer progress](#saving-private-offer)
+ [Updating the expiration of a private offer](#updating-private-offer-expiration)
+ [Cancelling a private offer](#cancelling-private-offer)

## Starting a new private offer
<a name="starting-new-private-offer"></a>

The following steps explain how to use [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home) to create a private offer and generate an offer ID. The process creates a blank offer in a draft state.

**To start a private offer**

1. Sign into [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home).

1. Choose **Private offers**.

1. On the **Private offers** page, choose **Create private offer**.

1. On the **Create private offer** page, choose the offer type, product type, and the product that you want to create your private offer from. Processing takes up to 30 seconds. Don't close or refresh the page until processing finishes.
**Note**  
You can't change the product type and product after you create the offer. For more information on private offers per product type, see [Supported product types](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-supported-product-types.html).
AWS Marketplace channel partners must choose between creating an offer for their own products, or creating a channel partner private offer (CPPO) from a resale authorization. When creating a CPPO, choose the independent software vendor (ISV), product, and authorization. For more information about resale authorizations, see [Creating a selling authorization for an AWS Marketplace Channel Partner as an ISV](channel-partner-isv-info.md) later in this guide.

1. Choose **Continue to offer details**. 

   A step-by-step experience guides you through the rest of the creation process.

**Geo-targeting private offers:**  
You now have the option to select the countries in which buyers can view and accept private offers.
+ If you extend the offer to a buyer outside of the selected countries, the buyer cannot accept the offer.
+ You can select **All Countries** to make your offer available to buyers globally.
+ India-based sellers can only sell to buyers located in India. This feature defaults to India for such sellers and cannot be changed.
+ If the buyer is a linked account that is part of an AWS organization, then geo-targeting rules will apply based on the buyer's location and not the payer account's location.

## Understanding offer statuses
<a name="understanding-offer-statuses"></a>

Offers have one of three statuses depending on the lifecycle:
+ **Draft** – The offer is incomplete and still being prepared by you. Private offers in a draft status are not subject to a retention schedule. All required details must be completed and submitted to publish the offer and extend it to your buyer.
+ **Active** – The offer is published and extended to the buyer. The offer hasn't expired, so buyers can subscribe to the offer.
+ **Expired** – The offer is published and extended to the buyer. The offer has expired, so buyers can't subscribe to the offer. The expiration date can be updated to give your buyers more time to accept the offer. To update offer expiration, refer to [Updating the expiration of a private offer](https://docs.aws.amazon.com/marketplace/latest/userguide/creating-private-offer.html#updating-private-offer-expiration). 

**Note**  
After the offer is accepted, it will show up as an agreement in the **Agreements** tab. The status of the offer won't change.

## Drafting and publishing the private offer
<a name="drafting-and-publishing-private-offer"></a>

Use the following process to draft and publish your private offer.

**To draft and publish your private offer**

1. On the **Provide offer information** page, provide the offer name, offer details, offer purpose, and offer expiration date. If this is a renewal offer, you must choose either **Existing Customer on AWS Marketplace** for renewals intended to renew an existing agreement created in AWS Marketplace, or **Existing Customer Moving to AWS Marketplace** for renewals intended to migrate your existing customer to AWS Marketplace.
**Note**  
The offer expiration date is the date that the offer becomes null and void. After 23:59:59 UTC on this date, the buyer won't be able to view and accept this private offer.
**Note**  
A renewal is defined as:  
Any private offer to a customer with an existing or prior private offer for the product, including expansions and upsells.
Any private offer to a customer with an existing paid software subscription between seller and customer that did not originate but was renewed through AWS Marketplace.
A private offer that moves the customer from a public AWS Marketplace subscription to a private offer is not considered a renewal.

1. Choose **Next**.

1. On the **Configure offer pricing and duration** page, choose the pricing model, contract or usage duration, pricing, currency, and payment schedule. For pricing models that have an installment plan, see [Private offer installment plans](installment-plans.md).
**Note**  
Private offers can be created in non-USD currencies for all pricing types. Make sure you have configured your non-USD disbursement preferences. For more information, see [Step 4: Set disbursement preferences](set-disbursement-preferences.md).  
All public offers and private offers with consumption pricing can only be created in USD.

1. On the **Add buyers** page, provide an AWS account ID for each AWS Marketplace buyer you are extending the private offer to. Each selected buyer must have an AWS account in a AWS Region where the selected offer currency is supported. To add another AWS account ID, choose **Add another buyer**. You can add up to 24 buyers to each private offer. 

1. Choose **Next**.

1. On the **Configure legal terms and offer documents** page, choose one of the following options:
   + Public offer end user license agreement (EULA) – Use the EULA from your public offer.
   + Standard contract for AWS Marketplace (SCMP) – Use the standard contract provided by AWS Marketplace.
   + Custom legal terms – Upload up to five files related to your private offer, including legal terms, a statement of work, a bill of materials, a pricing sheet, or other addendums. These files will be merged into one document when the offer is created.

1. Configure auto-renewal. Renewal terms define how this agreement renews when it reaches its end date.
   + **Renewal pricing** – how the price changes between cycles:
     + **No price uplift** – the agreement renews at the same price each cycle.
     + **Price uplift** – the price increases each cycle. Choose the type: **Fixed percentage** (one percentage applied evenly across all dimensions every cycle; it compounds, so a 10% uplift takes $100 to $110 to $121) or **Percentage range** (a minimum and maximum you finalize before each renewal's adjustment deadline; you can apply one flat percentage or set a different uplift per dimension, as long as each stays within the range).
     + **No renewal** – the offer carries no auto-renewal terms and the agreement ends at expiration.
   + **Renewal maximum** – how many times the agreement can auto-renew, or unlimited.
   + **Renewal decision deadline** – the last day a buyer or seller can change their auto-renewal decision before the next cycle is guaranteed.
   + **Adjustment deadline** (percentage range only) – the date by which you must finalize the uplift for the next cycle, for percentage range renewal pricing models. In order to provide buyers with adequate time to review the final renewal terms, we recommend allowing a reasonable period between the adjustment deadline and the renewal decision deadline, no shorter than the minimum notice period mandated by applicable local laws (for example, 14 days where no stricter requirement applies).
   + **Default uplift** (percentage range only) – the percentage applied automatically if you do not finalize a value by the adjustment deadline.

**Price uplift with percentage range:**  
Choose a price uplift range when you want to:
   + Adjust the uplift at each renewal – for example, to reflect a factor such as the consumer price index (CPI).
   + Set a different uplift value for each dimension.

   If you choose a price uplift range:
   + You must finalize the exact uplift percentage for each renewal cycle before the adjustment deadline.
   + You can set it from the **Auto-generated private offers** tab on the **Offers** page, or from the **Renewal details** tab of the agreement that is set to auto-renew.
   + If you do not finalize a value by the adjustment deadline, the default uplift applies.

   For more information, see [Auto-generated private offers](auto-generated-private-offers.md) and [Managing agreement renewals](managing-agreement-renewals.md).

**Renewal installment plan:**  
By default, renewals use the same payment frequency you set for the first contract cycle. You can change the renewal frequency if you want renewals billed on a different cadence.

   Because the renewal start date is not known in advance, you choose how each installment's due date is calculated relative to that start:
   + **By month** – the due date lands on a set month of the agreement, such as "month 3 of the agreement."
   + **By exact days** – a set number of days after the agreement starts, such as "90 days after the agreement starts."

   The preview shows pricing for the next renewal cycle only; each installment is shown as a percentage of the total contract value (TCV) for that cycle. If you configured a price uplift, the renewal total is higher, so each installment is larger even though the percentages stay the same.

   Buyers review all of these terms before they accept.

1. On the **Review and create** page, review the details of your private offer. After you review and confirm, choose **Create offer** to publish the offer and extend it to the buyers you chose. Offer publishing includes a request to the AWS Marketplace Catalog API, so it can take up to an hour to validate and process the offer. This request can be viewed on the **Requests** page.
**Note**  
The offer will be published and extended only if the request succeeds. If the request fails, it won’t be extended to the customer. A failure means that there was either a system error or an error you must correct before resubmitting.

## Adding private offer and demo request buttons
<a name="private-offer-requests-demos"></a>

Sellers can add call-to-action buttons to their product detail pages. The buttons enable buyers to request private offers and guided product demos. You can add one or both buttons to your product detail pages.

You can use the buttons with the following product types:
+ Amazon Machine Image
+ Software as a service (SaaS)
+ Container
+ CloudFormation templates

To use the buttons, you must belong to the APN Customer Engagements Program (ACE). When buyers request an offer or a demo, they enter their contact data and request details into a form. The AWS Demand generation team then qualifies the requests and transfers those qualified requests to you as AWS originated opportunities through ACE in Partner Central. You then follow up with customers to discuss offer details or schedule a guided demo. For more information about ACE, see the [APN Customer Engagements Program](https://aws.amazon.com/partners/programs/ace/) website and [Leads and Opportunities](https://partnercentral.awspartner.com/partnercentral2/s/article?category=ACE_Get_Started&article=ACE-Getting-Started-Frequently-Asked-Questions-FAQ#AWS-Originated-Referrals---Lead-and-Opportunity) in the *APN Customer Engagement (ACE) FAQs*.

Steps in the following topics explain how to add the buttons to your product detail pages.

**Topics**
+ [Button prerequisites](#button-prerequisites)
+ [Enabling the buttons](#enabling-the-buttons)

### Button prerequisites
<a name="button-prerequisites"></a>

Before you can add the call-to-action buttons to your product detail pages, you must have the following prerequisites:
+ Make sure you can receive AWS referred leads and opportunities in AWS Partner Central. For more information, see the [APN Customer Engagements Program](https://aws.amazon.com/partners/programs/ace/) website.
**Note**  
After you enroll in the ACE program, status updates occur every two weeks. The private offer and demo request buttons appear only after the status update is complete. If you choose these options and receive a message, your access is pending the next biweekly update.
+ Link your AWS Partner Central and AWS Marketplace accounts. To do that, you must:
  + Create the `CreatePartnerCentralCloudAdminRole` IAM: policy. For more information, see the [prerequisites for account linking](https://docs.aws.amazon.com/partner-central/latest/getting-started/account-linking.html#linking-prerequisites) in the *AWS Partner Central Getting Started Guide*. 
  + Link your AWS Partner Central and AWS Marketplace accounts. For more information, see [Link your AWS Partner Central account to your AWS Marketplace account](https://docs.aws.amazon.com/partner-central/latest/getting-started/account-linking.html#linking-apc-aws-marketplace), in the *AWS Partner Central Getting Started Guide*.

    After you link your AWS Partner Central and AWS Marketplace accounts, your Partner Central **Home** page displays the following status message:  
![The Partner Central learn page showing a status of "account linked."](http://docs.aws.amazon.com/marketplace/latest/userguide/images/linked-accounts.png)

For more information, sign in to Partner Central and see the following:
+ The [AWS Partner Central & Marketplace account linking guide](https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central&category=Introductory_resources#Introduction)
+ The [AWS Partner and Marketplace Account Linking Demo](https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central-and-Marketplace-Account-Linking-Demo&category=Introductory_resources) video

**Note**  
You must sign in to use these resources.

### Enabling the buttons
<a name="enabling-the-buttons"></a>

Once you become ACE eligible to receive AWS referrals, you use AWS Partner Central to enable one or both call-to-action buttons.

You follow separate processes to enable the buttons, depending on whether you create a new product listing or update a current listing.

**To enable buttons for new products**

1. Use [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home) to create the following types of products and make them public:
   + AMI
   + SaaS
   + Container
   + Cloud Front template

1. As part of creating the product, under **Guided demo and private offer requests**, choose any combination of **Enable guided demo requests for buyers** and **Enable private offer requests for buyers**.

**Note**  
The buttons only appear on the product detail pages in your private offers after you make the product public.

**To enable buttons for existing products**

1. In [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home), on the **Build** tab, select the product that you want to change.

1. Open the **Request changes** list and choose **Update product information**.

1. Choose any combination of **Enable guided demo requests for buyers** and **Enable private offer requests for buyers**.

The buttons only appear on the product detail page after you save your changes.

After you enable the buttons, you can remove public pricing from your listing so that buyers contact you through the **Request for private offer** button instead of purchasing through a public offer. For more information, see [Update pricing visibility](update-pricing-visibility.md).

## Sending a private offer to a buyer
<a name="send-private-offer"></a>

After the private offer has been published, buyers can view it by navigating to the **Available private offers** tab on the **Private offers** page in AWS Partner Central. On the **Available private offers** tab, the buyer can see offers extended by AWS Marketplace Channel Partners in the **Seller of record** column. The independent software vendor (ISV) will display in the **Publisher** column. A buyer can navigate to a private offer by choosing the appropriate **Offer ID** in their offers list.

Buyers can view offer IDs that have been accepted or that have expired on the **Accepted or expired offers** tab.

After the private offer has been published, you can send your buyer a URL to the fulfillment page for the offer.

**To send a private offer to your buyer**

1. Sign into [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home), and choose **Private offers**.

1. Select the **radio button** next to the offer.

1. Choose **Actions** and then **Copy Offer URL**.

1. Send the URL to your buyer.

## Cloning your private offer
<a name="cloning-your-private-offer"></a>

You can clone a private offer, including AWS Marketplace Channel Partner private offers. Use cloning to create a new offer using a template or to update and replace an existing offer.

**To clone a private offer**

1. Sign into [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home), and choose **Private offers**.

1. In the **Private offers** table, select the option next to the offer you want to clone.

1. Choose **Clone offer**.

1. A new offer-creation experience will open with pre-populated information from the selected offer. Review and modify the offer details as needed.

1. (Optional) If you're cloning to replace an existing offer, select **Cancel the existing offer**. When selected, the original offer will automatically expire and not be accessible to the buyer when this new offer is published. This only affects the offer's accessibility and does not impact any existing subscriptions if the buyer has already accepted the original offer.

1. Choose **Clone private offer**. This will publish the offer and extend it to the buyers you selected previously.

## Downloading offer details
<a name="download-offer-details"></a>

Use the following procedure to download offer details in a .pdf file.

**To download offer details**

1. Sign into [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home), and choose **Private offers**.

1. In the **Private offers** table, select the option next to the offer and choose **View details**. Alternatively, you can choose the link for the offer in the **Offer ID** column.

1. On the offer detail page, choose **Download PDF**.

## Saving your private offer progress
<a name="saving-private-offer"></a>

 Use the following process to save your progress and resume later.

**To save and resume your work**

1. At any completed step, choose **Save and exit**. In the dialog box, confirm that you're saving the content in a draft state and review any validation errors. If there are any validation errors or missing details, you can choose **Fix it** to go to the step and resolve the issue. When you're ready, choose **Save and exit** to save your changes.

   After you save and exit, the request is under review while it's processing. It could take a few minutes or hours to finish processing. You can't continue the steps or modify the request until it has succeeded. After the request has succeeded, you have completed the save. If the request fails, there was either a system error or an error you must correct before resubmitting.

1. To resume working on your offer, open the **Private offers** page, choose your offer, and then choose **Resume offer creation**.

1. When you're finished, you can choose either **Save and exit** to save your progress or **Create offer** to publish and extend the private offer to your selected buyers.

## Updating the expiration of a private offer
<a name="updating-private-offer-expiration"></a>

Use the following process to update the expiration date of a private offer.

**To update the expiration date of a private offer**

1. Sign into [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home), and choose **Private offers**.

1. On the **Private offers** page, choose the **offer** you want to update.

1. Choose **Edit**.

1. Provide a new **offer expiration date**.

1. Choose **Submit**.

   After the update is complete, the offer will change to an **Active** status and your buyer can accept the offer.

## Cancelling a private offer
<a name="cancelling-private-offer"></a>

Use the following process to cancel the private offer.

1. Sign into [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral/home), and choose **Private offers**.

1. On the **Private offers** page, choose the **offer** you want to update.
**Note**  
Cancelling the offer will modify the offer expiration date, so the offer will display as expired for buyers who were extended this offer.

1. Choose **Action** and then choose **Cancel offer**.