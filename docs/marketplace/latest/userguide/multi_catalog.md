# Multi-Catalog for AWS Marketplace Sellers

AWS Marketplace now provides sellers the ability to create and manage products across multiple separate catalogs. The Multi-Catalog capability enables you to list your software products in specialized marketplace environments beyond the standard commercial AWS Marketplace, each serving distinct customer bases with specific regulatory, data residency, or sovereignty requirements.

## What is Multi-Catalog?

Multi-Catalog allows you to maintain completely separate product catalogs in different AWS partitions while managing them from a single seller account. Each catalog operates independently with its own:

- Product listings and pricing
- Customer base and subscriptions
- Regulatory and compliance requirements
- Geographic or jurisdictional boundaries

You create and manage all catalogs through the AWS Marketplace Management Portal (AMMP) in the commercial region, using the catalog selection dropdown feature to switch between your available catalogs.

## Available Catalogs

Currently, AWS Marketplace supports Multi-Catalog capability for the following:

**AWS Marketplace - European Sovereign Cloud (ESC)**

The European Sovereign Cloud Marketplace is the first additional catalog available through the Multi-Catalog capability. The AWS European Sovereign Cloud provides EU-based organizations enhanced data residency and operational controls to help meet stringent European regulatory requirements.

Additional catalogs may become available in the future. Check the AWS Marketplace Management Portal for current catalog availability.

## European Sovereign Cloud (ESC) Marketplace

### Overview

The AWS European Sovereign Cloud (ESC) Marketplace enables you to offer your products to customers who require enhanced data sovereignty, residency, and operational control within the European Union. ESC is designed to help EU-based organizations meet strict regulatory requirements while leveraging the benefits of cloud computing.

### Why Sell in ESC Marketplace?

Selling in ESC Marketplace provides several benefits:

- **Expanded market access** Reach EU-based organizations with stringent data sovereignty requirements
- **Regulatory alignment** Help customers meet European regulatory compliance needs
- **Separate catalog management** Maintain distinct product offerings and pricing for ESC customers
- **Streamlined operations** Manage both commercial and ESC catalogs from a single seller account

### Key Differences: Commercial vs. ESC Marketplace

| Aspect                       | Commercial Marketplace     | ESC Marketplace                                     |
| ---------------------------- | -------------------------- | --------------------------------------------------- |
| **Customer base**            | Global AWS customers       | EU-based customers requiring data sovereignty       |
| **Data residency**           | Multiple global regions    | European Union regions only                         |
| **Partition**                | Standard AWS partition     | ESC partition (aws-eusc)                            |
| **Catalog management**       | Default catalog            | Separate ESC catalog via dropdown                   |
| **Product listing**          | Created in commercial AMMP | Created in commercial AMMP, replicated to ESC       |
| **AWS Account requirements** | Commercial AWS account     | Both commercial and ESC partition accounts required |

## Prerequisites for ESC Catalog Registration

Before you can register for the AWS Marketplace - European Sovereign Cloud (ESC) catalog and list products, you must complete all of the following prerequisites. **Incomplete prerequisites will result in registration delays or rejection.**

## Overview of Requirements

ESC Marketplace has stricter requirements than commercial AWS Marketplace due to European sovereignty and regulatory compliance needs. All sellers must meet these prerequisites before beginning the registration process.

**Estimated Time to Complete All Prerequisites:** 4-8 weeks (depending on KYC verification timeline)

### 1. Complete Commercial AWS Marketplace Registration

**Required Commercial Registration Components**

Your commercial seller registration must include:

- **Completed seller registration process** - All registration forms submitted and approved
- **Active public profile** - Public seller profile published and visible in AWS Marketplace
- **Tax information submitted and verified** - W-9 (US sellers) or W-8 (non-US sellers) forms completed
- **Bank account information provided** - At least one valid bank account configured for disbursements
- **At least one product listed** - Minimum of one product published in commercial AWS Marketplace (any product type)

**Verification Steps**

To verify your commercial registration status:

1. Sign in to the AWS Marketplace Management Portal at [https://aws.amazon.com/marketplace/management/](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/")
2. Navigate to **Settings** > **Seller profile**
3. Confirm your profile status shows **Active**
4. Navigate to **Products** and verify at least one product is listed
5. Navigate to **Settings** > **Payment information** and verify bank account is configured

**Important Notes**

- **ESC catalog registration is available only to existing AWS Marketplace sellers**
- You cannot register for ESC as your first marketplace catalog
- Your commercial registration must remain active throughout your ESC participation
- Any suspension or termination of your commercial seller account will affect your ESC catalog access

**If you have not completed commercial registration:** See "Registering as a seller" earlier in this guide for detailed instructions.

### 2. Complete Know Your Customer (KYC) Verification

ESC Marketplace requires all sellers to complete the Know Your Customer (KYC) validation process as part of the registration process. This is a mandatory compliance requirement for operating in the ESC Marketplace.

**Why KYC is Required for ESC**

KYC verification ensures compliance with:

- European Anti-Money Laundering (AML) regulations
- EU Counter-Terrorism Financing (CTF) requirements
- European data sovereignty and operational control standards
- Financial services regulatory requirements

**KYC Process Timeline**

- **Typical processing time:** 2 weeks
- **Maximum processing time:** Up to 30 calendar days
- **Document resubmission:** Additional 5-10 business days if documents require correction

**How to Complete KYC Verification**

1. Access the KYC portal through AWS Marketplace Management Portal
2. Navigate to **Settings** > **KYC Verification**
3. Complete the online KYC form with company and individual information
4. Upload all required documentation in PDF or image format (JPEG, PNG)
5. Submit for review
6. Monitor your email for KYC team requests or approval confirmation

**Important KYC Notes**

- **The Amazon Inc. workaround option is NOT available for ESC sellers** - You must complete full KYC validation
- All documents must be in English or accompanied by certified translations
- Documents must be clear, legible, and unaltered
- Expired documents will not be accepted
- Incomplete submissions will delay your ESC registration

**KYC Verification Delayed**

Issue: No response after 2 weeks, or document resubmission requested

**Solutions:**

- Ensure all documents are clear, legible, and current
- Provide certified translations for non-English documents
- Verify all required individuals are included
- Contact KYC support team for status update

**For detailed KYC instructions:** See "Complete the KYC process" in the "Registering as a seller" section of this guide.

**KYC Support Contact:**
[https://aws.amazon.com/marketplace/management/contact-us/?form=true](https://aws.amazon.com/marketplace/management/contact-us/?form=true "https://aws.amazon.com/marketplace/management/contact-us/?form=true")

### 3. EUR-Compatible Bank Account

ESC Marketplace transactions are processed exclusively in Euros (EUR). You must provide a bank account capable of receiving EUR currency disbursements.

**Bank Account Requirements**

Your bank account must:

- **Accept EUR currency transactions** - Account must support EUR deposits
- **Support international wire transfers** - Must accept SWIFT transfers
- **Be verified in AMMP** - Account must be validated by AWS Marketplace
- **Match your registered business entity** - Account holder name must match your seller registration

**Supported Bank Account Types**

- Business checking accounts (EUR-denominated)
- Multi-currency business accounts with EUR support
- European bank accounts (SEPA-enabled)
- International bank accounts with EUR conversion capabilities

**Setting Up EUR Disbursements**

To configure EUR disbursements in AWS Marketplace Management Portal:

1. Sign in to the AWS Marketplace Management Portal
2. Navigate to **Settings** > **Payment information**
3. In the **Disbursement methods** section, choose **Add disbursement method**
4. For **Currency**, select **EUR**
5. For **Bank account**, choose an existing account or add a new EUR-compatible account
6. Provide the following bank information:
   - Bank name
   - Bank address
   - SWIFT/BIC code
   - IBAN (for European banks) or account number
   - Account holder name (must match your business registration)

7. Select your disbursement frequency (daily or monthly)
8. Choose **Add disbursement method**

**Important Banking Notes**

- EUR disbursements for ESC transactions will only go to your designated EUR account
- Commercial marketplace disbursements (USD) will continue to your existing USD account
- Bank account changes require re-verification

**EUR Bank Account Verification Failed**

Issue**:** Bank account rejected or verification pending indefinitely

**Solutions:**

- Confirm account holder name matches business registration exactly
- Verify SWIFT/BIC code is correct
- Ensure account supports international wire transfers
- Contact your bank to confirm EUR acceptance capability

### 4. AWS Account Requirements

To operate in ESC Marketplace, you need **two separate AWS accounts** in different AWS partitions.

**Required Accounts**

**1. Commercial AWS Account**

- **Purpose:** Your existing AWS Marketplace seller account
- **Partition:** Standard AWS partition (aws)
- **Usage:**
  - Manage products and create listings
  - Access AWS Marketplace Management Portal (AMMP)
  - Manage catalog selection and product configuration
  - Receive disbursements and view financial reports

**This is your existing seller account** - no new account creation needed.

**2. ESC Partition AWS Account**

- **Purpose:** Dedicated account for ESC Marketplace operations
- **Partition:** AWS European Sovereign Cloud partition (aws-eusc)
- **Usage:**
  - Maintain ESC Marketplace catalog presence
  - Enable ESC-specific product replication
  - Support ESC customer entitlements and subscriptions

**You must create this new account** in the ESC partition.

**Creating Your ESC Partition Account**

To create an ESC partition AWS account:

1. Access the ESC partition account creation portal (contact AWS Seller Operations Team for access)
2. Complete the ESC account registration form
3. Provide business information (must match your commercial seller registration)
4. Accept ESC-specific terms and conditions
5. Verify your ESC account root email address
6. Complete ESC account security setup (MFA required)

**Important Account Notes**

- **You cannot use the same AWS account for both commercial and ESC partitions** - These are separate accounts in separate AWS partitions
- Both accounts must remain active throughout your ESC Marketplace participation
- Account suspension in either partition may affect your ESC catalog access
- Root email addresses for both accounts must be accessible during registration
- Multi-factor authentication (MFA) is required for both accounts

**Account Security Requirements**

For both accounts:

- Enable MFA on root account
- Create IAM users for administrative access (do not use root account for daily operations)
- Implement strong password policies
- Monitor account activity regularly
- Keep root email addresses accessible and monitored

**ESC Account Creation Access Denied**

Issue**:** Cannot access ESC partition account creation portal

**Solutions:**

- Verify commercial seller registration is fully approved
- Contact AWS Seller Operations Team for ESC partition access
- Ensure you're using correct AWS partition URL
- Confirm your organization is eligible for ESC participation

### 5. Deployed on AWS-Only Infrastructure

ESC Marketplace requires that all products are deployed **exclusively on AWS infrastructure** to meet European sovereignty and compliance requirements.

**Infrastructure Requirements**

Your product must:

- **Run entirely on AWS services and infrastructure** - No external dependencies
- **Use only AWS compute resources** - EC2, ECS, EKS, Lambda, etc.
- **Store all data on AWS storage services** - S3, EBS, EFS, RDS, etc.
- **Use AWS networking services** - VPC, CloudFront, Route 53, etc.
- **Operate within ESC-approved regions** - All resources must be in ESC regions

**Prohibited Dependencies**

Products **cannot** include:

- External infrastructure or hosting services (non-AWS)
- Third-party SaaS dependencies that store or process customer data outside AWS
- Hybrid deployments spanning AWS and non-AWS infrastructure
- On-premises components required for product functionality
- External APIs that process or store customer data outside ESC boundaries

**Acceptable Third-Party Integrations**

You may include third-party components if:

- They run entirely within your AWS infrastructure
- They do not transmit customer data outside ESC boundaries
- They are packaged within your product deployment
- They comply with ESC data sovereignty requirements

Examples of acceptable integrations:

- Open-source libraries and frameworks deployed on AWS
- Third-party software installed on your EC2 instances
- Containerized third-party applications running on ECS/EKS
- Database engines running on RDS or EC2

**Verification and Documentation**

To verify your product meets AWS-only infrastructure requirements:

- **Create an architecture diagram\*\***showing\*\*:
  - All AWS services used by your product
  - Data flow between components
  - External integrations (if any)
  - Data storage locations

- **Document all dependencies:**
  - List all AWS services used
  - Identify any third-party components
  - Explain how each component operates within AWS
  - Confirm no data leaves ESC boundaries

- **Prepare compliance statement:**
  - Written confirmation that product runs exclusively on AWS
  - Explanation of how data sovereignty is maintained
  - Description of ESC region deployment strategy

**ESC-Specific Considerations**

For ESC Marketplace:

- All product resources must be deployable in ESC regions
- Customer data must remain within ESC boundaries at all times
- Backup and disaster recovery must be within ESC territory
- No data replication or transfer outside ESC regions
- Logging and monitoring must use ESC-compliant services

**Product Infrastructure Does Not Meet Requirements**

Issue: Product has external dependencies or hybrid architecture

**Solutions:**

- Redesign architecture to use AWS-only services
- Migrate external dependencies to AWS infrastructure
- Remove or replace non-AWS components
- Consider creating ESC-specific product version

Be prepared to provide this documentation during the ESC registration process.

## Estimated Timeline for Prerequisites

|                              |                  |                                           |
| ---------------------------- | ---------------- | ----------------------------------------- |
| Commercial Registration      | Already complete | Must be done before ESC registration      |
| KYC Verification             | 2-4 weeks        | Can take up to 30 days                    |
| EUR Bank Account Setup       | 1-2 weeks        | Includes verification time                |
| ESC AWS Account Creation     | 1-3 days         | Requires ESC partition access             |
| Infrastructure Documentation | 1-2 weeks        | Depends on product complexity             |
| Total Estimated Time         | 4-8 weeks        | Concurrent activities can reduce timeline |

## ESC Catalog Registration Process

After completing all prerequisites, you can register for the ESC catalog through the AWS Marketplace Management Portal.

**Registration Overview**

The ESC registration process involves:

1. Submitting your registration request through AMMP
2. AWS Seller Operations Team validation and verification
3. Security verification via dual email confirmation
4. Final approval and catalog access enablement

\***\*Important:\*\*** Keep both your commercial and ESC AWS account root email addresses monitored throughout this process, as you will receive critical verification requests at both addresses.

### Step 1: Access the Catalog Registration

**Navigate to Registration Portal**

1. Sign in to the **AWS Marketplace Management Portal** at [https://aws.amazon.com/marketplace/management/](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/") using your **commercial AWS seller account** credentials
2. Navigate to one of the following locations:
   - **Settings** tab → **Catalog Registration** section, OR
   - **Products** tab → **Multi-Catalog** section

3. Look for the **Catalog Registration** or **Register for Additional Catalog** option
4. Select **Register for ESC Catalog** or choose **AWS Marketplace - European Sovereign Cloud (aws-eusc)** from available catalog options

### Step 2: Complete ESC Registration Form

The registration form collects information to validate your eligibility and link your accounts properly.

**Section A: ESC AWS Account Information**

**ESC Partition AWS Account ID**

- Enter your 12-digit ESC partition AWS Account ID
- This must be an account in the **aws-eusc partition** (not your commercial account)

**ESC Account Root Email Address**

- Provide the root email address associated with your ESC AWS account
- This email will receive security verification requests
- Ensure you have access to this email inbox

**Account Status Confirmation**

- Confirm the ESC account is active and accessible
- Verify the account is within the ESC partition (aws-eusc)

**Section B: Commercial Account Verification**

**Commercial AWS Account ID**

- Your existing AWS Marketplace seller account ID
- This should auto-populate based on your current session
- Verify the displayed account ID is correct

**Commercial Account Root Email Address**

- Provide the root email address for your commercial AWS account
- This email will also receive security verification requests
- Must be accessible for dual email confirmation process

### Step 3: Submit Registration Request

**Review Your Information**

Before submitting:

1. **Verify all account IDs are correct** - Double-check both commercial and ESC account IDs
2. **Confirm email addresses are accessible** - You will need to respond to verification emails
3. **Review all acknowledgments** - Ensure you understand all requirements
4. **Check prerequisite validation results** - Address any flagged issues before submitting

**Submit Your Request**

1. Choose **Submit Registration Request**
2. You will see a confirmation message: "Your ESC catalog registration request has been submitted"
3. Note your **registration request ID** (if provided) for future reference

### Step 4: AWS Seller Operations Team Review and Validation

After you submit your registration, the AWS Seller Operations Team begins a comprehensive validation process. This step includes **automated checks, manual verification, and mandatory dual email security confirmation** to prevent malicious account linking attempts.

**Initial Validation Checks**

The AWS Seller Operations Team will perform the following validations:

- **Receive automatic Salesforce case** Your registration creates an automatic support case in the MCO queue
- **Verify Public Profile** - The team verifies the commercial account has completed and published a public seller profile
- **Tax information verification** - The team confirms that the tax interview (W-9/W-8) is complete and verified
- **Validate KYC completion** The team verifies your KYC status via internal KYC dashboard
- **Verify EUR bank account** The team confirms your bank account can accept EUR transactions
- **Confirm AWS Account IDs** The team validates both your commercial and ESC partition accounts are active and in correct partitions
- **Send email requesting proof** You may receive an email requesting documentation to verify the prerequisites

**You must respond promptly to any AWS Seller Operations Team requests to avoid delays in your registration approval.**

**Dual Email Confirmation Security Process**

**CRITICAL SECURITY REQUIREMENT:** After initial validation checks pass, the Managed Catalog Operations (MCO) team implements a **strict dual email verification process** to prevent unauthorized account linking. Your ESC account must be linked to your commercial account to enable disbursements. The team will send two emails: one associated with your commercial root account and one associated with your ESC root account to request verification that you are registering and will have the accounts linked.

- A confirmation from both emails must be received to confirm account linking - no exceptions.
- Sellers will have 5 business days to confirm.
- Seller registration will be rejected if there is no response after 5 days, and the seller must resubmit again.

**Why Dual Email Confirmation is Required**

This security measure protects against:

- Malicious account linking attempts
- Unauthorized access to ESC catalog entitlements
- Account takeover scenarios
- Fraudulent seller registrations

**Both account root emails must confirm the account linking - no exceptions.**

### Step 5: Await Approval

**Timeline Expectations:**

- **Official SLA:** Up to 30 calendar days for registration processing
- **Typical completion time:** Within 2-14 calendar days

During this period, the AWS Seller Operations Team completes all validation checks and enables your account for ESC catalog access.

### Step 6: Receive Approval Confirmation

To prevent malicious account linking attempts, AWS implements a dual email confirmation process before granting ESC catalog entitlements.

Once approved, you will receive:

- Email confirmation to your AWS account root email address
- Access to the ESC catalog in the AWS Marketplace Management Portal
- Ability to create and publish ESC product listings

You can verify your ESC catalog access by checking for the catalog dropdown in the AMMP header, which will now include "AWS Marketplace - European Sovereign Cloud (aws-eusc)" as a selection option.

**Why Dual Email Confirmation?**
This security measure ensures:
Both account owners authorize the account linking
No unauthorized access to ESC catalog capabilities
Protection against account takeover attempts
Compliance with security best practices

**Didn't receive ESC verification email**

- Ensure you completed commercial verification first
- Check spam/junk folders for ESC account email
- Verify ESC root email address is correct
- Contact AWS Seller Operations Team if not received after 24 hours

**Verify Your ESC Catalog Access**

To confirm your ESC catalog access is enabled:

1. Sign in to the **AWS Marketplace Management Portal** at [https://aws.amazon.com/marketplace/management/](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/")
2. Look for the **catalog dropdown** in the header navigation (top of page)
3. Click the dropdown to view available catalogs
4. Verify you see: **AWS Marketplace - European Sovereign Cloud (aws-eusc)**
5. Select the ESC catalog to begin working with ESC products

**If you don't see the ESC catalog option:**

- Wait 1-2 hours for system propagation
- Clear your browser cache and sign in again
- Try accessing from an incognito/private browser window
- Contact AWS Seller Operations Team if still not visible after 24 hours

## Creating and Managing ESC Product Listings

After your ESC catalog registration is approved, you can begin creating product listings for the ESC Marketplace.

### Using the Catalog Selection Dropdown

The AWS Marketplace Management Portal includes a catalog selection dropdown in the header that allows you to switch between your available catalogs.

**To select your catalog:**

1. Sign in to the AWS Marketplace Management Portal.
2. Locate the catalog dropdown in the header navigation.
3. Choose **AWS Marketplace - European Sovereign Cloud (aws-eusc)** to work with ESC products.
4. Choose **AWS Marketplace** (default) to work with commercial products.

The selected catalog context determines where your products are created and published.

### Product Creation Workflow

**Important:** All ESC products must be created from the commercial region AMMP, even though they will be published to the ESC catalog.

**Step 1: Select ESC Catalog**

- In AMMP header, choose **AWS Marketplace - European Sovereign Cloud (aws-eusc)** from the catalog dropdown.

**Step 2: Create Product Listing**

- Navigate to the **Products** tab.
- Choose **Create new product** and select your product type:
- SaaS products (SaaS subscriptions, contracts, or contracts with consumption)
- AMI-based products
- Complete all required product information, including:
- Product name and description
- Pricing model and dimensions
- Usage instructions
- Support information
- End User License Agreement (EULA)

**Step 3: Configure ESC-Specific Settings**

- Review ESC-specific requirements for your product type
- Ensure all product information complies with European regulations
- Verify pricing is appropriate for the EUR currency market

**Step 4: Submit for Review**

- Submit your product for AWS Marketplace review
- The standard product review process applies for ESC products
- AWS Seller Operations Team will perform additional ESC authorization checks

### Supported Product Types

The following product types are currently supported for ESC Marketplace:

- **SaaS products** All SaaS pricing models (subscription, contract, contract with consumption)
- **AMI-based products** Amazon Machine Images with various pricing options

Additional product types may be supported in the future. Check the AWS Marketplace Management Portal for current product type availability in ESC.

### Managing Multiple Catalogs

You can maintain products in both commercial and ESC catalogs simultaneously:

- **Independent catalogs** Products in each catalog are separate and independent
- **Separate pricing** You can set different pricing for commercial vs. ESC products
- **Different product portfolios** Not all commercial products need to be listed in ESC
- **Unified management** Use the same AMMP account to manage all catalogs

**Best Practice:** Use clear product naming conventions to distinguish between commercial and ESC versions of similar products.

## Private Offers in ESC Marketplace

You can create private offers for ESC customers using the same private offer workflow as commercial marketplace, with ESC-specific considerations.

### Creating ESC Private Offers

1. Select **AWS Marketplace - European Sovereign Cloud (aws-eusc)** from the catalog dropdown.
2. Navigate to **Offers** and choose **Create private offer**.
3. Select your ESC product and complete the private offer details.
4. **Currency:** Private offers for ESC products can use **EUR** or **USD** currency, but will default to **EUR**. Public offers must use **EUR** currency.
5. Extend the offer to your ESC customer's AWS Account ID (must be in ESC partition).

### EUR Currency Requirements

**Before creating ESC private offers, ensure:**

- EUR is configured in your disbursement preferences
- Your bank account can accept EUR disbursements
- You understand EUR pricing and foreign exchange considerations

For more information about multi-currency private offers, see Multi-currency pricing for private offers in the "Product pricing" section of this guide.

## ESC Marketplace Customer Experience

Understanding how ESC customers discover and purchase your products helps you optimize your ESC listings.

### How ESC Customers Access Products

**ESC Partition Access:**

- ESC customers use AWS accounts in the ESC partition (aws-eusc)
- They access the ESC Marketplace through the ESC partition console
- They can search, procure, and fulfill products specifically listed in the ESC catalog

**Separate Marketplace:**

- ESC Marketplace operates independently from commercial AWS Marketplace
- ESC customers only see products listed in the ESC catalog
- Commercial marketplace products are not visible to ESC customers (unless also listed in ESC)

### Product Discovery

ESC customers find products through:

- **Search** Keyword and category search within ESC Marketplace
- **Browse** Category and filter-based browsing
- **Direct links** Product URLs shared by sellers
- **Private offers** Negotiated offers extended to specific customers

Optimize your ESC product listings with:

- Clear, descriptive product names
- Comprehensive product descriptions
- Relevant categories and keywords
- European use case examples

## Billing, Invoicing, and Disbursements

### EUR Transaction Processing

ESC Marketplace uses a **dual-partition payment processing model** that separates buyer-facing and seller-facing financial operations to maintain European sovereignty while enabling efficient seller payments.

**Understanding the Dual-Partition Payment Model**

**ESC operates across two AWS partitions for payment processing:**

**ESC Partition (aws-eusc) - Buyer Operations:**

- Buyer invoice processing occurs within ESC partition
- Customer subscriptions and entitlements managed in ESC
- All customer data and transactions remain within European boundaries
- Ensures data sovereignty and regulatory compliance

**Commercial Partition (aws) - Seller Operations:**

- Seller-related activities (listing fee invoices and disbursements) are handled in the commercial partition
- Seller payments processed through existing AWS Marketplace infrastructure
- Enables efficient EUR disbursements to sellers worldwide
- Maintains consistency with commercial marketplace seller experience

**Why This Matters:**

- Your ESC customers' data never leaves the ESC partition
- Your disbursements are processed reliably through proven commercial infrastructure
- You manage both catalogs from a single AMMP interface
- Account linking connects these two partitions securely

**EUR Transaction Processing**

All ESC Marketplace transactions are processed in Euros (EUR):

**Customer Invoicing:**

- ESC customers receive invoices in EUR
- Invoices are generated and processed within the ESC partition
- Customers pay in EUR through ESC-compliant payment methods

**Listing Fees:**

- AWS Marketplace listing fees are deducted in EUR
- Fees are calculated as a percentage of the transaction value
- Deductions occur in the commercial partition before disbursement

**Seller Disbursements:**

- You receive disbursements in EUR to your designated bank account
- Disbursements are processed through the commercial partition
- All ESC revenue is paid out in EUR currency

**Disbursement Timeline**

ESC disbursements follow the standard AWS Marketplace disbursement schedule:

**Timing:**

- Disbursements occur according to your selected schedule (daily or monthly)
- Processed through commercial partition infrastructure
- Same reliability as commercial marketplace disbursements

**Currency:**

- All ESC disbursements are in EUR
- Commercial marketplace disbursements (USD) remain separate

**Processing Time:**

- Typically 1-2 business days after disbursement date
- International wire transfers may take 3-5 business days
- SEPA transfers (European banks) typically 1-2 business days

**Disbursement Separation:**

- ESC disbursements (EUR) are separate from commercial disbursements (USD)
- You will receive distinct disbursement reports for each catalog
- Track ESC revenue separately in your financial systems

**Listing Fees**

Standard AWS Marketplace listing fees apply to ESC transactions:

**Fee Structure:**

- Listing fees are calculated as a percentage of the transaction value
- The same listing fee structure applies as commercial marketplace
- Fees are deducted in EUR from your ESC disbursements
- Fee deduction occurs in commercial partition before disbursement to you

**Fee Reporting:**

- Listing fees are itemized in your disbursement reports
- Separate reporting for ESC vs. commercial transactions

**Troubleshooting Disbursement Issues**

**Issue: EUR disbursement not received**

- Verify EUR bank account is configured correctly in AMMP
- Check that account can accept international wire transfers
- Confirm SWIFT/IBAN information is accurate
- Contact your bank to verify no incoming transfer blocks
- Review disbursement reports for processing status

**Issue: Disbursement amount doesn't match expected**

- Review listing fee deductions in disbursement report
- Check for any refunds or chargebacks
- Verify all transactions are included in the disbursement period
- Compare against customer subscription dates

### Tax Considerations

ESC transactions are subject to European tax regulations and have specific requirements that differ from commercial AWS Marketplace.

**European Tax Requirements**

**VAT (Value Added Tax):**

- You must provide VAT registration information for European operations
- VAT rates vary by EU member state
- B2B transactions may use reverse charge mechanism
- Keep accurate records of customer VAT status and location

**Tax Invoicing:**

- You may be responsible for tax invoicing, collections, and remittances depending on your location
- EU-based sellers typically must issue VAT-compliant invoices
- Non-EU sellers may have different obligations based on tax treaties

**Compliance:**

- Consult with your tax advisor regarding European tax obligations
- Stay current with EU tax regulation changes
- Maintain proper documentation for tax audits
- Consider registering for VAT in relevant EU countries if required

**Tax Inheritance Limitation for ESC**

**CRITICAL: Tax Inheritance is NOT supported for ESC catalog operations.**

**What is Tax Inheritance?**

Tax Inheritance is a feature in commercial AWS Marketplace that allows linked AWS accounts (in an AWS Organizations structure) to inherit tax settings from a management account. This simplifies tax configuration for sellers with multiple linked accounts.

**Why This Matters for ESC**

**ESC accounts cannot use Tax Inheritance** due to the separate partition structure (aws-eusc) and European sovereignty requirements. Each ESC account must have its own independent tax configuration.

**Pre-Registration Tax Inheritance Check**

**Before submitting your ESC registration, you MUST verify your tax inheritance status:**

1. Sign in to the AWS Marketplace Management Portal
2. Navigate to **Settings** > **Tax information**
3. Check if your account shows **"Tax settings inherited from management account"** or similar indicator
4. If Tax Inheritance is enabled, you have two options:

**Option A: Disable Tax Inheritance (Recommended)**

- Contact AWS Seller Operations Team to disable Tax Inheritance
- Provide independent tax information for your seller account
- Complete this change **before** submitting ESC registration
- This prevents any issues during account linking

**Option B: Proceed with Tax Inheritance Enabled (At Your Own Risk)**

- You will receive a **Tax Inheritance Confirmation Email** from the Managed Catalog Operations (MCO) team during registration
- The email will explain the risks and limitations
- You must explicitly confirm you want to proceed despite Tax Inheritance being enabled
- **Important:** If you confirm to proceed, **all issues following the account linking will be your responsibility**

**Risks of Proceeding with Tax Inheritance Enabled**

If you choose to proceed with Tax Inheritance enabled despite the warning:

**Potential Issues:**

- EUR disbursements may be delayed or fail due to tax configuration conflicts
- Tax reporting may be inaccurate or incomplete for ESC transactions
- Account linking process may encounter errors
- European tax compliance verification may fail
- You may be unable to resolve tax-related issues without disabling Tax Inheritance
- AWS support for tax-related problems will be limited

**Your Responsibilities:**

- The seller will own all troubleshooting and resolution of tax-related issues
- The seller must work with their tax advisor to ensure compliance
- The seller may need to disable Tax Inheritance later to resolve issues (requiring re-registration)
- The seller accept potential revenue delays or losses due to disbursement problems

**How to Disable Tax Inheritance**

If you need to disable Tax Inheritance:

1. **Contact AWS Seller Operations Team:**
   - Use AMMP "Contact Us" feature
   - Select issue category: "Tax Information"
   - Request: "Disable Tax Inheritance for ESC registration"
   - Provide your AWS Account ID

2. **Provide Independent Tax Information:**
   - Submit W-9 (US sellers) or W-8 (non-US sellers) directly for your seller account
   - Ensure tax information is complete and verified
   - Wait for confirmation that Tax Inheritance is disabled

3. **Verify Tax Inheritance is Disabled:**
   - Check Settings > Tax information in AMMP
   - Confirm you see your independent tax settings (not inherited)
   - Proceed with ESC registration

**Timeline:** Disabling Tax Inheritance typically takes 3-5 business days.

**Best Practice Recommendation**

**We strongly recommend disabling Tax Inheritance before starting ESC registration** to avoid:

- Registration delays
- Potential rejection
- Future operational issues
- Complex troubleshooting scenarios

**If you're unsure about your Tax Inheritance status:**

- Check your tax settings in AMMP before registration
- Contact AWS Seller Operations Team for clarification
- Consult with your tax advisor about the best approach

## Troubleshooting and Support

### Common Issues

**Registration Delays**

- **Issue:** ESC registration taking longer than expected
- **Resolution:**
- Verify all prerequisites are complete (KYC, EUR bank account, ESC AWS account)
- Check your root email address for AWS Seller Operations Team requests
- Respond promptly to any documentation requests
- Contact AWS Seller Operations Team if no response after 30 days

**Product Creation Errors**

- **Issue:** Errors when creating ESC products
- **Resolution:**
- Verify ESC catalog is selected in dropdown
- Ensure product type is supported for ESC
- Check that all required fields are completed
- Review error messages for specific issues

**Private Offer Currency Issues**

- **Issue:** Cannot create private offer in EUR
- **Resolution:**
- Verify EUR is configured in disbursement preferences
- Confirm EUR bank account is set up and verified
- Ensure ESC catalog is selected when creating offer

### Support Resources

**Documentation**

For additional information and guidance, refer to these resources:

- **AWS Marketplace Registration Process Guide** https://docs.aws.amazon.com/marketplace/latest/userguide/registration-process.html
- **Know Your Customer (KYC) Registration Information** Available through AWS Marketplace Management Portal
- **Local Currency Offers and Disbursement Setup Guide** Available through AWS Marketplace Management Portal

**Contact Support**

If you encounter issues with ESC catalog registration or product listings:

1. **AWS Marketplace Seller Operations Team** - Access through AWS Marketplace Management Portal - Choose **Contact Us** and select appropriate issue category - Provide detailed information including your AWS Account ID and ESC catalog context
2. **KYC Support** - For KYC verification issues - Contact the team through the provided link: [https://aws.amazon.com/marketplace/management/contact-us/?form=true](https://aws.amazon.com/marketplace/management/contact-us/?form=true "https://aws.amazon.com/marketplace/management/contact-us/?form=true")

### Best Practices

**Successful ESC Marketplace Participation**

1. **Complete prerequisites thoroughly** Ensure all registration requirements are met before applying
2. **Monitor both root email address** Keep your AWS root email monitored for AWS Seller Operations Team communications
3. **Respond promptly** Quick responses to documentation requests speed registration
4. **Plan for EUR pricing** Consider currency conversion and European pricing expectations
5. **Understand European regulations** Familiarize yourself with EU data sovereignty requirements
6. **Maintain separate accounts** Keep commercial and ESC AWS accounts properly separated
7. **Test products** Thoroughly test ESC products before publishing to customers
8. **Provide excellent documentation** Help ESC customers understand your product's compliance features

## Next Steps

After successfully registering for ESC catalog and understanding the Multi-Catalog capability:

1. **Create your first ESC product listing** Follow the product creation workflow for your product type
2. **Review ESC-specific requirements** Ensure your products meet European regulatory needs
3. **Optimize for ESC customers** Tailor your product descriptions and documentation for EU use cases
4. **Configure private offers** Set up EUR-based private offers for enterprise customers

For detailed product preparation guidance, see Preparing your product for AWS Marketplace in the next section of this guide.
