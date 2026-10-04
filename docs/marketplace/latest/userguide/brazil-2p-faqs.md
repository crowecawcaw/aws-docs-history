

# Brazil 2P FAQs
<a name="brazil-2p-faqs"></a>

The following frequently asked questions provide more information about selling through the AWS Brazil 2P distribution program.

**Topics**
+ [Why is the AWS Brazil 2P Distribution Program automated?](#brazil-2p-faq-automation)
+ [How do I agree to the seller terms and conditions of the AWS Brazil 2P Distribution Program?](#brazil-2p-faq-legal-terms)
+ [What are the prerequisites to participate in the AWS Brazil 2P Distribution Program?](#brazil-2p-faq-prerequisites)
+ [How do I enroll in the AWS ISV Accelerate program?](#brazil-2p-faq-enroll-isv)
+ [How do payments and taxes work?](#brazil-2p-faq-payments-taxes)
+ [What are the ISV fees associated with transacting through the AWS Brazil 2P Distribution Program?](#brazil-2p-faq-isv-fees)
+ [Who determines the customer's end price?](#brazil-2p-faq-end-price)
+ [What documents do I receive?](#brazil-2p-faq-documents)
+ [How do I know the disbursement status of a transaction?](#brazil-2p-faq-disbursement-status)
+ [How do refunds and cancellations work?](#brazil-2p-faq-refunds)
+ [Is there a deal threshold for Brazil 2P transactions?](#brazil-2p-faq-deal-threshold)
+ [Can channel partners be included in a Brazil 2P transaction?](#brazil-2p-faq-channel-partners)
+ [I am already transacting through the AWS Brazil 2P beta program. What changes for me?](#brazil-2p-faq-beta-migration)

## Why is the AWS Brazil 2P Distribution Program automated?
<a name="brazil-2p-faq-automation"></a>

Automation replaces manual processing with a standardized workflow. Specifically:
+ Distribution authorizations are created, and private offers are accepted through an automated workflow instead of manual processing.
+ Disbursements, withholding income tax calculation, invoicing, and seller reporting are handled automatically for each transaction.
+ SaaS Contract, SaaS Contract with Consumption, and SaaS PAYG pricing models are supported through the automated workflow.

## How do I agree to the seller terms and conditions of the AWS Brazil 2P Distribution Program?
<a name="brazil-2p-faq-legal-terms"></a>

The seller terms and conditions of the AWS Brazil 2P Distribution Program are available [online](https://s3.amazonaws.com/aws-mp-rcmp/AWS-Brazil-2P-Distribution-Program-Seller-Terms.pdf) and govern your participation in the AWS Brazil 2P Distribution Program and any distribution authorizations you create.

## What are the prerequisites to participate in the AWS Brazil 2P Distribution Program?
<a name="brazil-2p-faq-prerequisites"></a>

The prerequisites to participate in the AWS Brazil 2P Distribution Program are:
+ You must transact through the 2P distribution program through a foreign (non-Brazilian) entity.
+ You are enrolled in the ISV Accelerate program.
+ You have a valid bank account configured for USD disbursements.

## How do I enroll in the AWS ISV Accelerate program?
<a name="brazil-2p-faq-enroll-isv"></a>

Enroll in the AWS ISV Accelerate program by joining the [AWS Partner Network](https://partnercentral.awspartner.com/partnercentral2/s/SelfRegister?pg=cp&pp=pp) and becoming [APN Customer Engagement (ACE)](https://aws.amazon.com/partners/programs/ace/) eligible. For more details on the eligibility requirements, see [AWS ISV Accelerate program](https://aws.amazon.com/partners/programs/isv-accelerate/#get-started).

## How do payments and taxes work?
<a name="brazil-2p-faq-payments-taxes"></a>

**Payment timeline**
+ Disbursement terms: Net 60 days from the invoice date.
+ Currency: All disbursements are in US dollars (USD).
+ Timing: Disbursements are initiated any day between the 27th day and the 60th day from the invoice date, as determined by AWS.

**Example payment timeline**
+ Aug 1: Brazilian customer accepts the offer from AWS Brazil, and AWS Brazil issues the buyer invoice in BRL.
+ Aug 1: Seller invoice generated (in USD).
+ Aug 1: ISV payable calculated (Authorization Price − IRRF).
+ Aug 28–Sept 30: Disbursement window is between (Aug 1 \+ 27 days) and (Aug 1 \+ 60 days). During this window, your payment is processed and disbursed to your registered bank account.

**Withholding income tax (IRRF)**
+ AWS Brazil calculates and withholds an income tax called the Imposto sobre a Renda Retido na Fonte (IRRF) at the time of seller disbursement.
+ **Standard rate (15%)**: Applies if your company is domiciled in a jurisdiction classified as a non-tax haven by Brazil.
+ **Higher rate (25%)**: Applies if your company is domiciled in a jurisdiction classified as a tax haven by Brazil.

**Your net payment**
+ Disbursement = Authorization Price − IRRF withholding.
+ Example: $100 Authorization Price, 15% IRRF, you receive $85. The $15 is remitted to the Brazilian tax authorities.
+ For tax-haven countries: $100 Authorization Price, 25% IRRF, you receive $75. The $25 is remitted to the Brazilian tax authorities.

**Invoicing**
+ A seller invoice is generated for each transaction, which you can retain for your home-country tax records.
+ Seller invoices are accessible from the Tax Portal in AWS Partner Central for download and record-keeping.

**Tax compliance**
+ Ensure your tax identity and bank details are correctly configured during seller registration.
+ Contact your tax advisor about withholding tax (WHT) credits in your home country.

## What are the ISV fees associated with transacting through the AWS Brazil 2P Distribution Program?
<a name="brazil-2p-faq-isv-fees"></a>

There is no AWS fee for ISVs to transact through the AWS Brazil 2P Distribution Program. AWS Brazil adds a margin to the cost the ISV specifies in the distribution authorization, and that combined amount is the price charged to the buyer.

## Who determines the customer's end price?
<a name="brazil-2p-faq-end-price"></a>

AWS Brazil determines the customer's end price. During private offer creation, AWS Brazil adds a margin of 6% (6.38% markup) for new transactions and a margin of 5% (5.26% markup) for renewals to the cost specified by the ISV in the distribution authorization to AWS Brazil. The private offer is in USD, but the customer is invoiced in BRL.

The private offer price is calculated using the following formula:

**Private Offer Price = ISV Price ÷ (1 − Margin %)**

Example – an ISV extends a $100 distribution authorization for a SaaS product to AWS Brazil:
+ New deal (6% margin): Private Offer Price = $100 ÷ (1 − 0.06) = $100 ÷ 0.94 = $106.38.
+ Renewal (5% margin): Private Offer Price = $100 ÷ (1 − 0.05) = $100 ÷ 0.95 = $105.26.

**Note**  
The 6% (new) and 5% (renewal) margins are current and subject to change.

## What documents do I receive?
<a name="brazil-2p-faq-documents"></a>
+ **Seller invoice**: An invoice is generated and issued under your name for each transaction, accessible from the **Tax details** page on AWS Partner Central. For consumption or overages transactions, a monthly invoice is generated based on the usage.
+ **Seller reporting**: Reporting through the Seller Insights dashboard, showing transaction details, WHT amounts, authorization IDs, and payment status.
+ **WHT confirmation letter**: If you require additional documentation to substantiate that WHT deductions were performed, contact your Partner Development Manager to request a WHT confirmation letter. Because of IRRF filing timelines, this letter is only available after AWS Brazil completes its annual IRRF filing with the Brazilian Federal Revenue, typically by February of the following calendar year.

## How do I know the disbursement status of a transaction?
<a name="brazil-2p-faq-disbursement-status"></a>

You can track disbursement status in both the **Billed Revenue** dashboard and the **Collections and Disbursements** dashboard in AWS Partner Central. The **Disbursement status** column shows one of the following for each transaction:
+ Disbursed – AWS has paid the full amount to your bank account.
+ Failed – the disbursement attempt did not succeed.
+ Not disbursed – no funds have been disbursed yet.

For each transaction, the **Disbursement date** shows when AWS initiated the payment, and the **Disburse bank trace ID** lets you correlate your bank's deposit notifications with invoices in your AWS Marketplace reports. Your disbursement is made within 60 days from the disbursement invoice creation date and is independent of when the buyer pays AWS Brazil.

## How do refunds and cancellations work?
<a name="brazil-2p-faq-refunds"></a>

You cannot issue refunds or cancel agreements directly. The buyer must request a refund from the AWS Customer Service team, and each request is evaluated on a case-by-case basis. If approved, refunds or cancellations are implemented as determined by AWS. For more information, see [Refunds and cancellations in AWS Marketplace](refunds.md).

## Is there a deal threshold for Brazil 2P transactions?
<a name="brazil-2p-faq-deal-threshold"></a>

No. Brazil 2P transactions have no minimum deal size or threshold – any deal value is eligible.

## Can channel partners be included in a Brazil 2P transaction?
<a name="brazil-2p-faq-channel-partners"></a>

No. Channel partners cannot currently be included in Brazil 2P transactions.

## I am already transacting through the AWS Brazil 2P beta program. What changes for me?
<a name="brazil-2p-faq-beta-migration"></a>

All current 2P participants can start using the new automated workflow after the launch. AWS will share additional information regarding existing transactions and migration options in future communications.