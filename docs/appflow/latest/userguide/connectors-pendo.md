

# Pendo connector for Amazon AppFlow
<a name="connectors-pendo"></a>

Pendo is a product analytics solution that helps teams record, monitor, and analyze data about the user experience in their apps. If you're a Pendo user, your account contains data about your users and their behavior in your product. You can use Amazon AppFlow to transfer data from Pendo to certain AWS services or other supported applications.

## Amazon AppFlow support for Pendo
<a name="pendo-support"></a>

Amazon AppFlow supports Pendo as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Pendo.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Pendo.

## Before you begin
<a name="pendo-prereqs"></a>

To use Amazon AppFlow to transfer data from Pendo to supported destinations, you must meet these requirements:
+ You have an account with Pendo that contains the data that you want to transfer. For more information about the Pendo data objects that Amazon AppFlow supports, see [Supported objects](#pendo-objects).
+ In your Pendo account, you've created an integration key for Amazon AppFlow, and you've configured the key to allow write access. For the steps to create a key, see [Authentication](https://developers.pendo.io/docs/?bash#authentication) in the Pendo Developers documentation.

Note the value of the integration key. You provide this value to Amazon AppFlow when you connect to your Pendo account.

## Connecting Amazon AppFlow to your Pendo account
<a name="pendo-connecting"></a>

To connect Amazon AppFlow to your Pendo account, provide the value of your integration key so that Amazon AppFlow can access your data. If you haven't yet configured your Pendo account for Amazon AppFlow integration, see [Before you begin](#pendo-prereqs).

**To connect to Pendo**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Pendo**.

1. Choose **Create connection**.

1. In the **Connect to Pendo** window, for **API key**, enter the value of the integration key from your Pendo account.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Pendo as the data source, you can select this connection.

## Transferring data from Pendo with a flow
<a name="pendo-transfer-data"></a>

To transfer data from Pendo, create an Amazon AppFlow flow, and choose Pendo as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Pendo, see [Supported objects](#pendo-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#pendo-destinations).

## Supported destinations
<a name="pendo-destinations"></a>

When you create a flow that uses Pendo as the data source, you can set the destination to any of the following connectors: 
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
<a name="pendo-objects"></a>

When you create a flow that uses Pendo as the data source, you can transfer any of the following data objects to supported destinations:



- ** Account**
  - **** Field**:** Account ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Parent Account / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO

- ** Event**
  - **** Field**:** Account ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** App ID / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Date Time Range / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** Day / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Num Event / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Number Minute / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Page ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Parameter / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Remote IP / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Server / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** User Agent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Visitor ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS

- ** Feature**
  - **** Field**:** App ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** App Wide / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Created By User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created Designer Version / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Daily Merge First / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Daily Rollup First / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Dirty / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Element Initial Tag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Element Path Rule / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Element Selection Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Event Property Configuration / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Group / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Core Event / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Kind / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Updated At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Last Updated By User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Root Version ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Stable Version ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Suggested Match / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Valid Through / **** Data type**:** Long / **** Supported filters**:** 

- ** Feature Event**
  - **** Field**:** Account ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** App ID / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Date Time Range / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** Day / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Feature ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Num Event / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Number Minute / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Parameter / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Remote IP / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Server / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** User Agent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Visitor ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS

- ** Guide**
  - **** Field**:** App ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** App IDS / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Attribute / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Audience / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Audience UI Hint / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Authored Language / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Created By User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Current First Eligible To Be Seen At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Editor Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Configuration / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Email State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Module / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Multi Step / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Top Level / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Training / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Kind / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Updated At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Last Updated By User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Launch Method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Poll / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Published At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Recurrence / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Recurrence Eligibility Window / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Reset At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Root Version ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Shows After / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Stable Version ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Step / **** Data type**:** List / **** Supported filters**:** 

- ** Guide Event**
  - **** Field**:** Account ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Account IDS / **** Data type**:** List / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** App ID / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Browser Time / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Country / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Date Time Range / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** Element Path / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Event ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Guide ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Guide Seen Reason / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Guide Step ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Language / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Latitude / **** Data type**:** Double / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Load Time / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Longitude / **** Data type**:** Double / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Old Visitor ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Region / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Remote IP / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** ServerName / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** UI Element Action / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** UI Element ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** UI Element Text / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** UI Element Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** User Agent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Visitor ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS

- ** Page**
  - **** Field**:** App ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Created By User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Daily Merge First / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Daily Rollup First / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Dirty / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Group / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Auto Tagged / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Core Event / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Kind / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Updated At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Last Updated By User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Root Version ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rule / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Rules Json / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Stable Version ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Suggested Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Valid Through / **** Data type**:** Long / **** Supported filters**:** 

- ** Page Event**
  - **** Field**:** Account ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** App ID / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Date Time Range / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** Day / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Num Event / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Number Minute / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Page ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Parameter / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Remote IP / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Server / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** User Agent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Visitor ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS

- ** Poll Event**
  - **** Field**:** Account ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Account IDS / **** Data type**:** Struct / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** App ID / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Browser Time / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Country / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Date Time Range / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** Element Path / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Event Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Guide ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Guide Step ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Language / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Latitude / **** Data type**:** Double / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Load Time / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Longitude / **** Data type**:** Double / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Old Visitor ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Poll ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Poll Response / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Poll Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Region / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Remote IP / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** ServerName / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** User Agent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Visitor ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS

- ** Report**
  - **** Field**:** Aggregation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Created By User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Definition / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Kind / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Run At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Last Updated At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Last Updated By User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owned By User / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Root Version ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Scope / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Share / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Shared / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Stable Version ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Target / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Report Data**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Track Event**
  - **** Field**:** Account ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** App ID / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Date Time Range / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** Day / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Num Event / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Number Minute / **** Data type**:** Long / **** Supported filters**:** LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Parameter / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Property / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Remote IP / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Server / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Track Type ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** User Agent / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS
  - **** Field**:** Visitor ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS

- ** Visitor**
  - **** Field**:** Identified / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Visitor ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, CONTAINS

