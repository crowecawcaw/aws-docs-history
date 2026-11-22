

# Listing and Selling in AWS Marketplace for AWS European Sovereign Cloud

 AWS Marketplace in the AWS European Sovereign Cloud (ESC) enables you to offer your products to customers who require enhanced data sovereignty, residency, and operational control within the European Union. ESC is designed to help EU-based organizations meet strict regulatory requirements while using cloud computing services. For full comparison between AWS Marketplace in Commercial region and AWS Marketplace in ESC refer to [this documentation](https://docs.aws.eu/esc/latest/userguide/marketplace.html). 

 **AWS in European Sovereign Cloud account** 

 Before you begin, you must create a new dedicated account in the [ESC partition](https://eusc-de-east-1.signin.amazonaws-eusc.eu/) (`aws-eusc`). 

## Prerequisites for ESC catalog access
<a name="prerequisites-esc"></a>

 To register for and sell via AWS Marketplace, sellers have to meet prerequisites which are outlined and covered in following sections of this guide: [Selling on AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/using-aws-marketplace-as-a-provider.html) and [Registering as a seller on AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/seller-account-registering.html). The ESC catalog is exclusively available to sellers who already hold an active commercial registration. ESC catalog cannot be used as your primary or first catalog. ESC sellers must also meet these additional requirements: 

1. **Completed Paid Seller Registration**: If you have not registered as Seller in AWS Marketplace or want to set up a new seller account, see how to [Register your seller account](https://docs.aws.amazon.com/marketplace/latest/userguide/seller-account-registering.html).

1. **Activate Local currency Disbursement Preference for EURO**: AWS Marketplace in the AWS ESC public catalog is listed in EUR. You must [provide one or more bank accounts](https://docs.aws.amazon.com/marketplace/latest/userguide/provide-bank-information.html#provide-bank-information-steps) capable of receiving EUR and USD disbursements before you register for the ESC catalog. Add [SWIFT](https://docs.aws.amazon.com/marketplace/latest/userguide/provide-bank-information.html#provide-bank-information-steps) banking details that allows euro (EUR). SWIFT bank accounts are required for non-USD disbursements and optional for USD. US-based ACH accounts can only receive payments in USD. To configure your disbursement preferences, follow the steps in [Set Disbursement Preferences](https://docs.aws.amazon.com/marketplace/latest/userguide/set-disbursement-preferences.html) in this guide.

1. **Successful completion of KYC verification**: AWS Marketplace in the AWS ESC requires all sellers to complete Know Your Customer (KYC) validation as a mandatory compliance requirement. For detailed KYC instructions, see [Complete the KYC process](https://docs.aws.amazon.com/marketplace/latest/userguide/complete-kyc-process.html) in the [Registering as a seller](https://docs.aws.amazon.com/marketplace/latest/userguide/seller-account-registering.html) section of this guide.

1. **Deployment on AWS for SaaS products**: AWS Marketplace in the AWS ESC requires that all products run exclusively on AWS infrastructure to meet European sovereignty and compliance requirements. All product resources must be deployable in the ESC region (THF region). Customer data must remain within ESC boundaries at all times, including backups and disaster recovery. You must not replicate or transfer data outside ESC regions, and all logging and monitoring must use ESC-compliant services (see the [ESC-compliant services reference](https://builder.aws.com/build/capabilities/explore?f=eJyrVipOzUlNLklNCUpNz8zPK1ayUoqOUUotLU7WTUnVTU0sLtE1jFGKVdKBK3QsS8zMSUzKzMksqQSqdsyrVEARqgUA4l8dog&tab=service-feature)). Products cannot rely on external infrastructure or hosting services, or on external APIs that process or store customer data outside ESC boundaries.

   **What are acceptable third-party components?**

   You may include third-party components in your product if they run entirely within your AWS infrastructure, do not transmit customer data outside ESC boundaries, are packaged within your product deployment, and comply with ESC data sovereignty requirements. Acceptable examples include:

   1. Open-source libraries and frameworks deployed on AWS

   1. Third-party software installed on your Amazon EC2 instances

   1. Database engines running on Amazon RDS or Amazon EC2

1. **Access to AWS ESC Account**: Create a new dedicated account in the [ESC partition](https://eusc-de-east-1.signin.amazonaws-eusc.eu/) (`aws-eusc`). Getting access to the European Sovereign Cloud catalog requires you to have access to a European Sovereign Cloud AWS Account. This Account must be attached to your Seller Profile for the sole purpose of separating your listings and transactions between the partitions. If you do not already have an European Sovereign Cloud Account, you can [sign up as a European Sovereign Cloud customer](https://eusc-de-east-1.signin.amazonaws-eusc.eu/) and set up your Account. For ESC Account considerations and step-by-step guidance, see the [ESC getting started guide](https://docs.aws.eu/esc/latest/userguide/introduction.html). For frequently asked questions about ESC AWS Accounts, see the [ESC FAQ](https://aws.eu/faq/). Continue to next section for further information on ESC catalog access.

## ESC seller catalog registration
<a name="esc-registration"></a>

 Successful registration for the AWS European Sovereign Cloud Marketplace is subject to meeting all prerequisites described above. Please ensure you have access to the root-email associated with your AWS Account used as seller account. All multi-catalog registration communication will exclusively be sent to this email domain. To find your root email address, choose **Settings** and then **AWS Marketplace notifications** in AWS Partner Central. 

### Registering for the ESC catalog
<a name="registering-esc-catalog"></a>

Upon meeting all prerequisites, please follow the below steps to register and obtain access to the AWS Marketplace in ESC catalog management:

1. Sign in to the **[AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/)** using your **commercial AWS seller account** credentials.

1. Navigate to one of the following locations:
   + **Settings** tab → **Manage catalogs** section, OR
   + **Products** tab → **Multi-Catalog** section

1. Look for the **Catalog Registration** or **Register for Additional Catalog** option

1. Select **Register for ESC Catalog** or choose **AWS Marketplace - European Sovereign Cloud (aws-eusc)** from available catalog options

1. Choose **Submit registration**

### ESC Account Confirmation
<a name="esc-account-confirmation"></a>

 After the initial validation checks pass, the AWS Seller Operations team implements a dual email verification process to prevent unauthorized account linking. Because your ESC account must be linked to your commercial account to enable disbursements, the team sends one verification email to your commercial account root email address and one to your ESC account root email address, requesting confirmation that you authorize the account linking. 

 You must confirm from **both** email addresses — no exceptions. You have **5 business days** to respond. If no response is received within 5 business days, your registration is rejected and you must resubmit. 

**Important**  
Please ensure that the ESC account that you provided is the correct account for linking to your commercial one.

### ESC Approval and Access
<a name="esc-approval-access"></a>

Once approved, you will receive an email confirmation to your AWS account root email address. You also get access to the ESC catalog in AWS Partner Central, where you can create and publish ESC product listings.

**To verify your ESC catalog access**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. For **Catalog**, choose the AWS European Sovereign Cloud catalog (`aws-eusc`).

   If the ESC catalog isn't in the list, see [Troubleshooting and Support in the ESC](#troubleshooting-esc).

Before you add ESC products, add your public profile and disbursement preferences for the ESC catalog. For more information, see [ESC Seller Profile completion](#esc-seller-profile).

Both Commercial and ESC accounts must remain active throughout your AWS Marketplace in the AWS ESC participation. Suspension of your commercial account may affect your ESC catalog access.

### ESC Seller Profile completion
<a name="esc-seller-profile"></a>

Once submitted, AWS Marketplace catalog operations will contact you to confirm your ESC AWS Account ID.

**Note**  
This communication will be sent to the root email of your AWS Seller Account. Before being able to add and list products, you will be required to complete the following:  
Add [public profile](https://docs.aws.amazon.com/marketplace/latest/userguide/create-public-profile.html#create-public-profile-steps)
Add [disbursement preferences](https://docs.aws.amazon.com/marketplace/latest/userguide/set-disbursement-preferences.html)

## Creating and Managing ESC product listings
<a name="esc-product-listings"></a>

 All ESC products must be created from the commercial region in AWS Marketplace, even though they will be published to the ESC catalog. You can maintain products in both commercial and ESC catalogs simultaneously. Products in each catalog are independent, allowing separate pricing and distinct product portfolios. Not all commercial products need to be listed in ESC and vice-versa. The following product types are currently supported for AWS Marketplace in the AWS ESC: 

### SaaS products
<a name="saas-products-esc"></a>

All SaaS pricing models: Free, subscription, contract, and contract with consumption.

Sellers who have registered as an AWS Marketplace in the AWS ESC seller and have created an AWS ESC account (see [Multi-Catalog for Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/multi_catalog.html) for more information), can start listing their SaaS products. Supported pricing models: Contract, Subscription, Contract with Consumption, Pay-as-you-go (PAYG), and Free.

1. List your product in AWS Partner Central. For the steps, see [How to create a product listing in ESC](#create-product-listing-esc).

1. Select the "aws-eusc" catalog before creating

1. Integrate using region eusc-de-east-1 and AWS Marketplace EventBridge events (SNS is not supported)

1. Pricing in EUR - public listings must use EUR, while private offers may use EUR or USD

1. Test end-to-end in the ESC console, then request public visibility and submit for AWS Marketplace Seller Operations review

**Best practices:**

1. Do not create listings without first selecting the ESC catalog

1. Do not use commercial partition endpoints for API calls

1. Do not rely on SNS topic notifications — use EventBridge

1. Do not submit for public listing without completing end-to-end testing

Please refer to [SaaS-based products](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-products.html) and [diff doc](https://docs.aws.eu/esc/latest/userguide/marketplace.html) for further reference.

### AMI-based products
<a name="ami-products-esc"></a>

AMI-based products in the AWS European Sovereign Cloud deliver Amazon Machine Images (AMIs) with the **AMI (standalone)** delivery method. In AWS Partner Central, the **AMI with CloudFormation** and **EC2 Image Builder component** delivery methods aren't offered for the AWS European Sovereign Cloud catalog. AMI-based products support the following pricing options: Free, hourly, and hourly annual.

Sellers who have registered as AWS Marketplace sellers in the AWS ESC and have created an AWS ESC account (see [Multi-Catalog for Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/multi_catalog.html) for more information) can start listing their AMI products. To list an AMI-based product, complete the following steps:

1. List your product in AWS Partner Central. For the steps, see [How to create a product listing in ESC](#create-product-listing-esc).

1. Select the `aws-eusc` catalog before you create your product listing.

1. Complete each step under **Complete your listing**. Your product ID and product code appear on the product's page when you create the product.

1. Set pricing in EUR. Public listings must use EUR, and private offers can use EUR or USD.

1. Test end-to-end in the ESC console. Subscribe to and launch your product in the ESC partition to validate all use cases. If needed, update your product in AWS Partner Central with the ESC catalog selected.

1. Go public. If you created any test versions, restrict them first. Then set the product visibility to **Public** with EUR pricing.

1. Submit your product for review by the AWS Marketplace Seller Operations team.

For more information, see [AMI-based products](https://docs.aws.amazon.com/marketplace/latest/userguide/ami-products.html) and [AWS Marketplace in the AWS European Sovereign Cloud](https://docs.aws.eu/esc/latest/userguide/marketplace.html).

### Container products
<a name="container-products-esc"></a>

Container products are software packaged as container images that buyers deploy on AWS container services such as Amazon ECS and Amazon EKS. Container products support the following pricing options: Free, hourly, hourly annual, usage-based, Bring Your Own License (BYOL), and monthly.

Sellers who have registered as AWS Marketplace sellers in the AWS ESC and have created an AWS ESC account (see [Multi-Catalog for Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/multi_catalog.html) for more information) can start listing their container products. To list a container product, complete the following steps:

1. List your product in AWS Partner Central. For the steps, see [How to create a product listing in ESC](#create-product-listing-esc).

1. Select the `aws-eusc` catalog before you create your product listing.

1. Complete each step under **Complete your listing**. Your product ID and product code appear on the product's page when you create the product.

1. Set pricing in EUR. Public listings must use EUR, and private offers can use EUR or USD.

1. Test end-to-end in the ESC console. Subscribe to and launch your product in the ESC partition to validate all use cases. If needed, update your product in AWS Partner Central with the ESC catalog selected.

1. Go public. If you created any test versions, restrict them first. Then set the product visibility to **Public** with EUR pricing.

1. Submit your product for review by the AWS Marketplace Seller Operations team.

For more information, see [Container-based products](https://docs.aws.amazon.com/marketplace/latest/userguide/container-based-products.html).

### How to create a product listing in ESC
<a name="create-product-listing-esc"></a>

**To create an ESC product listing**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. For **Catalog**, choose the AWS European Sovereign Cloud catalog (`aws-eusc`).

1. Choose **Create product**.

   Under **Product details**, **Catalog** shows the catalog that you chose.

1. For **Product name**, enter a unique name of 2 to 72 characters.

1. For **Product type**, choose **Software**, and then for **Software type**, choose **SaaS**, **AMI-based**, or **Container**.

   The ESC catalog offers only these product types.

1. If you chose **Container**, for **Delivery option**, choose **AWS Marketplace Containers**.

1. Choose **Create product**.

   AWS Partner Central creates the product as a draft and opens the product's page.

**To publish an ESC product listing**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. For **Catalog**, choose the AWS European Sovereign Cloud catalog (`aws-eusc`).

1. Choose the product.

1. Complete each step under **Complete your listing**.

   Check that your product information complies with European regulations and that your pricing suits the EUR currency market.

1. Choose **Publish**.

1. In the confirmation dialog box, choose **Submit for review**.

AWS Marketplace reviews your listing against its policies before it goes live. Automated checks can approve it within hours. If a check flags your listing, the review usually takes 3 to 5 business days. The AWS Marketplace Seller Operations team also performs additional ESC authorization checks.

For detailed product preparation guidance, see the [Preparing your product for AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/product-preparation.html) section of this guide.

## Private Offers in AWS Marketplace in the AWS ESC
<a name="private-offers-esc"></a>

The ESC currently supports the following private offer types with flexible payment scheduler (FPS) and upfront payment:
+ **Direct Private Offers**: Create customized offers directly with buyers, including custom pricing, payment terms, and contract duration
+ **Channel Partner Private Offers (CPPO)**: Extend private offers through authorized channel partners who resell your products to end customers

While core private offer capabilities are available, some advanced features may differ or have limitations compared to the commercial marketplace experience (view [this documentation](https://docs.aws.eu/esc/latest/userguide/marketplace.html) for full overview).

### Creating Private Offers in AWS Marketplace in the AWS ESC
<a name="creating-private-offers-esc"></a>

You can create private offers for ESC customers using the same private offer workflow as the commercial Marketplace.

#### For Direct Private Offers
<a name="direct-private-offers-esc"></a>

1. Open the [**Offers**](https://console.aws.amazon.com/partnercentral/offers) page in AWS Partner Central, and sign in to your seller account.

1. Select **European Sovereign Cloud (aws-eusc)** from the **Catalog** drop-down menu.

1. On the **Private offers** tab, choose **Create private offer**.

1. Select your ESC product and complete the private offer details.

1. Choose either **Contract pricing with installment plan**, which is the flexible payment scheduler (FPS), or **Contract pricing with upfront payment**.

1. Set the currency. Private offers for ESC products default to EUR, but private offers can also use USD.

1. Extend the offer to your ESC customer's AWS account ID. The customer's account must be in the ESC partition.

**Note**  
Public offers must use EUR.

Before creating ESC private offers, confirm that EUR is configured in your disbursement preferences and that your bank account can accept EUR disbursements. For more information, see [Multi-currency pricing for private offers](https://docs.aws.amazon.com/marketplace/latest/userguide/multi-currency-pricing.html) in the [Product pricing](https://docs.aws.amazon.com/marketplace/latest/userguide/pricing.html) section of this guide.

#### For CPPO
<a name="cppo-esc"></a>

To create a selling authorization for a Channel Partner, follow the same procedure as in the commercial Marketplace. See [Create a selling authorization](channel-partner-isv-info.md#create-selling-authorization). The only difference is that you select **European Sovereign Cloud (aws-eusc)** from the **Catalog** drop-down menu in [AWS Partner Central](https://console.aws.amazon.com/partnercentral/home?region=us-east-1).

**Note**  
For Channel Partner Private Offers (CPPOs), both the ISV and the Channel Partner must be individually registered in the AWS Marketplace in the AWS ESC to transact within the same partition. Verify that both parties have completed ESC catalog registration before creating or accepting a CPPO. If either party is not yet registered, complete ESC registration first.

## Billing, Disbursements and Reporting
<a name="billing-esc"></a>

AWS Marketplace in the AWS ESC uses a dual-partition payment model that separates buyer-facing and seller-facing financial operations. This maintains European data sovereignty while enabling efficient seller payments.
+ **ESC partition (aws-eusc) — Buyer operations:** Buyer invoice processing, customer subscriptions, and entitlements are managed entirely within the ESC partition. All customer data and transactions remain within European boundaries, ensuring data sovereignty and regulatory compliance.
+ **Commercial partition (aws) — Seller operations:** Seller disbursements and listing fee invoices are handled through the commercial partition using existing AWS Marketplace infrastructure. This provides reliable EUR disbursements to sellers worldwide and maintains consistency with the commercial marketplace seller experience.

Your ESC customers' data never leaves the ESC partition. Your disbursements are processed through proven commercial infrastructure. You manage disbursements and reports for both catalogs in AWS Partner Central. Account linking connects the two partitions securely. Sellers can access their European Sovereign Cloud reports from the same UI available for the above listed dashboards. You will need to select the ESC dropdown from the Catalog Control available in seller dashboards.

### EUR transaction processing
<a name="eur-transaction-processing"></a>

All AWS Marketplace in the AWS ESC transactions are processed in Euros (EUR):
+ **Customer invoicing**: ESC customers receive invoices in EUR or their selected preferred currency, generated and processed within the ESC partition.
+ **Seller reporting**: ESC disbursements (EUR) are reported separately from commercial disbursements (USD). You will receive distinct disbursement reports for each catalog. See [Seller dashboards](https://docs.aws.amazon.com/marketplace/latest/userguide/dashboards.html) for additional information.

For more general details around disbursements please check the [Managing disbursements](https://docs.aws.amazon.com/marketplace/latest/userguide/managing-disbursements.html) section of this guide.

## Tax considerations
<a name="tax-esc"></a>

ESC transactions follow the same tax treatment as commercial AWS Marketplace transactions. The same tax logic, rates, and obligations apply; no special or separate tax rules are introduced for ESC. For detailed guidance, refer to the [Tax Help page for Sellers](https://aws.amazon.com/tax-help/marketplace-sellers/).

## Troubleshooting and Support in the ESC
<a name="troubleshooting-esc"></a>

The following table describes common issues you may encounter when registering for and using the ESC Marketplace, and their solutions.


| Issue | Solution | 
| --- | --- | 
| KYC verification delayed: No response received after two weeks, or the KYC team has requested document resubmission. | 1. Review all email communications from AWS Marketplace, including your spam and junk folders. 2. Verify that the root email address associated with your seller account is current and accessible. 3. Confirm that all submitted documents are clear, legible, and not expired; all required fields are visible and complete; file formats are accepted (PDF, JPG, or PNG); and document types match what was requested, such as a government-issued ID, business registration, or tax documents. 4. If resubmission was requested, review the specific feedback provided, correct the identified documents, and resubmit. 5. Contact KYC support for a status update. | 
| EUR bank account verification failed: Bank account rejected or verification pending indefinitely. | 1. Confirm the account holder name matches your business registration exactly. 2. Verify your SWIFT/BIC code is correct. 3. Confirm with your bank that the account supports international SWIFT wire transfers and EUR deposits. | 
| Cannot access ESC partition account creation portal: Access denied error when attempting to reach the portal. | 1. Verify that your commercial seller registration is fully approved. 2. Contact the AWS Seller Operations Team to request ESC partition access. 3. Confirm you are using the correct ESC partition URL provided by the AWS Seller Operations Team. 4. Confirm that your organization is eligible for ESC participation. | 
| ESC catalog not visible after approval: The ESC catalog does not appear in the Catalog dropdown list after receiving approval. | 1. Update your ESC public profile. 2. Update your ESC disbursement preferences. 3. Wait 1–2 hours for system propagation. 4. Clear your browser cache and sign in again. 5. Try accessing from an incognito or private browser window. 6. Contact the AWS Seller Operations Team if the catalog is still not visible after 24 hours. | 
| Verification email not received: Dual email confirmation not received at commercial or ESC account root address. | 1. Check spam and junk folders for both your commercial and ESC account root email addresses. 2. Verify that both root email addresses are correct. 3. Contact the AWS Seller Operations Team if you have not received the email after 24 hours. | 
| Product has external dependencies or hybrid architecture: Product does not meet the AWS-only infrastructure requirement. | 1. Redesign your architecture to use AWS-only services. 2. Migrate external dependencies to AWS infrastructure. 3. Remove or replace non-AWS components. 4. Consider creating an ESC-specific version of your product that meets the infrastructure requirement. | 
| EUR disbursement not received: Expected EUR disbursement has not arrived. | 1. Verify the EUR bank account is configured correctly. 2. Confirm the account supports international wire transfers. 3. Verify your SWIFT and IBAN information is accurate. 4. Contact your bank to confirm there are no blocks on incoming transfers. 5. Review your disbursement reports for processing status. | 
| Disbursement amount does not match expected value: Disbursement received is lower or higher than expected. | 1. Review listing fee deductions in your disbursement report. 2. Check for any refunds or chargebacks. 3. Verify all transactions are included in the disbursement period. 4. Compare against customer subscription start dates. | 
| Registration taking longer than expected: ESC registration has not been approved within the expected timeframe. | 1. Verify that all prerequisites are complete: KYC verification, EUR bank account, and ESC AWS account creation. 2. Check both root email addresses for requests from the AWS Seller Operations Team. 3. Respond promptly to any documentation requests. 4. Contact the AWS Seller Operations Team if you have not received a response. | 
| Product creation error: Errors encountered when creating ESC product listings. | 1. Verify that the ESC catalog is selected in the Catalog dropdown list on the Products and services page. 2. Confirm the product type is supported for ESC Marketplace. 3. Check that all required fields are completed. 4. Review the error message for specific guidance. | 
| Cannot create private offer in EUR: EUR is not available as a currency option when creating a private offer. | 1. Verify that EUR is configured in your disbursement preferences. 2. Confirm your EUR bank account is set up and verified. 3. Ensure the ESC catalog is selected when creating the offer. | 
| CPPO transaction unavailable or fails in ESC | Both the ISV and the Channel Partner must be individually registered in the AWS Marketplace in the AWS ESC to transact within the same partition. | 

If the preceding table doesn't resolve your issue, contact the Seller Operations team on the [ Partner Central and Marketplace Support page](https://us-east-1.console.aws.amazon.com/partnercentral/support?region=us-east-1). Select the appropriate issue category, and provide your AWS account ID and ESC catalog context.