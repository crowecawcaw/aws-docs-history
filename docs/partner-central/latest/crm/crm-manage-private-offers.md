

# Managing private offers
<a name="crm-manage-private-offers"></a>

The following topics explain how to use Salesforce to create and manage private offers for your AWS Marketplace products. Topics include creating, modifying, and tracking private offers, creating flexible payment schedules, create future-dated agreements, and manage the entire lifecycle of your private offers.

**Topics**
+ [Accessing your private offers](#crm-view-private-offers)
+ [Creating private offers](#crm-create-private-offer)

## Accessing your private offers
<a name="crm-view-private-offers"></a>

To create and manage AWS Marketplace private offers from within Salesforce, you use the **private offers** tab in the **AWS Partner CRM connector**. The following steps explain how to start the tab.

1.  Sign in to the Salesforce organization as an AWS Marketplace user. 

1.  From the App launcher, search for and choose **AWS Partner CRM connector**. 

1.  Choose the **Private Offers** tab. 

## Creating private offers
<a name="crm-create-private-offer"></a>

The following topics explain how to create AWS Marketplace private offers from within Salesforce. Expand each section to learn more.

### Steps for creating private offers
<a name="private-offer-creation-steps"></a>

**Note**  
When creating a private offer, dynamic fields appear based on your chosen product, and on your selections as you move through the creation process.

The following steps explain how to create a private offer. You must complete the [Required fields for private offers](#private-offer-required-fields). Optionally, you can create a flexible payment schedule and a future dated agreement, depending on the type of product selected. Also, you can save the offer as a draft, or publish it to the buyer account.

1.  On the **Private Offers** tab, choose **New**. 

1.  On the **Create an Offer** page, at a minimum, complete the [Required fields for private offers](#private-offer-required-fields) listed in the next section. 

1. Do some or all of the following:
   + **To create a flexible payment schedule**

     1.  In the **Product and Buyers** section, choose **Enable fixed units and allow buyers to pay for this product in installments**. 

     1.  Configure payments in the **Payment Schedule** section. 
   + **To create a future dated agreement**

     1. In the **Service Length** section, choose **New offer starting at future date**.

     1.  Enter **Service start date** and **Service end date** (if required). 

1. Choose **Create Offer** to publish the offer to the buyer.

   —OR—

   Choose **Save as draft** to save the offer as a draft to complete later without releasing it to the buyer.

### Required fields for private offers
<a name="private-offer-required-fields"></a>

To create an AWS Marketplace private offer, you must complete the fields in the following list, including any options. 

**Products and buyers**  
**ISV** – Self  
**Products** – Choose from the list of products synced through the connector.  
**Buyer accounts** – Enter your own seller test account to validate the integration.

**Offer details**  
**Offer name** – Enter a custom name.  
**Offer description** – Enter a custom offer description.

**Service length or contract duration**  
Choose **New offer** then choose a service lent, such as 12 months.

**Offer dimensions**  
Choose the entitlement type that you want to offer.  
Add offer rates to or update existing rates of your chosen dimensions.  
To submit an offer in which any of the dimension rates are set at $0, choose **I want to enable zero dollar pricing**.

**End User License Agreement (EULA)**  
Choose **Standard Contract for AWS Marketplace** or **Custom EULA**.   
If you choose **Custom EULA**, you must configure an Amazon S3 bucket to store the custom EULA when you onboard the AWS seller account. For more information, refer to [Creating your first Amazon S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket) in the *Amazon Simple Storage Service User Guide*.

**Renewals**  
For **Is this offer intended to renew an existing paid subscription with an existing customer for the same underlying product?**, choose ** Yes** or **No**.

**Expiration information**  
Enter the offer expiration date. For subscription-type products, enter the subscription end date.

### Viewing and refreshing offer status
<a name="view-refresh-status"></a>

1.  Open the **Private Offers** tab. 

1.  From the **Private Offers** list, choose the **Private Offer Name**. 

1.  Choose **Refresh Offer Status**. The offer status appears at the bottom of the page. Available values: **PREPARING**, **APPLYING**, **SUCCEEDED**, or **FAILED**. 

**Note**  
The status can take up to two hours to change to **SUCCEEDED**.

### Modifying an offer's expiration date
<a name="modify-private-offer-expiration"></a>

1.  Open the **Private Offers** tab. 

1.  From the **Private Offers** list, choose the **Private Offer Name**. 

1.  Choose **Modify expiry/validity**. 

1.  Choose the new **Offer expiration date.** 

1.  Choose **Modify expiry/validity** to save your selection. 

### Modifying a private offer's expiration date
<a name="cancel-private-offer"></a>

 After you cancel a private offer, no new customers can subscribe to it. Customers with existing subscriptions will stay subscribed until their offer terms expire. 

1.  Open the **Private Offers** tab. 

1.  From the **Private Offers** list, choose the **Private Offer Name**. 

1.  Choose **Cancel Offer**, then choose **Cancel offer** again to confirm the cancellation. 

### Copying a private offer's URL
<a name="copy-offer-url"></a>

1.  Open the **Private Offers** tab. 

1.  From the **Private Offers** list, choose the **Private Offer Name**. 

1.  Locate the **Offer status** section towards the bottom of the page. 

1.  Choose **Copy URL**. 

### Cloning a private offer
<a name="clone-private-offer"></a>

 Cloning a private offer creates a new offer that contains data from the cloned offer. If you enable the connector's **Add seller account to buyer list** setting, the connector automatically inserts the AWS seller account number in the **Buyer Accounts** list. This helps the seller refer to the private offer from the buyer's perspective. 

1.  Open the **Private Offers** tab. 

1.  From the **Private Offers** list, choose the **Private Offer Name**. 

1.  Choose **Clone Offer.** 

1.  Edit the **Offer Details** section of the cloned offer as necessary. 

1.  If necessary, re-upload the EULA. 

1.  Choose **Create offer**. 

### Using the FPS utility to populate payment schedules
<a name="use-fps"></a>

 When creating an AWS Marketplace private offer, use the FPS utility to populate payment schedules with fixed costs and equal payment gaps. 

**To use FPS**

1.  On the **Payment Schedule** tab, choose **Yes** to generate a payment schedule with fixed cost and equal payment gaps. 

1.  Choose a **Payment Frequency** of 15, 30, 90. or 365 days. 

1.  Choose **Remainder Options**. To place the remainder of the uneven payment on the first payment, choose **Frontload**. To place the remainder on the last payment, choose **Backend**. 

1.  For **Calendar Options**, to configure the payment frequency to include weekend days, choose **Calendar Day**. To not include weekend days, choose **Business Day**. 

1.  Enter the payment amount (sum of all payments), payment start date (first payment), and approximate payment end date. 

1.  Choose **Generate Schedule**. 

1.  Review and edit the payment amounts and invoice dates as needed. 