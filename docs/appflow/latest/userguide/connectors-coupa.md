# Coupa connector for Amazon AppFlow

Coupa is a business spend software as a service (SaaS) solution. If you’re a
Coupa user, your account contains data on procurements, invoicing, expenses,
payments, and more. You can use Amazon AppFlow to transfer data between Coupa and certain
AWS services or other supported applications.

## Amazon AppFlow support for Coupa

Amazon AppFlow supports Coupa as follows.

**Supported as a data source?**

Yes. You can use Amazon AppFlow to transfer data from Coupa.

**Supported as a data destination?**

No. You can't use Amazon AppFlow to transfer data to Coupa.

## Before you begin

To use Amazon AppFlow to transfer data from Coupa to supported destinations, you must meet these
requirements:

- You have an account with Coupa that contains the data that you want to transfer. For more
  information about the Coupa data objects that Amazon AppFlow supports, see [Supported objects](#coupa-objects "#coupa-objects").
- In your Amazon AppFlow account, you've created an OAuth2/OIDC client app for Amazon AppFlow. The app
  provides the client credentials that Amazon AppFlow uses to access your data securely when it makes
  authenticated calls to your account.

For information about how to create an OAuth2 client app, see [OAuth 2.0 Getting Started with Coupa API](https://compass.coupa.com/en-us/products/core-platform/integration-playbooks-and-resources/integration-knowledge-articles/oauth-2.0-getting-started-with-coupa-api "https://compass.coupa.com/en-us/products/core-platform/integration-playbooks-and-resources/integration-knowledge-articles/oauth-2.0-getting-started-with-coupa-api") in the _Coupa
Compass_.

- You've given your app a Grant type of Client Credentials.
- You've chosen the following scopes to be included in the API:
  - `core.accounting.read`
  - `core.approval.read`
  - `core.common.read`
  - `core.easyform_response.read`
  - `core.expense.read`
  - `core.integration.read`
  - `core.inventory.adjustment.read`
  - `core.inventory.asn.read`
  - `core.inventory.balance.read`
  - `core.inventory.consumption.read`
  - `core.inventory.cycle_counts.read`
  - `core.inventory.receiving.read`
  - `core.inventory.return_to_supplier.read`
  - `core.inventory.transfer. read`
  - `core.invoice.read`
  - `core.item.read`
  - `core.legal_entity.read`
  - `core.pay.charges.read`
  - `core.pay.payment_accounts.read`
  - `core.pay.payments.read`
  - `core.pay.virtual_cards.read`
  - `core.payables.allocations.read`
  - `core.payables.expense.read`
  - `core.payables.external.read"`
  - `core.payables.invoice.read`
  - `core.payables.order.read`
  - `core.project.read`
  - `core.purchase_order. read`
  - `core.requisition.read`
  - `core.sourcing.pending_supplier.read`
  - `core.sourcing.read`
  - `core.sourcing.response.read`
  - `core.supplier.read`
  - `core.supplier_information_sites.read`
  - `core.supplier_information_tax registrations.read`
  - `core.supplier_sharing_settings.read`
  - `core.supplier_sites.read`
  - `core.uom.read`
  - `core.user.read`
  - `core.user_group.read`
  - `email login offline_access openid profile`
  - `travel_booking.common.read`
  - `travel_booking.team.read`
  - `travel_booking.trip.read`
  - `travel_booking.user.read`
  - `treasury.cash_management.read`

Note the client ID, client secret, and instance URL for your Coupa
project.

## Connecting Amazon AppFlow to your Coupa account

To connect Amazon AppFlow to your Coupa account,
provide details from your Coupa project so that Amazon AppFlow can access your data. If you
haven't yet configured your Coupa project for Amazon AppFlow integration, see [Before you begin](#coupa-prereqs "#coupa-prereqs").

###### To connect to Coupa

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Coupa**.
4. Choose **Create connection**.
5. In the **Connect to Coupa** window, enter the following
   information:
   - **Connection name** — A name for the connection.
   - **Authorization tokens URL** — From the dropdown menu, choose one of the following options: For partner and demo instances, choose https://\{company_name}.coupacloud.com.oauth2/token. For customer instances, choose https://\{company_name}.coupahost.com.oauth2/token.
   - **Custom authorization tokens URL** — The same company name used in the authorization tokens URL.
   - **Client ID** — The client ID in your Coupa
     project.
   - **Client secret** — The client secret in your Coupa
     project.
   - **Instance URL** — The instance URL of your Coupa project. For example,
     https://{company_name}.coupacloud.com (for partner and demo instances), or
     https://{company_name}.coupahost.com (for customer instances).

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your Coupa account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Coupa as the data source, you can select this connection.

## Transferring data from Coupa with a flow

To transfer data from Coupa, create an Amazon AppFlow flow, and choose Coupa as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Coupa, see [Supported objects](#coupa-objects "#coupa-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#coupa-destinations "#coupa-destinations").

## Supported destinations

When you create a flow that uses Coupa as the data source, you can set the destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- [HubSpot](connectors-hubspot.md "connectors-hubspot.md")
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")
- [Zoho CRM](connectors-zoho-crm.md "connectors-zoho-crm.md")

## Supported objects

When you create a flow that uses Coupa as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                                         | **Field**       | **Data type**                                                                                              | **Supported filters**                                                                                     |
| -------------------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Approval                                           |                 |                                                                                                            |                                                                                                           |
| Charge                                             | account-type-id | Integer                                                                                                    | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO          |
| accounting-currency                                | Struct          |                                                                                                            |
| accounting-total                                   | BigDecimal      |                                                                                                            |
| card-provider-account                              | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| charge-allocations                                 | List            |                                                                                                            |
| charge-date                                        | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| charge-tax-lines                                   | List            |                                                                                                            |
| coupa-pay-id                                       | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| coupa-pay-statement-id                             | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| created-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| created-by                                         | Struct          |                                                                                                            |
| currency                                           | Struct          |                                                                                                            |
| document-id                                        | Integer         |                                                                                                            |
| document-type                                      | String          |                                                                                                            |
| expense-holding-account                            | Struct          |                                                                                                            |
| exported                                           | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| external-ref-id                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| holding-account                                    | Struct          |                                                                                                            |
| id                                                 | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| issuer-bank                                        | Struct          |                                                                                                            |
| issuer-reconciliation-id                           | String          |                                                                                                            |
| last-exported-at                                   | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| mcc                                                | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| merchant-currency                                  | Struct          |                                                                                                            |
| merchant-reference                                 | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| merchant-total                                     | BigDecimal      |                                                                                                            |
| order-header-currency                              | String          |                                                                                                            |
| order-header-id                                    | Integer         |                                                                                                            |
| order-header-number                                | String          |                                                                                                            |
| order-header-total                                 | String          |                                                                                                            |
| payment-partner                                    | Struct          |                                                                                                            |
| posting-date                                       | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| statement                                          | Struct          |                                                                                                            |
| statement-id                                       | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| statement-name                                     | String          |                                                                                                            |
| supplier                                           | Struct          |                                                                                                            |
| supplier-id                                        | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| supplier-name                                      | String          |                                                                                                            |
| tax-currency                                       | Struct          |                                                                                                            |
| tax-total                                          | BigDecimal      |                                                                                                            |
| total                                              | BigDecimal      |                                                                                                            |
| updated-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| updated-by                                         | Struct          |                                                                                                            |
| virtual-card                                       | Struct          |                                                                                                            |
| virtual-card-id                                    | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| Expense Report                                     | approvals       | List                                                                                                       |                                                                                                           |
| art-der-ausgabe                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| audit-score                                        | Integer         |                                                                                                            |
| auditor-note                                       | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| comments                                           | List            |                                                                                                            |
| created-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| created-by                                         | Struct          |                                                                                                            |
| currency                                           | Struct          |                                                                                                            |
| end-date                                           | DateTime        | EQUAL_TO, BETWEEN, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| events                                             | List            |                                                                                                            |
| expense-lines                                      | List            |                                                                                                            |
| expense-policy-violations                          | List            |                                                                                                            |
| expense-report-preapprovals                        | List            |                                                                                                            |
| expensed-by                                        | Struct          |                                                                                                            |
| exported                                           | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| external-src-name                                  | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| external-src-ref                                   | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| id                                                 | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| is-trip                                            | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| last-exported-at                                   | DateTime        | EQUAL_TO, BETWEEN, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| paid                                               | Boolean         |                                                                                                            |
| past-due                                           | Boolean         |                                                                                                            |
| payment                                            | Struct          |                                                                                                            |
| payment-channel                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| reconciliation-lines                               | List            |                                                                                                            |
| reimbursable-total-amount                          | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| reimbursable-total-currency                        | Struct          |                                                                                                            |
| reject-reason                                      | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| report-due-date                                    | DateTime        |                                                                                                            |
| report-warnings                                    | List            |                                                                                                            |
| start-date                                         | DateTime        | EQUAL_TO, BETWEEN, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| status                                             | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| submitted-at                                       | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| submitted-by                                       | Struct          |                                                                                                            |
| title                                              | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| total                                              | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| travel-trip                                        | Struct          |                                                                                                            |
| type-de-note-de-frais                              | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| type-of-expense                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| updated-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| updated-by                                         | Struct          |                                                                                                            |
| Invoice                                            | abandon-reason  | Struct                                                                                                     |                                                                                                           |
| account-type                                       | Struct          |                                                                                                            |
| advance-payment-received-amount                    | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| amount-due                                         | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| amount-due-less-discount                           | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| amount-of-advance-payment                          | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| approvals                                          | List            |                                                                                                            |
| archive-entity-id                                  | Integer         |                                                                                                            |
| attachments                                        | List            |                                                                                                            |
| bill-to-address                                    | Struct          |                                                                                                            |
| buyer-tax-registration                             | Struct          |                                                                                                            |
| canceled                                           | Boolean         |                                                                                                            |
| cash-accounting-scheme-reference                   | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| cash-register-operator                             | String          |                                                                                                            |
| channel                                            | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| clearance-document                                 | String          |                                                                                                            |
| comments                                           | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| compliant                                          | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| confirmation                                       | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| content-validation                                 | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| contract                                           | Struct          |                                                                                                            |
| correct-value-of-supply                            | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| coupa-accelerate-status                            | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| created-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| created-by                                         | Struct          |                                                                                                            |
| credit-note-differences-with-original-invoice      | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| credit-reason                                      | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| currency                                           | Struct          |                                                                                                            |
| currency-id                                        | Integer         |                                                                                                            |
| current-integration-history-records                | List            |                                                                                                            |
| custom-fields                                      | Struct          |                                                                                                            |
| customer-accounting-tax                            | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| customer-accounting-tax-less-discount              | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| customs-declaration-date                           | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| customs-declaration-number                         | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| customs-office                                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| date-of-discovery-of-facts-decisive-for-correction | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| date-received                                      | DateTime        |                                                                                                            |
| delivery-date                                      | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| delivery-number                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| destination-country                                | Struct          |                                                                                                            |
| discount-amount                                    | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| discount-due-date                                  | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| discount-percent                                   | Float           | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| dispute-method                                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| dispute-reasons                                    | List            |                                                                                                            |
| document-type                                      | String          |                                                                                                            |
| early-payment-provisions                           | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| endorsement-on-invoices                            | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| exchange-rate                                      | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| exported                                           | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| failed-tolerances                                  | List            |                                                                                                            |
| folio-number                                       | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| form-of-payment                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| freight-type                                       | String          |                                                                                                            |
| gross-total                                        | BigDecimal      |                                                                                                            |
| gross-total-less-discount                          | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| handling-amount                                    | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| id                                                 | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| image-scan                                         | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| image-scan-content-type                            | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| image-scan-file-name                               | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| image-scan-file-size                               | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| image-scan-url                                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| inbound-invoice                                    | Struct          |                                                                                                            |
| inbox-name                                         | String          |                                                                                                            |
| internal-note                                      | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| invoice-charges                                    | List            |                                                                                                            |
| invoice-date                                       | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| invoice-from-address                               | Struct          |                                                                                                            |
| invoice-issuance-time                              | String          |                                                                                                            |
| invoice-lines                                      | List            |                                                                                                            |
| invoice-number                                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| invoice-payment-receipts                           | List            |                                                                                                            |
| invoice-reference-number                           | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| is-credit-note                                     | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| issuance-place                                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| last-exported-at                                   | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| late-payment-penalties                             | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| legal-destination-country                          | Struct          |                                                                                                            |
| line-count                                         | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| line-level-taxation                                | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| lock-version-key                                   | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| margin-scheme                                      | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| means-of-payment                                   | String          |                                                                                                            |
| misc-amount                                        | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| municipal-tax-number                               | String          |                                                                                                            |
| national-enrollment-of-conveyor                    | String          |                                                                                                            |
| nature-of-operation                                | String          |                                                                                                            |
| net-due-date                                       | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| net-total-less-discount                            | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| new-means-of-transport                             | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| origin-country                                     | Struct          |                                                                                                            |
| origin-currency-gross                              | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| origin-currency-net                                | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| original-invoice-date                              | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| original-invoice-number                            | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| original-value-of-supply                           | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| paid                                               | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| pay-invoice                                        | Struct          |                                                                                                            |
| payment-agreement-notes                            | List            |                                                                                                            |
| payment-channel                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| payment-date                                       | DateTime        |                                                                                                            |
| payment-method                                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| payment-notes                                      | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| payment-order-number                               | String          |                                                                                                            |
| payment-order-reference                            | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| payment-term                                       | Struct          |                                                                                                            |
| payments                                           | List            |                                                                                                            |
| place-of-issuance                                  | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| place-of-supply                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| pre-payment-date                                   | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| protocol-number                                    | String          |                                                                                                            |
| reconciliation-lines                               | List            |                                                                                                            |
| remit-to-address                                   | Struct          |                                                                                                            |
| requested-by                                       | Struct          |                                                                                                            |
| requester-email                                    | String          |                                                                                                            |
| requester-lookup-name                              | String          |                                                                                                            |
| requester-name                                     | String          |                                                                                                            |
| resolution-number                                  | String          |                                                                                                            |
| reverse-charge-reference                           | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| security-code-of-issuer                            | String          |                                                                                                            |
| self-billing-reference                             | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| sender-email                                       | String          |                                                                                                            |
| serial-code-of-fiscal-invoice                      | String          |                                                                                                            |
| series                                             | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| ship-from-address                                  | Struct          |                                                                                                            |
| ship-to-address                                    | Struct          |                                                                                                            |
| shipping-amount                                    | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| shipping-term                                      | Struct          |                                                                                                            |
| show-tax-information                               | Boolean         |                                                                                                            |
| signed-qr-code                                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| spend-load-id                                      | String          |                                                                                                            |
| split-payment-mechanism                            | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| state-tax-number                                   | String          |                                                                                                            |
| state-tax-number-for-substitute-taxpayer           | String          |                                                                                                            |
| status                                             | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| supplier                                           | Struct          |                                                                                                            |
| supplier-created                                   | Boolean         |                                                                                                            |
| supplier-invoice-issuer-name                       | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| supplier-invoice-reviewer-name                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| supplier-note                                      | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| supplier-payment-collector-name                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| supplier-remit-to                                  | Struct          |                                                                                                            |
| supplier-tax-registration                          | Struct          |                                                                                                            |
| supplier-total                                     | BigDecimal      |                                                                                                            |
| taggings                                           | List            |                                                                                                            |
| tags                                               | List            |                                                                                                            |
| tax-amount                                         | BigDecimal      |                                                                                                            |
| tax-amount-engine                                  | BigDecimal      |                                                                                                            |
| tax-code                                           | Struct          |                                                                                                            |
| tax-code-engine                                    | String          |                                                                                                            |
| tax-due-to-supplier                                | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| tax-lines                                          | List            |                                                                                                            |
| tax-rate                                           | Float           |                                                                                                            |
| tax-rate-engine                                    | String          |                                                                                                            |
| taxes-in-origin-country-currency                   | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| tcs-tax-lines                                      | List            |                                                                                                            |
| tolerance-failures                                 | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| total-taxes-less-discount                          | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| total-with-taxes                                   | BigDecimal      |                                                                                                            |
| transaction-notification-date                      | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| transaction-uuid                                   | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| type-of-document                                   | String          |                                                                                                            |
| type-of-operation                                  | String          |                                                                                                            |
| type-of-receipt                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| type-of-relationship                               | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| unique-identification-code-of-cash-receipt         | String          |                                                                                                            |
| updated-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| updated-by                                         | Struct          |                                                                                                            |
| use-of-invoice                                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| vehicle-license-plate                              | String          |                                                                                                            |
| verification-code                                  | String          |                                                                                                            |
| volume-amount                                      | String          |                                                                                                            |
| volume-brand                                       | String          |                                                                                                            |
| volume-gross-weight                                | String          |                                                                                                            |
| volume-liquid-weight                               | String          |                                                                                                            |
| volume-numbering                                   | String          |                                                                                                            |
| volume-type                                        | String          |                                                                                                            |
| withholding-tax-lines                              | List            |                                                                                                            |
| withholding-tax-override                           | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| Payment                                            | created-at      | DateTime                                                                                                   | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, BETWEEN |
| created-by                                         | Struct          |                                                                                                            |
| description                                        | String          | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, CONTAINS |
| digital-check                                      | String          |                                                                                                            |
| error-text                                         | String          | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, CONTAINS |
| estimated-pay-from-total                           | BigDecimal      |                                                                                                            |
| exchange-rate                                      | String          | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, CONTAINS |
| exported                                           | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| external-ref-id                                    | Integer         |                                                                                                            |
| id                                                 | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| last-exported-at                                   | DateTime        | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, BETWEEN  |
| line-num                                           | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| pay-from-account                                   | List            |                                                                                                            |
| pay-from-currency                                  | Struct          |                                                                                                            |
| pay-from-external-gl-account                       | List            |                                                                                                            |
| pay-from-total                                     | BigDecimal      |                                                                                                            |
| pay-to-account                                     | List            |                                                                                                            |
| pay-to-currency                                    | Struct          |                                                                                                            |
| pay-to-external-gl-account                         | List            |                                                                                                            |
| pay-to-total                                       | BigDecimal      |                                                                                                            |
| payee                                              | Struct          |                                                                                                            |
| payment-batch                                      | Struct          |                                                                                                            |
| payment-batch-id                                   | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| payment-details                                    | List            |                                                                                                            |
| payment-identifier                                 | String          | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, CONTAINS |
| released-at                                        | String          |                                                                                                            |
| reporting-currency                                 | Struct          |                                                                                                            |
| reporting-pay-from-total                           | BigDecimal      |                                                                                                            |
| reporting-pay-to-total                             | BigDecimal      |                                                                                                            |
| source-name                                        | String          | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, CONTAINS |
| source-reference                                   | String          | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, CONTAINS |
| status                                             | String          | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, CONTAINS |
| type                                               | String          | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, CONTAINS |
| updated-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, BETWEEN  |
| updated-by                                         | Struct          |                                                                                                            |
| Purchase Order                                     | acknowledged-at | DateTime                                                                                                   | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| acknowledged-flag                                  | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| attachments                                        | List            |                                                                                                            |
| change-type                                        | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| classification                                     | String          |                                                                                                            |
| confirm-by-hrs                                     | Integer         |                                                                                                            |
| coupa-accelerate-status                            | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| created-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| created-by                                         | Struct          |                                                                                                            |
| currency                                           | Struct          |                                                                                                            |
| current-integration-history-records                | List            |                                                                                                            |
| custom-fields                                      | Struct          |                                                                                                            |
| exported                                           | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| hide-price                                         | Boolean         |                                                                                                            |
| id                                                 | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| internal-revision                                  | Integer         |                                                                                                            |
| invoice-stop                                       | Boolean         |                                                                                                            |
| last-exported-at                                   | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| milestones                                         | List            |                                                                                                            |
| order-confirmation-level                           | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| payment-method                                     | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| payment-term                                       | Struct          |                                                                                                            |
| pcard                                              | Struct          |                                                                                                            |
| po-number                                          | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| price-hidden                                       | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| reason-insight-events                              | List            |                                                                                                            |
| recurring-rules                                    | List            |                                                                                                            |
| requester                                          | Struct          |                                                                                                            |
| ship-to-address                                    | Struct          |                                                                                                            |
| ship-to-attention                                  | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| ship-to-user                                       | Struct          |                                                                                                            |
| shipping-term                                      | Struct          |                                                                                                            |
| spend-load-id                                      | String          |                                                                                                            |
| status                                             | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| supplier                                           | Struct          |                                                                                                            |
| supplier-site                                      | Struct          |                                                                                                            |
| transmission-emails                                | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| transmission-method-override                       | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| transmission-status                                | String          |                                                                                                            |
| type                                               | String          |                                                                                                            |
| updated-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| updated-by                                         | Struct          |                                                                                                            |
| user-group-members                                 | List            |                                                                                                            |
| user-members                                       | List            |                                                                                                            |
| version                                            | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| Purchase Order Line                                | account         | Struct                                                                                                     |                                                                                                           |
| account-allocations                                | List            |                                                                                                            |
| accounting-total                                   | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| accounting-total-currency                          | Struct          |                                                                                                            |
| amount-components                                  | List            |                                                                                                            |
| asset-tags                                         | List            |                                                                                                            |
| attachments                                        | List            |                                                                                                            |
| bulk-price                                         | Struct          |                                                                                                            |
| commodity                                          | Struct          |                                                                                                            |
| contract                                           | Struct          |                                                                                                            |
| created-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| created-by                                         | Struct          |                                                                                                            |
| currency                                           | Struct          |                                                                                                            |
| custom-fields                                      | Struct          |                                                                                                            |
| department                                         | Struct          |                                                                                                            |
| description                                        | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| easy-form-response-id                              | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| external-reference-number                          | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| external-reference-type                            | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| extra-line-attribute                               | Struct          |                                                                                                            |
| form-response                                      | List            |                                                                                                            |
| id                                                 | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| invoice-stop                                       | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| invoiced                                           | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| item                                               | Struct          |                                                                                                            |
| line-num                                           | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| line-owner                                         | Struct          |                                                                                                            |
| manufacturer-name                                  | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| manufacturer-part-number                           | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| match-type                                         | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| milestones                                         | List            |                                                                                                            |
| minimum-order-quantity                             | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| need-by-date                                       | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| order-header-id                                    | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| order-header-number                                | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| order-increment                                    | Struct          |                                                                                                            |
| order-line-tax-detail                              | Struct          |                                                                                                            |
| period                                             | Struct          |                                                                                                            |
| price                                              | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| quantity                                           | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| receipt-approval-required                          | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| receipt-required                                   | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| received                                           | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| receiving-warehouse                                | Struct          |                                                                                                            |
| recurring-rules                                    | List            |                                                                                                            |
| reporting-total                                    | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| requester                                          | Struct          |                                                                                                            |
| requisition-line-id                                | Integer         |                                                                                                            |
| rfq-easy-form-response-id                          | Integer         |                                                                                                            |
| rfq-form-response                                  | List            |                                                                                                            |
| savings-pct                                        | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| service-type                                       | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| source-part-num                                    | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| spend-load-id                                      | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| status                                             | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| sub-line-num                                       | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| supp-aux-part-num                                  | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| supplier                                           | Struct          |                                                                                                            |
| supplier-order-number                              | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| supplier-site-id                                   | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| third_party_supplier                               | Struct          |                                                                                                            |
| total                                              | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| type                                               | String          | EQUAL_TO, NOT_EQUAL_TO, CONTAINS, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| uom                                                | Struct          |                                                                                                            |
| updated-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| updated-by                                         | Struct          |                                                                                                            |
| version                                            | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| Receipt                                            | account         | Struct                                                                                                     |                                                                                                           |
| account-allocations                                | List            |                                                                                                            |
| adjustment-code                                    | Struct          |                                                                                                            |
| asn-header                                         | Struct          |                                                                                                            |
| asn-line                                           | Struct          |                                                                                                            |
| asset-tags                                         | List            |                                                                                                            |
| attachments                                        | List            |                                                                                                            |
| barcode                                            | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| comments                                           | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| created-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| created-by                                         | Struct          |                                                                                                            |
| currency                                           | Struct          |                                                                                                            |
| current-integration-history-records                | List            |                                                                                                            |
| exported                                           | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| from-warehouse                                     | Struct          |                                                                                                            |
| from-warehouse-location                            | Struct          |                                                                                                            |
| id                                                 | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| inspection-code                                    | Struct          |                                                                                                            |
| inventory-transaction-lots                         | List            |                                                                                                            |
| inventory-transaction-valuations                   | List            |                                                                                                            |
| item                                               | Struct          |                                                                                                            |
| last-exported-at                                   | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| match-reference                                    | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| order-line                                         | Struct          |                                                                                                            |
| original-transaction                               | Struct          |                                                                                                            |
| original-transaction-id                            | Integer         |                                                                                                            |
| price                                              | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| quantity                                           | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| reason-insight                                     | Struct          |                                                                                                            |
| receipt                                            | Struct          |                                                                                                            |
| receipts-batch-id                                  | Integer         |                                                                                                            |
| received-weight                                    | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| receiving-form-response                            | Struct          |                                                                                                            |
| rfid-tag                                           | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| soft-close-for-receiving                           | Boolean         |                                                                                                            |
| spend-load-id                                      | String          |                                                                                                            |
| status                                             | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| to-warehouse                                       | Struct          |                                                                                                            |
| to-warehouse-location                              | Struct          |                                                                                                            |
| total                                              | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| transaction-date                                   | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| type                                               | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| uom                                                | Struct          |                                                                                                            |
| updated-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| updated-by                                         | Struct          |                                                                                                            |
| voided-value                                       | BigDecimal      | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| Requisition                                        | approvals       | List                                                                                                       |                                                                                                           |
| approver                                           | Struct          |                                                                                                            |
| attachments                                        | List            |                                                                                                            |
| buyer-note                                         | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| created-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| created-by                                         | Struct          |                                                                                                            |
| currency                                           | Struct          |                                                                                                            |
| current-approval                                   | Struct          |                                                                                                            |
| custom-fields                                      | Struct          |                                                                                                            |
| department                                         | Struct          |                                                                                                            |
| exported                                           | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| external-po-reference                              | String          |                                                                                                            |
| hide-price                                         | Struct          |                                                                                                            |
| id                                                 | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| justification                                      | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| line-count                                         | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| milestones                                         | List            |                                                                                                            |
| mobile-currency                                    | Struct          |                                                                                                            |
| mobile-total                                       | BigDecimal      |                                                                                                            |
| need-by-date                                       | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| pcard                                              | Struct          |                                                                                                            |
| price-hidden                                       | Boolean         | EQUAL_TO, NOT_EQUAL_TO                                                                                     |
| receiving-warehouse-id                             | Integer         |                                                                                                            |
| recurring-rules                                    | List            |                                                                                                            |
| reject-reason-comment                              | String          |                                                                                                            |
| req-title                                          | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| requested-by                                       | Struct          |                                                                                                            |
| requester                                          | Struct          |                                                                                                            |
| ship-to-address                                    | Struct          |                                                                                                            |
| ship-to-attention                                  | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| spend-load-id                                      | String          |                                                                                                            |
| status                                             | String          | EQUAL_TO, CONTAINS, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| submitted-at                                       | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| taggings                                           | List            |                                                                                                            |
| tags                                               | List            |                                                                                                            |
| total                                              | BigDecimal      |                                                                                                            |
| updated-at                                         | DateTime        | EQUAL_TO, NOT_EQUAL_TO, BETWEEN, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO  |
| updated-by                                         | Struct          |                                                                                                            |
| user-group-members                                 | List            |                                                                                                            |
| user-members                                       | List            |                                                                                                            |
| Requisition Line                                   | account         | Struct                                                                                                     |                                                                                                           |
| account-allocations                                | List            |                                                                                                            |
| alternate-status                                   | String          |                                                                                                            |
| asset-tags                                         | List            |                                                                                                            |
| attachments                                        | List            |                                                                                                            |
| commodity                                          | Struct          |                                                                                                            |
| confirm-by-hrs                                     | BigDecimal      |                                                                                                            |
| contract                                           | Struct          |                                                                                                            |
| created-at                                         | DateTime        |                                                                                                            |
| created-by                                         | Struct          |                                                                                                            |
| currency                                           | Struct          |                                                                                                            |
| description                                        | String          |                                                                                                            |
| easy-form-response-id                              | Integer         |                                                                                                            |
| extra-line-attribute                               | Struct          |                                                                                                            |
| form-response                                      | List            |                                                                                                            |
| id                                                 | Integer         |                                                                                                            |
| image-url                                          | String          |                                                                                                            |
| item                                               | Struct          |                                                                                                            |
| line-num                                           | Integer         |                                                                                                            |
| line-owner                                         | Struct          |                                                                                                            |
| line-type                                          | String          |                                                                                                            |
| manufacturer-name                                  | String          |                                                                                                            |
| manufacturer-part-number                           | String          |                                                                                                            |
| milestones                                         | List            |                                                                                                            |
| minimum-order-quantity                             | BigDecimal      |                                                                                                            |
| need-by-date                                       | DateTime        |                                                                                                            |
| order-confirmation-level                           | String          |                                                                                                            |
| order-increment                                    | String          |                                                                                                            |
| order-line-id                                      | Integer         |                                                                                                            |
| order-pad-line                                     | Struct          |                                                                                                            |
| payment-term                                       | Struct          |                                                                                                            |
| period                                             | Struct          |                                                                                                            |
| punchout-site                                      | Struct          |                                                                                                            |
| quantity                                           | BigDecimal      |                                                                                                            |
| realtime-extension                                 | Struct          |                                                                                                            |
| receipt-required                                   | Boolean         |                                                                                                            |
| recurring-rules                                    | List            |                                                                                                            |
| requisition-line-tax-detail                        | Struct          |                                                                                                            |
| requisition_id                                     | Integer         | EQUAL_TO, NOT_EQUAL_TO, LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| service-type                                       | String          |                                                                                                            |
| shipping-term                                      | Struct          |                                                                                                            |
| source                                             | String          |                                                                                                            |
| source-details                                     | String          |                                                                                                            |
| source-part-num                                    | String          |                                                                                                            |
| source-type                                        | String          |                                                                                                            |
| spend-load-id                                      | String          |                                                                                                            |
| status                                             | String          |                                                                                                            |
| sub-line-num                                       | Integer         |                                                                                                            |
| supp-aux-part-num                                  | String          |                                                                                                            |
| supplier                                           | Struct          |                                                                                                            |
| supplier-site                                      | Struct          |                                                                                                            |
| supplier-site-id                                   | Integer         |                                                                                                            |
| taggings                                           | List            |                                                                                                            |
| tags                                               | List            |                                                                                                            |
| total                                              | BigDecimal      |                                                                                                            |
| transmission-emails                                | String          |                                                                                                            |
| transmission-method-override                       | String          |                                                                                                            |
| unit-price                                         | BigDecimal      |                                                                                                            |
| unit-price-in-usd                                  | BigDecimal      |                                                                                                            |
| unspsc-code                                        | String          |                                                                                                            |
| uom                                                | Struct          |                                                                                                            |
| updated-at                                         | DateTime        |                                                                                                            |
| updated-by                                         | Struct          |                                                                                                            |
| Supplier Information                               |                 |                                                                                                            |                                                                                                           |
