

# Getting started as a seller through Brazil 2P
<a name="brazil-2p-getting-started"></a>

The AWS Brazil 2P distribution program enables AWS Brazil (Amazon AWS Serviços Brasil Ltda.) to distribute your eligible AWS Marketplace SaaS product licenses to buyers in Brazil. To participate, you must be a foreign (non-Brazilian) seller. Under this program, AWS Brazil is the seller of record, acquiring the rights to distribute SaaS product licenses to the end buyer. AWS Brazil issues invoices in Brazilian reais (BRL) that include the applicable Brazilian taxes (COFINS, ISS, and PIS). This gives Brazilian customers a localized purchasing experience.

## Key benefits
<a name="brazil-2p-key-benefits"></a>
+ Reach buyers in Brazil with local, BRL-denominated invoicing, without setting up a local entity – AWS Brazil distributes your eligible SaaS product licenses through an automated program.
+ AWS Brazil invoices buyers in Brazilian reais (BRL), with applicable Brazilian taxes (COFINS, ISS, and PIS) included on the invoice.
+ Price your distribution authorization in USD, while AWS Brazil handles invoicing and tax collection for buyers in Brazil.

**Important considerations**
+ AWS Brazil is the seller of record to the end buyer.
+ Payments to ISVs are subject to withholding tax on Brazil 2P transactions.
+ There are no ISV AWS listing fees to transact through the 2P distribution program. Instead, AWS Brazil adds a margin of 6% (new) and 5% (renewals) to the buyer's cost.
+ Currently, channel partners cannot be included in the 2P distribution program.

## Eligible products and pricing models
<a name="brazil-2p-eligible-products"></a>

The following pricing models are supported in the Brazil 2P distribution program:
+ SaaS Contract
+ SaaS Contract with Consumption
+ SaaS pay-as-you-go (PAYG)

**Note**  
Amazon Machine Image (AMI) products, container products, and professional services products are not eligible to transact through the Brazil 2P distribution program.

## Pricing and currency
<a name="brazil-2p-pricing-currency"></a>

The following pricing and currency details apply to the Brazil 2P distribution program:
+ Your distribution authorization to AWS Brazil is displayed in US dollars (USD). AWS Brazil prices the private offer in USD to the end buyer, which is invoiced in Brazilian reais (BRL), converted from USD to BRL at the time of invoice generation.
+ The BRL amount is calculated using the Oanda exchange rate on the invoice creation date.
+ For multi-year contracts and Consumption or PAYG products, each invoice uses the exchange rate in effect on the date that the invoice is created.

## Registration process to sell through the AWS Brazil 2P program
<a name="brazil-2p-registration"></a>

To authorize AWS Brazil to distribute your eligible SaaS products to buyers in Brazil through the AWS Brazil 2P distribution program, complete the following steps.

### Step 1: Confirm program eligibility
<a name="brazil-2p-step-1"></a>

Confirm that your product uses a pricing model supported by the Brazil 2P program: SaaS Contract, SaaS Contract with Consumption, or SaaS pay-as-you-go (PAYG). Amazon Machine Image (AMI), container, and professional services products are not eligible. You must transact through a foreign (non-Brazilian) entity and be enrolled in the [AWS ISV Accelerate program](https://aws.amazon.com/partners/programs/isv-accelerate/#get-started).

### Step 2: Complete seller registration on AWS Partner Central
<a name="brazil-2p-step-2"></a>

To participate in the Brazil 2P program, you must be a non-Brazilian seller with an AWS account. If you are not already a registered AWS Marketplace seller, complete seller registration in AWS Partner Central. For general seller registration guidance, see [Getting started as an AWS Marketplace seller](https://docs.aws.amazon.com/marketplace/latest/userguide/user-guide-for-sellers.html).

**Note**  
Brazil 2P does not use tax inheritance. If your account is part of an AWS Organization, it does not inherit tax settings from the management account for Brazil 2P transactions. The account that agrees to the "2P Distribution Program Seller Terms" during distribution authorization creation is the account that receives payments for the rights granted to AWS Brazil to distribute SaaS product licenses locally to Brazilian customers.

### Step 3: Provide bank account information
<a name="brazil-2p-step-3"></a>

The AWS Brazil 2P program supports disbursements in US dollars (USD) only, so you must add a bank account that can receive USD. You can add either an ACH or a SWIFT bank account. For more information, see [Providing your bank account information](https://docs.aws.amazon.com/marketplace/latest/userguide/provide-bank-information.html).

### Step 4: Add disbursement method
<a name="brazil-2p-step-4"></a>

After you provide your bank account information, set up a disbursement preference for the USD currency and associate it with your bank account. For more information, see [Step 4: Set disbursement preferences](set-disbursement-preferences.md).

### Step 5: Service-linked role (SLR) creation
<a name="brazil-2p-step-5"></a>

For ISVs participating in the AWS Brazil distribution program, a one-time configuration is required before you initiate any offers.

To create a selling authorization service-linked role:
+ Sign in to AWS Partner Central using your AWS Marketplace seller account.
+ Go to **Marketplace Settings**.
+ Select **Service linked roles**.
+ Choose **Create service-linked role**.
+ The portal updates the status to show that the role is created.

### Step 6: Agree to the AWS Brazil 2P Distribution Program seller terms and create a distribution authorization to the AWS Brazil account
<a name="brazil-2p-step-6"></a>

Agree to the AWS Brazil 2P Distribution Program seller terms and create a distribution authorization to the AWS Brazil account (664418980131) to grant rights to AWS Brazil and authorize this entity to distribute your eligible SaaS product licenses to buyers in Brazil as the seller of record.
+ From the **Selling authorization** menu in AWS Partner Central, choose **Create authorization**.
+ Provide the authorization name and select the SaaS product you want to sell.
+ Under **Recipient information**, select **Distributor**, and enter the AWS Brazil distributor account number 664418980131.
+ Choose **Next**. A pop-up appears with a link to the [AWS Brazil 2P distribution program seller terms](https://s3.amazonaws.com/aws-mp-rcmp/AWS-Brazil-2P-Distribution-Program-Seller-Terms.pdf) and a notice that disbursements are subject to withholding tax as required by Brazilian tax law. You must acknowledge both before proceeding to extend a distribution authorization to the AWS Brazil distributor.
+ After you accept these terms, create the distribution authorization by providing the following details:
  + Product pricing
  + Contract duration
  + Product dimensions
  + Buyer installment plan (if applicable)
  + Authorization availability
  + Buyer account ID

You can also create the distribution authorization to AWS Brazil through the [AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace/latest/developerguide/work-with-resale-authorizations.html).

**Note**  
A distribution authorization created for AWS Brazil is single use and can target only one buyer. You can upload a custom end user license agreement (EULA) or select the public EULA, which is passed on to the end customer.

## Taxes
<a name="brazil-2p-taxes"></a>

AWS Brazil calculates and withholds an income tax called the Imposto sobre a Renda Retido na Fonte (IRRF) before disbursement. The rate depends on your company's domicile:
+ **Standard rate (15%)**: Applies if your company is domiciled in a jurisdiction classified as a non-tax haven by Brazil.
+ **Higher rate (25%)**: Applies if your company is domiciled in a jurisdiction classified as a tax haven by Brazil.

## Invoicing
<a name="brazil-2p-invoicing"></a>

A seller disbursement invoice is generated for each transaction, issued under your name and business details, and accessible from the **Tax details** page in AWS Partner Central. Disbursements are paid in US dollars (USD) to your registered bank account.

To retrieve a disbursement invoice:
+ Go to the **Tax details** menu in AWS Partner Central.
+ Select the **Disbursement invoices (2P)** tab, which lists all your seller disbursement invoices for the Brazil 2P program.
+ Search using the offer ID or invoice ID. Filter by date and invoice type.

## Refunds
<a name="brazil-2p-refunds"></a>

You cannot issue refunds or cancel agreements directly. The buyer must request a refund from the AWS Customer Service team, and each request is evaluated on a case-by-case basis. If approved, refunds or cancellations are implemented as determined by AWS. For more information, see [Refunds and cancellations in AWS Marketplace](refunds.md).

## Notifications
<a name="brazil-2p-notifications"></a>

As a seller in the AWS Brazil 2P program, you receive a notification at each of the following events:
+ Each time you create a distribution authorization to AWS Brazil.
+ When the AWS Brazil distributor creates a private offer to the end customer based on your distribution authorization.
+ When the end customer accepts the private offer.

You can receive these notifications either through email or through Amazon EventBridge. For more information, see [Seller notifications for AWS Marketplace events](notifications.md).

## Seller reporting
<a name="brazil-2p-seller-reporting"></a>

You can track your AWS Brazil 2P transactions through the Seller Insights dashboards and data feeds in AWS Partner Central. Because Brazil 2P is a distribution motion, each transaction reports across the existing distribution and wholesale columns.

ISVs participating in the Brazil 2P distribution program can track transactions using the following columns in the **Billed Revenue** dashboard and the **Collections and Disbursements** dashboard:


| Column | Description | 
| --- | --- | 
| Gross revenue | The total invoice amount billed for the product's usage or monthly fees on the sale from the ISV to AWS Brazil. | 
| Seller net revenue | The amount being disbursed to the ISV. | 
| Distribution AWS tax share | The tax on the sale between the ISV and the distributor where AWS is tax liable, such as withholding tax deducted from the amount paid to the ISV. For all other transactions, this field is 0. | 
| AWS seller of record | For Brazil 2P, this displays Amazon AWS Serviços Brasil Ltda. | 
| Distribution invoice ID | The AWS ID assigned to the invoice representing the sale between the ISV and the distributor. If more than one distribution invoice applies, the IDs are separated by commas. For all other transactions, this field is not applicable. | 
| Distribution invoice date | The date of the distribution invoice. This field is empty for transactions without a distribution invoice. | 
| Distribution invoice due date | The payment due date of the distribution invoice. This field is empty for transactions without a distribution invoice. | 
| Disbursement status | The status indicates whether AWS has disbursed no funds, partial funds, or all funds to your bank account. Possible statuses: Disbursed, Partially disbursed, Failed, Not disbursed. | 
| Disbursement date | The date AWS initiated the disbursement to the seller's bank. | 
| Disburse bank trace ID | The trace ID assigned by the bank for disbursement. Use it to correlate your bank's deposit notifications and reports to invoices in AWS Marketplace reports. | 

For more information, see [Seller reporting](https://docs.aws.amazon.com/marketplace/latest/userguide/billed-revenue-dashboard.html).