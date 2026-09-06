

# Getting started as a seller in India
<a name="getting-started-seller-india"></a>

AWS Marketplace allows sellers in India to sell paid offers to buyers in India (user agreement is with Amazon Web Services India Private Limited (Amazon India) refer [here](https://docs.aws.amazon.com/accounts/latest/reference/managing-accounts-india.html)). Buyers can procure software and services from sellers in India and receive invoices from AWS India in Indian rupees (INR).

## Key benefits
<a name="india-seller-key-benefits"></a>
+ Sellers in India can sell paid offers on AWS Marketplace and receive disbursements to bank accounts in India in Indian rupees (INR).
+ Buyers are invoiced in Indian rupees (INR) and invoices include Goods and Service Tax (GST), as applicable.
+ AWS India facilitates issuance of tax-compliant invoices to AWS customers in INR with you as Seller of Record (SoR), based on information provided in the tax registration tab in AWS Partner Central.

## Important considerations
<a name="india-seller-considerations"></a>
+ If you are a seller based outside India, your sales to buyers in India remain in USD via AWS Inc.
+ If you are selling using an account that is part of AWS Organizations, you must use a separate (standalone) account to sell in India to avoid taxation errors.
+ Private offers for Container products with contract with consumption pricing and usage-based pricing remain in USD.

## Registration process for sellers in India
<a name="india-seller-registration-process"></a>

Follow these steps to register as a seller in India:

### Step 1: Create a new standalone AWS account
<a name="india-seller-step-1"></a>

Create a new AWS India account ID. This account should be a standalone account and not a linked account in your AWS Organizations.

**Important**  
Using a linked account may lead to incorrect and non-compliant tax invoices.

### Step 2: Complete seller registration on AWS Partner Central
<a name="india-seller-step-2"></a>

Once you create a new AWS account, use that account to create an AWS Marketplace seller account.

1. Register as a seller on AWS Partner Central.

1. Provide a unique legal business name. This name is used on tax invoices.

1. Create your public profile as described in [Step 1: Register and create your seller profile](create-public-profile.md). Ensure that the root email provided is monitored, because all tax invoices are sent to your root email address. Your public profile is approved within 1-3 business days, and you receive a confirmation.

### Step 3: Provide tax information
<a name="india-seller-step-3"></a>

**Note**  
Under applicable tax regulations, there is a relaxation from affixing signatures on invoices for B2B transactions that are subject to e-invoicing. While we expect that most sellers will transact primarily with business customers, the classification of a transaction as B2B or B2C depends on whether the customer has provided valid GST details in their AWS India profile. If GST details are provided, the transaction is treated as B2B. If GST details aren't provided, the transaction is treated as B2C. In such cases, a tax invoice must include the seller's signature. Without this, the invoice is treated as non-compliant. To ensure compliance, we require a specimen signature of your authorized signatory. This allows us to print the signature on invoices generated in your name. The specimen signature you provide is used solely for the limited purpose of generating invoices on your behalf. Consistent with the [AWS Privacy Notice](https://aws.amazon.com/privacy/), we apply strict purpose-limitation principles and maintain robust safeguards to protect your personal information. We remain committed to handling your data securely and in accordance with applicable laws.

After you complete your public profile, your account is verified by the AWS Marketplace operations team. You then receive an email from AWS to proceed with tax verification on AWS Partner Central.

You must submit the following information before you can start listing your offers:

1. GST identification number (GSTIN)

1. Permanent Account Number (PAN) - auto-populated from the GSTIN you provided

1. Seller signature that is used on tax invoices for your buyers – In the tax registration form, upload an image of your authorized seller signature under the **Seller signature** section. You can access the tax registration form from the **Tax summary** container on the **Tax details** page.

   The following requirements apply to seller signature uploads:
   + File format: .png, .jpg, .jpeg, or .gif only
   + Maximum file size: 3.5 MB
   + Maximum files: 1

   After you upload your signature, it goes through a validation process that can take up to 30 minutes. The validation status (accepted or rejected) is displayed in the **Tax summary** container on the **Tax details** page. If your signature is rejected, a reason is provided so you can adjust and re-upload your signature.

   You will also receive email notifications if any compliance validation process fails for GSTIN updates or seller signature updates.

1. Legal business name and address that corresponds to your GSTIN for tax purposes

1. Acknowledgements on:

   1. non-applicability of Withholding Tax (WHT) on listing fees;

   1. confirmation that your GSTIN is enabled for e-invoicing;

   1. authorization to AWS India to raise invoices (e-invoices to GST registered buyers) for sales made by you through AWS Marketplace, along with a declaration that you are responsible for remitting the applicable GST to the Government

**Important**  
Ensure that e-invoicing is enabled for your GSTIN number before proceeding. Failure to enable this functionality results in tax invoice generation failures. In the event of such a failure, you need to:  
Enable e-invoicing for your GSTIN.
Cancel any existing agreements with failed tax invoice production.
Regenerate the offer to successfully produce the tax invoice.
We recommend verifying your e-invoicing status before initiating any new agreements to avoid processing delays.

### Step 4: Provide bank account information
<a name="india-seller-step-4"></a>

After your tax information is completed and seller signature is verified, you can provide your bank account information.

Your bank account information must include:
+ Account number
+ Indian Financial System Code (IFSC) number
+ Full name and address associated with the account

### Step 5: Add disbursement method
<a name="india-seller-step-5"></a>

After you provide banking information, navigate to Payment information menu, find Disbursement methods and choose Add disbursement method.

1. Select the disbursement currency from Currency dropdown and select the appropriate bank account for INR.

1. Sellers in India can only receive disbursements in INR.

1. Choose to receive disbursements either monthly or daily.

1. You can only associate INR currency to one bank account, but you can switch association to a different bank account.

1. All disbursements are sent through applicable clearance and settlement systems (NEFT/RTGS) to your designated bank account.

**Note**  
Public offers remain in USD. You do not need to add USD as a disbursement method because you cannot receive disbursements in USD.

### Step 6: Create offers
<a name="india-seller-step-6"></a>

**Note**  
Sellers in India can sell public and private offers to buyers in India only. Even if you target countries other than India or send private offers to buyers outside India, buyers outside India cannot subscribe to those offers.

After you provide banking information and configure disbursement preferences, you can create private offers in USD or INR. Private offers can be created only after you create a product listing. For more information, see [Preparing your product for AWS Marketplace](product-preparation.md).

Important considerations:
+ AWS Marketplace product listings are always in USD. However, INR option is available when creating private offers.
+ Product title should be suffixed with `[IN]`.

#### Creating direct private offers
<a name="india-seller-direct-private-offers"></a>

1. From the Offers menu in AWS Partner Central, choose Create private offer.

1. Select Direct private offer, product type, and your product.

1. At offer creation step 2 (set offer duration and prices), select the currency from the dropdown.

1. Enter all details, review the offer, and choose Create private offer.

#### Creating Channel Partner Private Offers
<a name="india-seller-channel-partner-offers"></a>

As an ISV or DSOR partner, you must complete the following preliminary steps before creating a Channel Partner Private Offer:
+ Check that the ISV you are extending the offer from is currently onboarded on AWS India AWS Marketplace.
+ CP, ISV, and DSOR to create a one-time resale authorization.
+ Channel Partner to submit a request for allowlisting through the Channel Partner Submission Program (refer to the following section).

##### Service-Linked Role (SLR) creation
<a name="india-seller-cppo-slr-creation"></a>

For ISV or Channel Partner accounts participating in the CPPO process, a mandatory one-time configuration is required before initiating any offers.

To create a selling authorization Service-Linked Role:

1. Log into AWS Partner Central using your AWS Marketplace seller account.

1. Navigate to **Marketplace Settings**.

1. Select **Service linked roles**.

1. Choose **Create service-linked role**.

1. The status updates in the portal to show it's created.

**Note**  
This SLR is required for ISVs, DSORs, and Channel Partners to create and accept selling authorizations.

##### Channel Partner Submission Program enrollment
<a name="india-seller-cppo-submission-program"></a>

To request allowlisting through the Channel Partner Submission Program:

1. Complete the [enrollment request form](https://pages.awscloud.com/awsmp_consulting_partner_offers).

1. In the **Briefly describe support required** field, enter: "I would like to enroll my AWS account ID XXXX-XXXX-XXXX into the Channel Program".

1. Submit the request.

Once your request is submitted, approved, and processed, a response email is sent to the Channel Partner, and ISVs are authorized to enable your AWS account ID to resell their products.

We recommend verifying your e-invoicing status using the India e-Invoicing portal before initiating any new agreements to avoid processing delays.

After you complete the preliminary steps, create the Channel Partner Private Offer in AWS Partner Central. For step-by-step instructions, see [Creating private offers as an AWS Marketplace Channel Partner](channel-partner-offers.md) and [Creating a selling authorization for an AWS Marketplace Channel Partner as an ISV](channel-partner-isv-info.md).

**Note**  
Sellers in India and DSORs can only send resale authorizations to channel partners in India. If you issue a resale authorization to a channel partner based outside India, the resale authorization fails. Your channel partner can only create CPPO in the same currency and can extend CPPOs to buyers in India only.