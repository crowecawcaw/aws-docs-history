

# Instagram Ads connector for Amazon AppFlow
<a name="connectors-instagram-ads"></a>

Instagram Ads is an advertising solution for Instagram. If you run ads on Instagram, your account contains data about your ads, campaigns, ad images, and more. You can use Amazon AppFlow to transfer data from Instagram Ads to certain AWS services or other supported applications.

## Amazon AppFlow support for Instagram Ads
<a name="instagram-ads-support"></a>

Amazon AppFlow supports Instagram Ads as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Instagram Ads.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Instagram Ads.

## Before you begin
<a name="instagram-ads-prereqs"></a>

To use Amazon AppFlow to transfer data from Instagram Ads to supported destinations, you must meet these requirements:
+ You have an Instagram business account that you use to run your ads. For more information about the Instagram Ads data objects that Amazon AppFlow supports, see [Supported objects](#instagram-ads-objects).
+ You've connected your Instagram business account to a Facebook Page. This connection makes it possible for third-party applications like Amazon AppFlow to access your Instagram data. For the steps to connect, see [Add or Remove an Instagram Account From Your Facebook Page](https://www.facebook.com/business/help/connect-instagram-to-page) in the Meta Business Help Center.
+ You have a Meta for Developers account.
+ Your Meta for Developers account contains an app with its type set to *Business*. For information about how to create an app, see [Create an App](https://developers.facebook.com/docs/development/create-an-app) in the Meta for Developers App Development documentation.
+ Your Meta for Developers app includes the *Facebook Login* product, and you've configured the product to meet the following additional requirements:
  + Client OAuth login is enabled.
  + Web OAuth login is enabled.
  + One or more OAuth redirect URIs are present for Amazon AppFlow. Each of these URIs has the following form:

    `https://{{region}}.console.aws.amazon.com/appflow/oauth`

    In this URI, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from the Marketing API. For example, if you use Amazon AppFlow in the US East (N. Virginia) region, the URI is `https://us-east-1.console.aws.amazon.com/appflow/oauth`.

    For the AWS Regions that Amazon AppFlow supports, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

  For more information about Facebook Login, see [Facebook Login](https://developers.facebook.com/docs/facebook-login) in the Meta For Developers documentation.
+ Your app includes the *Marketing API* product, and you use this product to manage the ads that Amazon AppFlow transfers data about.
+ You've configured your app with the following permissions:
  + `ads_management`
  + `ads_read`
  + `business_management`
  + `read_insights`

  For more information about these permissions, see [Permissions Reference](https://developers.facebook.com/docs/permissions/reference) in the Meta for Developers Graph API documentation.

  Each of these permissions must be approved for *Advanced Access* through the *App Review* process. For the steps to create an App Review submission, see [Submitting For Review]() in the Meta for Developers App Review documentation.

From the settings for your app, note the app ID and app secret. You provide these values to Amazon AppFlow when you connect to your account.

## Connecting Amazon AppFlow to Instagram Ads
<a name="instagram-ads-connecting"></a>

To connect Amazon AppFlow to Instagram Ads, provide the app credentials from your Meta for Developers app so that Amazon AppFlow can access your data. If you haven't yet configured an app for Amazon AppFlow integration, see [Before you begin](#instagram-ads-prereqs).

**To connect to Instagram Ads**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Instagram Ads**.

1. Choose **Create connection**.

1. In the **Connect to Instagram Ads** window, enter the following information:
   + **Client ID** – The app ID from your Meta for Developers app.
   + **Client secret** – The app secret from your Meta for Developers app.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**.

1. In the window that appears, sign in to your account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Instagram Ads as the data source, you can select this connection.

## Transferring data from Instagram Ads with a flow
<a name="instagram-ads-transfer-data"></a>



To transfer data from Instagram Ads, create an Amazon AppFlow flow, and choose Instagram Ads as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Instagram Ads, see [Supported objects](#instagram-ads-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#instagram-ads-destinations).

## Supported destinations
<a name="instagram-ads-destinations"></a>

When you create a flow that uses Instagram Ads as the data source, you can set the destination to any of the following connectors: 
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
<a name="instagram-ads-objects"></a>

When you create a flow that uses Instagram ads as the data source, you can transfer any of the following data objects to supported destinations:



- ** Ad**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Ad Creative**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Ad Image**
  - **** Field**:** Account ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Creative / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Hash / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Height / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Associated Creatives In Adgroup / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Original Height / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Original Width / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Permalink URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** URL 128 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Width / **** Data type**:** Integer / **** Supported filters**:** 

- ** Ad Insight**
  - **** Field**:** Account Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Account ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Account Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Action Value / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Ad Click Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Ad ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ad Impression Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Ad Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Adset ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Adset Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Age Targeting / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Attribution Setting / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Auction Bid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Auction Competitiveness / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Auction Max Competitor Bid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Buying Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CPC / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CPM / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CTR / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Campaign ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Campaign Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Canvas Avg View Percent / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Canvas Avg View Time / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Catalog Segment Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Catalog Segment Value / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Catalog Segment Value Mobile / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Catalog Segment Value Omni / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Catalog Segment Value Website / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Click / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Conversion / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Conversion Rate Ranking / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Conversion Value / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Converted Product Quantity / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Converted Product Value / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost Per 15sec Video View / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost Per Action Type / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost Per Ad Click / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost Per Conversion / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost Per DDA Count / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Cost Per Inline Link Click / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Cost Per Inline Post Engagement / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Cost Per One Thousand Ad Impression / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost Per Outbound Click / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost Per Thruplay / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost Per Unique Action Type / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost Per Unique Click / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Cost Per Unique Inline Link Click / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Cost Per Unique Outbound Click / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Cost per 2sec Video View / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** DDA Count / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** DDA Result / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Engagement Rate Ranking / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Frequency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Full View Impression / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Full View Reach / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Impression / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inline Link Click / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inline Link Click CTR / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inline Post Engagement / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Instant Experience Clicks To Open / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Instant Experience Clicks To Start / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Instant Experience Outbound Click / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Mobile App Purchase Roas / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Objective / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Optimization Goal / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Outbound Click / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Outbound Clicks CTR / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Purchase Roas / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Qualifying Question Qualify Answer Rate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Quality Ranking / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Reach / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Social Spend / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Spend / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Start Date / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Stop Date / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Unique Click / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Video 30sec Watched Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Video Avg Time Watched Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Video P100 Watched Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Video P25 Watched Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Video P50 Watched Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Video P95 Watched Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Video Play Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Video Play Curve Action / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Website CTR / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Website Purchase Roas / **** Data type**:** List / **** Supported filters**:** 

- ** Ad Set**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Campaign**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

