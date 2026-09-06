

# Snapchat Ads connector for Amazon AppFlow
<a name="connectors-snapchat-ads"></a>

You can use the Snapchat Ads connector in Amazon AppFlow to transfer data about the ads that you run on Snapchat. After you connect Amazon AppFlow to your ad account with Snapchat business, you can transfer data about your ads, campaigns, customer segments, and more. You can transfer this data to certain AWS services or other supported applications.

## Amazon AppFlow support for Snapchat Ads
<a name="snapchat-ads-support"></a>

Amazon AppFlow supports Snapchat Ads as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Snapchat Ads.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Snapchat Ads.

## Before you begin
<a name="snapchat-ads-prereqs"></a>

To use Amazon AppFlow to transfer data from Snapchat Ads to supported destinations, you must meet these requirements:
+ You have a Snapchat business account, and you've used it to create an ad account. The ad account contains the data that you want to transfer with Amazon AppFlow. For more information about ad accounts, see [Create an Ad Account](https://businesshelp.snapchat.com/s/article/create-ad-account?language=en_US) in the Snapchat Business Help Center.
+ In your Snapchat account, you've created an OAuth app for Amazon AppFlow. The app provides the credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For the steps to create an app, see [Activate Access to the Snapchat Marketing API](https://businesshelp.snapchat.com/s/article/api-apply?language=en_US) in the Snapchat Business Help Center.
+ You've configured the OAuth app with one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Snapchat Ads. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

From the OAuth app settings, note the values for Snap client ID and Snap client secret key. You provide these values to Amazon AppFlow when you connect to your Snapchat account.

## Connecting Amazon AppFlow to your Snapchat Ads account
<a name="snapchat-ads-connecting"></a>

To connect Amazon AppFlow to Snapchat Ads, provide the credentials from the OAuth app in your Snapchat account so that Amazon AppFlow can access your data. If you haven't yet configured your Snapchat account for Amazon AppFlow integration, see [Before you begin](#snapchat-ads-prereqs).

**To connect to Snapchat Ads**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Snapchat Ads**.

1. Choose **Create connection**.

1. In the **Connect to Snapchat Ads** window, enter the following information:
   + **Client ID** — The Snap client ID from your OAuth app.
   + **Client secret** — The Snap client secret key from your OAuth app.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your Snapchat account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Snapchat Ads as the data source, you can select this connection.

## Transferring data from Snapchat Ads with a flow
<a name="snapchat-ads-transfer-data"></a>

To transfer data from Snapchat Ads, create an Amazon AppFlow flow, and choose Snapchat Ads as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Snapchat Ads, see [Supported objects](#snapchat-ads-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#snapchat-ads-destinations).

## Supported destinations
<a name="snapchat-ads-destinations"></a>

When you create a flow that uses Snapchat Ads as the data source, you can set the destination to any of the following connectors: 
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
<a name="snapchat-ads-objects"></a>

When you create a flow that uses Snapchat Ads as the data source, you can transfer any of the following data objects to supported destinations:



- ** Ad Account**
  - **** Field**:** Advertiser / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Advertiser Organization Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Agency Representing Client / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Billing Center Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Billing Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Client Paying Invoices / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Funding Source Ids / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Lifetime Spend Cap Micro / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Organization Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timezone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Ad Squad**
  - **** Field**:** Auto Bid / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Bid Micro / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Bid Strategy / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Billing Event / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Campaign Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creation State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Daily Budget Micro / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Delivery Constraint / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Delivery Status / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Optimization Goal / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pacing Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Placement V2 / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Read Deleted Entities / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Skadnetwork Properties / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Start Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Target Bid / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Targeting / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Targeting Reach Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Ad Under Ad Account**
  - **** Field**:** Ad Squad Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creative Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Delivery Status / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Read Deleted Entities / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Render Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Review Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Review Status Reasons / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Ad Under Campaign**
  - **** Field**:** Ad Squad Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Approval Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creative Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Delivery Status / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Render Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Review Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Review Status Reasons / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Campaign**
  - **** Field**:** Ad Account Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Daily Budget Micro / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Deleted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Delivery Status / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** End Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Objective / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Read Deleted Entities / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Start Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Creative**
  - **** Field**:** Ad Account Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ad Product / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Brand Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Call To Action / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Headline / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Longform Video Properties / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Packaging Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Render Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Review Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Shareable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Top Snap Crop Position / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Top Snap Media Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Media**
  - **** Field**:** Ad Account Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** File Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Demo Media / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Media Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Visibility / **** Data type**:** String / **** Supported filters**:** 

- ** Organization**
  - **** Field**:** Accepted Term Version / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ad Accounts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Address Line 1 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Administrative District Level 1 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Business Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Configuration Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Contact Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Contact Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Contact Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Contact Phone Optin / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Country / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Agency / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Locality / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Marketing Optin / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** My Display Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** My Invited Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** My Member Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Postal Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Roles / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tax Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** created By Caller / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Segment**
  - **** Field**:** Ad Account Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Approximate Number Users / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Retention In Days / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Source Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Targetable Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Upload Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Visible To / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** organization Id / **** Data type**:** String / **** Supported filters**:** 

