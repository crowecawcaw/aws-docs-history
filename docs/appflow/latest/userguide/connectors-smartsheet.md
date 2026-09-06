

# Smartsheet connector for Amazon AppFlow
<a name="connectors-smartsheet"></a>

Smartsheet is a spreadsheet-based online collaboration service that helps teams plan and track their projects and initiatives. If you're a Smartsheet user, your account contains data about your sheets, such as their dates when created, dates when modified, owners, access levels, and more. You can use Amazon AppFlow to transfer data from Smartsheet to certain AWS services or other supported applications.

## Amazon AppFlow support for Smartsheet
<a name="smartsheet-support"></a>

Amazon AppFlow supports Smartsheet as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Smartsheet.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Smartsheet.

## Before you begin
<a name="smartsheet-prereqs"></a>

To use Amazon AppFlow to transfer data from Smartsheet to supported destinations, you must meet these requirements:
+ You have an account with Smartsheet that contains the data that you want to transfer. For more information about the Smartsheet data objects that Amazon AppFlow supports, see [Supported objects](#smartsheet-objects).
+ In your Smartsheet account, you've created an app for Amazon AppFlow. The app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For the steps to create an app, see [OAuth Walkthrough](https://smartsheet.redoc.ly/#section/OAuth-Walkthrough) in the *Smartsheet API Reference (2.0.0)*.
+ You've configured the app with one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Smartsheet. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

Note the client ID and secret from the settings for your app. You provide these values to Amazon AppFlow when you connect to your Smartsheet account.

## Connecting Amazon AppFlow to your Smartsheet account
<a name="smartsheet-connecting"></a>

To connect Amazon AppFlow to your Smartsheet account, provide the client credentials from your app so that Amazon AppFlow can access your data. If you haven't yet configured your Smartsheet account for Amazon AppFlow integration, see [Before you begin](#smartsheet-prereqs).

**To connect to Smartsheet**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Smartsheet**.

1. Choose **Create connection**.

1. In the **Connect to Smartsheet** window, enter the following information:
   + **Authorization tokens URL** – Do one of the following:
     + To connect to the Smartsheet US region, choose **https://api.smartsheet.com/2.0/token**.
     + To connect to the Smartsheet EU region, choose **https://api.smartsheet.eu/2.0/token**.
   + **Authorization code URL** – Do one of the following:
     + To connect to the Smartsheet US region, choose **https://api.smartsheet.com/b/authorize**.
     + To connect to the Smartsheet EU region, choose **https://api.smartsheet.eu/b/authorize**.
   + **Client ID** – The client ID from app in your Smartsheet account.
   + **Client secret** – The client secret from the app in your Smartsheet account.
   + **Instance URL** – Do one of the following:
     + To connect to the Smartsheet US region, choose **https://api.smartsheet.com**.
     + To connect to the Smartsheet EU region, choose **https://api.smartsheet.eu**.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your Smartsheet account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Smartsheet as the data source, you can select this connection.

## Transferring data from Smartsheet with a flow
<a name="smartsheet-transfer-data"></a>

To transfer data from Smartsheet, create an Amazon AppFlow flow, and choose Smartsheet as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Smartsheet, see [Supported objects](#smartsheet-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#smartsheet-destinations).

## Supported destinations
<a name="smartsheet-destinations"></a>

When you create a flow that uses Smartsheet as the data source, you can set the destination to any of the following connectors: 
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
<a name="smartsheet-objects"></a>

When you create a flow that uses SmartSheet as the data source, you can transfer any of the following data objects to supported destinations:



- ** Event**
  - **** Field**:** Access Token Name / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Action / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Additional Details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Event Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Event Timestamp / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Object Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Object Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Request User Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** User Id / **** Data type**:** Integer / **** Supported filters**:** 

- ** List Sheet**
  - **** Field**:** Access Level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Modified At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Modified Since / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Permalink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Version / **** Data type**:** Integer / **** Supported filters**:** 

- ** Row Metadata**
  - **** Field**:** Access Level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Attachment / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Column / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Conditional Format / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created By / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Discussion / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Expanded / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Filter Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Filtered Out / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Format / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** In Critical Path / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Locked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Locked For User / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Modified At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Modified By / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Permalink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Proofs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Row Number / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Rows Modified Since / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN
  - **** Field**:** Sheet Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Sibling Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Total Row Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Version / **** Data type**:** Integer / **** Supported filters**:** 

- ** Sheet Data**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Sheet Metadata**
  - **** Field**:** Access Level / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Attachment / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cell Image Upload Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Column / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Cross Sheet Reference / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Dependencies Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Discussion / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Effective Attachment Option / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Favorite / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Filter / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** From Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Gantt Config / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Gantt Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Summary Field / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Is Multi Picklist Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Modified At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Permalink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Project Setting / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Read Only / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Resource Management Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Resource Management Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Show Parent Rows For Filter / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Summary / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Total Row Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** User Permission / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** User Setting / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Version / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Workspace / **** Data type**:** Struct / **** Supported filters**:** 

