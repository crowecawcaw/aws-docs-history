# Stripe connector for Amazon AppFlow

Stripe powers ecommerce with payment processing and other commerce solutions for
businesses. If you're a Stripe user, your account contains data about your
transactions, such as your balance, charges, and payouts. You can use Amazon AppFlow to transfer data from
Stripe to certain AWS services or other supported applications.

## Amazon AppFlow support for Stripe

Amazon AppFlow supports Stripe as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Stripe.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Stripe.

## Before you begin

Before you can use Amazon AppFlow to transfer data from Stripe, you must have a
Stripe account that contains the data to transfer. For more information about the
Stripe data objects that Amazon AppFlow supports, see [Supported objects](#stripe-objects "#stripe-objects").

From your Stripe account, you must obtain a test or live API key. You provide
this key to Amazon AppFlow when you connect to your Stripe account. For the steps to obtain
these keys, see [Manage
API keys](https://stripe.com/docs/development/dashboard/manage-api-keys "https://stripe.com/docs/development/dashboard/manage-api-keys") in the Stripe Docs.

## Connecting Amazon AppFlow to your Stripe

account

To connect Amazon AppFlow to your Stripe account, provide your API key so that Amazon AppFlow
can access your data. If you haven't yet configured your Stripe account for Amazon AppFlow
integration, see [Before you begin](#stripe-prereqs "#stripe-prereqs").

###### To connect to Stripe

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Stripe**.
4. Choose **Create connection**.
5. In the **Connect to Stripe** window, for **API
   Key**, enter a test or live API key from your Stripe account
   settings.
6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Stripe as the data source, you can select this connection.

## Transferring data from Stripe with a flow

To transfer data from Stripe, create an Amazon AppFlow flow, and choose Stripe as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Stripe, see [Supported objects](#stripe-objects "#stripe-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#stripe-destinations "#stripe-destinations").

## Supported destinations

When you create a flow that uses Stripe as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Stripe as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                        | **Field**          | **Data type**                                             | **Supported filters**                                     |
| --------------------------------- | ------------------ | --------------------------------------------------------- | --------------------------------------------------------- |
| Account                           | business_profile   | Struct                                                    |                                                           |
| capabilities                      | Struct             |                                                           |
| charges_enabled                   | Boolean            |                                                           |
| controller                        | Struct             |                                                           |
| country                           | String             |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| default_currency                  | String             |                                                           |
| details_submitted                 | Boolean            |                                                           |
| email                             | String             |                                                           |
| external_account                  | Struct             |                                                           |
| future_requirements               | Struct             |                                                           |
| id                                | Integer            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| payouts_enabled                   | Boolean            |                                                           |
| requirements                      | Struct             |                                                           |
| settings                          | Struct             |                                                           |
| type                              | String             |                                                           |
| Application Fee                   | account            | String                                                    |                                                           |
| amount                            | Integer            | EQUAL_TO                                                  |
| amount_refunded                   | Integer            | EQUAL_TO                                                  |
| application                       | String             |                                                           |
| balance_transaction               | String             |                                                           |
| charge                            | String             | EQUAL_TO                                                  |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             |                                                           |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| object                            | String             |                                                           |
| originating_transaction           | String             |                                                           |
| refunded                          | Boolean            | EQUAL_TO                                                  |
| refunds                           | List               |                                                           |
| Balance                           | amount             | Integer                                                   |                                                           |
| currency                          | String             |                                                           |
| source_types                      | Struct             |                                                           |
| Balance Transaction               | amount             | Integer                                                   |                                                           |
| available_on                      | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             |                                                           |
| description                       | String             |                                                           |
| exchange_rate                     | Double             |                                                           |
| fee                               | Integer            |                                                           |
| fee_details                       | List               |                                                           |
| id                                | String             |                                                           |
| net                               | Integer            |                                                           |
| object                            | String             |                                                           |
| reporting_category                | String             |                                                           |
| source                            | String             | EQUAL_TO                                                  |
| status                            | String             |                                                           |
| type                              | String             | EQUAL_TO                                                  |
| Charge                            | amount             | Integer                                                   | EQUAL_TO                                                  |
| amount_captured                   | Integer            |                                                           |
| amount_refunded                   | Integer            |                                                           |
| application                       | String             |                                                           |
| application_fee                   | String             |                                                           |
| application_fee_amount            | Integer            |                                                           |
| balance_transaction               | String             |                                                           |
| billing_details                   | Struct             |                                                           |
| calculated_statement_descriptor   | String             |                                                           |
| captured                          | Boolean            |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             |                                                           |
| customer                          | String             | EQUAL_TO                                                  |
| description                       | String             |                                                           |
| destination                       | String             |                                                           |
| dispute                           | String             |                                                           |
| disputed                          | Boolean            | EQUAL_TO                                                  |
| failure_balance_transaction       | String             |                                                           |
| failure_code                      | String             |                                                           |
| failure_message                   | String             |                                                           |
| fraud_details                     | Struct             |                                                           |
| id                                | String             |                                                           |
| invoice                           | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| on_behalf_of                      | String             |                                                           |
| order                             | String             |                                                           |
| outcome                           | Struct             |                                                           |
| paid                              | Boolean            |                                                           |
| payment_intent                    | String             | EQUAL_TO                                                  |
| payment_method                    | String             |                                                           |
| payment_method_details            | Struct             |                                                           |
| receipt_email                     | String             |                                                           |
| receipt_number                    | String             |                                                           |
| receipt_url                       | String             |                                                           |
| refunded                          | Boolean            | EQUAL_TO                                                  |
| refunds                           | Struct             |                                                           |
| review                            | String             |                                                           |
| shipping                          | Struct             |                                                           |
| source                            | String             |                                                           |
| source_transfer                   | String             |                                                           |
| statement_descriptor              | String             |                                                           |
| statement_descriptor_suffix       | String             |                                                           |
| status                            | String             |                                                           |
| transfer_data                     | Struct             |                                                           |
| transfer_group                    | String             | EQUAL_TO                                                  |
| Country Spec                      | default_currency   | String                                                    |                                                           |
| id                                | String             |                                                           |
| object                            | String             |                                                           |
| supported_bank_account_currencies | Struct             |                                                           |
| supported_payment_currencies      | List               |                                                           |
| supported_payment_methods         | List               |                                                           |
| supported_transfer_countries      | List               |                                                           |
| verification_fields               | Struct             |                                                           |
| Coupon                            | amount_off         | Integer                                                   |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             | EQUAL_TO                                                  |
| duration                          | String             | EQUAL_TO                                                  |
| duration_in_months                | Integer            | EQUAL_TO                                                  |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| max_redemptions                   | Integer            | EQUAL_TO                                                  |
| metadata                          | Struct             |                                                           |
| name                              | String             |                                                           |
| object                            | String             |                                                           |
| percent_off                       | Double             | EQUAL_TO                                                  |
| redeem_by                         | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| times_redeemed                    | Integer            |                                                           |
| valid                             | Boolean            |                                                           |
| Credit Note                       | amount             | Integer                                                   |                                                           |
| created                           | DateTime           |                                                           |
| currency                          | String             |                                                           |
| customer                          | String             | EQUAL_TO                                                  |
| customer_balance_transaction      | String             |                                                           |
| discount_amount                   | Integer            |                                                           |
| discount_amounts                  | List               |                                                           |
| id                                | String             |                                                           |
| invoice                           | String             | EQUAL_TO                                                  |
| lines                             | List               |                                                           |
| livemode                          | Boolean            |                                                           |
| memo                              | String             |                                                           |
| metadata                          | Struct             |                                                           |
| number                            | String             |                                                           |
| object                            | String             |                                                           |
| out_of_band_amount                | Integer            |                                                           |
| pdf                               | String             |                                                           |
| reason                            | String             |                                                           |
| refund                            | String             |                                                           |
| status                            | String             |                                                           |
| subtotal                          | Integer            |                                                           |
| tax_amounts                       | List               |                                                           |
| total                             | Integer            |                                                           |
| type                              | String             |                                                           |
| voided_at                         | DateTime           |                                                           |
| Customer                          | address            | Struct                                                    |                                                           |
| balance                           | Integer            |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             |                                                           |
| default_source                    | String             |                                                           |
| delinquent                        | Boolean            | EQUAL_TO                                                  |
| description                       | String             |                                                           |
| discount                          | Struct             |                                                           |
| email                             | String             | EQUAL_TO                                                  |
| id                                | String             |                                                           |
| invoice_prefix                    | String             |                                                           |
| invoice_settings                  | Struct             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| name                              | String             |                                                           |
| next_invoice_sequence             | Integer            |                                                           |
| object                            | String             |                                                           |
| phone                             | String             |                                                           |
| preferred_locales                 | List               |                                                           |
| shipping                          | Struct             |                                                           |
| tax_exempt                        | String             |                                                           |
| test_clock                        | String             |                                                           |
| Dispute                           | amount             | Integer                                                   | EQUAL_TO                                                  |
| balance_transaction               | String             |                                                           |
| balance_transactions              | List               |                                                           |
| charge                            | String             | EQUAL_TO                                                  |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             |                                                           |
| evidence                          | Struct             |                                                           |
| evidence_details                  | Struct             |                                                           |
| id                                | String             |                                                           |
| is_charge_refundable              | Boolean            |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| payment_intent                    | String             | EQUAL_TO                                                  |
| reason                            | String             | EQUAL_TO                                                  |
| status                            | String             | EQUAL_TO                                                  |
| Early Fraud Warning               | actionable         | Boolean                                                   |                                                           |
| charge                            | String             | EQUAL_TO                                                  |
| created                           | DateTime           |                                                           |
| fraud_type                        | String             |                                                           |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| object                            | String             |                                                           |
| payment_intent                    | String             | EQUAL_TO                                                  |
| File Link                         | created            | DateTime                                                  | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| expired                           | Boolean            | EQUAL_TO                                                  |
| expires_at                        | DateTime           |                                                           |
| file                              | String             | EQUAL_TO                                                  |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| url                               | String             |                                                           |
| Invoice                           | account_country    | String                                                    |                                                           |
| account_name                      | String             |                                                           |
| account_tax_ids                   | List               |                                                           |
| amount_due                        | Integer            |                                                           |
| amount_paid                       | Integer            |                                                           |
| amount_remaining                  | Integer            |                                                           |
| application                       | String             |                                                           |
| application_fee_amount            | Integer            |                                                           |
| attempt_count                     | Integer            |                                                           |
| attempted                         | Boolean            | EQUAL_TO                                                  |
| auto_advance                      | Boolean            | EQUAL_TO                                                  |
| automatic_tax                     | Struct             |                                                           |
| billing_reason                    | String             | EQUAL_TO                                                  |
| charge                            | String             |                                                           |
| collection_method                 | String             | EQUAL_TO                                                  |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             |                                                           |
| custom_fields                     | List               |                                                           |
| customer                          | String             | EQUAL_TO                                                  |
| customer_address                  | Struct             |                                                           |
| customer_email                    | String             |                                                           |
| customer_name                     | String             |                                                           |
| customer_phone                    | String             |                                                           |
| customer_shipping                 | Struct             |                                                           |
| customer_tax_exempt               | String             |                                                           |
| customer_tax_ids                  | List               |                                                           |
| default_payment_method            | String             |                                                           |
| default_source                    | String             |                                                           |
| default_tax_rates                 | List               |                                                           |
| description                       | String             |                                                           |
| discount                          | Struct             |                                                           |
| discounts                         | List               |                                                           |
| due_date                          | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| ending_balance                    | Integer            |                                                           |
| footer                            | String             |                                                           |
| hosted_invoice_url                | String             |                                                           |
| id                                | String             |                                                           |
| invoice_pdf                       | String             |                                                           |
| last_finalization_error           | Struct             |                                                           |
| lines                             | List               |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| next_payment_attempt              | DateTime           |                                                           |
| number                            | String             |                                                           |
| object                            | String             |                                                           |
| on_behalf_of                      | String             |                                                           |
| paid                              | Boolean            | EQUAL_TO                                                  |
| paid_out_of_band                  | Boolean            |                                                           |
| payment_intent                    | String             |                                                           |
| payment_settings                  | Struct             |                                                           |
| period_end                        | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| period_start                      | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| post_payment_credit_notes_amount  | Integer            |                                                           |
| pre_payment_credit_notes_amount   | Integer            |                                                           |
| quote                             | String             |                                                           |
| receipt_number                    | String             |                                                           |
| starting_balance                  | Integer            |                                                           |
| statement_descriptor              | String             |                                                           |
| status                            | String             | EQUAL_TO                                                  |
| status_transitions                | Struct             |                                                           |
| subscription                      | Integer            |                                                           |
| subtotal                          | Integer            | EQUAL_TO                                                  |
| tax                               | Integer            |                                                           |
| test_clock                        | String             |                                                           |
| total                             | Integer            | EQUAL_TO                                                  |
| total_discount_amounts            | List               |                                                           |
| total_tax_amounts                 | List               |                                                           |
| transfer_data                     | Struct             |                                                           |
| webhooks_delivered_at             | DateTime           |                                                           |
| Invoice Item                      | amount             | Integer                                                   | EQUAL_TO                                                  |
| currency                          | String             |                                                           |
| customer                          | String             | EQUAL_TO                                                  |
| date                              | DateTime           |                                                           |
| description                       | String             |                                                           |
| discountable                      | Boolean            |                                                           |
| discounts                         | List               |                                                           |
| id                                | String             |                                                           |
| invoice                           | String             | EQUAL_TO                                                  |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| period                            | Struct             |                                                           |
| plan                              | String             |                                                           |
| price                             | Struct             |                                                           |
| proration                         | Boolean            | EQUAL_TO                                                  |
| quantity                          | Integer            |                                                           |
| subscription                      | String             |                                                           |
| subscription_item                 | String             |                                                           |
| tax_rates                         | List               |                                                           |
| test_clock                        | String             |                                                           |
| unit_amount                       | Integer            |                                                           |
| unit_amount_decimal               | String             |                                                           |
| Payment Intent                    | amount             | Integer                                                   |                                                           |
| amount_capturable                 | Integer            |                                                           |
| amount_details                    | Struct             |                                                           |
| amount_received                   | Integer            |                                                           |
| application                       | String             |                                                           |
| application_fee_amount            | Integer            |                                                           |
| automatic_payment_methods         | Struct             |                                                           |
| canceled_at                       | DateTime           |                                                           |
| cancellation_reason               | String             |                                                           |
| capture_method                    | String             |                                                           |
| charges                           | List               |                                                           |
| client_secret                     | String             |                                                           |
| confirmation_method               | String             |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             |                                                           |
| customer                          | String             | EQUAL_TO                                                  |
| description                       | String             |                                                           |
| id                                | String             |                                                           |
| invoice                           | String             |                                                           |
| last_payment_error                | Struct             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| next_action                       | Struct             |                                                           |
| object                            | String             |                                                           |
| on_behalf_of                      | String             |                                                           |
| payment_method                    | String             |                                                           |
| payment_method_options            | Struct             |                                                           |
| payment_method_types              | List               |                                                           |
| processing                        | Struct             |                                                           |
| receipt_email                     | String             |                                                           |
| review                            | String             |                                                           |
| setup_future_usage                | String             |                                                           |
| shipping                          | Struct             |                                                           |
| source                            | String             |                                                           |
| statement_descriptor              | String             |                                                           |
| statement_descriptor_suffix       | String             |                                                           |
| status                            | String             |                                                           |
| transfer_data                     | Struct             |                                                           |
| transfer_group                    | String             |                                                           |
| Payout                            | amount             | Integer                                                   | EQUAL_TO                                                  |
| arrival_date                      | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| automatic                         | Boolean            |                                                           |
| balance_transaction               | String             |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             |                                                           |
| description                       | String             |                                                           |
| destination                       | String             | EQUAL_TO                                                  |
| failure_balance_transaction       | String             |                                                           |
| failure_code                      | String             |                                                           |
| failure_message                   | String             |                                                           |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| method                            | String             |                                                           |
| object                            | String             |                                                           |
| original_payout                   | String             |                                                           |
| reversed_by                       | String             |                                                           |
| source_type                       | String             |                                                           |
| statement_descriptor              | String             |                                                           |
| status                            | String             |                                                           |
| type                              | String             |                                                           |
| Plan                              | active             | Boolean                                                   | EQUAL_TO                                                  |
| aggregate_usage                   | String             |                                                           |
| amount                            | Integer            |                                                           |
| amount_decimal                    | String             |                                                           |
| billing_scheme                    | String             |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             | EQUAL_TO                                                  |
| id                                | String             |                                                           |
| interval                          | String             | EQUAL_TO                                                  |
| interval_count                    | Integer            |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| nickname                          | String             |                                                           |
| object                            | String             |                                                           |
| product                           | String             | EQUAL_TO                                                  |
| tiers_mode                        | String             |                                                           |
| transform_usage                   | Struct             |                                                           |
| trial_period_days                 | Integer            | EQUAL_TO                                                  |
| usage_type                        | String             |                                                           |
| Price                             | active             | Boolean                                                   | EQUAL_TO                                                  |
| billing_scheme                    | String             |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             | EQUAL_TO                                                  |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| lookup_key                        | String             |                                                           |
| metadata                          | Struct             |                                                           |
| nickname                          | String             |                                                           |
| object                            | String             |                                                           |
| product                           | String             | EQUAL_TO                                                  |
| recurring                         | Struct             |                                                           |
| tax_behaviour                     | String             |                                                           |
| tiers_mode                        | String             |                                                           |
| transform_quantity                | Struct             |                                                           |
| type                              | String             | EQUAL_TO                                                  |
| unit_amount                       | Integer            |                                                           |
| unit_amount_decimal               | String             |                                                           |
| Product                           | active             | Boolean                                                   | EQUAL_TO                                                  |
| attributes                        | List               |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| default_price                     | String             |                                                           |
| description                       | String             |                                                           |
| id                                | String             |                                                           |
| images                            | List               |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| name                              | String             |                                                           |
| object                            | String             |                                                           |
| package_dimensions                | Struct             |                                                           |
| shippable                         | Boolean            |                                                           |
| statement_descriptor              | String             |                                                           |
| tax_code                          | String             |                                                           |
| type                              | String             | EQUAL_TO                                                  |
| unit_label                        | String             |                                                           |
| updated                           | DateTime           |                                                           |
| url                               | String             |                                                           |
| Promotion Code                    | active             | Boolean                                                   | EQUAL_TO                                                  |
| code                              | String             | EQUAL_TO                                                  |
| coupon                            | Struct             |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| customer                          | String             |                                                           |
| expires_at                        | DateTime           |                                                           |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| max_redemptions                   | Integer            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| restrictions                      | Struct             |                                                           |
| times_redeemed                    | Integer            |                                                           |
| Quote                             | amount_subtotal    | Integer                                                   |                                                           |
| amount_total                      | Integer            |                                                           |
| application                       | String             |                                                           |
| application_fee_amount            | Integer            |                                                           |
| application_fee_percent           | Double             |                                                           |
| automatic_tax                     | Struct             |                                                           |
| collection_method                 | String             |                                                           |
| computed                          | Struct             |                                                           |
| created                           | DateTime           |                                                           |
| currency                          | String             |                                                           |
| customer                          | String             | EQUAL_TO                                                  |
| default_tax_rates                 | List               |                                                           |
| description                       | String             |                                                           |
| discounts                         | List               |                                                           |
| expires_at                        | DateTime           |                                                           |
| footer                            | String             |                                                           |
| from_quote                        | Struct             |                                                           |
| header                            | String             |                                                           |
| id                                | String             |                                                           |
| invoice                           | String             |                                                           |
| invoice_settings                  | Struct             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| number                            | String             |                                                           |
| object                            | String             |                                                           |
| on_behalf_of                      | String             |                                                           |
| status                            | String             | EQUAL_TO                                                  |
| status_transitions                | Struct             |                                                           |
| subscription                      | String             |                                                           |
| subscription_data                 | Struct             |                                                           |
| subscription_schedule             | String             |                                                           |
| test_clock                        | String             |                                                           |
| total_details                     | Struct             |                                                           |
| transfer_data                     | Struct             |                                                           |
| Refund                            | amount             | Integer                                                   |                                                           |
| balance_transaction               | String             |                                                           |
| charge                            | String             | EQUAL_TO                                                  |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             |                                                           |
| id                                | String             |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| payment_intent                    | String             | EQUAL_TO                                                  |
| reason                            | String             |                                                           |
| receipt_number                    | String             |                                                           |
| source_transfer_reversal          | String             |                                                           |
| status                            | String             |                                                           |
| transfer_reversal                 | String             |                                                           |
| Report Type                       | data_available_end | DateTime                                                  |                                                           |
| data_available_start              | DateTime           |                                                           |
| default_columns                   | List               |                                                           |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| name                              | String             |                                                           |
| object                            | String             |                                                           |
| updated                           | DateTime           |                                                           |
| version                           | Integer            |                                                           |
| Session                           | after_expiration   | Struct                                                    |                                                           |
| allow_promotion_codes             | Boolean            |                                                           |
| amount_subtotal                   | Integer            |                                                           |
| amount_total                      | Integer            |                                                           |
| automatic_tax                     | Struct             |                                                           |
| billing_address_collection        | String             |                                                           |
| cancel_url                        | String             |                                                           |
| client_reference_id               | String             |                                                           |
| consent                           | Struct             |                                                           |
| consent_collection                | Struct             |                                                           |
| currency                          | String             |                                                           |
| customer                          | String             |                                                           |
| customer_creation                 | String             |                                                           |
| customer_details                  | Struct             |                                                           |
| customer_email                    | String             |                                                           |
| expires_at                        | DateTime           |                                                           |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| locale                            | String             |                                                           |
| metadata                          | Struct             |                                                           |
| mode                              | String             |                                                           |
| object                            | String             |                                                           |
| payment_intent                    | String             | EQUAL_TO                                                  |
| payment_link                      | String             |                                                           |
| payment_method_options            | Struct             |                                                           |
| payment_method_types              | List               |                                                           |
| payment_status                    | String             |                                                           |
| phone_number_collection           | Struct             |                                                           |
| recovered_from                    | String             |                                                           |
| setup_intent                      | String             |                                                           |
| shipping                          | Struct             |                                                           |
| shipping_address_collection       | Struct             |                                                           |
| shipping_options                  | Struct             |                                                           |
| shipping_rate                     | String             |                                                           |
| status                            | String             |                                                           |
| submit_type                       | String             |                                                           |
| subscription                      | String             |                                                           |
| success_url                       | String             |                                                           |
| total_details                     | Struct             |                                                           |
| url                               | String             |                                                           |
| Setup Intent                      | application        | String                                                    |                                                           |
| cancellation_reason               | String             |                                                           |
| client_secret                     | String             |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| customer                          | String             | EQUAL_TO                                                  |
| description                       | String             |                                                           |
| id                                | String             |                                                           |
| last_setup_error                  | Struct             |                                                           |
| latest_attempt                    | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| mandate                           | String             |                                                           |
| metadata                          | Struct             |                                                           |
| next_action                       | Struct             |                                                           |
| object                            | String             |                                                           |
| on_behalf_of                      | String             |                                                           |
| payment_method                    | String             |                                                           |
| payment_method_options            | Struct             |                                                           |
| payment_method_types              | List               |                                                           |
| single_use_mandate                | String             |                                                           |
| status                            | String             |                                                           |
| usage                             | String             |                                                           |
| Shipping Rate                     | active             | Boolean                                                   | EQUAL_TO                                                  |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| delivery_estimate                 | Struct             |                                                           |
| display_name                      | String             |                                                           |
| fixed_amount                      | Struct             |                                                           |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| tax_behavior                      | String             |                                                           |
| tax_code                          | String             |                                                           |
| type                              | String             |                                                           |
| Subscription                      | application        | String                                                    |                                                           |
| application_fee_percent           | Double             |                                                           |
| automatic_tax                     | Struct             |                                                           |
| billing_cycle_anchor              | DateTime           |                                                           |
| billing_thresholds                | Struct             |                                                           |
| cancel_at                         | DateTime           |                                                           |
| cancel_at_period_end              | Boolean            |                                                           |
| canceled_at                       | DateTime           |                                                           |
| collection_method                 | String             | EQUAL_TO                                                  |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| current_period_end                | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| current_period_start              | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| customer                          | String             | EQUAL_TO                                                  |
| days_until_due                    | Integer            |                                                           |
| default_payment_method            | String             |                                                           |
| default_source                    | String             |                                                           |
| default_tax_rates                 | List               |                                                           |
| description                       | String             |                                                           |
| discount                          | Struct             |                                                           |
| ended_at                          | DateTime           |                                                           |
| id                                | String             |                                                           |
| items                             | List               |                                                           |
| latest_invoice                    | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| next_pending_invoice_item_invoice | DateTime           |                                                           |
| object                            | String             |                                                           |
| pause_collection                  | Struct             |                                                           |
| payment_settings                  | Struct             |                                                           |
| pending_invoice_item_interval     | Struct             |                                                           |
| pending_setup_intent              | String             |                                                           |
| pending_update                    | Struct             |                                                           |
| plan                              | Struct             |                                                           |
| quantity                          | Integer            |                                                           |
| schedule                          | String             |                                                           |
| start_date                        | DateTime           |                                                           |
| status                            | String             | EQUAL_TO                                                  |
| test_clock                        | String             |                                                           |
| transfer_data                     | Struct             |                                                           |
| trial_end                         | DateTime           |                                                           |
| trial_start                       | DateTime           |                                                           |
| Subscription Item                 | billing_thresholds | Struct                                                    |                                                           |
| created                           | DateTime           |                                                           |
| id                                | String             |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| plan                              | Struct             |                                                           |
| price                             | Struct             |                                                           |
| subscription                      | String             |                                                           |
| tax_rates                         | List               |                                                           |
| Subscription Schedule             | application        | String                                                    |                                                           |
| canceled_at                       | DateTime           |                                                           |
| completed_at                      | DateTime           |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| current_phase                     | Struct             |                                                           |
| customer                          | String             | EQUAL_TO                                                  |
| default_settings                  | Struct             |                                                           |
| end_behavior                      | String             |                                                           |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| phases                            | List               |                                                           |
| released_at                       | DateTime           |                                                           |
| released_subscription             | String             |                                                           |
| renewal_interval                  | String             |                                                           |
| status                            | String             |                                                           |
| subscription                      | String             |                                                           |
| test_clock                        | String             |                                                           |
| Tax Code                          | description        | String                                                    |                                                           |
| id                                | String             |                                                           |
| name                              | String             |                                                           |
| object                            | String             |                                                           |
| Tax Rate                          | active             | Boolean                                                   | EQUAL_TO                                                  |
| country                           | String             |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| description                       | String             |                                                           |
| display_name                      | String             |                                                           |
| id                                | String             |                                                           |
| inclusive                         | Boolean            | EQUAL_TO                                                  |
| jurisdiction                      | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| percentage                        | Double             |                                                           |
| state                             | String             |                                                           |
| tax_type                          | String             |                                                           |
| Transfer                          | amount             | Integer                                                   | EQUAL_TO                                                  |
| amount_reversed                   | Integer            |                                                           |
| balance_transaction               | String             |                                                           |
| created                           | DateTime           | EQUAL_TO, GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO |
| currency                          | String             | EQUAL_TO                                                  |
| description                       | String             |                                                           |
| destination                       | String             | EQUAL_TO                                                  |
| destination_payment               | String             |                                                           |
| id                                | String             |                                                           |
| livemode                          | Boolean            |                                                           |
| metadata                          | Struct             |                                                           |
| object                            | String             |                                                           |
| reversals                         | List               |                                                           |
| reversed                          | Boolean            |                                                           |
| source_transaction                | String             |                                                           |
| source_type                       | String             |                                                           |
| transfer_group                    | String             | EQUAL_TO                                                  |
