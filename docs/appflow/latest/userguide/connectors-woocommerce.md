

# WooCommerce connector for Amazon AppFlow
<a name="connectors-woocommerce"></a>

WooCommerce helps online merchants build commercial websites with a plugin for WordPress. If you're a WooCommerce user, then your account contains data about your site and your transactions, such as your orders, products, reviews, shipments, and more. You can use Amazon AppFlow to transfer data from WooCommerce to certain AWS services or other supported applications.

## Amazon AppFlow support for WooCommerce
<a name="woocommerce-support"></a>

Amazon AppFlow supports WooCommerce as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from WooCommerce.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to WooCommerce.

## Before you begin
<a name="woocommerce-prereqs"></a>

To use Amazon AppFlow to transfer data from WooCommerce to supported destinations, you must meet these requirements:
+ You have an account with WooCommerce that contains the data that you want to transfer. For more information about the WooCommerce data objects that Amazon AppFlow supports, see [Supported objects](#woocommerce-objects).
+ In your WooCommerce account, you've created a REST API key for Amazon AppFlow. For information about how create a key, see [Authentication](https://woocommerce.github.io/woocommerce-rest-api-docs/?shell#authentication) in the WooCommerce documentation.

From the REST API key details, note the consumer key and consumer secret. You provide these values to Amazon AppFlow when you connect to your WooCommerce account.

## Connecting Amazon AppFlow to your WooCommerce account
<a name="woocommerce-connecting"></a>

To connect Amazon AppFlow to your WooCommerce account, provide the credentials from the REST API key in your WooCommerce account so that Amazon AppFlow can access your data. If you haven't yet configured your WooCommerce account for Amazon AppFlow integration, see [Before you begin](#woocommerce-prereqs).

**To connect to WooCommerce**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **WooCommerce**.

1. Choose **Create connection**.

1. In the **Connect to WooCommerce** window, enter the following information:
   + **Consumer Key** — The consumer key from your REST API key.
   + **Consumer Secret** — The consumer secret from your REST API key.
   + **Instance URL** — The site name that you assigned when you created your site in WooCommerce.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your WooCommerce account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses WooCommerce as the data source, you can select this connection.

## Transferring data from WooCommerce with a flow
<a name="woocommerce-transfer-data"></a>

To transfer data from WooCommerce, create an Amazon AppFlow flow, and choose WooCommerce as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for WooCommerce, see [Supported objects](#woocommerce-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#woocommerce-destinations).

## Supported destinations
<a name="woocommerce-destinations"></a>

When you create a flow that uses WooCommerce as the data source, you can set the destination to any of the following connectors: 
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
<a name="woocommerce-objects"></a>

When you create a flow that uses WooCommerce as the data source, you can transfer any of the following data objects to supported destinations:



- ** Coupon**
  - **** Field**:** After / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Amount / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Before / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Created GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Expires GMT / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Expiry / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Modified GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Discount Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Restriction / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Exclude Sale Item / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Excluded Product Category List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Excluded Product ID / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Free Shipping / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Individual Use / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Limit Usage To X Item / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Maximum Amount / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Meta Data / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Minimum Amount / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Product Category List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Product ID / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Usage Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Usage Limit / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Usage Limit Per User / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Used By / **** Data type**:** List / **** Supported filters**:** 

- ** Coupon Total**
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total / **** Data type**:** String / **** Supported filters**:** 

- ** Customer Total**
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total / **** Data type**:** String / **** Supported filters**:** 

- ** Order**
  - **** Field**:** After / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Before / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Billing / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Cart Hash / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Cart Tax / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Coupon Line / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Created Via / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Currency Symbol / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Customer / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Customer IP Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Customer Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Customer Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Customer User Agent / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** DP / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Completed / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Completed GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Created GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Modified GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Paid / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Paid GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Discount Tax / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Discount Total / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Fee Line / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Is Editable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Line Item / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Meta Data / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Needs Payment / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Needs Processing / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order Key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Parent ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Payment Method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Payment Method Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Payment Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Prices Include Tax / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Product / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Refund / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Set Paid / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Shipping / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Shipping Line / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Shipping Tax / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Shipping Total / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tax Line / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Total / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Tax / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Transaction ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Version / **** Data type**:** String / **** Supported filters**:** 

- ** Order Total**
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total / **** Data type**:** String / **** Supported filters**:** 

- ** Payment Gateway**
  - **** Field**:** Connection Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Method Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Method Support / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Method Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Needs Setup / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Post Install Script / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Required Settings Key / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Setting / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Settings Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Setup Help Text / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 

- ** Product**
  - **** Field**:** After / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Attribute List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Average Rating / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Backorder / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Backordered / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Backorders Allowed / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Before / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Button Text / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Catalog Visibility / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Category List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Created GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Modified GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date On Sale From / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date On Sale From GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date On Sale To / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date On Sale To GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Default Attribute List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Dimension / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Download / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Download Expiry / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Download Limit / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Downloadable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** External Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Featured / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Grouped Product List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Has Option / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Image List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Jetpack Likes Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Jetpack Publicize Connection / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Jetpack Sharing Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** List of Cross Sell ID / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** List of Jetpack Related Post / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** List of Upsell ID / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Low Stock Amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Manage Stock / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Menu Order / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Meta Data / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** On Sale / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Parent ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Permalink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Price Html / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Purchasable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Purchase Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rating Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Regular Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Related ID / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Reviews Allowed / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Sale Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Shipping Class / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Shipping Class ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Shipping Required / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Shipping Taxable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Short Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Sku / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Sold Individually / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Stock Quantity / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Stock Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tag / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Tag / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tax Class / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tax Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Sale / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Variation List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Virtual / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Weight / **** Data type**:** String / **** Supported filters**:** 

- ** Product Attribute**
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Has Archive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Product Attribute Term**
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Hide Empty / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Menu Order / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Parent / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Product / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Product Category**
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Display / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Hide Empty / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Image / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Menu Order / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Parent / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Product / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Product Review**
  - **** Field**:** After / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Before / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Created GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Product ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Product Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Product Permalink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rating / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Review / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Reviewer / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Reviewer Avatar URL / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Reviewer Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Verified / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Product Shipping Class**
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Hide Empty / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Product / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Product Tag**
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Hide Empty / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Product / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Product Total**
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total / **** Data type**:** String / **** Supported filters**:** 

- ** Product Variation**
  - **** Field**:** After / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Backorder / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Backordered / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Backorders Allowed / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Before / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Created GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Modified GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date On Sale From / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date On Sale From GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date On Sale To / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date On Sale To GMT / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Dimension / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Download / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Download Expiry / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Download Limit / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Downloadable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Image / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** List of attribute / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Low Stock Amount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** MAX Price / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** MIN Price / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Manage Stock / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Menu Order / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Meta Data / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** On Sale / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Permalink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Purchasable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Regular Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Sale Price / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Shipping Class / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Shipping Class ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Sku / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Stock Quantity / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Stock Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tax Class / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tax Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Virtual / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Weight / **** Data type**:** String / **** Supported filters**:** 

- ** Report**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 

- ** Review Total**
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total / **** Data type**:** String / **** Supported filters**:** 

- ** Sale Report**
  - **** Field**:** Average Sale / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Max / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Min / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Net Sale / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Total / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Total Customer / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Total Discount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Total Item / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Total Order / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Total Refund / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Total Sale / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Shipping / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Tax / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Totals Grouped By / **** Data type**:** String / **** Supported filters**:** 

- ** Shipping Method**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 

- ** Shipping Zone**
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** Integer / **** Supported filters**:** 

- ** Shipping Zone Location**
  - **** Field**:** Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Shipping Zone Method**
  - **** Field**:** Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Instance ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Method Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Method ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Method Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Setting / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 

- ** Tax Class**
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 

- ** Tax Rate**
  - **** Field**:** Cities / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** City / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Class / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Compound / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Country / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Postcode / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Postcode / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Priority / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Rate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Shipping / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** 

- ** Top Seller Report**
  - **** Field**:** Context / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Max / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Min / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Product ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Quantity / **** Data type**:** Integer / **** Supported filters**:** 

