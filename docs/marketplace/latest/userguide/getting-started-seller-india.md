# Getting started as a seller in India

AWS Marketplace allows sellers in India to sell paid offers to buyers in India. Buyers can procure software and services from sellers in India and receive invoices from AWS India in Indian rupees (INR).

## Key benefits

- Sellers in India can sell paid offers on AWS Marketplace and receive disbursements to bank accounts in India in Indian rupees (INR).
- Buyers are invoiced in Indian rupees (INR) and invoices include Goods and Service Tax (GST), as applicable.
- AWS India facilitates issuance of tax-compliant invoices to AWS customers in INR with you as Seller of Record (SoR), based on information provided in the tax registration tab in AWS Marketplace Management Portal.

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

### Step 2: Complete seller registration on AWS Marketplace Management Portal

Once you create a new AWS account, use that account to create an AWS Marketplace seller account.

1. Register as a seller on AWS Marketplace Management Portal.
2. Provide a unique legal business name. This name is used on tax invoices.
3. Create your public profile as described in [Step 1: Register and create your seller profile](create-public-profile.md "create-public-profile.md").

### Step 3: Provide tax information

###### Note

Under applicable tax regulations, there is a relaxation from affixing signatures on invoices for B2B transactions that are subject to e-invoicing. While we expect that most sellers will transact primarily with business customers, the classification of a transaction as B2B or B2C depends on whether the customer has provided valid GST details in their AWS India profile. If GST details are provided, the transaction is treated as B2B. If GST details aren't provided, the transaction is treated as B2C. In such cases, a tax invoice must include the seller's signature. Without this, the invoice is treated as non-compliant. To ensure compliance, we require a specimen signature of your authorized signatory. This allows us to print the signature on invoices generated in your name. The specimen signature you provide is used solely for the limited purpose of generating invoices on your behalf. Consistent with the [AWS Privacy Notice](https://aws.amazon.com/privacy/ "https://aws.amazon.com/privacy/"), we apply strict purpose-limitation principles and maintain robust safeguards to protect your personal information. We remain committed to handling your data securely and in accordance with applicable laws.

After you complete your public profile, your account is verified by the AWS Marketplace operations team. You then receive an email from AWS to proceed with tax verification on AWS Marketplace Management Portal.

You must submit the following information before you can start listing your offers:

1. GST identification number (GSTIN)
2. Permanent Account Number (PAN) - auto-populated from the GSTIN you provided
3. Seller signature that is used on tax invoices for your buyers - submit a ticket using the contact us form to submit signature
4. Legal business name and address that corresponds to your GSTIN for tax purposes
5. Acknowledgements on: (a) non-applicability of Withholding Tax (WHT) on listing fees; (b) confirmation that your GSTIN is enabled for e-invoicing; (c) authorization to AWS India to raise invoices (e-invoices to GST registered buyers) for sales made by you through AWS Marketplace, along with a declaration that you are responsible for remitting the applicable GST to the Government

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

1. From the Offers menu in AWS Marketplace Management Portal, choose Create private offer.
2. Select Direct private offer, product type, and your product.
3. At offer creation step 2 (set offer duration and prices), select the currency from the dropdown.
4. Enter all details, review the offer, and choose Create private offer.

#### Creating Channel Partner Private Offers

As an ISV or DSOR partner, you must first create a resale authorization.

**For ISVs or CP accounts that will be participating in the CPPO process:** Before you initiate an offer, complete a mandatory one-time step of creating a selling authorization Service-Linked Role (SLR). To do this, log into AWS Marketplace Management Portal with your AWS Marketplace seller account. Navigate to the **Settings** tab, then choose **Service linked roles**, then choose **Create service-linked role**. The SLR is required for ISVs, DSORs and CPs to create and accept selling authorizations.

1. From the Partners menu in AWS Marketplace Management Portal, choose Create opportunity.
2. Under Discounts and Products, select the discount type and your product for resale.
3. Select currency from the dropdown.
4. Enter all details, review the authorization, and choose Create opportunity.

###### Note

Sellers in India and DSORs can only send resale authorizations to channel partners in India. If you issue a resale authorization to a channel partner based outside India, the resale authorization fails. Your channel partner can only create CPPO in the same currency and can extend CPPOs to buyers in India only.
