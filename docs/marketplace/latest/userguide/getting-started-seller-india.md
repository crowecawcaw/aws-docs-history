# Getting started as a seller in India

AWS Marketplace allows sellers in India to sell paid offers to buyers in India (user agreement is with Amazon Web Services India Private Limited (Amazon India) refer [here](../../../accounts/latest/reference/managing-accounts-india.md "../../../accounts/latest/reference/managing-accounts-india.md")). Buyers can procure software and services from sellers in India and receive invoices from AWS India in Indian rupees (INR).

## Key benefits

- Sellers in India can sell paid offers on AWS Marketplace and receive disbursements to bank accounts in India in Indian rupees (INR).
- Buyers are invoiced in Indian rupees (INR) and invoices include Goods and Service Tax (GST), as applicable.
- AWS India facilitates issuance of tax-compliant invoices to AWS customers in INR with you as Seller of Record (SoR), based on information provided in the tax registration tab in AWS Partner Central.

## Important considerations

- If you are a seller based outside India, your sales to buyers in India remain in USD via AWS Inc.
- If you are selling using an account that is part of AWS Organizations, you must use a separate (standalone) account to sell in India to avoid taxation errors.
- Private offers for Container products with contract with consumption pricing and usage-based pricing remain in USD.

## Registration process for sellers in India

Follow these steps to register as a seller in India:

### Step 1: Create a new standalone AWS account

Create a new AWS India account ID. This account should be a standalone account and not a linked account in your AWS Organizations.

###### Important

Using a linked account may lead to incorrect and non-compliant tax invoices.

### Step 2: Complete seller registration on AWS Partner Central

Once you create a new AWS account, use that account to create an AWS Marketplace seller account.

1. Register as a seller on AWS Partner Central.
2. Provide a unique legal business name. This name is used on tax invoices.
3. Create your public profile as described in [Step 1: Register and create your seller profile](create-public-profile.md "create-public-profile.md"). Ensure that the root email provided is monitored, because all tax invoices are sent to your root email address. Your public profile is approved within 1-3 business days, and you receive a confirmation.

### Step 3: Provide tax information

###### Note

Under applicable tax regulations, there is a relaxation from affixing signatures on invoices for B2B transactions that are subject to e-invoicing. While we expect that most sellers will transact primarily with business customers, the classification of a transaction as B2B or B2C depends on whether the customer has provided valid GST details in their AWS India profile. If GST details are provided, the transaction is treated as B2B. If GST details aren't provided, the transaction is treated as B2C. In such cases, a tax invoice must include the seller's signature. Without this, the invoice is treated as non-compliant. To ensure compliance, we require a specimen signature of your authorized signatory. This allows us to print the signature on invoices generated in your name. The specimen signature you provide is used solely for the limited purpose of generating invoices on your behalf. Consistent with the [AWS Privacy Notice](https://aws.amazon.com/privacy/ "https://aws.amazon.com/privacy/"), we apply strict purpose-limitation principles and maintain robust safeguards to protect your personal information. We remain committed to handling your data securely and in accordance with applicable laws.

After you complete your public profile, your account is verified by the AWS Marketplace operations team. You then receive an email from AWS to proceed with tax verification on AWS Partner Central.

You must submit the following information before you can start listing your offers:

1. GST identification number (GSTIN)
2. Permanent Account Number (PAN) - auto-populated from the GSTIN you provided
3. Seller signature that is used on tax invoices for your buyers – In the tax registration form, upload an image of your authorized seller signature under the **Seller signature** section. You can access the tax registration form from the **Tax summary** container on the **Tax details** page.

The following requirements apply to seller signature uploads:

    * File format: .png, .jpg, .jpeg, or .gif only
    * Maximum file size: 3.5 MB
    * Maximum files: 1

After you upload your signature, it goes through a validation process that can take up to 30 minutes. The validation status (accepted or rejected) is displayed in the **Tax summary** container on the **Tax details** page. If your signature is rejected, a reason is provided so you can adjust and re-upload your signature.

You will also receive email notifications if any compliance validation process fails for GSTIN updates or seller signature updates. 4. Legal business name and address that corresponds to your GSTIN for tax purposes 5. Acknowledgements on:

    1. non-applicability of Withholding Tax (WHT) on listing fees;
    2. confirmation that your GSTIN is enabled for e-invoicing;
    3. authorization to AWS India to raise invoices (e-invoices to GST registered buyers) for sales made by you through AWS Marketplace, along with a declaration that you are responsible for remitting the applicable GST to the Government

###### Important

Ensure that e-invoicing is enabled for your GSTIN number before proceeding. Failure to enable this functionality results in tax invoice generation failures. In the event of such a failure, you need to:

1. Enable e-invoicing for your GSTIN.
2. Cancel any existing agreements with failed tax invoice production.
3. Regenerate the offer to successfully produce the tax invoice.
   We recommend verifying your e-invoicing status before initiating any new agreements to avoid processing delays.

### Step 4: Provide bank account information

After your tax information is completed and seller signature is verified, you can provide your bank account information.

Your bank account information must include:

- Account number
- Indian Financial System Code (IFSC) number
- Full name and address associated with the account

### Step 5: Add disbursement method

After you provide banking information, navigate to Payment information menu, find Disbursement methods and choose Add disbursement method.

1. Select the disbursement currency from Currency dropdown and select the appropriate bank account for INR.
2. Sellers in India can only receive disbursements in INR.
3. Choose to receive disbursements either monthly or daily.
4. You can only associate INR currency to one bank account, but you can switch association to a different bank account.
5. All disbursements are sent through applicable clearance and settlement systems (NEFT/RTGS) to your designated bank account.

###### Note

Public offers remain in USD. You do not need to add USD as a disbursement method because you cannot receive disbursements in USD.

### Step 6: Create offers

###### Note

Sellers in India can sell public and private offers to buyers in India only. Even if you target countries other than India or send private offers to buyers outside India, buyers outside India cannot subscribe to those offers.

After you provide banking information and configure disbursement preferences, you can create private offers in USD or INR. Private offers can be created only after you create a product listing. For more information, see [Preparing your product for AWS Marketplace](product-preparation.md "product-preparation.md").

Important considerations:

- AWS Marketplace product listings are always in USD. However, INR option is available when creating private offers.
- Product title should be suffixed with `[IN]`.

#### Creating direct private offers

1. From the Offers menu in AWS Partner Central, choose Create private offer.
2. Select Direct private offer, product type, and your product.
3. At offer creation step 2 (set offer duration and prices), select the currency from the dropdown.
4. Enter all details, review the offer, and choose Create private offer.

#### Creating Channel Partner Private Offers

As an ISV or DSOR partner, you must complete the following preliminary steps before creating a Channel Partner Private Offer:

- Check that the ISV you are extending the offer from is currently onboarded on AWS India AWS Marketplace.
- CP, ISV, and DSOR to create a one-time resale authorization.
- Channel Partner to submit a request for allowlisting through the Channel Partner Submission Program (refer to the following section).

##### Service-Linked Role (SLR) creation

For ISV or Channel Partner accounts participating in the CPPO process, a mandatory one-time configuration is required before initiating any offers.

To create a selling authorization Service-Linked Role:

1. Log into AWS Partner Central using your AWS Marketplace seller account.
2. Navigate to **Marketplace Settings**.
3. Select **Service linked roles**.
4. Choose **Create service-linked role**.
5. The status updates in the portal to show it's created.

###### Note

This SLR is required for ISVs, DSORs, and Channel Partners to create and accept selling authorizations.

##### Channel Partner Submission Program enrollment

To request allowlisting through the Channel Partner Submission Program:

1. Complete the [enrollment request form](https://pages.awscloud.com/awsmp_consulting_partner_offers "https://pages.awscloud.com/awsmp_consulting_partner_offers").
2. In the **Briefly describe support required** field, enter: "I would like to enroll my AWS account ID XXXX-XXXX-XXXX into the Channel Program".
3. Submit the request.

Once your request is submitted, approved, and processed, a response email is sent to the Channel Partner, and ISVs are authorized to enable your AWS account ID to resell their products.

We recommend verifying your e-invoicing status using the India e-Invoicing portal before initiating any new agreements to avoid processing delays.

After you complete the preliminary steps, create the Channel Partner Private Offer in AWS Partner Central. For step-by-step instructions, see [Creating private offers as an AWS Marketplace Channel Partner](channel-partner-offers.md "channel-partner-offers.md") and [Creating a selling authorization for an AWS Marketplace Channel Partner as an ISV](channel-partner-isv-info.md "channel-partner-isv-info.md").

###### Note

Sellers in India and DSORs can only send resale authorizations to channel partners in India. If you issue a resale authorization to a channel partner based outside India, the resale authorization fails. Your channel partner can only create CPPO in the same currency and can extend CPPOs to buyers in India only.
