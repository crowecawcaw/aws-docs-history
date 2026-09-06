

# Adobe Analytics connector for Amazon AppFlow
<a name="connectors-adobeanalytics"></a>

Adobe Analytics is a business analysis software as a service (SaaS) solution. If you’re an Adobe Analytics user, your account contains business data, analytics, and more. You can use Amazon AppFlow to transfer data from Adobe Analytics to certain AWS services or other supported applications.

## Amazon AppFlow support for Adobe Analytics
<a name="adobeanalytics-support"></a>

Amazon AppFlow supports Adobe Analytics as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Adobe Analytics.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Adobe Analytics.

## Before you begin
<a name="adobeanalytics-prereqs"></a>

To use Amazon AppFlow to transfer data from Adobe Analytics to supported destinations, you must meet these requirements:
+ You have an account with Adobe Analytics that contains the data that you want to transfer. For more information about the Adobe Analytics data objects that Amazon AppFlow supports, see [Supported objects](#adobeanalytics-objects).
+ In your Adobe Analytics account, you've created an app for Amazon AppFlow. The app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For information about how to create an app, see [Add a new app](https://experienceleague.adobe.com/docs/mobile-services/using/manage-apps-ug/t-new-app.html?lang=en) in the Adobe Analytics documentation.
+ You've configured the app with a redirect URL for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Adobe Analytics. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

Note the client ID and client secret from your app settings. You provide these values to Amazon AppFlow when you create your connection.

### Connecting Amazon AppFlow to your Adobe Analytics account
<a name="adobeanalytics-connecting"></a>

To connect Amazon AppFlow to your Adobe Analytics account, provide the client credentials from your Adobe Analytics app so that Amazon AppFlow can access your data. If you haven't yet configured your Adobe Analytics account for Amazon AppFlow integration, see [Before you begin](#adobeanalytics-prereqs).

**To connect to Adobe Analytics**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Adobe Analytics**.

1. Choose **Create connection**.

1. In the **Connect to Adobe Analytics** window, enter the following information:
   + **Connection name** — A name for the connection.
   + **Client ID** — The client ID in your Adobe Analytics app.
   + **Client secret** — The client secret in your Adobe Analytics app. 
   + **X-API-KEY** — Re-enter the client ID in this field.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. Choose **Connect**.

1. In the window that appears, sign in to your Adobe Analytics account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Adobe Analytics as the data source, you can select this connection.

### Transferring data from Adobe Analytics with a flow
<a name="adobeanalytics-transfer-data"></a>

To transfer data from Adobe Analytics, create an Amazon AppFlow flow, and choose Adobe Analytics as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Adobe Analytics, see [Supported objects](#adobeanalytics-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#adobeanalytics-destinations).

### Supported destinations
<a name="adobeanalytics-destinations"></a>

When you create a flow that uses Adobe Analytics as the data source, you can set the destination to any of the following connectors: 
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

### Supported objects
<a name="adobeanalytics-objects"></a>

When you create a flow that uses Adobe Analytics as the data source, you can transfer any of the following data objects to supported destinations:



- ** Annotation**
  - **** Field**:** Apply To All Reports / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Approved / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Company Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Created Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Range / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Favorite / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Filter By Date Range / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Filter By Ids / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Filter By Modified After / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Include Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Modified By Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Modified Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Owner FullName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Report Suite Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rsid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Scope / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Shares / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Sort Property / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** System User Owned / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Usage Summary / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Usage Summary With Relevancy Score / **** Data type**:** String / **** Supported filters**:** 

- ** Calculated Metric**
  - **** Field**:** Approved / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Categories / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Compatibility / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Definition / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Favorite / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Filter By Ids / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Include Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Owner Full Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Polarity / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Precision / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Report Suite Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rsid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rsids / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Site Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Sort Direction / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Sort Property / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tag Names / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** To Be Used In Rs Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Calculated Metric Function**
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Definition / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Example / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Example Key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Namespace / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Persistable / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Component Metadata Share**
  - **** Field**:** Access Level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Component Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Component Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ims Org Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Include Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Share From Ims Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Share Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Share To Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Share To Ims Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Share To Login / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Share To Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** shareToDisplayName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** user Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO

- ** Component Metadata Tag**
  - **** Field**:** Components / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 

- ** Date Range**
  - **** Field**:** Alternate Variable Names / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Approved / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Company ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Create Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Curated Item / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Curated RSID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Definition / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Disabled Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Favorite / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Filter By IDs / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Filter By Modified After / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** IMS Org ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Include Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** New Definition / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Owner Full Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Shares / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Shares Full Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** System User Owned / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Template / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Usage Summary / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Usage Summary With Relevancy Score / **** Data type**:** String / **** Supported filters**:** 

- ** Dimension**
  - **** Field**:** Allowed For Reporting / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Categories / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Classifiable / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Extra Title Info / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Filter Reportable / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Multi Valued / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** None Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Parent / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pathable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Reportable / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Segmentable / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Standard Component / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Support / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Supports Data Governance / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Discovery**
  - **** Field**:** Companies / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** IMS Org Id / **** Data type**:** String / **** Supported filters**:** 

- ** Metric**
  - **** Field**:** Allocation / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Allowed For Reporting / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Categories / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Extra Title Info / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Help Link / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Polarity / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Precision / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Segmentable / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Standard Component / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Support / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Supports Data Governance / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** calculated / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Project**
  - **** Field**:** Access Level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Approved / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Company Template / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Complexity / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Definition / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** External References / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Favorite / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Filter By IDs / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Include Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Migrated IDs / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Owner ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Report Suite Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rsid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Shares / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Site Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Template / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Usage Summary / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** versionNotes / **** Data type**:** String / **** Supported filters**:** 

- ** Report Suite**
  - **** Field**:** Calendar Type / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Collection Item Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** RS Id Contains / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** RS Ids / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rsid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timezone Zone Info / **** Data type**:** String / **** Supported filters**:** 

- ** Report Top Item**
  - **** Field**:** Date Range / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** End Date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Item Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Lookup None Values / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Search And / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Search Not / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Search Or / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Search Phrase / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Start Date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Value / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** search-clause / **** Data type**:** String / **** Supported filters**:** 

- ** Segment**
  - **** Field**:** Categories / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Definition / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Definition Last Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Filter By Published Segments / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Include Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Modified By ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Owner Full Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Publishing Status / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** RSIDs / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Report Suite Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rsid / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Segment Filter / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Site Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Sort Direction / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Sort Property / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tag Names / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** compatibility / **** Data type**:** Struct / **** Supported filters**:** 

- ** Timezone**
  - **** Field**:** Current Timezone Offset / **** Data type**:** Float / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timezone Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Timezone Zoneinfo / **** Data type**:** String / **** Supported filters**:** 

- ** Usage Log**
  - **** Field**:** Date Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** End Date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Event / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Event Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Event Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** IP / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** IP Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Login / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Rsid / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Start Date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

- ** User**
  - **** Field**:** Admin / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Change Password / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Company ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Disabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Full Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** IMS User ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Access / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Login / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Login ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Phone Number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** createDate / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** tempLoginEnd / **** Data type**:** DateTime / **** Supported filters**:** 

