

# Recharge connector for Amazon AppFlow
<a name="connectors-recharge"></a>

Recharge is a subscription payment solution designed for merchants to set up and manage dynamic, recurring billing across web and mobile applications. If you're a Recharge user, your account contains data about your customers, transactions, subscriptions, and more. You can use Amazon AppFlow to transfer data from Recharge to certain AWS services or other supported applications.

## Amazon AppFlow support for Recharge
<a name="recharge-support"></a>

Amazon AppFlow supports Recharge as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Recharge.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Recharge.

## Before you begin
<a name="recharge-prereqs"></a>

To use Amazon AppFlow to transfer data from Recharge to supported destinations, you must meet these requirements:
+ You have an account with Recharge that contains the data that you want to transfer. For more information about the Recharge data objects that Amazon AppFlow supports, see [Supported objects](#recharge-objects).
+ In your Recharge account, you've created an API token. For the steps to create this token, see [Recharge API key](https://docs.rechargepayments.com/docs/recharge-api-key) in the Recharge documentation.
+ You've configured the API token with read permissions that allow Amazon AppFlow to access the data that you want to transfer.

From your account settings, note your API token key because you provide this value to Amazon AppFlow when you connect to your Recharge account.

## Connecting Amazon AppFlow to your Recharge account
<a name="recharge-connecting"></a>

To connect Amazon AppFlow to your Recharge account, provide the API token from your account settings.

**To connect to Recharge**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Recharge**.

1. Choose **Create connection**.

1. In the **Connect to Recharge** window, for **API Token**, enter your API token key.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Recharge as the data source, you can select this connection.

## Transferring data from Recharge with a flow
<a name="recharge-transfer-data"></a>

To transfer data from Recharge, create an Amazon AppFlow flow, and choose Recharge as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Recharge, see [Supported objects](#recharge-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#recharge-destinations).

## Supported destinations
<a name="recharge-destinations"></a>

When you create a flow that uses Recharge as the data source, you can set the destination to any of the following connectors: 
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
<a name="recharge-objects"></a>

When you create a flow that uses Recharge as the data source, you can transfer any of the following data objects to supported destinations:



- ** Address**
  - **** Field**:** Address1 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Address2 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** City / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Company / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Country Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Customer ID / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Discount Code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Discount Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Discounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Is Active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Payment Method ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Presentment Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Province / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Shipping Lines Conserved / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Shipping Lines Override / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Updated At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Zip / **** Data type**:** String / **** Supported filters**:** 

- ** Charge**
  - **** Field**:** Address ID / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Analytics Data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Billing Address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Charge Attempts / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Client Details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Customer / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Customer Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Discount Code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Discount Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Discounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Error / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Error Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** External Order ID / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** External Order ID E-Commerce / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** External Transaction ID / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** External Variant Id not found / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Uncommitted Changes / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Include / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Line Items / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order Attributes / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Orders Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Payment Processor / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Processed At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Processed At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Processed At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Purchase Item Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Retry Date / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Scheduled At / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Scheduled At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Scheduled At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Shipping Address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Shipping Lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Sort By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Subtotal Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tax Lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Taxable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Total Discounts / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Duties / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Line Items Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Refunds / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Tax / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Weight Grams / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Updated At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

- ** Collection**
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Sort Order / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Customer**
  - **** Field**:** Analytics Data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** External Customer Id / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** External Customer Id E-Commerce / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** First Charge Processed At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Has Payment Method In Dunning / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Valid Payment Method / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Hash / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Include / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subscriptions Active Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Subscriptions Total Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Tax Exempt / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Updated At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

- ** Discount**
  - **** Field**:** Applies To / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Channel Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Discount Code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Discount Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Ends At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** External Discount Id / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** External Discount Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Prerequisite Subtotal Min / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Starts At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Updated At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Usage Limits / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value Type / **** Data type**:** String / **** Supported filters**:** 

- ** Metafield**
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Namespace / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Owner Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Owner Resource / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value Type / **** Data type**:** String / **** Supported filters**:** 

- ** Onetime**
  - **** Field**:** Address Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Customer Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** External Product Id / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** External Variant ID / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** External Variant ID E-Commerce / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Include Cancelled / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Is Cancelled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Next Charge Scheduled At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Presentment Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Price / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Product Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Properties / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Quantity / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** SKU / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SKU Override / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Updated At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Variant Title / **** Data type**:** String / **** Supported filters**:** 

- ** Order**
  - **** Field**:** Address ID / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Billing Address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Charge / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Charge Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Client Details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Customer / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Customer Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Discounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Error / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** External Cart Token / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** External Customer Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** External Order ID / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** External Order ID E-Commerce / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** External Order Name / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** External Order Number / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Has External Order / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Include / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Is Prepaid / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Line Items / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order Attributes / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Processed At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Purchase Item Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Scheduled At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Scheduled At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Scheduled At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Shipping Address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Shipping Lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Subtotal Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tax Lines / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Taxable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Total Discounts / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Duties / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Line Items Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Refunds / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Tax / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Weight Grams / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Updated At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

- ** Store**
  - **** Field**:** Checkout Logo Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Checkout Platform / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Customer Portal Base Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Default Api Version / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** External Platform / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Identifier / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Merchant Portal Base Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timezone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Weight Unit / **** Data type**:** String / **** Supported filters**:** 

- ** Subscription**
  - **** Field**:** Address Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Analytics Data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Cancellation Reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Cancellation Reason Comments / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Cancelled At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Charge Interval Frequency / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Customer Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Expire After Specific Number Of Charges / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** External Product Id / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** External Variant ID E-Commerce / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** External Variant Id / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Has Queued Charges / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Include / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Is Prepaid / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Skippable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Swappable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Max Retries Reached / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Next Charge Scheduled At / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Order Day Of Month / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Order Day Of Week / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Order Interval Frequency / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Order Interval Unit / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Presentment Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Product Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Properties / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Quantity / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** SKU / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SKU Override / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Updated At Max / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At Min / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Variant Title / **** Data type**:** String / **** Supported filters**:** 

