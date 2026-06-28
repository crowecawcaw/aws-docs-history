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
   - **Authorization tokens URL** — From the dropdown menu, choose one of the following options: For partner and demo instances, choose https://\{company\_name}.coupacloud.com.oauth2/token. For customer instances, choose https://\{company\_name}.coupahost.com.oauth2/token.
   - **Custom authorization tokens URL** — The same company name used in the authorization tokens URL.
   - **Client ID** — The client ID in your Coupa
     project.
   - **Client secret** — The client secret in your Coupa
     project.
   - **Instance URL** — The instance URL of your Coupa project. For example,
     https://{company\_name}.coupacloud.com (for partner and demo instances), or
     https://{company\_name}.coupahost.com (for customer instances).

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

| **Object**                                         | **Field**       | **Data type**                                                                                                           | **Supported filters**                                                                                                  |
| -------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Approval                                           |                 |                                                                                                                         |                                                                                                                        |
| Charge                                             | account-type-id | Integer                                                                                                                 | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO          |
| accounting-currency                                | Struct          |                                                                                                                         |
| accounting-total                                   | BigDecimal      |                                                                                                                         |
| card-provider-account                              | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| charge-allocations                                 | List            |                                                                                                                         |
| charge-date                                        | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| charge-tax-lines                                   | List            |                                                                                                                         |
| coupa-pay-id                                       | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| coupa-pay-statement-id                             | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| created-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| created-by                                         | Struct          |                                                                                                                         |
| currency                                           | Struct          |                                                                                                                         |
| document-id                                        | Integer         |                                                                                                                         |
| document-type                                      | String          |                                                                                                                         |
| expense-holding-account                            | Struct          |                                                                                                                         |
| exported                                           | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| external-ref-id                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| holding-account                                    | Struct          |                                                                                                                         |
| id                                                 | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| issuer-bank                                        | Struct          |                                                                                                                         |
| issuer-reconciliation-id                           | String          |                                                                                                                         |
| last-exported-at                                   | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| mcc                                                | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| merchant-currency                                  | Struct          |                                                                                                                         |
| merchant-reference                                 | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| merchant-total                                     | BigDecimal      |                                                                                                                         |
| order-header-currency                              | String          |                                                                                                                         |
| order-header-id                                    | Integer         |                                                                                                                         |
| order-header-number                                | String          |                                                                                                                         |
| order-header-total                                 | String          |                                                                                                                         |
| payment-partner                                    | Struct          |                                                                                                                         |
| posting-date                                       | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| statement                                          | Struct          |                                                                                                                         |
| statement-id                                       | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| statement-name                                     | String          |                                                                                                                         |
| supplier                                           | Struct          |                                                                                                                         |
| supplier-id                                        | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| supplier-name                                      | String          |                                                                                                                         |
| tax-currency                                       | Struct          |                                                                                                                         |
| tax-total                                          | BigDecimal      |                                                                                                                         |
| total                                              | BigDecimal      |                                                                                                                         |
| updated-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| updated-by                                         | Struct          |                                                                                                                         |
| virtual-card                                       | Struct          |                                                                                                                         |
| virtual-card-id                                    | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| Expense Report                                     | approvals       | List                                                                                                                    |                                                                                                                        |
| art-der-ausgabe                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| audit-score                                        | Integer         |                                                                                                                         |
| auditor-note                                       | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| comments                                           | List            |                                                                                                                         |
| created-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| created-by                                         | Struct          |                                                                                                                         |
| currency                                           | Struct          |                                                                                                                         |
| end-date                                           | DateTime        | EQUAL\_TO, BETWEEN, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| events                                             | List            |                                                                                                                         |
| expense-lines                                      | List            |                                                                                                                         |
| expense-policy-violations                          | List            |                                                                                                                         |
| expense-report-preapprovals                        | List            |                                                                                                                         |
| expensed-by                                        | Struct          |                                                                                                                         |
| exported                                           | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| external-src-name                                  | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| external-src-ref                                   | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| id                                                 | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| is-trip                                            | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| last-exported-at                                   | DateTime        | EQUAL\_TO, BETWEEN, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| paid                                               | Boolean         |                                                                                                                         |
| past-due                                           | Boolean         |                                                                                                                         |
| payment                                            | Struct          |                                                                                                                         |
| payment-channel                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| reconciliation-lines                               | List            |                                                                                                                         |
| reimbursable-total-amount                          | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| reimbursable-total-currency                        | Struct          |                                                                                                                         |
| reject-reason                                      | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| report-due-date                                    | DateTime        |                                                                                                                         |
| report-warnings                                    | List            |                                                                                                                         |
| start-date                                         | DateTime        | EQUAL\_TO, BETWEEN, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| status                                             | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| submitted-at                                       | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| submitted-by                                       | Struct          |                                                                                                                         |
| title                                              | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| total                                              | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| travel-trip                                        | Struct          |                                                                                                                         |
| type-de-note-de-frais                              | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| type-of-expense                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| updated-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| updated-by                                         | Struct          |                                                                                                                         |
| Invoice                                            | abandon-reason  | Struct                                                                                                                  |                                                                                                                        |
| account-type                                       | Struct          |                                                                                                                         |
| advance-payment-received-amount                    | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| amount-due                                         | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| amount-due-less-discount                           | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| amount-of-advance-payment                          | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| approvals                                          | List            |                                                                                                                         |
| archive-entity-id                                  | Integer         |                                                                                                                         |
| attachments                                        | List            |                                                                                                                         |
| bill-to-address                                    | Struct          |                                                                                                                         |
| buyer-tax-registration                             | Struct          |                                                                                                                         |
| canceled                                           | Boolean         |                                                                                                                         |
| cash-accounting-scheme-reference                   | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| cash-register-operator                             | String          |                                                                                                                         |
| channel                                            | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| clearance-document                                 | String          |                                                                                                                         |
| comments                                           | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| compliant                                          | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| confirmation                                       | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| content-validation                                 | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| contract                                           | Struct          |                                                                                                                         |
| correct-value-of-supply                            | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| coupa-accelerate-status                            | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| created-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| created-by                                         | Struct          |                                                                                                                         |
| credit-note-differences-with-original-invoice      | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| credit-reason                                      | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| currency                                           | Struct          |                                                                                                                         |
| currency-id                                        | Integer         |                                                                                                                         |
| current-integration-history-records                | List            |                                                                                                                         |
| custom-fields                                      | Struct          |                                                                                                                         |
| customer-accounting-tax                            | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| customer-accounting-tax-less-discount              | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| customs-declaration-date                           | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| customs-declaration-number                         | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| customs-office                                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| date-of-discovery-of-facts-decisive-for-correction | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| date-received                                      | DateTime        |                                                                                                                         |
| delivery-date                                      | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| delivery-number                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| destination-country                                | Struct          |                                                                                                                         |
| discount-amount                                    | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| discount-due-date                                  | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| discount-percent                                   | Float           | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| dispute-method                                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| dispute-reasons                                    | List            |                                                                                                                         |
| document-type                                      | String          |                                                                                                                         |
| early-payment-provisions                           | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| endorsement-on-invoices                            | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| exchange-rate                                      | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| exported                                           | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| failed-tolerances                                  | List            |                                                                                                                         |
| folio-number                                       | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| form-of-payment                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| freight-type                                       | String          |                                                                                                                         |
| gross-total                                        | BigDecimal      |                                                                                                                         |
| gross-total-less-discount                          | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| handling-amount                                    | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| id                                                 | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| image-scan                                         | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| image-scan-content-type                            | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| image-scan-file-name                               | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| image-scan-file-size                               | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| image-scan-url                                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| inbound-invoice                                    | Struct          |                                                                                                                         |
| inbox-name                                         | String          |                                                                                                                         |
| internal-note                                      | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| invoice-charges                                    | List            |                                                                                                                         |
| invoice-date                                       | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| invoice-from-address                               | Struct          |                                                                                                                         |
| invoice-issuance-time                              | String          |                                                                                                                         |
| invoice-lines                                      | List            |                                                                                                                         |
| invoice-number                                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| invoice-payment-receipts                           | List            |                                                                                                                         |
| invoice-reference-number                           | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| is-credit-note                                     | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| issuance-place                                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| last-exported-at                                   | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| late-payment-penalties                             | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| legal-destination-country                          | Struct          |                                                                                                                         |
| line-count                                         | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| line-level-taxation                                | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| lock-version-key                                   | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| margin-scheme                                      | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| means-of-payment                                   | String          |                                                                                                                         |
| misc-amount                                        | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| municipal-tax-number                               | String          |                                                                                                                         |
| national-enrollment-of-conveyor                    | String          |                                                                                                                         |
| nature-of-operation                                | String          |                                                                                                                         |
| net-due-date                                       | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| net-total-less-discount                            | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| new-means-of-transport                             | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| origin-country                                     | Struct          |                                                                                                                         |
| origin-currency-gross                              | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| origin-currency-net                                | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| original-invoice-date                              | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| original-invoice-number                            | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| original-value-of-supply                           | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| paid                                               | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| pay-invoice                                        | Struct          |                                                                                                                         |
| payment-agreement-notes                            | List            |                                                                                                                         |
| payment-channel                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| payment-date                                       | DateTime        |                                                                                                                         |
| payment-method                                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| payment-notes                                      | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| payment-order-number                               | String          |                                                                                                                         |
| payment-order-reference                            | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| payment-term                                       | Struct          |                                                                                                                         |
| payments                                           | List            |                                                                                                                         |
| place-of-issuance                                  | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| place-of-supply                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| pre-payment-date                                   | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| protocol-number                                    | String          |                                                                                                                         |
| reconciliation-lines                               | List            |                                                                                                                         |
| remit-to-address                                   | Struct          |                                                                                                                         |
| requested-by                                       | Struct          |                                                                                                                         |
| requester-email                                    | String          |                                                                                                                         |
| requester-lookup-name                              | String          |                                                                                                                         |
| requester-name                                     | String          |                                                                                                                         |
| resolution-number                                  | String          |                                                                                                                         |
| reverse-charge-reference                           | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| security-code-of-issuer                            | String          |                                                                                                                         |
| self-billing-reference                             | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| sender-email                                       | String          |                                                                                                                         |
| serial-code-of-fiscal-invoice                      | String          |                                                                                                                         |
| series                                             | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| ship-from-address                                  | Struct          |                                                                                                                         |
| ship-to-address                                    | Struct          |                                                                                                                         |
| shipping-amount                                    | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| shipping-term                                      | Struct          |                                                                                                                         |
| show-tax-information                               | Boolean         |                                                                                                                         |
| signed-qr-code                                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| spend-load-id                                      | String          |                                                                                                                         |
| split-payment-mechanism                            | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| state-tax-number                                   | String          |                                                                                                                         |
| state-tax-number-for-substitute-taxpayer           | String          |                                                                                                                         |
| status                                             | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| supplier                                           | Struct          |                                                                                                                         |
| supplier-created                                   | Boolean         |                                                                                                                         |
| supplier-invoice-issuer-name                       | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| supplier-invoice-reviewer-name                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| supplier-note                                      | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| supplier-payment-collector-name                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| supplier-remit-to                                  | Struct          |                                                                                                                         |
| supplier-tax-registration                          | Struct          |                                                                                                                         |
| supplier-total                                     | BigDecimal      |                                                                                                                         |
| taggings                                           | List            |                                                                                                                         |
| tags                                               | List            |                                                                                                                         |
| tax-amount                                         | BigDecimal      |                                                                                                                         |
| tax-amount-engine                                  | BigDecimal      |                                                                                                                         |
| tax-code                                           | Struct          |                                                                                                                         |
| tax-code-engine                                    | String          |                                                                                                                         |
| tax-due-to-supplier                                | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| tax-lines                                          | List            |                                                                                                                         |
| tax-rate                                           | Float           |                                                                                                                         |
| tax-rate-engine                                    | String          |                                                                                                                         |
| taxes-in-origin-country-currency                   | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| tcs-tax-lines                                      | List            |                                                                                                                         |
| tolerance-failures                                 | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| total-taxes-less-discount                          | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| total-with-taxes                                   | BigDecimal      |                                                                                                                         |
| transaction-notification-date                      | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| transaction-uuid                                   | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| type-of-document                                   | String          |                                                                                                                         |
| type-of-operation                                  | String          |                                                                                                                         |
| type-of-receipt                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| type-of-relationship                               | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| unique-identification-code-of-cash-receipt         | String          |                                                                                                                         |
| updated-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| updated-by                                         | Struct          |                                                                                                                         |
| use-of-invoice                                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| vehicle-license-plate                              | String          |                                                                                                                         |
| verification-code                                  | String          |                                                                                                                         |
| volume-amount                                      | String          |                                                                                                                         |
| volume-brand                                       | String          |                                                                                                                         |
| volume-gross-weight                                | String          |                                                                                                                         |
| volume-liquid-weight                               | String          |                                                                                                                         |
| volume-numbering                                   | String          |                                                                                                                         |
| volume-type                                        | String          |                                                                                                                         |
| withholding-tax-lines                              | List            |                                                                                                                         |
| withholding-tax-override                           | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| Payment                                            | created-at      | DateTime                                                                                                                | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, BETWEEN |
| created-by                                         | Struct          |                                                                                                                         |
| description                                        | String          | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS |
| digital-check                                      | String          |                                                                                                                         |
| error-text                                         | String          | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS |
| estimated-pay-from-total                           | BigDecimal      |                                                                                                                         |
| exchange-rate                                      | String          | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS |
| exported                                           | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| external-ref-id                                    | Integer         |                                                                                                                         |
| id                                                 | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| last-exported-at                                   | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, BETWEEN  |
| line-num                                           | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| pay-from-account                                   | List            |                                                                                                                         |
| pay-from-currency                                  | Struct          |                                                                                                                         |
| pay-from-external-gl-account                       | List            |                                                                                                                         |
| pay-from-total                                     | BigDecimal      |                                                                                                                         |
| pay-to-account                                     | List            |                                                                                                                         |
| pay-to-currency                                    | Struct          |                                                                                                                         |
| pay-to-external-gl-account                         | List            |                                                                                                                         |
| pay-to-total                                       | BigDecimal      |                                                                                                                         |
| payee                                              | Struct          |                                                                                                                         |
| payment-batch                                      | Struct          |                                                                                                                         |
| payment-batch-id                                   | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| payment-details                                    | List            |                                                                                                                         |
| payment-identifier                                 | String          | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS |
| released-at                                        | String          |                                                                                                                         |
| reporting-currency                                 | Struct          |                                                                                                                         |
| reporting-pay-from-total                           | BigDecimal      |                                                                                                                         |
| reporting-pay-to-total                             | BigDecimal      |                                                                                                                         |
| source-name                                        | String          | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS |
| source-reference                                   | String          | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS |
| status                                             | String          | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS |
| type                                               | String          | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, CONTAINS |
| updated-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, BETWEEN  |
| updated-by                                         | Struct          |                                                                                                                         |
| Purchase Order                                     | acknowledged-at | DateTime                                                                                                                | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| acknowledged-flag                                  | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| attachments                                        | List            |                                                                                                                         |
| change-type                                        | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| classification                                     | String          |                                                                                                                         |
| confirm-by-hrs                                     | Integer         |                                                                                                                         |
| coupa-accelerate-status                            | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| created-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| created-by                                         | Struct          |                                                                                                                         |
| currency                                           | Struct          |                                                                                                                         |
| current-integration-history-records                | List            |                                                                                                                         |
| custom-fields                                      | Struct          |                                                                                                                         |
| exported                                           | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| hide-price                                         | Boolean         |                                                                                                                         |
| id                                                 | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| internal-revision                                  | Integer         |                                                                                                                         |
| invoice-stop                                       | Boolean         |                                                                                                                         |
| last-exported-at                                   | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| milestones                                         | List            |                                                                                                                         |
| order-confirmation-level                           | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| payment-method                                     | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| payment-term                                       | Struct          |                                                                                                                         |
| pcard                                              | Struct          |                                                                                                                         |
| po-number                                          | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| price-hidden                                       | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| reason-insight-events                              | List            |                                                                                                                         |
| recurring-rules                                    | List            |                                                                                                                         |
| requester                                          | Struct          |                                                                                                                         |
| ship-to-address                                    | Struct          |                                                                                                                         |
| ship-to-attention                                  | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| ship-to-user                                       | Struct          |                                                                                                                         |
| shipping-term                                      | Struct          |                                                                                                                         |
| spend-load-id                                      | String          |                                                                                                                         |
| status                                             | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| supplier                                           | Struct          |                                                                                                                         |
| supplier-site                                      | Struct          |                                                                                                                         |
| transmission-emails                                | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| transmission-method-override                       | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| transmission-status                                | String          |                                                                                                                         |
| type                                               | String          |                                                                                                                         |
| updated-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| updated-by                                         | Struct          |                                                                                                                         |
| user-group-members                                 | List            |                                                                                                                         |
| user-members                                       | List            |                                                                                                                         |
| version                                            | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| Purchase Order Line                                | account         | Struct                                                                                                                  |                                                                                                                        |
| account-allocations                                | List            |                                                                                                                         |
| accounting-total                                   | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| accounting-total-currency                          | Struct          |                                                                                                                         |
| amount-components                                  | List            |                                                                                                                         |
| asset-tags                                         | List            |                                                                                                                         |
| attachments                                        | List            |                                                                                                                         |
| bulk-price                                         | Struct          |                                                                                                                         |
| commodity                                          | Struct          |                                                                                                                         |
| contract                                           | Struct          |                                                                                                                         |
| created-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| created-by                                         | Struct          |                                                                                                                         |
| currency                                           | Struct          |                                                                                                                         |
| custom-fields                                      | Struct          |                                                                                                                         |
| department                                         | Struct          |                                                                                                                         |
| description                                        | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| easy-form-response-id                              | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| external-reference-number                          | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| external-reference-type                            | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| extra-line-attribute                               | Struct          |                                                                                                                         |
| form-response                                      | List            |                                                                                                                         |
| id                                                 | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| invoice-stop                                       | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| invoiced                                           | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| item                                               | Struct          |                                                                                                                         |
| line-num                                           | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| line-owner                                         | Struct          |                                                                                                                         |
| manufacturer-name                                  | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| manufacturer-part-number                           | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| match-type                                         | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| milestones                                         | List            |                                                                                                                         |
| minimum-order-quantity                             | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| need-by-date                                       | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| order-header-id                                    | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| order-header-number                                | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| order-increment                                    | Struct          |                                                                                                                         |
| order-line-tax-detail                              | Struct          |                                                                                                                         |
| period                                             | Struct          |                                                                                                                         |
| price                                              | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| quantity                                           | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| receipt-approval-required                          | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| receipt-required                                   | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| received                                           | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| receiving-warehouse                                | Struct          |                                                                                                                         |
| recurring-rules                                    | List            |                                                                                                                         |
| reporting-total                                    | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| requester                                          | Struct          |                                                                                                                         |
| requisition-line-id                                | Integer         |                                                                                                                         |
| rfq-easy-form-response-id                          | Integer         |                                                                                                                         |
| rfq-form-response                                  | List            |                                                                                                                         |
| savings-pct                                        | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| service-type                                       | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| source-part-num                                    | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| spend-load-id                                      | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| status                                             | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| sub-line-num                                       | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| supp-aux-part-num                                  | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| supplier                                           | Struct          |                                                                                                                         |
| supplier-order-number                              | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| supplier-site-id                                   | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| third\_party\_supplier                             | Struct          |                                                                                                                         |
| total                                              | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| type                                               | String          | EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| uom                                                | Struct          |                                                                                                                         |
| updated-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| updated-by                                         | Struct          |                                                                                                                         |
| version                                            | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| Receipt                                            | account         | Struct                                                                                                                  |                                                                                                                        |
| account-allocations                                | List            |                                                                                                                         |
| adjustment-code                                    | Struct          |                                                                                                                         |
| asn-header                                         | Struct          |                                                                                                                         |
| asn-line                                           | Struct          |                                                                                                                         |
| asset-tags                                         | List            |                                                                                                                         |
| attachments                                        | List            |                                                                                                                         |
| barcode                                            | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| comments                                           | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| created-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| created-by                                         | Struct          |                                                                                                                         |
| currency                                           | Struct          |                                                                                                                         |
| current-integration-history-records                | List            |                                                                                                                         |
| exported                                           | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| from-warehouse                                     | Struct          |                                                                                                                         |
| from-warehouse-location                            | Struct          |                                                                                                                         |
| id                                                 | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| inspection-code                                    | Struct          |                                                                                                                         |
| inventory-transaction-lots                         | List            |                                                                                                                         |
| inventory-transaction-valuations                   | List            |                                                                                                                         |
| item                                               | Struct          |                                                                                                                         |
| last-exported-at                                   | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| match-reference                                    | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| order-line                                         | Struct          |                                                                                                                         |
| original-transaction                               | Struct          |                                                                                                                         |
| original-transaction-id                            | Integer         |                                                                                                                         |
| price                                              | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| quantity                                           | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| reason-insight                                     | Struct          |                                                                                                                         |
| receipt                                            | Struct          |                                                                                                                         |
| receipts-batch-id                                  | Integer         |                                                                                                                         |
| received-weight                                    | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| receiving-form-response                            | Struct          |                                                                                                                         |
| rfid-tag                                           | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| soft-close-for-receiving                           | Boolean         |                                                                                                                         |
| spend-load-id                                      | String          |                                                                                                                         |
| status                                             | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| to-warehouse                                       | Struct          |                                                                                                                         |
| to-warehouse-location                              | Struct          |                                                                                                                         |
| total                                              | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| transaction-date                                   | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| type                                               | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| uom                                                | Struct          |                                                                                                                         |
| updated-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| updated-by                                         | Struct          |                                                                                                                         |
| voided-value                                       | BigDecimal      | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| Requisition                                        | approvals       | List                                                                                                                    |                                                                                                                        |
| approver                                           | Struct          |                                                                                                                         |
| attachments                                        | List            |                                                                                                                         |
| buyer-note                                         | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| created-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| created-by                                         | Struct          |                                                                                                                         |
| currency                                           | Struct          |                                                                                                                         |
| current-approval                                   | Struct          |                                                                                                                         |
| custom-fields                                      | Struct          |                                                                                                                         |
| department                                         | Struct          |                                                                                                                         |
| exported                                           | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| external-po-reference                              | String          |                                                                                                                         |
| hide-price                                         | Struct          |                                                                                                                         |
| id                                                 | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| justification                                      | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| line-count                                         | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| milestones                                         | List            |                                                                                                                         |
| mobile-currency                                    | Struct          |                                                                                                                         |
| mobile-total                                       | BigDecimal      |                                                                                                                         |
| need-by-date                                       | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| pcard                                              | Struct          |                                                                                                                         |
| price-hidden                                       | Boolean         | EQUAL\_TO, NOT\_EQUAL\_TO                                                                                               |
| receiving-warehouse-id                             | Integer         |                                                                                                                         |
| recurring-rules                                    | List            |                                                                                                                         |
| reject-reason-comment                              | String          |                                                                                                                         |
| req-title                                          | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| requested-by                                       | Struct          |                                                                                                                         |
| requester                                          | Struct          |                                                                                                                         |
| ship-to-address                                    | Struct          |                                                                                                                         |
| ship-to-attention                                  | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| spend-load-id                                      | String          |                                                                                                                         |
| status                                             | String          | EQUAL\_TO, CONTAINS, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO |
| submitted-at                                       | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| taggings                                           | List            |                                                                                                                         |
| tags                                               | List            |                                                                                                                         |
| total                                              | BigDecimal      |                                                                                                                         |
| updated-at                                         | DateTime        | EQUAL\_TO, NOT\_EQUAL\_TO, BETWEEN, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO  |
| updated-by                                         | Struct          |                                                                                                                         |
| user-group-members                                 | List            |                                                                                                                         |
| user-members                                       | List            |                                                                                                                         |
| Requisition Line                                   | account         | Struct                                                                                                                  |                                                                                                                        |
| account-allocations                                | List            |                                                                                                                         |
| alternate-status                                   | String          |                                                                                                                         |
| asset-tags                                         | List            |                                                                                                                         |
| attachments                                        | List            |                                                                                                                         |
| commodity                                          | Struct          |                                                                                                                         |
| confirm-by-hrs                                     | BigDecimal      |                                                                                                                         |
| contract                                           | Struct          |                                                                                                                         |
| created-at                                         | DateTime        |                                                                                                                         |
| created-by                                         | Struct          |                                                                                                                         |
| currency                                           | Struct          |                                                                                                                         |
| description                                        | String          |                                                                                                                         |
| easy-form-response-id                              | Integer         |                                                                                                                         |
| extra-line-attribute                               | Struct          |                                                                                                                         |
| form-response                                      | List            |                                                                                                                         |
| id                                                 | Integer         |                                                                                                                         |
| image-url                                          | String          |                                                                                                                         |
| item                                               | Struct          |                                                                                                                         |
| line-num                                           | Integer         |                                                                                                                         |
| line-owner                                         | Struct          |                                                                                                                         |
| line-type                                          | String          |                                                                                                                         |
| manufacturer-name                                  | String          |                                                                                                                         |
| manufacturer-part-number                           | String          |                                                                                                                         |
| milestones                                         | List            |                                                                                                                         |
| minimum-order-quantity                             | BigDecimal      |                                                                                                                         |
| need-by-date                                       | DateTime        |                                                                                                                         |
| order-confirmation-level                           | String          |                                                                                                                         |
| order-increment                                    | String          |                                                                                                                         |
| order-line-id                                      | Integer         |                                                                                                                         |
| order-pad-line                                     | Struct          |                                                                                                                         |
| payment-term                                       | Struct          |                                                                                                                         |
| period                                             | Struct          |                                                                                                                         |
| punchout-site                                      | Struct          |                                                                                                                         |
| quantity                                           | BigDecimal      |                                                                                                                         |
| realtime-extension                                 | Struct          |                                                                                                                         |
| receipt-required                                   | Boolean         |                                                                                                                         |
| recurring-rules                                    | List            |                                                                                                                         |
| requisition-line-tax-detail                        | Struct          |                                                                                                                         |
| requisition\_id                                    | Integer         | EQUAL\_TO, NOT\_EQUAL\_TO, LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO           |
| service-type                                       | String          |                                                                                                                         |
| shipping-term                                      | Struct          |                                                                                                                         |
| source                                             | String          |                                                                                                                         |
| source-details                                     | String          |                                                                                                                         |
| source-part-num                                    | String          |                                                                                                                         |
| source-type                                        | String          |                                                                                                                         |
| spend-load-id                                      | String          |                                                                                                                         |
| status                                             | String          |                                                                                                                         |
| sub-line-num                                       | Integer         |                                                                                                                         |
| supp-aux-part-num                                  | String          |                                                                                                                         |
| supplier                                           | Struct          |                                                                                                                         |
| supplier-site                                      | Struct          |                                                                                                                         |
| supplier-site-id                                   | Integer         |                                                                                                                         |
| taggings                                           | List            |                                                                                                                         |
| tags                                               | List            |                                                                                                                         |
| total                                              | BigDecimal      |                                                                                                                         |
| transmission-emails                                | String          |                                                                                                                         |
| transmission-method-override                       | String          |                                                                                                                         |
| unit-price                                         | BigDecimal      |                                                                                                                         |
| unit-price-in-usd                                  | BigDecimal      |                                                                                                                         |
| unspsc-code                                        | String          |                                                                                                                         |
| uom                                                | Struct          |                                                                                                                         |
| updated-at                                         | DateTime        |                                                                                                                         |
| updated-by                                         | Struct          |                                                                                                                         |
| Supplier Information                               |                 |                                                                                                                         |                                                                                                                        |
