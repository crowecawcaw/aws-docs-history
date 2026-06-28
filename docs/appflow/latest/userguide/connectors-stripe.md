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

## Connecting Amazon AppFlow to your Stripe account

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

| **Object**                            | **Field**            | **Data type**                                                      | **Supported filters**                                              |
| ------------------------------------- | -------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Account                               | business\_profile    | Struct                                                             |                                                                    |
| capabilities                          | Struct               |                                                                    |
| charges\_enabled                      | Boolean              |                                                                    |
| controller                            | Struct               |                                                                    |
| country                               | String               |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| default\_currency                     | String               |                                                                    |
| details\_submitted                    | Boolean              |                                                                    |
| email                                 | String               |                                                                    |
| external\_account                     | Struct               |                                                                    |
| future\_requirements                  | Struct               |                                                                    |
| id                                    | Integer              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| payouts\_enabled                      | Boolean              |                                                                    |
| requirements                          | Struct               |                                                                    |
| settings                              | Struct               |                                                                    |
| type                                  | String               |                                                                    |
| Application Fee                       | account              | String                                                             |                                                                    |
| amount                                | Integer              | EQUAL\_TO                                                          |
| amount\_refunded                      | Integer              | EQUAL\_TO                                                          |
| application                           | String               |                                                                    |
| balance\_transaction                  | String               |                                                                    |
| charge                                | String               | EQUAL\_TO                                                          |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               |                                                                    |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| object                                | String               |                                                                    |
| originating\_transaction              | String               |                                                                    |
| refunded                              | Boolean              | EQUAL\_TO                                                          |
| refunds                               | List                 |                                                                    |
| Balance                               | amount               | Integer                                                            |                                                                    |
| currency                              | String               |                                                                    |
| source\_types                         | Struct               |                                                                    |
| Balance Transaction                   | amount               | Integer                                                            |                                                                    |
| available\_on                         | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               |                                                                    |
| description                           | String               |                                                                    |
| exchange\_rate                        | Double               |                                                                    |
| fee                                   | Integer              |                                                                    |
| fee\_details                          | List                 |                                                                    |
| id                                    | String               |                                                                    |
| net                                   | Integer              |                                                                    |
| object                                | String               |                                                                    |
| reporting\_category                   | String               |                                                                    |
| source                                | String               | EQUAL\_TO                                                          |
| status                                | String               |                                                                    |
| type                                  | String               | EQUAL\_TO                                                          |
| Charge                                | amount               | Integer                                                            | EQUAL\_TO                                                          |
| amount\_captured                      | Integer              |                                                                    |
| amount\_refunded                      | Integer              |                                                                    |
| application                           | String               |                                                                    |
| application\_fee                      | String               |                                                                    |
| application\_fee\_amount              | Integer              |                                                                    |
| balance\_transaction                  | String               |                                                                    |
| billing\_details                      | Struct               |                                                                    |
| calculated\_statement\_descriptor     | String               |                                                                    |
| captured                              | Boolean              |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               |                                                                    |
| customer                              | String               | EQUAL\_TO                                                          |
| description                           | String               |                                                                    |
| destination                           | String               |                                                                    |
| dispute                               | String               |                                                                    |
| disputed                              | Boolean              | EQUAL\_TO                                                          |
| failure\_balance\_transaction         | String               |                                                                    |
| failure\_code                         | String               |                                                                    |
| failure\_message                      | String               |                                                                    |
| fraud\_details                        | Struct               |                                                                    |
| id                                    | String               |                                                                    |
| invoice                               | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| on\_behalf\_of                        | String               |                                                                    |
| order                                 | String               |                                                                    |
| outcome                               | Struct               |                                                                    |
| paid                                  | Boolean              |                                                                    |
| payment\_intent                       | String               | EQUAL\_TO                                                          |
| payment\_method                       | String               |                                                                    |
| payment\_method\_details              | Struct               |                                                                    |
| receipt\_email                        | String               |                                                                    |
| receipt\_number                       | String               |                                                                    |
| receipt\_url                          | String               |                                                                    |
| refunded                              | Boolean              | EQUAL\_TO                                                          |
| refunds                               | Struct               |                                                                    |
| review                                | String               |                                                                    |
| shipping                              | Struct               |                                                                    |
| source                                | String               |                                                                    |
| source\_transfer                      | String               |                                                                    |
| statement\_descriptor                 | String               |                                                                    |
| statement\_descriptor\_suffix         | String               |                                                                    |
| status                                | String               |                                                                    |
| transfer\_data                        | Struct               |                                                                    |
| transfer\_group                       | String               | EQUAL\_TO                                                          |
| Country Spec                          | default\_currency    | String                                                             |                                                                    |
| id                                    | String               |                                                                    |
| object                                | String               |                                                                    |
| supported\_bank\_account\_currencies  | Struct               |                                                                    |
| supported\_payment\_currencies        | List                 |                                                                    |
| supported\_payment\_methods           | List                 |                                                                    |
| supported\_transfer\_countries        | List                 |                                                                    |
| verification\_fields                  | Struct               |                                                                    |
| Coupon                                | amount\_off          | Integer                                                            |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               | EQUAL\_TO                                                          |
| duration                              | String               | EQUAL\_TO                                                          |
| duration\_in\_months                  | Integer              | EQUAL\_TO                                                          |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| max\_redemptions                      | Integer              | EQUAL\_TO                                                          |
| metadata                              | Struct               |                                                                    |
| name                                  | String               |                                                                    |
| object                                | String               |                                                                    |
| percent\_off                          | Double               | EQUAL\_TO                                                          |
| redeem\_by                            | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| times\_redeemed                       | Integer              |                                                                    |
| valid                                 | Boolean              |                                                                    |
| Credit Note                           | amount               | Integer                                                            |                                                                    |
| created                               | DateTime             |                                                                    |
| currency                              | String               |                                                                    |
| customer                              | String               | EQUAL\_TO                                                          |
| customer\_balance\_transaction        | String               |                                                                    |
| discount\_amount                      | Integer              |                                                                    |
| discount\_amounts                     | List                 |                                                                    |
| id                                    | String               |                                                                    |
| invoice                               | String               | EQUAL\_TO                                                          |
| lines                                 | List                 |                                                                    |
| livemode                              | Boolean              |                                                                    |
| memo                                  | String               |                                                                    |
| metadata                              | Struct               |                                                                    |
| number                                | String               |                                                                    |
| object                                | String               |                                                                    |
| out\_of\_band\_amount                 | Integer              |                                                                    |
| pdf                                   | String               |                                                                    |
| reason                                | String               |                                                                    |
| refund                                | String               |                                                                    |
| status                                | String               |                                                                    |
| subtotal                              | Integer              |                                                                    |
| tax\_amounts                          | List                 |                                                                    |
| total                                 | Integer              |                                                                    |
| type                                  | String               |                                                                    |
| voided\_at                            | DateTime             |                                                                    |
| Customer                              | address              | Struct                                                             |                                                                    |
| balance                               | Integer              |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               |                                                                    |
| default\_source                       | String               |                                                                    |
| delinquent                            | Boolean              | EQUAL\_TO                                                          |
| description                           | String               |                                                                    |
| discount                              | Struct               |                                                                    |
| email                                 | String               | EQUAL\_TO                                                          |
| id                                    | String               |                                                                    |
| invoice\_prefix                       | String               |                                                                    |
| invoice\_settings                     | Struct               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| name                                  | String               |                                                                    |
| next\_invoice\_sequence               | Integer              |                                                                    |
| object                                | String               |                                                                    |
| phone                                 | String               |                                                                    |
| preferred\_locales                    | List                 |                                                                    |
| shipping                              | Struct               |                                                                    |
| tax\_exempt                           | String               |                                                                    |
| test\_clock                           | String               |                                                                    |
| Dispute                               | amount               | Integer                                                            | EQUAL\_TO                                                          |
| balance\_transaction                  | String               |                                                                    |
| balance\_transactions                 | List                 |                                                                    |
| charge                                | String               | EQUAL\_TO                                                          |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               |                                                                    |
| evidence                              | Struct               |                                                                    |
| evidence\_details                     | Struct               |                                                                    |
| id                                    | String               |                                                                    |
| is\_charge\_refundable                | Boolean              |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| payment\_intent                       | String               | EQUAL\_TO                                                          |
| reason                                | String               | EQUAL\_TO                                                          |
| status                                | String               | EQUAL\_TO                                                          |
| Early Fraud Warning                   | actionable           | Boolean                                                            |                                                                    |
| charge                                | String               | EQUAL\_TO                                                          |
| created                               | DateTime             |                                                                    |
| fraud\_type                           | String               |                                                                    |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| object                                | String               |                                                                    |
| payment\_intent                       | String               | EQUAL\_TO                                                          |
| File Link                             | created              | DateTime                                                           | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| expired                               | Boolean              | EQUAL\_TO                                                          |
| expires\_at                           | DateTime             |                                                                    |
| file                                  | String               | EQUAL\_TO                                                          |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| url                                   | String               |                                                                    |
| Invoice                               | account\_country     | String                                                             |                                                                    |
| account\_name                         | String               |                                                                    |
| account\_tax\_ids                     | List                 |                                                                    |
| amount\_due                           | Integer              |                                                                    |
| amount\_paid                          | Integer              |                                                                    |
| amount\_remaining                     | Integer              |                                                                    |
| application                           | String               |                                                                    |
| application\_fee\_amount              | Integer              |                                                                    |
| attempt\_count                        | Integer              |                                                                    |
| attempted                             | Boolean              | EQUAL\_TO                                                          |
| auto\_advance                         | Boolean              | EQUAL\_TO                                                          |
| automatic\_tax                        | Struct               |                                                                    |
| billing\_reason                       | String               | EQUAL\_TO                                                          |
| charge                                | String               |                                                                    |
| collection\_method                    | String               | EQUAL\_TO                                                          |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               |                                                                    |
| custom\_fields                        | List                 |                                                                    |
| customer                              | String               | EQUAL\_TO                                                          |
| customer\_address                     | Struct               |                                                                    |
| customer\_email                       | String               |                                                                    |
| customer\_name                        | String               |                                                                    |
| customer\_phone                       | String               |                                                                    |
| customer\_shipping                    | Struct               |                                                                    |
| customer\_tax\_exempt                 | String               |                                                                    |
| customer\_tax\_ids                    | List                 |                                                                    |
| default\_payment\_method              | String               |                                                                    |
| default\_source                       | String               |                                                                    |
| default\_tax\_rates                   | List                 |                                                                    |
| description                           | String               |                                                                    |
| discount                              | Struct               |                                                                    |
| discounts                             | List                 |                                                                    |
| due\_date                             | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| ending\_balance                       | Integer              |                                                                    |
| footer                                | String               |                                                                    |
| hosted\_invoice\_url                  | String               |                                                                    |
| id                                    | String               |                                                                    |
| invoice\_pdf                          | String               |                                                                    |
| last\_finalization\_error             | Struct               |                                                                    |
| lines                                 | List                 |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| next\_payment\_attempt                | DateTime             |                                                                    |
| number                                | String               |                                                                    |
| object                                | String               |                                                                    |
| on\_behalf\_of                        | String               |                                                                    |
| paid                                  | Boolean              | EQUAL\_TO                                                          |
| paid\_out\_of\_band                   | Boolean              |                                                                    |
| payment\_intent                       | String               |                                                                    |
| payment\_settings                     | Struct               |                                                                    |
| period\_end                           | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| period\_start                         | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| post\_payment\_credit\_notes\_amount  | Integer              |                                                                    |
| pre\_payment\_credit\_notes\_amount   | Integer              |                                                                    |
| quote                                 | String               |                                                                    |
| receipt\_number                       | String               |                                                                    |
| starting\_balance                     | Integer              |                                                                    |
| statement\_descriptor                 | String               |                                                                    |
| status                                | String               | EQUAL\_TO                                                          |
| status\_transitions                   | Struct               |                                                                    |
| subscription                          | Integer              |                                                                    |
| subtotal                              | Integer              | EQUAL\_TO                                                          |
| tax                                   | Integer              |                                                                    |
| test\_clock                           | String               |                                                                    |
| total                                 | Integer              | EQUAL\_TO                                                          |
| total\_discount\_amounts              | List                 |                                                                    |
| total\_tax\_amounts                   | List                 |                                                                    |
| transfer\_data                        | Struct               |                                                                    |
| webhooks\_delivered\_at               | DateTime             |                                                                    |
| Invoice Item                          | amount               | Integer                                                            | EQUAL\_TO                                                          |
| currency                              | String               |                                                                    |
| customer                              | String               | EQUAL\_TO                                                          |
| date                                  | DateTime             |                                                                    |
| description                           | String               |                                                                    |
| discountable                          | Boolean              |                                                                    |
| discounts                             | List                 |                                                                    |
| id                                    | String               |                                                                    |
| invoice                               | String               | EQUAL\_TO                                                          |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| period                                | Struct               |                                                                    |
| plan                                  | String               |                                                                    |
| price                                 | Struct               |                                                                    |
| proration                             | Boolean              | EQUAL\_TO                                                          |
| quantity                              | Integer              |                                                                    |
| subscription                          | String               |                                                                    |
| subscription\_item                    | String               |                                                                    |
| tax\_rates                            | List                 |                                                                    |
| test\_clock                           | String               |                                                                    |
| unit\_amount                          | Integer              |                                                                    |
| unit\_amount\_decimal                 | String               |                                                                    |
| Payment Intent                        | amount               | Integer                                                            |                                                                    |
| amount\_capturable                    | Integer              |                                                                    |
| amount\_details                       | Struct               |                                                                    |
| amount\_received                      | Integer              |                                                                    |
| application                           | String               |                                                                    |
| application\_fee\_amount              | Integer              |                                                                    |
| automatic\_payment\_methods           | Struct               |                                                                    |
| canceled\_at                          | DateTime             |                                                                    |
| cancellation\_reason                  | String               |                                                                    |
| capture\_method                       | String               |                                                                    |
| charges                               | List                 |                                                                    |
| client\_secret                        | String               |                                                                    |
| confirmation\_method                  | String               |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               |                                                                    |
| customer                              | String               | EQUAL\_TO                                                          |
| description                           | String               |                                                                    |
| id                                    | String               |                                                                    |
| invoice                               | String               |                                                                    |
| last\_payment\_error                  | Struct               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| next\_action                          | Struct               |                                                                    |
| object                                | String               |                                                                    |
| on\_behalf\_of                        | String               |                                                                    |
| payment\_method                       | String               |                                                                    |
| payment\_method\_options              | Struct               |                                                                    |
| payment\_method\_types                | List                 |                                                                    |
| processing                            | Struct               |                                                                    |
| receipt\_email                        | String               |                                                                    |
| review                                | String               |                                                                    |
| setup\_future\_usage                  | String               |                                                                    |
| shipping                              | Struct               |                                                                    |
| source                                | String               |                                                                    |
| statement\_descriptor                 | String               |                                                                    |
| statement\_descriptor\_suffix         | String               |                                                                    |
| status                                | String               |                                                                    |
| transfer\_data                        | Struct               |                                                                    |
| transfer\_group                       | String               |                                                                    |
| Payout                                | amount               | Integer                                                            | EQUAL\_TO                                                          |
| arrival\_date                         | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| automatic                             | Boolean              |                                                                    |
| balance\_transaction                  | String               |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               |                                                                    |
| description                           | String               |                                                                    |
| destination                           | String               | EQUAL\_TO                                                          |
| failure\_balance\_transaction         | String               |                                                                    |
| failure\_code                         | String               |                                                                    |
| failure\_message                      | String               |                                                                    |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| method                                | String               |                                                                    |
| object                                | String               |                                                                    |
| original\_payout                      | String               |                                                                    |
| reversed\_by                          | String               |                                                                    |
| source\_type                          | String               |                                                                    |
| statement\_descriptor                 | String               |                                                                    |
| status                                | String               |                                                                    |
| type                                  | String               |                                                                    |
| Plan                                  | active               | Boolean                                                            | EQUAL\_TO                                                          |
| aggregate\_usage                      | String               |                                                                    |
| amount                                | Integer              |                                                                    |
| amount\_decimal                       | String               |                                                                    |
| billing\_scheme                       | String               |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               | EQUAL\_TO                                                          |
| id                                    | String               |                                                                    |
| interval                              | String               | EQUAL\_TO                                                          |
| interval\_count                       | Integer              |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| nickname                              | String               |                                                                    |
| object                                | String               |                                                                    |
| product                               | String               | EQUAL\_TO                                                          |
| tiers\_mode                           | String               |                                                                    |
| transform\_usage                      | Struct               |                                                                    |
| trial\_period\_days                   | Integer              | EQUAL\_TO                                                          |
| usage\_type                           | String               |                                                                    |
| Price                                 | active               | Boolean                                                            | EQUAL\_TO                                                          |
| billing\_scheme                       | String               |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               | EQUAL\_TO                                                          |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| lookup\_key                           | String               |                                                                    |
| metadata                              | Struct               |                                                                    |
| nickname                              | String               |                                                                    |
| object                                | String               |                                                                    |
| product                               | String               | EQUAL\_TO                                                          |
| recurring                             | Struct               |                                                                    |
| tax\_behaviour                        | String               |                                                                    |
| tiers\_mode                           | String               |                                                                    |
| transform\_quantity                   | Struct               |                                                                    |
| type                                  | String               | EQUAL\_TO                                                          |
| unit\_amount                          | Integer              |                                                                    |
| unit\_amount\_decimal                 | String               |                                                                    |
| Product                               | active               | Boolean                                                            | EQUAL\_TO                                                          |
| attributes                            | List                 |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| default\_price                        | String               |                                                                    |
| description                           | String               |                                                                    |
| id                                    | String               |                                                                    |
| images                                | List                 |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| name                                  | String               |                                                                    |
| object                                | String               |                                                                    |
| package\_dimensions                   | Struct               |                                                                    |
| shippable                             | Boolean              |                                                                    |
| statement\_descriptor                 | String               |                                                                    |
| tax\_code                             | String               |                                                                    |
| type                                  | String               | EQUAL\_TO                                                          |
| unit\_label                           | String               |                                                                    |
| updated                               | DateTime             |                                                                    |
| url                                   | String               |                                                                    |
| Promotion Code                        | active               | Boolean                                                            | EQUAL\_TO                                                          |
| code                                  | String               | EQUAL\_TO                                                          |
| coupon                                | Struct               |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| customer                              | String               |                                                                    |
| expires\_at                           | DateTime             |                                                                    |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| max\_redemptions                      | Integer              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| restrictions                          | Struct               |                                                                    |
| times\_redeemed                       | Integer              |                                                                    |
| Quote                                 | amount\_subtotal     | Integer                                                            |                                                                    |
| amount\_total                         | Integer              |                                                                    |
| application                           | String               |                                                                    |
| application\_fee\_amount              | Integer              |                                                                    |
| application\_fee\_percent             | Double               |                                                                    |
| automatic\_tax                        | Struct               |                                                                    |
| collection\_method                    | String               |                                                                    |
| computed                              | Struct               |                                                                    |
| created                               | DateTime             |                                                                    |
| currency                              | String               |                                                                    |
| customer                              | String               | EQUAL\_TO                                                          |
| default\_tax\_rates                   | List                 |                                                                    |
| description                           | String               |                                                                    |
| discounts                             | List                 |                                                                    |
| expires\_at                           | DateTime             |                                                                    |
| footer                                | String               |                                                                    |
| from\_quote                           | Struct               |                                                                    |
| header                                | String               |                                                                    |
| id                                    | String               |                                                                    |
| invoice                               | String               |                                                                    |
| invoice\_settings                     | Struct               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| number                                | String               |                                                                    |
| object                                | String               |                                                                    |
| on\_behalf\_of                        | String               |                                                                    |
| status                                | String               | EQUAL\_TO                                                          |
| status\_transitions                   | Struct               |                                                                    |
| subscription                          | String               |                                                                    |
| subscription\_data                    | Struct               |                                                                    |
| subscription\_schedule                | String               |                                                                    |
| test\_clock                           | String               |                                                                    |
| total\_details                        | Struct               |                                                                    |
| transfer\_data                        | Struct               |                                                                    |
| Refund                                | amount               | Integer                                                            |                                                                    |
| balance\_transaction                  | String               |                                                                    |
| charge                                | String               | EQUAL\_TO                                                          |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               |                                                                    |
| id                                    | String               |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| payment\_intent                       | String               | EQUAL\_TO                                                          |
| reason                                | String               |                                                                    |
| receipt\_number                       | String               |                                                                    |
| source\_transfer\_reversal            | String               |                                                                    |
| status                                | String               |                                                                    |
| transfer\_reversal                    | String               |                                                                    |
| Report Type                           | data\_available\_end | DateTime                                                           |                                                                    |
| data\_available\_start                | DateTime             |                                                                    |
| default\_columns                      | List                 |                                                                    |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| name                                  | String               |                                                                    |
| object                                | String               |                                                                    |
| updated                               | DateTime             |                                                                    |
| version                               | Integer              |                                                                    |
| Session                               | after\_expiration    | Struct                                                             |                                                                    |
| allow\_promotion\_codes               | Boolean              |                                                                    |
| amount\_subtotal                      | Integer              |                                                                    |
| amount\_total                         | Integer              |                                                                    |
| automatic\_tax                        | Struct               |                                                                    |
| billing\_address\_collection          | String               |                                                                    |
| cancel\_url                           | String               |                                                                    |
| client\_reference\_id                 | String               |                                                                    |
| consent                               | Struct               |                                                                    |
| consent\_collection                   | Struct               |                                                                    |
| currency                              | String               |                                                                    |
| customer                              | String               |                                                                    |
| customer\_creation                    | String               |                                                                    |
| customer\_details                     | Struct               |                                                                    |
| customer\_email                       | String               |                                                                    |
| expires\_at                           | DateTime             |                                                                    |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| locale                                | String               |                                                                    |
| metadata                              | Struct               |                                                                    |
| mode                                  | String               |                                                                    |
| object                                | String               |                                                                    |
| payment\_intent                       | String               | EQUAL\_TO                                                          |
| payment\_link                         | String               |                                                                    |
| payment\_method\_options              | Struct               |                                                                    |
| payment\_method\_types                | List                 |                                                                    |
| payment\_status                       | String               |                                                                    |
| phone\_number\_collection             | Struct               |                                                                    |
| recovered\_from                       | String               |                                                                    |
| setup\_intent                         | String               |                                                                    |
| shipping                              | Struct               |                                                                    |
| shipping\_address\_collection         | Struct               |                                                                    |
| shipping\_options                     | Struct               |                                                                    |
| shipping\_rate                        | String               |                                                                    |
| status                                | String               |                                                                    |
| submit\_type                          | String               |                                                                    |
| subscription                          | String               |                                                                    |
| success\_url                          | String               |                                                                    |
| total\_details                        | Struct               |                                                                    |
| url                                   | String               |                                                                    |
| Setup Intent                          | application          | String                                                             |                                                                    |
| cancellation\_reason                  | String               |                                                                    |
| client\_secret                        | String               |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| customer                              | String               | EQUAL\_TO                                                          |
| description                           | String               |                                                                    |
| id                                    | String               |                                                                    |
| last\_setup\_error                    | Struct               |                                                                    |
| latest\_attempt                       | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| mandate                               | String               |                                                                    |
| metadata                              | Struct               |                                                                    |
| next\_action                          | Struct               |                                                                    |
| object                                | String               |                                                                    |
| on\_behalf\_of                        | String               |                                                                    |
| payment\_method                       | String               |                                                                    |
| payment\_method\_options              | Struct               |                                                                    |
| payment\_method\_types                | List                 |                                                                    |
| single\_use\_mandate                  | String               |                                                                    |
| status                                | String               |                                                                    |
| usage                                 | String               |                                                                    |
| Shipping Rate                         | active               | Boolean                                                            | EQUAL\_TO                                                          |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| delivery\_estimate                    | Struct               |                                                                    |
| display\_name                         | String               |                                                                    |
| fixed\_amount                         | Struct               |                                                                    |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| tax\_behavior                         | String               |                                                                    |
| tax\_code                             | String               |                                                                    |
| type                                  | String               |                                                                    |
| Subscription                          | application          | String                                                             |                                                                    |
| application\_fee\_percent             | Double               |                                                                    |
| automatic\_tax                        | Struct               |                                                                    |
| billing\_cycle\_anchor                | DateTime             |                                                                    |
| billing\_thresholds                   | Struct               |                                                                    |
| cancel\_at                            | DateTime             |                                                                    |
| cancel\_at\_period\_end               | Boolean              |                                                                    |
| canceled\_at                          | DateTime             |                                                                    |
| collection\_method                    | String               | EQUAL\_TO                                                          |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| current\_period\_end                  | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| current\_period\_start                | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| customer                              | String               | EQUAL\_TO                                                          |
| days\_until\_due                      | Integer              |                                                                    |
| default\_payment\_method              | String               |                                                                    |
| default\_source                       | String               |                                                                    |
| default\_tax\_rates                   | List                 |                                                                    |
| description                           | String               |                                                                    |
| discount                              | Struct               |                                                                    |
| ended\_at                             | DateTime             |                                                                    |
| id                                    | String               |                                                                    |
| items                                 | List                 |                                                                    |
| latest\_invoice                       | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| next\_pending\_invoice\_item\_invoice | DateTime             |                                                                    |
| object                                | String               |                                                                    |
| pause\_collection                     | Struct               |                                                                    |
| payment\_settings                     | Struct               |                                                                    |
| pending\_invoice\_item\_interval      | Struct               |                                                                    |
| pending\_setup\_intent                | String               |                                                                    |
| pending\_update                       | Struct               |                                                                    |
| plan                                  | Struct               |                                                                    |
| quantity                              | Integer              |                                                                    |
| schedule                              | String               |                                                                    |
| start\_date                           | DateTime             |                                                                    |
| status                                | String               | EQUAL\_TO                                                          |
| test\_clock                           | String               |                                                                    |
| transfer\_data                        | Struct               |                                                                    |
| trial\_end                            | DateTime             |                                                                    |
| trial\_start                          | DateTime             |                                                                    |
| Subscription Item                     | billing\_thresholds  | Struct                                                             |                                                                    |
| created                               | DateTime             |                                                                    |
| id                                    | String               |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| plan                                  | Struct               |                                                                    |
| price                                 | Struct               |                                                                    |
| subscription                          | String               |                                                                    |
| tax\_rates                            | List                 |                                                                    |
| Subscription Schedule                 | application          | String                                                             |                                                                    |
| canceled\_at                          | DateTime             |                                                                    |
| completed\_at                         | DateTime             |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| current\_phase                        | Struct               |                                                                    |
| customer                              | String               | EQUAL\_TO                                                          |
| default\_settings                     | Struct               |                                                                    |
| end\_behavior                         | String               |                                                                    |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| phases                                | List                 |                                                                    |
| released\_at                          | DateTime             |                                                                    |
| released\_subscription                | String               |                                                                    |
| renewal\_interval                     | String               |                                                                    |
| status                                | String               |                                                                    |
| subscription                          | String               |                                                                    |
| test\_clock                           | String               |                                                                    |
| Tax Code                              | description          | String                                                             |                                                                    |
| id                                    | String               |                                                                    |
| name                                  | String               |                                                                    |
| object                                | String               |                                                                    |
| Tax Rate                              | active               | Boolean                                                            | EQUAL\_TO                                                          |
| country                               | String               |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| description                           | String               |                                                                    |
| display\_name                         | String               |                                                                    |
| id                                    | String               |                                                                    |
| inclusive                             | Boolean              | EQUAL\_TO                                                          |
| jurisdiction                          | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| percentage                            | Double               |                                                                    |
| state                                 | String               |                                                                    |
| tax\_type                             | String               |                                                                    |
| Transfer                              | amount               | Integer                                                            | EQUAL\_TO                                                          |
| amount\_reversed                      | Integer              |                                                                    |
| balance\_transaction                  | String               |                                                                    |
| created                               | DateTime             | EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO |
| currency                              | String               | EQUAL\_TO                                                          |
| description                           | String               |                                                                    |
| destination                           | String               | EQUAL\_TO                                                          |
| destination\_payment                  | String               |                                                                    |
| id                                    | String               |                                                                    |
| livemode                              | Boolean              |                                                                    |
| metadata                              | Struct               |                                                                    |
| object                                | String               |                                                                    |
| reversals                             | List                 |                                                                    |
| reversed                              | Boolean              |                                                                    |
| source\_transaction                   | String               |                                                                    |
| source\_type                          | String               |                                                                    |
| transfer\_group                       | String               | EQUAL\_TO                                                          |
