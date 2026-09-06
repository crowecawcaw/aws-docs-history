

# LinkedIn Ads connector for Amazon AppFlow
<a name="connectors-linkedin-ads"></a>

LinkedIn Ads is an ad platform that helps organizations and brands to reach audiences throughout the user community of professionals on LinkedIn. If you use LinkedIn Ads, your account contains data about your ads and campaigns. You can use Amazon AppFlow to transfer data from LinkedIn Ads to certain AWS services or other supported applications.

## Amazon AppFlow support for LinkedIn Ads
<a name="linkedin-ads-support"></a>

Amazon AppFlow supports LinkedIn Ads as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from LinkedIn Ads.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to LinkedIn Ads.

**Supported API version**  
Amazon AppFlow retrieves your LinkedIn Ads data by sending requests to version 202509 of the LinkedIn API.

## Before you begin
<a name="linkedin-ads-prereqs"></a>

To use Amazon AppFlow to transfer data from LinkedIn Ads to supported destinations, you must meet these requirements:
+ You have a LinkedIn account and a LinkedIn Page. For the steps to create a page, see [Create a LinkedIn Page](https://www.linkedin.com/help/linkedin/answer/a543852/create-a-linkedin-page?lang=en) on LinkedIn Help.
+ In LinkedIn Developers, you've created an app, and you've configured it with the following settings:
  + The app is associated with your LinkedIn Page.
  + The app includes the Marketing Developer Platform product.
  + The app Auth settings have one or more redirect URLs for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from LinkedIn Ads. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
+ From your LinkedIn account, you've created a LinkedIn Campaign Manager account, which you use to manage your ads on LinkedIn. For the steps to create an account, see [Create an ad account in Campaign Manager as a new advertiser](https://www.linkedin.com/help/linkedin/answer/a426102/create-an-ad-account-in-campaign-manager-as-a-new-advertiser?lang=en) on LinkedIn Help.

From the Auth settings for your app, note the client ID and client secret. You provide these values to Amazon AppFlow when you connect to LinkedIn Ads.

## Connecting Amazon AppFlow to LinkedIn Ads
<a name="linkedin-ads-connecting"></a>

To connect Amazon AppFlow to LinkedIn Ads, provide the client credentials from your LinkedIn Developers app so that Amazon AppFlow can access your data. If you haven't yet configured your LinkedIn account for Amazon AppFlow integration, see [Before you begin](#linkedin-ads-prereqs).

**To connect to LinkedIn Ads**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **LinkedIn Ads**.

1. Choose **Create connection**.

1. In the **Connect to LinkedIn Ads** window, enter the following information:
   + **Client ID** – The client ID from the Auth settings of your LinkedIn Developers app.
   + **Client secret** – The client secret from the Auth settings of your LinkedIn Developers app.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**.

1. In the window that appears, sign in to your LinkedIn account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses LinkedIn Ads as the data source, you can select this connection.

## Transferring data from LinkedIn Ads with a flow
<a name="linkedin-ads-transfer-data"></a>

To transfer data from LinkedIn Ads, create an Amazon AppFlow flow, and choose LinkedIn Ads as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for LinkedIn Ads, see [Supported objects](#linkedin-ads-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#linkedin-ads-destinations).

## Supported destinations
<a name="linkedin-ads-destinations"></a>

When you create a flow that uses LinkedIn Ads as the data source, you can set the destination to any of the following connectors: 
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
<a name="linkedin-ads-objects"></a>

When you create a flow that uses LinkedIn Ads as the data source, you can transfer any of the following data objects to supported destinations:



- ** Ad Account**
  - **** Field**:** Change Audit Stamp / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Field / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Notified On Campaign Optimization / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Notified On Creative Approval / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Notified On Creative Rejection / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Notified On End Of Campaign / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Notified On New Features Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Reference / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Serving Status / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Test / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Version / **** Data type**:** Struct / **** Supported filters**:** 

- ** Ad Analytics**
  - **** Field**:** Action Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Ad Unit Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Approximate Unique Impression / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Card Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Card Impression / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Comment / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Comment Like / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Company Page Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Conversion Value In Local Currency / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Cost In Local Currency / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Cost In USD / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Date Range / **** Data type**:** Struct / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** External Website Conversion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** External Website Post Click Conversion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** External Website Post View Conversion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Follow / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Full Screen Play / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Impression / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Landing Page Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Lead Generation Mail Contact Info Share / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Lead Generation Mail Interested Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Like / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** One Click Lead / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** One Click Lead Form Open / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Open / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Other Engagement / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Pivot / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pivot Value / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pivot Value List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Reaction / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Send / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Share / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Start / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, BETWEEN
  - **** Field**:** Text URL Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Total Engagement / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Video Completion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Video First Quartile Completion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Video Midpoint Completion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Video Start / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Video Third Quartile Completion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Video View / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Card Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Comment / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Comment Like / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Company Page Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral External Website Conversion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral External Website Post Click Conversion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral External Website Post View Conversion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Follow / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Full Screen Play / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Impression / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Job Application / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Viral Landing Page Click / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Like / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral One Click Lead / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral One Click Lead Form Open / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Other Engagement / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Reaction / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Share / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Total Engagement / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Video Completion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Video First Quartile Completion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Video Midpoint Completion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Video Start / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Video Third Quartile Completion / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Viral Video View / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** viral Card Impression / **** Data type**:** Long / **** Supported filters**:** 

- ** Ad Creative**
  - **** Field**:** Campaign / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Change Audit Stamp / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Field / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Reference / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Review / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Serving Status / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Sort / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Test / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Variable / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Version / **** Data type**:** Struct / **** Supported filters**:** 

- ** Campaign**
  - **** Field**:** Account / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Associated Entity / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Audience Expansion Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Campaign Group / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Change Audit Stamp / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Cost Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Creative Selection / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Daily Budget / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Field / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Format / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Locale / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Objective Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Offsite Delivery Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Offsite Preferences / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Optimization Target Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Pacing Strategy / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Run Schedule / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Serving Status / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Story Delivery Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Targeting Criteria / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Test / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Total Budget / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Unit Cost / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Version / **** Data type**:** Struct / **** Supported filters**:** 

- ** Campaign Group**
  - **** Field**:** Account / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Allowed Campaign Type / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Backfilled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Change Audit Stamp / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Field / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Run Schedule / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Serving Status / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Test / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Total Budget / **** Data type**:** Struct / **** Supported filters**:** 

- ** Share Statistic**
  - **** Field**:** Organizational Entity / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Start / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, BETWEEN
  - **** Field**:** Time Range / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Total Share Statistic / **** Data type**:** Struct / **** Supported filters**:** 

