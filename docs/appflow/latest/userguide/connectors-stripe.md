

# Stripe connector for Amazon AppFlow
<a name="connectors-stripe"></a>

Stripe powers ecommerce with payment processing and other commerce solutions for businesses. If you're a Stripe user, your account contains data about your transactions, such as your balance, charges, and payouts. You can use Amazon AppFlow to transfer data from Stripe to certain AWS services or other supported applications.

## Amazon AppFlow support for Stripe
<a name="stripe-support"></a>

Amazon AppFlow supports Stripe as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Stripe.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Stripe.



## Before you begin
<a name="stripe-prereqs"></a>

Before you can use Amazon AppFlow to transfer data from Stripe, you must have a Stripe account that contains the data to transfer. For more information about the Stripe data objects that Amazon AppFlow supports, see [Supported objects](#stripe-objects).

From your Stripe account, you must obtain a test or live API key. You provide this key to Amazon AppFlow when you connect to your Stripe account. For the steps to obtain these keys, see [Manage API keys](https://stripe.com/docs/development/dashboard/manage-api-keys) in the Stripe Docs.

## Connecting Amazon AppFlow to your Stripe account
<a name="stripe-connecting"></a>

To connect Amazon AppFlow to your Stripe account, provide your API key so that Amazon AppFlow can access your data. If you haven't yet configured your Stripe account for Amazon AppFlow integration, see [Before you begin](#stripe-prereqs).

**To connect to Stripe**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Stripe**.

1. Choose **Create connection**.

1. In the **Connect to Stripe** window, for **API Key**, enter a test or live API key from your Stripe account settings.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Stripe as the data source, you can select this connection.

## Transferring data from Stripe with a flow
<a name="stripe-transfer-data"></a>

To transfer data from Stripe, create an Amazon AppFlow flow, and choose Stripe as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Stripe, see [Supported objects](#stripe-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#stripe-destinations).

## Supported destinations
<a name="stripe-destinations"></a>

When you create a flow that uses Stripe as the data source, you can set the destination to any of the following connectors: 
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
<a name="stripe-objects"></a>

When you create a flow that uses Stripe as the data source, you can transfer any of the following data objects to supported destinations:



- ** Account**
  - **** Field**:** business\_profile / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** capabilities / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** charges\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** controller / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** country / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** default\_currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** details\_submitted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** external\_account / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** future\_requirements / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payouts\_enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** requirements / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 

- ** Application Fee**
  - **** Field**:** account / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** amount\_refunded / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** application / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** balance\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** charge / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** originating\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** refunded / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** refunds / **** Data type**:** List / **** Supported filters**:** 

- ** Balance**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source\_types / **** Data type**:** Struct / **** Supported filters**:** 

- ** Balance Transaction**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** available\_on / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** exchange\_rate / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** fee / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** fee\_details / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** net / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** reporting\_category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Charge**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** amount\_captured / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** amount\_refunded / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** application / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** application\_fee / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** application\_fee\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** balance\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** billing\_details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** calculated\_statement\_descriptor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** captured / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** destination / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** dispute / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** disputed / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** failure\_balance\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** failure\_code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** failure\_message / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** fraud\_details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** on\_behalf\_of / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** order / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** outcome / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** paid / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** payment\_intent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** payment\_method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_method\_details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** receipt\_email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** receipt\_number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** receipt\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** refunded / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** refunds / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** review / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** shipping / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source\_transfer / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** statement\_descriptor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** statement\_descriptor\_suffix / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** transfer\_data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** transfer\_group / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Country Spec**
  - **** Field**:** default\_currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** supported\_bank\_account\_currencies / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** supported\_payment\_currencies / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** supported\_payment\_methods / **** Data type**:** List  / **** Supported filters**:** 
  - **** Field**:** supported\_transfer\_countries / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** verification\_fields / **** Data type**:** Struct / **** Supported filters**:** 

- ** Coupon**
  - **** Field**:** amount\_off / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** duration / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** duration\_in\_months / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** max\_redemptions / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** percent\_off / **** Data type**:** Double / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** redeem\_by / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** times\_redeemed / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** valid / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Credit Note**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** customer\_balance\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** discount\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** discount\_amounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** memo / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** out\_of\_band\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** pdf / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** refund / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** subtotal / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** tax\_amounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** total / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** voided\_at / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Customer**
  - **** Field**:** address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** balance / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** default\_source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** delinquent / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** discount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice\_prefix / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice\_settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** next\_invoice\_sequence / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** preferred\_locales / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** shipping / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** tax\_exempt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** test\_clock / **** Data type**:** String / **** Supported filters**:** 

- ** Dispute**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** balance\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** balance\_transactions / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** charge / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** evidence / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** evidence\_details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** is\_charge\_refundable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_intent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** reason / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Early Fraud Warning**
  - **** Field**:** actionable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** charge / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** fraud\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_intent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** File Link**
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** expired / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** expires\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** file / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** url / **** Data type**:** String / **** Supported filters**:** 

- ** Invoice**
  - **** Field**:** account\_country / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** account\_name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** account\_tax\_ids / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** amount\_due / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** amount\_paid / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** amount\_remaining / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** application / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** application\_fee\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** attempt\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** attempted / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** auto\_advance / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** automatic\_tax / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** billing\_reason / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** charge / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** collection\_method / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** custom\_fields / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** customer\_address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** customer\_email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer\_name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer\_phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer\_shipping / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** customer\_tax\_exempt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer\_tax\_ids / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** default\_payment\_method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** default\_source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** default\_tax\_rates / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** discount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** discounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** due\_date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** ending\_balance / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** footer / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** hosted\_invoice\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice\_pdf / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** last\_finalization\_error / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** next\_payment\_attempt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** on\_behalf\_of / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** paid / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** paid\_out\_of\_band / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** payment\_intent / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** period\_end / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** period\_start / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** post\_payment\_credit\_notes\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** pre\_payment\_credit\_notes\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** quote / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** receipt\_number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** starting\_balance / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** statement\_descriptor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** status\_transitions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** subscription / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** subtotal / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** tax / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** test\_clock / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** total / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** total\_discount\_amounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** total\_tax\_amounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** transfer\_data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** webhooks\_delivered\_at / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Invoice Item**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** discountable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** discounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** period / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** plan / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** price / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** proration / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** quantity / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** subscription / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** subscription\_item / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tax\_rates / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** test\_clock / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** unit\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** unit\_amount\_decimal / **** Data type**:**  String / **** Supported filters**:** 

- ** Payment Intent**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** amount\_capturable / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** amount\_details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** amount\_received / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** application / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** application\_fee\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** automatic\_payment\_methods / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** canceled\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** cancellation\_reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** capture\_method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** charges / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** client\_secret / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** confirmation\_method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** last\_payment\_error / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** next\_action / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** on\_behalf\_of / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_method\_options / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payment\_method\_types / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** processing / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** receipt\_email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** review / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** setup\_future\_usage / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** shipping / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** statement\_descriptor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** statement\_descriptor\_suffix / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** transfer\_data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** transfer\_group / **** Data type**:** String / **** Supported filters**:** 

- ** Payout**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** arrival\_date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** automatic / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** balance\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** destination / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** failure\_balance\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** failure\_code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** failure\_message / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** original\_payout / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** reversed\_by / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** statement\_descriptor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 

- ** Plan**
  - **** Field**:** active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** aggregate\_usage / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** amount\_decimal / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** billing\_scheme / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** interval / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** interval\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** nickname / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** product / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** tiers\_mode / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** transform\_usage / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** trial\_period\_days / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** usage\_type / **** Data type**:** String / **** Supported filters**:** 

- ** Price**
  - **** Field**:** active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** billing\_scheme / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** lookup\_key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** nickname / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** product / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** recurring / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** tax\_behaviour / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tiers\_mode / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** transform\_quantity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** unit\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** unit\_amount\_decimal / **** Data type**:** String / **** Supported filters**:** 

- ** Product**
  - **** Field**:** active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** attributes / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** default\_price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** images / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** package\_dimensions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** shippable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** statement\_descriptor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tax\_code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** unit\_label / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updated / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** url / **** Data type**:** String / **** Supported filters**:** 

- ** Promotion Code**
  - **** Field**:** active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** coupon / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** expires\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** max\_redemptions / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** restrictions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** times\_redeemed / **** Data type**:** Integer / **** Supported filters**:** 

- ** Quote**
  - **** Field**:** amount\_subtotal / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** amount\_total / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** application / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** application\_fee\_amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** application\_fee\_percent / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** automatic\_tax / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** collection\_method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** computed / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** default\_tax\_rates / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** discounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** expires\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** footer / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** from\_quote / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** header / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** invoice\_settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** on\_behalf\_of / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** status\_transitions / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** subscription / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** subscription\_data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** subscription\_schedule / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** test\_clock / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** total\_details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** transfer\_data / **** Data type**:** Struct / **** Supported filters**:** 

- ** Refund**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** balance\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** charge / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_intent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** receipt\_number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source\_transfer\_reversal / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** transfer\_reversal / **** Data type**:** String / **** Supported filters**:** 

- ** Report Type**
  - **** Field**:** data\_available\_end / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** data\_available\_start / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** default\_columns / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** updated / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** version / **** Data type**:** Integer / **** Supported filters**:** 

- ** Session**
  - **** Field**:** after\_expiration / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** allow\_promotion\_codes / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** amount\_subtotal / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** amount\_total / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** automatic\_tax / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** billing\_address\_collection / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** cancel\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** client\_reference\_id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** consent / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** consent\_collection / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer\_creation / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** customer\_details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** customer\_email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** expires\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** locale / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** mode / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_intent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** payment\_link / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_method\_options / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payment\_method\_types / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** payment\_status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** phone\_number\_collection / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** recovered\_from / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** setup\_intent / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** shipping / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** shipping\_address\_collection / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** shipping\_options / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** shipping\_rate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** submit\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** subscription / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** success\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** total\_details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** url / **** Data type**:** String / **** Supported filters**:** 

- ** Setup Intent**
  - **** Field**:** application / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** cancellation\_reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** client\_secret / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** last\_setup\_error / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** latest\_attempt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** mandate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** next\_action / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** on\_behalf\_of / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** payment\_method\_options / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payment\_method\_types / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** single\_use\_mandate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** usage / **** Data type**:** String / **** Supported filters**:** 

- ** Shipping Rate**
  - **** Field**:** active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** delivery\_estimate / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** display\_name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** fixed\_amount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tax\_behavior / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tax\_code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 

- ** Subscription**
  - **** Field**:** application / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** application\_fee\_percent / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** automatic\_tax / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** billing\_cycle\_anchor / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** billing\_thresholds / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** cancel\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** cancel\_at\_period\_end / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** canceled\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** collection\_method / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** current\_period\_end / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** current\_period\_start / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** days\_until\_due / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** default\_payment\_method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** default\_source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** default\_tax\_rates / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** discount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ended\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** items / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** latest\_invoice / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** next\_pending\_invoice\_item\_invoice / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** pause\_collection / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** payment\_settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** pending\_invoice\_item\_interval / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** pending\_setup\_intent / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** pending\_update / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** plan / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** quantity / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** schedule / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** start\_date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** test\_clock / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** transfer\_data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** trial\_end / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** trial\_start / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Subscription Item**
  - **** Field**:** billing\_thresholds / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** plan / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** price / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** subscription / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tax\_rates / **** Data type**:** List / **** Supported filters**:** 

- ** Subscription Schedule**
  - **** Field**:** application / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** canceled\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** completed\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** current\_phase / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** default\_settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** end\_behavior / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** phases / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** released\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** released\_subscription / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** renewal\_interval / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** subscription / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** test\_clock / **** Data type**:** String / **** Supported filters**:** 

- ** Tax Code**
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 

- ** Tax Rate**
  - **** Field**:** active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** country / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** display\_name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** inclusive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** jurisdiction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** percentage / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** state / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tax\_type / **** Data type**:** String / **** Supported filters**:** 

- ** Transfer**
  - **** Field**:** amount / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** amount\_reversed / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** balance\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** currency / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** destination / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** destination\_payment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** livemode / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** reversals / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** reversed / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** source\_transaction / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** transfer\_group / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

