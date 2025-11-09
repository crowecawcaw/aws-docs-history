# Recharge connector for Amazon AppFlow

Recharge is a subscription payment solution designed for merchants to set up and
manage dynamic, recurring billing across web and mobile applications. If you're a
Recharge user, your account contains data about your customers, transactions,
subscriptions, and more. You can use Amazon AppFlow to transfer data from
Recharge to certain AWS services or other supported applications.

## Amazon AppFlow support for Recharge

Amazon AppFlow supports Recharge as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Recharge.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Recharge.

## Before you begin

To use Amazon AppFlow to transfer data from Recharge to supported destinations, you must meet these
requirements:

- You have an account with Recharge that contains the data that you want to transfer. For more
  information about the Recharge data objects that Amazon AppFlow supports, see [Supported objects](#recharge-objects "#recharge-objects").
- In your Recharge account, you've created an API token. For the steps to create
  this token, see [Recharge API key](https://docs.rechargepayments.com/docs/recharge-api-key "https://docs.rechargepayments.com/docs/recharge-api-key") in the Recharge documentation.
- You've configured the API token with read permissions that allow Amazon AppFlow to access the data
  that you want to transfer.

From your account settings, note your API token key because you provide this value to Amazon AppFlow
when you connect to your Recharge account.

## Connecting Amazon AppFlow to your Recharge

account

To connect Amazon AppFlow to your Recharge account, provide the API token from your
account settings.

###### To connect to Recharge

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Recharge**.
4. Choose **Create connection**.
5. In the **Connect to Recharge** window, for **API
   Token**, enter your API token key.
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
that uses Recharge as the data source, you can select this connection.

## Transferring data from Recharge with a flow

To transfer data from Recharge, create an Amazon AppFlow flow, and choose Recharge as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Recharge, see [Supported objects](#recharge-objects "#recharge-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#recharge-destinations "#recharge-destinations").

## Supported destinations

When you create a flow that uses Recharge as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Recharge as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                              | **Field**         | **Data type** | **Supported filters** |
| --------------------------------------- | ----------------- | ------------- | --------------------- |
| Address                                 | Address1          | String        |                       |
| Address2                                | String            |               |
| City                                    | String            |               |
| Company                                 | String            |               |
| Country Code                            | String            |               |
| Created At                              | DateTime          |               |
| Created At Max                          | DateTime          | EQUAL_TO      |
| Created At Min                          | DateTime          | EQUAL_TO      |
| Customer ID                             | Integer           | EQUAL_TO      |
| Discount Code                           | String            | EQUAL_TO      |
| Discount Id                             | String            | EQUAL_TO      |
| Discounts                               | List              |               |
| First Name                              | String            |               |
| Id                                      | Integer           |               |
| Is Active                               | Boolean           | EQUAL_TO      |
| Last Name                               | String            |               |
| Order Note                              | String            |               |
| Payment Method ID                       | Integer           |               |
| Phone                                   | String            |               |
| Presentment Currency                    | String            |               |
| Province                                | String            |               |
| Shipping Lines Conserved                | List              |               |
| Shipping Lines Override                 | List              |               |
| Updated At                              | DateTime          |               |
| Updated At Max                          | DateTime          | EQUAL_TO      |
| Updated At Min                          | DateTime          | EQUAL_TO      |
| Zip                                     | String            |               |
| Charge                                  | Address ID        | Integer       | EQUAL_TO              |
| Analytics Data                          | Struct            |               |
| Billing Address                         | Struct            |               |
| Charge Attempts                         | Integer           |               |
| Client Details                          | Struct            |               |
| Created At                              | DateTime          |               |
| Created At Max                          | DateTime          | EQUAL_TO      |
| Created At Min                          | DateTime          | EQUAL_TO      |
| Currency                                | String            |               |
| Customer                                | Struct            |               |
| Customer Id                             | String            | EQUAL_TO      |
| Discount Code                           | String            | EQUAL_TO      |
| Discount Id                             | String            | EQUAL_TO      |
| Discounts                               | List              |               |
| Error                                   | String            |               |
| Error Type                              | String            |               |
| External Order ID                       | Struct            |               |
| External Order ID E-Commerce            | String            | EQUAL_TO      |
| External Transaction ID                 | Struct            |               |
| External Variant Id not found           | Boolean           |               |
| Has Uncommitted Changes                 | Boolean           |               |
| Id                                      | Integer           |               |
| Include                                 | Struct            |               |
| Line Items                              | List              |               |
| Note                                    | String            |               |
| Order Attributes                        | List              |               |
| Orders Count                            | Integer           |               |
| Payment Processor                       | String            |               |
| Processed At                            | DateTime          |               |
| Processed At Max                        | DateTime          | EQUAL_TO      |
| Processed At Min                        | DateTime          | EQUAL_TO      |
| Purchase Item Id                        | String            | EQUAL_TO      |
| Retry Date                              | Date              |               |
| Scheduled At                            | Date              | EQUAL_TO      |
| Scheduled At Max                        | DateTime          | EQUAL_TO      |
| Scheduled At Min                        | DateTime          | EQUAL_TO      |
| Shipping Address                        | Struct            |               |
| Shipping Lines                          | List              |               |
| Sort By                                 | String            | EQUAL_TO      |
| Status                                  | String            | EQUAL_TO      |
| Subtotal Price                          | String            |               |
| Tags                                    | String            |               |
| Tax Lines                               | List              |               |
| Taxable                                 | Boolean           |               |
| Total Discounts                         | String            |               |
| Total Duties                            | String            |               |
| Total Line Items Price                  | String            |               |
| Total Price                             | String            |               |
| Total Refunds                           | String            |               |
| Total Tax                               | String            |               |
| Total Weight Grams                      | Integer           |               |
| Type                                    | String            |               |
| Updated At                              | DateTime          |               |
| Updated At Max                          | DateTime          | EQUAL_TO      |
| Updated At Min                          | DateTime          | EQUAL_TO      |
| Collection                              | Created At        | DateTime      |                       |
| Description                             | String            |               |
| Id                                      | Integer           |               |
| Sort Order                              | String            |               |
| Title                                   | String            | EQUAL_TO      |
| Type                                    | String            | EQUAL_TO      |
| Updated At                              | DateTime          |               |
| Customer                                | Analytics Data    | Struct        |                       |
| Created At                              | DateTime          |               |
| Created At Max                          | DateTime          | EQUAL_TO      |
| Created At Min                          | DateTime          | EQUAL_TO      |
| Email                                   | String            | EQUAL_TO      |
| External Customer Id                    | Struct            |               |
| External Customer Id E-Commerce         | String            | EQUAL_TO      |
| First Charge Processed At               | DateTime          |               |
| First Name                              | String            |               |
| Has Payment Method In Dunning           | Boolean           |               |
| Has Valid Payment Method                | Boolean           |               |
| Hash                                    | String            | EQUAL_TO      |
| Id                                      | Integer           |               |
| Include                                 | Struct            |               |
| Last Name                               | String            |               |
| Phone                                   | String            |               |
| Subscriptions Active Count              | Integer           |               |
| Subscriptions Total Count               | Integer           |               |
| Tax Exempt                              | Boolean           |               |
| Updated At                              | DateTime          |               |
| Updated At Max                          | DateTime          | EQUAL_TO      |
| Updated At Min                          | DateTime          | EQUAL_TO      |
| Discount                                | Applies To        | Struct        |                       |
| Channel Settings                        | Struct            |               |
| Code                                    | String            |               |
| Created At                              | DateTime          |               |
| Created At Max                          | DateTime          | EQUAL_TO      |
| Created At Min                          | DateTime          | EQUAL_TO      |
| Discount Code                           | String            | EQUAL_TO      |
| Discount Type                           | String            | EQUAL_TO      |
| Ends At                                 | DateTime          |               |
| External Discount Id                    | Struct            |               |
| External Discount Source                | String            |               |
| Id                                      | Integer           |               |
| Prerequisite Subtotal Min               | Integer           |               |
| Starts At                               | DateTime          |               |
| Status                                  | String            | EQUAL_TO      |
| Updated At                              | DateTime          |               |
| Updated At Max                          | DateTime          | EQUAL_TO      |
| Updated At Min                          | DateTime          | EQUAL_TO      |
| Usage Limits                            | Struct            |               |
| Value                                   | String            |               |
| Value Type                              | String            |               |
| Metafield                               | Created At        | DateTime      |                       |
| Description                             | String            |               |
| Id                                      | Integer           |               |
| Key                                     | String            |               |
| Namespace                               | String            | EQUAL_TO      |
| Owner Id                                | Integer           | EQUAL_TO      |
| Owner Resource                          | String            | EQUAL_TO      |
| Updated At                              | DateTime          |               |
| Value                                   | String            |               |
| Value Type                              | String            |               |
| Onetime                                 | Address Id        | Integer       | EQUAL_TO              |
| Created At                              | DateTime          |               |
| Created At Max                          | DateTime          | EQUAL_TO      |
| Created At Min                          | DateTime          | EQUAL_TO      |
| Customer Id                             | Integer           | EQUAL_TO      |
| External Product Id                     | Struct            |               |
| External Variant ID                     | Struct            |               |
| External Variant ID E-Commerce          | String            | EQUAL_TO      |
| Id                                      | Integer           |               |
| Include Cancelled                       | Boolean           | EQUAL_TO      |
| Is Cancelled                            | Boolean           |               |
| Next Charge Scheduled At                | DateTime          |               |
| Presentment Currency                    | String            |               |
| Price                                   | Integer           |               |
| Product Title                           | String            |               |
| Properties                              | List              |               |
| Quantity                                | Integer           |               |
| SKU                                     | String            |               |
| SKU Override                            | Boolean           |               |
| Updated At                              | DateTime          |               |
| Updated At Max                          | DateTime          | EQUAL_TO      |
| Updated At Min                          | DateTime          | EQUAL_TO      |
| Variant Title                           | String            |               |
| Order                                   | Address ID        | Integer       | EQUAL_TO              |
| Billing Address                         | Struct            |               |
| Charge                                  | Struct            |               |
| Charge Id                               | String            | EQUAL_TO      |
| Client Details                          | Struct            |               |
| Created At                              | DateTime          |               |
| Created At Max                          | DateTime          | EQUAL_TO      |
| Created At Min                          | DateTime          | EQUAL_TO      |
| Currency                                | String            |               |
| Customer                                | Struct            |               |
| Customer Id                             | String            | EQUAL_TO      |
| Discounts                               | List              |               |
| Error                                   | String            |               |
| External Cart Token                     | String            |               |
| External Customer Id                    | String            | EQUAL_TO      |
| External Order ID                       | Struct            |               |
| External Order ID E-Commerce            | String            | EQUAL_TO      |
| External Order Name                     | Struct            |               |
| External Order Number                   | Struct            |               |
| Has External Order                      | Boolean           | EQUAL_TO      |
| Id                                      | Integer           |               |
| Include                                 | Struct            |               |
| Is Prepaid                              | Boolean           |               |
| Line Items                              | List              |               |
| Note                                    | String            |               |
| Order Attributes                        | List              |               |
| Processed At                            | DateTime          |               |
| Purchase Item Id                        | String            | EQUAL_TO      |
| Scheduled At                            | DateTime          |               |
| Scheduled At Max                        | DateTime          | EQUAL_TO      |
| Scheduled At Min                        | DateTime          | EQUAL_TO      |
| Shipping Address                        | Struct            |               |
| Shipping Lines                          | List              |               |
| Status                                  | String            | EQUAL_TO      |
| Subtotal Price                          | String            |               |
| Tags                                    | String            |               |
| Tax Lines                               | List              |               |
| Taxable                                 | Boolean           |               |
| Total Discounts                         | String            |               |
| Total Duties                            | String            |               |
| Total Line Items Price                  | String            |               |
| Total Price                             | String            |               |
| Total Refunds                           | String            |               |
| Total Tax                               | String            |               |
| Total Weight Grams                      | Integer           |               |
| Type                                    | String            | EQUAL_TO      |
| Updated At                              | DateTime          |               |
| Updated At Max                          | DateTime          | EQUAL_TO      |
| Updated At Min                          | DateTime          | EQUAL_TO      |
| Store                                   | Checkout Logo Url | String        |                       |
| Checkout Platform                       | String            |               |
| Created At                              | DateTime          |               |
| Currency                                | String            |               |
| Customer Portal Base Url                | String            |               |
| Default Api Version                     | String            |               |
| Email                                   | String            |               |
| External Platform                       | String            |               |
| Id                                      | Integer           |               |
| Identifier                              | String            |               |
| Merchant Portal Base Url                | String            |               |
| Name                                    | String            |               |
| Phone                                   | String            |               |
| Timezone                                | Struct            |               |
| Updated At                              | DateTime          |               |
| Weight Unit                             | String            |               |
| Subscription                            | Address Id        | Integer       | EQUAL_TO              |
| Analytics Data                          | Struct            |               |
| Cancellation Reason                     | String            |               |
| Cancellation Reason Comments            | String            |               |
| Cancelled At                            | DateTime          |               |
| Charge Interval Frequency               | Integer           |               |
| Created At                              | DateTime          |               |
| Created At Max                          | DateTime          | EQUAL_TO      |
| Created At Min                          | DateTime          | EQUAL_TO      |
| Customer Id                             | Integer           | EQUAL_TO      |
| Expire After Specific Number Of Charges | Integer           |               |
| External Product Id                     | Struct            |               |
| External Variant ID E-Commerce          | String            | EQUAL_TO      |
| External Variant Id                     | Struct            |               |
| Has Queued Charges                      | Boolean           |               |
| Id                                      | Integer           |               |
| Include                                 | Struct            |               |
| Is Prepaid                              | Boolean           |               |
| Is Skippable                            | Boolean           |               |
| Is Swappable                            | Boolean           |               |
| Max Retries Reached                     | Boolean           |               |
| Next Charge Scheduled At                | Date              |               |
| Order Day Of Month                      | Integer           |               |
| Order Day Of Week                       | Integer           |               |
| Order Interval Frequency                | Integer           |               |
| Order Interval Unit                     | String            |               |
| Presentment Currency                    | String            |               |
| Price                                   | String            |               |
| Product Title                           | String            |               |
| Properties                              | List              |               |
| Quantity                                | Integer           |               |
| SKU                                     | String            |               |
| SKU Override                            | Boolean           |               |
| Status                                  | String            | EQUAL_TO      |
| Updated At                              | DateTime          |               |
| Updated At Max                          | DateTime          | EQUAL_TO      |
| Updated At Min                          | DateTime          | EQUAL_TO      |
| Variant Title                           | String            |               |
