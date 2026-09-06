

# Coupa connector for Amazon AppFlow
<a name="connectors-coupa"></a>

Coupa is a business spend software as a service (SaaS) solution. If you’re a Coupa user, your account contains data on procurements, invoicing, expenses, payments, and more. You can use Amazon AppFlow to transfer data between Coupa and certain AWS services or other supported applications.

## Amazon AppFlow support for Coupa
<a name="coupa-support"></a>

Amazon AppFlow supports Coupa as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Coupa.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Coupa.

## Before you begin
<a name="coupa-prereqs"></a>

To use Amazon AppFlow to transfer data from Coupa to supported destinations, you must meet these requirements:
+ You have an account with Coupa that contains the data that you want to transfer. For more information about the Coupa data objects that Amazon AppFlow supports, see [Supported objects](#coupa-objects).
+ In your Amazon AppFlow account, you've created an OAuth2/OIDC client app for Amazon AppFlow. The app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. 

  For information about how to create an OAuth2 client app, see [OAuth 2.0 Getting Started with Coupa API ](https://compass.coupa.com/en-us/products/core-platform/integration-playbooks-and-resources/integration-knowledge-articles/oauth-2.0-getting-started-with-coupa-api) in the *Coupa Compass*.
+ You've given your app a Grant type of Client Credentials. 
+ You've chosen the following scopes to be included in the API: 
  + `core.accounting.read`
  + `core.approval.read`
  + `core.common.read`
  + `core.easyform_response.read`
  + `core.expense.read`
  + `core.integration.read`
  + `core.inventory.adjustment.read`
  + `core.inventory.asn.read`
  + `core.inventory.balance.read`
  + `core.inventory.consumption.read`
  + `core.inventory.cycle_counts.read`
  + `core.inventory.receiving.read`
  + `core.inventory.return_to_supplier.read`
  + `core.inventory.transfer. read`
  + `core.invoice.read`
  + `core.item.read`
  + `core.legal_entity.read`
  + `core.pay.charges.read`
  + `core.pay.payment_accounts.read`
  + `core.pay.payments.read`
  + `core.pay.virtual_cards.read`
  + `core.payables.allocations.read`
  + `core.payables.expense.read`
  + `core.payables.external.read"`
  + `core.payables.invoice.read`
  + `core.payables.order.read`
  + `core.project.read`
  + `core.purchase_order. read`
  + `core.requisition.read`
  + `core.sourcing.pending_supplier.read`
  + `core.sourcing.read`
  + `core.sourcing.response.read`
  + `core.supplier.read`
  + `core.supplier_information_sites.read`
  + `core.supplier_information_tax registrations.read`
  + `core.supplier_sharing_settings.read`
  + `core.supplier_sites.read`
  + `core.uom.read`
  + `core.user.read`
  + `core.user_group.read`
  + `email login offline_access openid profile`
  + `travel_booking.common.read`
  + `travel_booking.team.read`
  + `travel_booking.trip.read`
  + `travel_booking.user.read`
  + `treasury.cash_management.read`

Note the client ID, client secret, and instance URL for your Coupa project.

## Connecting Amazon AppFlow to your Coupa account
<a name="coupa-connecting"></a>

To connect Amazon AppFlow to your Coupa account, provide details from your Coupa project so that Amazon AppFlow can access your data. If you haven't yet configured your Coupa project for Amazon AppFlow integration, see [Before you begin](#coupa-prereqs).

**To connect to Coupa**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Coupa**.

1. Choose **Create connection**.

1. In the **Connect to Coupa** window, enter the following information:
   + **Connection name** — A name for the connection.
   + **Authorization tokens URL** — From the dropdown menu, choose one of the following options: For partner and demo instances, choose https://\\{company\_name}.coupacloud.com.oauth2/token. For customer instances, choose https://\\{company\_name}.coupahost.com.oauth2/token. 
   + **Custom authorization tokens URL** — The same company name used in the authorization tokens URL.
   + **Client ID** — The client ID in your Coupa project.
   + **Client secret** — The client secret in your Coupa project. 
   + **Instance URL** — The instance URL of your Coupa project. For example, https://{company\_name}.coupacloud.com (for partner and demo instances), or https://{company\_name}.coupahost.com (for customer instances).

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your Coupa account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Coupa as the data source, you can select this connection.

## Transferring data from Coupa with a flow
<a name="coupa-transfer-data"></a>

To transfer data from Coupa, create an Amazon AppFlow flow, and choose Coupa as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Coupa, see [Supported objects](#coupa-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#coupa-destinations).

## Supported destinations
<a name="coupa-destinations"></a>

When you create a flow that uses Coupa as the data source, you can set the destination to any of the following connectors: 
+ [Amazon Lookout for Metrics](lookout.md)
+ [Amazon Redshift](redshift.md)
+ [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md)
+ [Amazon S3](s3.md)
+ [HubSpot](connectors-hubspot.md)
+ [Marketo](marketo.md)
+ [Salesforce](salesforce.md)
+ [SAP OData](sapodata.md)
+ [Snowflake](snowflake.md)
+ [Upsolver](upsolver.md)
+ [Zendesk](zendesk.md)
+ [Zoho CRM](connectors-zoho-crm.md)

## Supported objects
<a name="coupa-objects"></a>

When you create a flow that uses Coupa as the data source, you can transfer any of the following data objects to supported destinations:



- ** Approval**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Charge**
  - **** Field**:** account-type-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** accounting-currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** accounting-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** card-provider-account / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** charge-allocations / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** charge-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** charge-tax-lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** coupa-pay-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** coupa-pay-statement-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** document-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** document-type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** expense-holding-account / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** exported / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** external-ref-id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** holding-account / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** issuer-bank / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** issuer-reconciliation-id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** last-exported-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** mcc / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** merchant-currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** merchant-reference / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** merchant-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** order-header-currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order-header-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** order-header-number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order-header-total / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment-partner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** posting-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** statement / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** statement-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** statement-name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** supplier / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** supplier-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supplier-name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tax-currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** tax-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** updated-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** virtual-card / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** virtual-card-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO

- ** Expense Report**
  - **** Field**:** approvals / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** art-der-ausgabe / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** audit-score / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** auditor-note / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** comments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** created-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** end-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, BETWEEN, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** events / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** expense-lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** expense-policy-violations / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** expense-report-preapprovals / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** expensed-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** exported / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** external-src-name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** external-src-ref / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** is-trip / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** last-exported-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, BETWEEN, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** paid / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** past-due / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** payment / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payment-channel / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** reconciliation-lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** reimbursable-total-amount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** reimbursable-total-currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** reject-reason / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** report-due-date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** report-warnings / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** start-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, BETWEEN, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** submitted-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** submitted-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** total / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** travel-trip / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** type-de-note-de-frais / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** type-of-expense / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated-by / **** Data type**:** Struct / **** Supported filters**:** 

- ** Invoice**
  - **** Field**:** abandon-reason / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** account-type / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** advance-payment-received-amount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** amount-due / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** amount-due-less-discount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** amount-of-advance-payment / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** approvals / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** archive-entity-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** attachments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** bill-to-address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** buyer-tax-registration / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** canceled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** cash-accounting-scheme-reference / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** cash-register-operator / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** channel / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** clearance-document / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** comments / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** compliant / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** confirmation / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** content-validation / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** contract / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** correct-value-of-supply / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** coupa-accelerate-status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** credit-note-differences-with-original-invoice / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** credit-reason / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** currency-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** current-integration-history-records / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** custom-fields / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** customer-accounting-tax / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** customer-accounting-tax-less-discount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** customs-declaration-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** customs-declaration-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** customs-office / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** date-of-discovery-of-facts-decisive-for-correction / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** date-received / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** delivery-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** delivery-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** destination-country / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** discount-amount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** discount-due-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** discount-percent / **** Data type**:** Float / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** dispute-method / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** dispute-reasons / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** document-type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** early-payment-provisions / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** endorsement-on-invoices / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** exchange-rate / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** exported / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** failed-tolerances / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** folio-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** form-of-payment / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** freight-type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** gross-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** gross-total-less-discount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** handling-amount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** image-scan / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** image-scan-content-type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** image-scan-file-name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** image-scan-file-size / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** image-scan-url / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** inbound-invoice / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** inbox-name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** internal-note / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** invoice-charges / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** invoice-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** invoice-from-address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** invoice-issuance-time / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice-lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** invoice-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** invoice-payment-receipts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** invoice-reference-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** is-credit-note / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** issuance-place / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** last-exported-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** late-payment-penalties / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** legal-destination-country / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** line-count / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** line-level-taxation / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** lock-version-key / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** margin-scheme / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** means-of-payment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** misc-amount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** municipal-tax-number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** national-enrollment-of-conveyor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** nature-of-operation / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** net-due-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** net-total-less-discount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** new-means-of-transport / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** origin-country / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** origin-currency-gross / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** origin-currency-net / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** original-invoice-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** original-invoice-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** original-value-of-supply / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** paid / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** pay-invoice / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payment-agreement-notes / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** payment-channel / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** payment-date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** payment-method / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** payment-notes / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** payment-order-number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment-order-reference / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** payment-term / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** place-of-issuance / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** place-of-supply / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** pre-payment-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** protocol-number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** reconciliation-lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** remit-to-address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** requested-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** requester-email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** requester-lookup-name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** requester-name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** resolution-number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** reverse-charge-reference / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** security-code-of-issuer / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** self-billing-reference / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** sender-email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** serial-code-of-fiscal-invoice / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** series / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** ship-from-address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ship-to-address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** shipping-amount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** shipping-term / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** show-tax-information / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** signed-qr-code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** spend-load-id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** split-payment-mechanism / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** state-tax-number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** state-tax-number-for-substitute-taxpayer / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supplier / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** supplier-created / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** supplier-invoice-issuer-name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supplier-invoice-reviewer-name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supplier-note / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supplier-payment-collector-name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supplier-remit-to / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** supplier-tax-registration / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** supplier-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** taggings / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** tax-amount / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** tax-amount-engine / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** tax-code / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** tax-code-engine / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tax-due-to-supplier / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** tax-lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** tax-rate / **** Data type**:** Float / **** Supported filters**:** 
  - **** Field**:** tax-rate-engine / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** taxes-in-origin-country-currency / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** tcs-tax-lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** tolerance-failures / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** total-taxes-less-discount / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** total-with-taxes / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** transaction-notification-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** transaction-uuid / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** type-of-document / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type-of-operation / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type-of-receipt / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** type-of-relationship / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** unique-identification-code-of-cash-receipt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updated-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** use-of-invoice / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** vehicle-license-plate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** verification-code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** volume-amount / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** volume-brand / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** volume-gross-weight / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** volume-liquid-weight / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** volume-numbering / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** volume-type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** withholding-tax-lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** withholding-tax-override / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO

- ** Payment**
  - **** Field**:** created-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, BETWEEN
  - **** Field**:** created-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS
  - **** Field**:** digital-check / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** error-text / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS
  - **** Field**:** estimated-pay-from-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** exchange-rate / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS
  - **** Field**:** exported / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** external-ref-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** last-exported-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, BETWEEN
  - **** Field**:** line-num / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** pay-from-account / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** pay-from-currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** pay-from-external-gl-account / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** pay-from-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** pay-to-account / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** pay-to-currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** pay-to-external-gl-account / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** pay-to-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** payee / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payment-batch / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payment-batch-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** payment-details / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** payment-identifier / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS
  - **** Field**:** released-at / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** reporting-currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** reporting-pay-from-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** reporting-pay-to-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** source-name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS
  - **** Field**:** source-reference / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS
  - **** Field**:** updated-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, BETWEEN
  - **** Field**:** updated-by / **** Data type**:** Struct / **** Supported filters**:** 

- ** Purchase Order**
  - **** Field**:** acknowledged-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** acknowledged-flag / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** attachments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** change-type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** classification / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** confirm-by-hrs / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** coupa-accelerate-status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** current-integration-history-records / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** custom-fields / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** exported / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** hide-price / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** internal-revision / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** invoice-stop / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** last-exported-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** milestones / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** order-confirmation-level / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** payment-method / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** payment-term / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** pcard / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** po-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** price-hidden / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** reason-insight-events / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** recurring-rules / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** requester / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ship-to-address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ship-to-attention / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** ship-to-user / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** shipping-term / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** spend-load-id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supplier / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** supplier-site / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** transmission-emails / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** transmission-method-override / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** transmission-status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updated-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** user-group-members / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** user-members / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** version / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO

- ** Purchase Order Line**
  - **** Field**:** account / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** account-allocations / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** accounting-total / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** accounting-total-currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** amount-components / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** asset-tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** attachments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** bulk-price / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** commodity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** contract / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** created-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** custom-fields / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** department / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** easy-form-response-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** external-reference-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** external-reference-type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** extra-line-attribute / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** form-response / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** invoice-stop / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** invoiced / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** item / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** line-num / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** line-owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** manufacturer-name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** manufacturer-part-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** match-type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** milestones / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** minimum-order-quantity / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** need-by-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** order-header-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** order-header-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** order-increment / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** order-line-tax-detail / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** period / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** price / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** quantity / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** receipt-approval-required / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** receipt-required / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** received / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** receiving-warehouse / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** recurring-rules / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** reporting-total / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** requester / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** requisition-line-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** rfq-easy-form-response-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** rfq-form-response / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** savings-pct / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** service-type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** source-part-num / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** spend-load-id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** sub-line-num / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supp-aux-part-num / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supplier / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** supplier-order-number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** supplier-site-id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** third\_party\_supplier / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** total / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** uom / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** updated-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** version / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO

- ** Receipt**
  - **** Field**:** account / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** account-allocations / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** adjustment-code / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** asn-header / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** asn-line / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** asset-tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** attachments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** barcode / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** comments / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** current-integration-history-records / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** exported / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** from-warehouse / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** from-warehouse-location / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** inspection-code / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** inventory-transaction-lots / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** inventory-transaction-valuations / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** item / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** last-exported-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** match-reference / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** order-line / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** original-transaction / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** original-transaction-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** price / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** quantity / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** reason-insight / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** receipt / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** receipts-batch-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** received-weight / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** receiving-form-response / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** rfid-tag / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** soft-close-for-receiving / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** spend-load-id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** to-warehouse / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** to-warehouse-location / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** total / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** transaction-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** uom / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** updated-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** voided-value / **** Data type**:** BigDecimal / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO

- ** Requisition**
  - **** Field**:** approvals / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** approver / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** attachments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** buyer-note / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** current-approval / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** custom-fields / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** department / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** exported / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** external-po-reference / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** hide-price / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** justification / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** line-count / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** milestones / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** mobile-currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** mobile-total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** need-by-date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** pcard / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** price-hidden / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** receiving-warehouse-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** recurring-rules / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** reject-reason-comment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** req-title / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** requested-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** requester / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ship-to-address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ship-to-attention / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** spend-load-id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** submitted-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** taggings / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** updated-at / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** updated-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** user-group-members / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** user-members / **** Data type**:** List / **** Supported filters**:** 

- ** Requisition Line**
  - **** Field**:** account / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** account-allocations / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** alternate-status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** asset-tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** attachments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** commodity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** confirm-by-hrs / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** contract / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** created-at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** created-by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** easy-form-response-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** extra-line-attribute / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** form-response / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** image-url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** item / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** line-num / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** line-owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** line-type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** manufacturer-name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** manufacturer-part-number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** milestones / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** minimum-order-quantity / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** need-by-date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** order-confirmation-level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order-increment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order-line-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** order-pad-line / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payment-term / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** period / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** punchout-site / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** quantity / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** realtime-extension / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** receipt-required / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** recurring-rules / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** requisition-line-tax-detail / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** requisition\_id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** service-type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** shipping-term / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source-details / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source-part-num / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source-type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** spend-load-id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** sub-line-num / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** supp-aux-part-num / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** supplier / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** supplier-site / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** supplier-site-id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** taggings / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** total / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** transmission-emails / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** transmission-method-override / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** unit-price / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** unit-price-in-usd / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** unspsc-code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** uom / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** updated-at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** updated-by / **** Data type**:** Struct / **** Supported filters**:** 

- ** Supplier Information**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

