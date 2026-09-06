

# Transfer billing management to external accounts
<a name="orgs_transfer_billing"></a>

Billing transfer allows a management account to designate an account external to its organization to manage and pay for its consolidated bill. To set up billing transfer, an external account *(bill-transfer account)* sends a billing transfer invitation to a management account *(bill-source account)*. If accepted, the external account becomes the *bill-transfer account*, managing and paying for the *bill-source account's* consolidated bill, starting on the date specified in the invitation.

**Topics**
+ [Terms and concepts](#orgs_transfer_billing-concepts)
+ [Considerations](#orgs_transfer_billing-considerations)
+ [Important impacts](#orgs_transfer_billing-impacts)
+ [How billing transfer works](#orgs_transfer_billing-how-it-works)
+ [Sending invitations](orgs_transfer_billing-send-invitation.md)
+ [Viewing invitations](orgs_transfer_billing-view-invitation.md)
+ [Canceling invitations](orgs_transfer_billing-cancel-invitation.md)
+ [Responding to invitations](orgs_transfer_billing-respond-invitation.md)
+ [Viewing transfers](orgs_transfer_billing-view-transfer.md)
+ [Updating transfers](orgs_transfer_billing-update-transfer.md)
+ [Withdrawing transfers](orgs_transfer_billing-stop-transfer.md)
+ [Viewing Billing and Cost Management data as a Bill Transfer account](orgs_transfer_billing-view-account.md)
+ [Quotas](orgs_transfer_billing-quotas.md)
+ [Best practices](orgs_transfer_billing-best-practices.md)

## Terms and concepts
<a name="orgs_transfer_billing-concepts"></a>

**Management account**  <a name="tb-management-account"></a>
The *management account* is the account that created and owns an organization. For more information, see [AWS Organizations terminology and concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organization-structure).

**Payer account**  <a name="tb-payer-account"></a>
A *payer account* is the account that generates, manages and pays for a consolidated bill.

**Bill-Transfer Account**  <a name="tb-bill-transfer-account"></a>
A *bill-transfer account* is a management account designated to manage and pay for the consolidated bill of another management account.

**Bill-Source Account**  <a name="tb-bill-source-account"></a>
A *bill-source account* is an account that generates a consolidated bill.

**Billing transfer invitation**  <a name="tb-transfer-billing-invitation"></a>
A *billing transfer invitation* is a request for the recipient to designate the sender's account as their *bill-transfer account*.

**Billing transfer**  <a name="tb-transfer-billing"></a>
A *billing transfer* is an arrangement between two management accounts where one management account manages and pays for the consolidated bill of the other management account, and member accounts under it.

## Considerations
<a name="orgs_transfer_billing-considerations"></a>

**Only management accounts can send invitations**

Invitations can only be sent between management accounts.

**Invitations are unidirectional**

Only the account that will manage and pay for the consolidated bill (bill-transfer account) can send invitations. Bill-source accounts cannot send invitations asking other accounts to manage and pay for their consolidated bill.

**Invitations must be accepted before the billing transfer effective start date**

Invites must be accepted 24 hours before the start date of the billing transfer, in UTC time. The start date is the first day of the month specified in the invitation. For example, invites with a start date of Feb 1st must be accepted by Jan 30th 7PM EST.

**Withdrawal can be done by either management account in a transfer**

Either management account involved in a transfer can withdraw the transfer at any time.

**Transfer start and end dates align with the calendar month**

If an invitation is accepted, the start date is Midnight 00:00:00 UTC on the first day of the month specified in the invitation (for Eastern Standard Time this is 8:00 PM on the evening before the first day of the month).

If a transfer is withdrawn, the end date is 23:59:59 UTC on the last day of the current or next month (for Eastern Standard Time this is 7:59 PM on the evening before the last day of the month).

**Setting up Billing Transfer using console requires the use of AWS Billing Conductor**

AWS Billing Conductor enables the bill source accounts to view pro forma cost data configured by your account (bill transfer account). You will incur charges for the use of AWS Billing Conductor. If you don't use AWS Billing Conductor, you might configure Billing Transfer using API. We recommend you configure AWS Billing Conductor to ensure that the bill source accounts have access to the pro forma cost data. For more information, see [AWS Billing Conductor Pricing](https://aws.amazon.com/aws-cost-management/aws-billing-conductor/pricing/).

## Important impacts
<a name="orgs_transfer_billing-impacts"></a>

Review the following considerations and impact to the bill-source account before opting into to Billing Transfer.

**Loss of historical data access**  
After transition, historical cost data becomes unavailable in AWS Cost Explorer, AWS Budgets, and AWS Cost Anomaly Detection. Cost and budget forecasting tools require 36-60 days of new data for accurate forecasts. AWS Cost and Usage Report (CUR) files become unavailable.  
Recommended actions:  
- Download historical cost data and CUR files before transition  
- Configure a CUDOS dashboard to visualize historical data

**CUR reconfiguration requirement**  
After transfer, existing AWS Cost and Usage Report (CUR) configurations become inactive and display as `Unhealthy`.  
Recommended actions:  
- Reconfigure CUR preferences after transfer

**AWS Cost Anomaly Detection (CAD)**  
CAD is not supported for bill-source accounts. As a bill-source account, existing monitors and newly created monitors won't generate alerts.  
Bill-transfer accounts also do not have access to CAD for bill-source account usage, but they can continue to use CAD for their own account (applicable only to two-level transfers).

**Pro forma billing limitations specific to Billing Transfer**  
Pro forma billing data might not match your final invoice from the billing entity because some pricing elements aren't yet supported. The following items don't appear in pro forma billing data: Support plan charges, AWS credits, AWS Free Tier usage (exclusively credits based free tier).  
The bill receiver can configure these items to appear in pro forma billing artifacts using AWS Billing Conductor. For more information, see the [Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html).

**Credit tracking restrictions**  
The bill source account cannot track credit balances on the **Credits** page in the Billing and Cost Management console. This affects your ability to predict end-of-month net spend.  
The bill source account cannot view AWS Credits in pro forma artifacts (AWS CUR, Cost Explorer, Bills page) bu default.  
The bill source account cannot view contractual credits in the **Credits** page (for example, MAP). Our recommendation: bill transfer account can explicitly model credits in the pro forma billing artifacts by using AWS Billing Conductor functionalities. For more information, see the [Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html).  
Contractual credits will continue to not be visible in the **Credits** page but will be visible in pro forma artifacts.

**Reserved Instance and Savings Plans recommendations**  
Savings recommendations are based on public pricing. While the recommended purchase amounts are accurate, the projected savings amounts might be higher than actual savings.

**Rightsizing recommendations**  
Bill source accounts can only access pre-discount recommendations. Post-discount recommendations aren't available for billing transfer users.  
Recommended action: Validate rightsizing recommendations against your existing Reserved Instance and Savings Plans inventory.

**Cost analysis restrictions**  
When you use Cost Explorer with a Bill Source account, you can view pro forma data with either daily or monthly granularity. Hourly granularity is not available in Cost Explorer for pro forma data. To analyze costs with hourly granularity, you can use AWS Cost and Usage Report (CUR).

**Cost categories and tags**  
Cost categories and cost allocation tags configured by the bill source account appear in the AWS Cost and Usage Report (CUR) that the bill receiver sets up.

## How billing transfer works
<a name="orgs_transfer_billing-how-it-works"></a>

Billing transfers begin with an invitation. An external account *(bill-transfer account)* sends a billing transfer invitation to another organization's management account *(bill-source account)*. The invitation includes the date when the *bill-transfer account* will start managing and paying for the *bill-source account's* consolidated bill. When sending the invitation, the bill transfer account must select the pricing configuration that calculates cloud costs allocated to bill source accounts for chargeback or showback purposes. The bill transfer account can choose from two Billing Conductor pricing configurations: Billing Conductor base pricing, and existing custom pricing.

For more information about pricing configuration, see [AWS Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html).

The *bill-source account* receives an email notification. If the invitation is accepted, the *bill-transfer account* becomes designated to manage and pay for the *bill-source account's* consolidated bill, beginning on the start date specified in the invitation.

When the transfer begins, the bill transfer account:
+ Receives distinct AWS invoices (for example, distinct consolidated bills) for charges from bill source accounts after the transfer becomes effective. These appear only in the bill transfer account. For more information, see [What is AWS Billing and Cost Management?](billing-what-is.md).
+ Controls the cost data visible to the bill source account in the Billing and Cost Management console, using Billing Conductor.
+ Gains access to two billing transfer views for each bill source account:

  - My view: Shows the billing data that the bill transfer account is financially responsible for.

  - Showback/chargeback view: Shows billing data configured through Billing Conductor for showback or chargeback purposes using Billing Conductor.

The bill transfer account can access these billing views in Cost Explorer, AWS Cost and Usage Report, Budgets, and Bills page.

**Note**  
As an AWS Partner, when a new account transfers its bill to your bill transfer account, you must configure a AWS Cost and Usage Report after the billing transfer starts (as specified in the invitation) and before the end of the billing cycle if you use the AWS Cost and Usage Report for customer chargebacks.

For more information, see the [AWS Cost Management User Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html).

When the transfer begins, the bill source account:
+ Remains responsible for paying any usage charges from before the transfer start date.
+ No longer receives AWS invoices for usage after the transfer start date, as these go to the bill transfer account.
+ No longer has access to billed cost data (priced by AWS).
+ The bill source account and its member accounts are added to a billing group, where they can view only their costs as priced by the bill transfer account (either gross of non-public discounts rates or custom rates) through Billing Conductor. The bill transfer account can view the consumption and billing metadata (such as cost categories and cost allocation tags) of bill source accounts in Cost Explorer and AWS Cost and Usage Report.

For more information about which Billing and Cost Management services will be available to the bill source accounts see [AWS services for accounts in billing groups](https://docs.aws.amazon.com/billingconductor/latest/userguide/service-integrations-support-proforma.html). For more information about billing groups see [Billing groups](https://docs.aws.amazon.com/billingconductor/latest/userguide/service-integrations-support-proforma.html).

Either account *(bill-source account* or *bill-transfer account)* can withdraw the billing transfer at any time.


| Transfer phase | Account designated to manage and pay for consolidated bills | 
| --- | --- | 
| When the transfer starts | + Consolidated bills for charges accrued before the start date are managed and paid for by the organization's own management account *(bill-source account)*.<br />+ Consolidated bills for charges accrued after the start date are managed and paid for by the *bill-transfer account*. | 
| When the transfer ends | + Consolidated bills for charges accrued between the start and end date are managed and paid for by the *bill-transfer account*.<br />+ Consolidated bills for charges accrued after the end date are managed and paid for by the organization's own management account *(bill-source account)*. | 

![Billing transfer flow showing management accounts, bill-transfer and bill-source accounts, consolidated bill, and pricing configuration.](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/images/transfer-billing-how-it-works.jpg)


*Figure 1: Diagram depicting how billing transfer works between two organizations.*

Billing transfer doesn't affect the computational boundary of each AWS Organizations that uses it. Volume discount tiers, Reserved Instances, and Savings Plans continue to be calculated and applied at the individual AWS Organizations level. For more information on Reserved Instances and Savings Plans for billing transfer users, see [Reserved Instances](ri-behavior.md) and [Calculating Costs with Savings Plans](con-bill-blended-rates.md#cb_calculating_sp).

### Two-level billing transfers
<a name="orgs_transfer_billing-two"></a>

Billing transfer supports two-level transfers for selected accounts. A bill transfer account can transfer its own bill and all its bill source account bills to an external management account (bill transfer receiver). This receiving account is responsible for paying bills from both the original bill source accounts and the intermediary bill transfer account, which becomes a bill source account when transferring its bill. For more information about two-level transfers, see [Quotas](orgs_transfer_billing-quotas.md).


**Table 1: Role description in one-level transfers**  

| Account role | Role description | 
| --- | --- | 
| Bill Source | Account that generates a consolidated bill and agrees to transfer its bill away to an external management account | 
| Bill Transfer | Account that receives and pays for the consolidated bill of the Bill Source account and the consolidated bill of its own account. This account also manages the pricing of cloud cost data visible to the Bill Source account, using AWS Billing Conductor. | 


**Table 2: Role description in two-levels transfers**  

| Account role | Role description | 
| --- | --- | 
| Bill Source | Account that generates a consolidated bill and agrees to transfer its bill away to an external management account | 
| Bill Transfer | This account further transfers its bill and the bills of the Bill Source accounts to another Bill Transfer account (Bill receiver). As a result, this account is a Bill Transfer account relative to the Bill Source accounts and it's a Bill Source account relative to the Bill Transfer account receiving the bill (Bill Receiver). This account also manages the pricing of cloud cost that is visible to the Bill Source accounts, using AWS Billing Conductor. | 
| Bill Transfer (bill receiver) | Account that receives and pays for the consolidated bill of the Bill Source accounts (including the Bill Transfer account) and the consolidated bill of its own account. This account also manages the pricing of cloud cost for all the Bill Source accounts (including the Bill Transfer account) using AWS Billing Conductor. Only the Bill Transfer accounts view the costs of the Bill Source accounts priced by the Bill Transfer (Bill Receiver) account, as the Bill Source accounts only view their costs priced by the Bill Transfer account. | 

**Note**  
The Bill Transfer (bill receiver) account doesn't send invitations to bill source accounts. The bill transfer sends the invitation. When a bill source account accepts, the bill receiver gets a CloudTrail notification and automatically assumes billing for the bill source accounts.
In two-level transfer configurations, the bill receiver must configure a billing group in the bill source accounts' organization using AWS Billing Conductor. This configuration enables the bill receiver to view allocated costs from bill source accounts. For AWS Partner Network (APN) Distribution program participants, this allows downstream sellers to track amounts owed to their distributor for end-customer usage. For help automating this configuration, contact Support.

**Important**  
As an AWS Partner, when a new account transfers its bill to your bill transfer account through either single-level or two-level transfer, you must configure a AWS Cost and Usage Report after the billing transfer starts (as specified in the invitation) and before the end of the billing cycle if you use the AWS Cost and Usage Report for customer chargebacks.

For more information, see [Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html).

### Related services
<a name="orgs_transfer_billing-related"></a>

#### AWS Billing and Cost Management
<a name="orgs_transfer_billing-AB"></a>

AWS Billing and Cost Management helps you set up billing, retrieve and pay invoices, and analyze, organize, plan, and optimize your costs. To get started, set up your billing preferences. For individuals or small organizations, AWS automatically charges your credit card. For larger organizations, you can use AWS Organizations to consolidate charges across multiple AWS accounts. You can then configure invoicing, tax, purchase order, and payment methods to match your organization's procurement processes.

You can allocate costs to teams, applications, or environments by using cost categories or cost allocation tags, or using Cost Explorer. You can also export data to your preferred data warehouse or business intelligence tool. For more information, see [What is AWS Billing and Cost Management?](billing-what-is.md).

#### Billing Conductor
<a name="orgs_transfer_billing-ABC"></a>

Billing Conductor is a custom billing service that supports showback and chargeback workflows for AWS Partners reselling AWS services and solutions, and AWS customers purchasing cloud services directly. You can create a customized version of your monthly billing data. The service models the billing relationship between you and your customers or business units. Billing Conductor doesn't change how AWS bills you each month. Instead, you can use it to configure, generate, and display rates for specific customers over a given billing period. You can also analyze the difference between the rates you apply to your groupings and the actual AWS rates for those accounts. With your Billing Conductor configuration, the management account can see the custom rate applied on the billing details page of the AWS Billing and Cost Management console. The management account can also configure AWS Cost and Usage Report per billing group.

When bill transfer account users sign in, Billing Conductor allows the management account of the AWS Organizations transferring their bills (bill source account) to view only their usage priced with rates from the bill transfer account.

For more information, see [Billing Conductor](https://docs.aws.amazon.com/billingconductor/latest/userguide/what-is-billingconductor.html).

#### Billing views
<a name="orgs_transfer_billing-billingviews"></a>

Billing view is a feature that helps you manage and control access to cost management data in your AWS environment. Billing view represents cost management data as an AWS resource. Through resource-based policies, you can configure which data is accessible when using AWS Billing and Cost Management tools. Each billing view has a unique Amazon Resource Name (ARN), which you can reference in identity-based policies to perform specific IAM actions on the cost management data in that billing view.

For more information, see [Controlling cost management data access with Billing View](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-view.html).

### Key benefits
<a name="orgs_transfer_billing-benefits"></a>

The key benefits of using billing transfer are:
+ **Separate billing and administration**: The management account that accepted the invitation maintains complete administration over its organization, while its consolidated bill is managed and paid for by the *bill-transfer account*.
+ **Pricing privacy**: After a transfer starts, the *bill-transfer account* manages the pricing seen by the *bill-source account* using [AWS Billing Conductor](https://docs.aws.amazon.com/aws-cost-management/aws-billing-conductor/).
+ **Centralized billing management**: The consolidated bills of multiple organizations can be managed and paid for from a single *bill-transfer account*.