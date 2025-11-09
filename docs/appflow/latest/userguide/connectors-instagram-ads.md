# Instagram Ads connector for Amazon AppFlow

Instagram Ads is an advertising solution for Instagram. If you run ads on Instagram,
your account contains data about your ads, campaigns, ad images, and more. You can use Amazon AppFlow to
transfer data from Instagram Ads to certain AWS services or other supported
applications.

## Amazon AppFlow support for Instagram Ads

Amazon AppFlow supports Instagram Ads as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Instagram Ads.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Instagram Ads.

## Before you begin

To use Amazon AppFlow to transfer data from Instagram Ads to supported destinations, you must meet these
requirements:

- You have an Instagram business account that you use to run your ads. For more
  information about the Instagram Ads data objects that Amazon AppFlow supports, see [Supported objects](#instagram-ads-objects "#instagram-ads-objects").
- You've connected your Instagram business account to a Facebook Page. This connection
  makes it possible for third-party applications like Amazon AppFlow to access your Instagram data.
  For the steps to connect, see [Add or Remove an
  Instagram Account From Your Facebook Page](https://www.facebook.com/business/help/connect-instagram-to-page "https://www.facebook.com/business/help/connect-instagram-to-page") in the Meta Business Help
  Center.
- You have a Meta for Developers account.
- Your Meta for Developers account contains an app with its type set to _Business_. For information about how to create an app, see
  [Create an
  App](https://developers.facebook.com/docs/development/create-an-app "https://developers.facebook.com/docs/development/create-an-app") in the Meta for Developers App Development documentation.
- Your Meta for Developers app includes the _Facebook
  Login_ product, and you've configured the product to meet the following
  additional requirements:

      + Client OAuth login is enabled.
      + Web OAuth login is enabled.
      + One or more OAuth redirect URIs are present for Amazon AppFlow. Each of these URIs has the
       following form:


      `https://`region`.console.aws.amazon.com/appflow/oauth`


      In this URI, *region* is the code for the AWS Region
       where you use Amazon AppFlow to transfer data from the Marketing API. For example, if you use Amazon AppFlow
       in the US East (N. Virginia) region, the URI is
       `https://us-east-1.console.aws.amazon.com/appflow/oauth`.


      For the AWS Regions that Amazon AppFlow supports, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md") in the *AWS General Reference.*

  For more information about Facebook Login, see [Facebook Login](https://developers.facebook.com/docs/facebook-login "https://developers.facebook.com/docs/facebook-login") in the Meta
  For Developers documentation.

- Your app includes the _Marketing API_ product, and you
  use this product to manage the ads that Amazon AppFlow transfers data about.
- You've configured your app with the following permissions:

      + `ads_management`
      + `ads_read`
      + `business_management`
      + `read_insights`

  For more information about these permissions, see [Permissions
  Reference](https://developers.facebook.com/docs/permissions/reference "https://developers.facebook.com/docs/permissions/reference") in the Meta for Developers Graph API documentation.

Each of these permissions must be approved for _Advanced
Access_ through the _App Review_ process. For
the steps to create an App Review submission, see Submitting For Review in
the Meta for Developers App Review documentation.

From the settings for your app, note the app ID and app secret. You provide these values
to Amazon AppFlow when you connect to your account.

## Connecting Amazon AppFlow to Instagram Ads

To connect Amazon AppFlow to Instagram Ads, provide the app credentials from your Meta for
Developers app so that Amazon AppFlow can access your data. If you haven't yet configured an app for
Amazon AppFlow integration, see [Before you begin](#instagram-ads-prereqs "#instagram-ads-prereqs").

###### To connect to Instagram Ads

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Instagram Ads**.
4. Choose **Create connection**.
5. In the **Connect to Instagram Ads** window, enter the following
   information:
   - **Client ID** – The app ID from your Meta for Developers
     app.
   - **Client secret** – The app secret from your Meta for
     Developers app.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. 9. In the window that appears, sign in to your account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Instagram Ads as the data source, you can select this connection.

## Transferring data from Instagram Ads with a flow

To transfer data from Instagram Ads, create an Amazon AppFlow flow, and choose Instagram Ads as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Instagram Ads, see [Supported objects](#instagram-ads-objects "#instagram-ads-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#instagram-ads-destinations "#instagram-ads-destinations").

## Supported destinations

When you create a flow that uses Instagram Ads as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Instagram ads as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                              | **Field**        | **Data type** | **Supported filters** |
| --------------------------------------- | ---------------- | ------------- | --------------------- |
| Ad                                      |                  |               |                       |
| Ad Creative                             |                  |               |                       |
| Ad Image                                | Account ID       | String        |                       |
| Created Time                            | DateTime         |               |
| Creative                                | List             |               |
| Hash                                    | String           | EQUAL_TO      |
| Height                                  | Integer          |               |
| ID                                      | String           |               |
| Is Associated Creatives In Adgroup      | Boolean          |               |
| Name                                    | String           |               |
| Original Height                         | Integer          |               |
| Original Width                          | Integer          |               |
| Permalink URL                           | String           |               |
| Status                                  | String           |               |
| URL                                     | String           |               |
| URL 128                                 | String           |               |
| Updated Time                            | DateTime         |               |
| Width                                   | Integer          |               |
| Ad Insight                              | Account Currency | String        |                       |
| Account ID                              | String           |               |
| Account Name                            | String           |               |
| Action                                  | List             |               |
| Action Value                            | List             |               |
| Ad Click Action                         | List             |               |
| Ad ID                                   | String           |               |
| Ad Impression Action                    | List             |               |
| Ad Name                                 | String           |               |
| Adset ID                                | String           |               |
| Adset Name                              | String           |               |
| Age Targeting                           | String           |               |
| Attribution Setting                     | String           |               |
| Auction Bid                             | String           |               |
| Auction Competitiveness                 | String           |               |
| Auction Max Competitor Bid              | String           |               |
| Buying Type                             | String           |               |
| CPC                                     | String           |               |
| CPM                                     | String           |               |
| CTR                                     | String           |               |
| Campaign ID                             | String           |               |
| Campaign Name                           | String           |               |
| Canvas Avg View Percent                 | String           |               |
| Canvas Avg View Time                    | String           |               |
| Catalog Segment Action                  | List             |               |
| Catalog Segment Value                   | List             |               |
| Catalog Segment Value Mobile            | List             |               |
| Catalog Segment Value Omni              | List             |               |
| Catalog Segment Value Website           | List             |               |
| Click                                   | String           |               |
| Conversion                              | List             |               |
| Conversion Rate Ranking                 | String           |               |
| Conversion Value                        | List             |               |
| Converted Product Quantity              | List             |               |
| Converted Product Value                 | List             |               |
| Cost Per 15sec Video View               | List             |               |
| Cost Per Action Type                    | List             |               |
| Cost Per Ad Click                       | List             |               |
| Cost Per Conversion                     | List             |               |
| Cost Per DDA Count                      | String           |               |
| Cost Per Inline Link Click              | String           |               |
| Cost Per Inline Post Engagement         | String           |               |
| Cost Per One Thousand Ad Impression     | List             |               |
| Cost Per Outbound Click                 | List             |               |
| Cost Per Thruplay                       | List             |               |
| Cost Per Unique Action Type             | List             |               |
| Cost Per Unique Click                   | String           |               |
| Cost Per Unique Inline Link Click       | String           |               |
| Cost Per Unique Outbound Click          | List             |               |
| Cost per 2sec Video View                | List             |               |
| DDA Count                               | String           |               |
| DDA Result                              | List             |               |
| Engagement Rate Ranking                 | String           |               |
| Frequency                               | String           |               |
| Full View Impression                    | String           |               |
| Full View Reach                         | String           |               |
| Impression                              | String           |               |
| Inline Link Click                       | String           |               |
| Inline Link Click CTR                   | String           |               |
| Inline Post Engagement                  | String           |               |
| Instant Experience Clicks To Open       | String           |               |
| Instant Experience Clicks To Start      | String           |               |
| Instant Experience Outbound Click       | List             |               |
| Mobile App Purchase Roas                | List             |               |
| Objective                               | String           |               |
| Optimization Goal                       | String           |               |
| Outbound Click                          | List             |               |
| Outbound Clicks CTR                     | List             |               |
| Purchase Roas                           | List             |               |
| Qualifying Question Qualify Answer Rate | String           |               |
| Quality Ranking                         | String           |               |
| Reach                                   | String           |               |
| Social Spend                            | String           |               |
| Spend                                   | String           |               |
| Start Date                              | String           |               |
| Stop Date                               | String           |               |
| Unique Click                            | String           |               |
| Video 30sec Watched Action              | List             |               |
| Video Avg Time Watched Action           | List             |               |
| Video P100 Watched Action               | List             |               |
| Video P25 Watched Action                | List             |               |
| Video P50 Watched Action                | List             |               |
| Video P95 Watched Action                | List             |               |
| Video Play Action                       | List             |               |
| Video Play Curve Action                 | List             |               |
| Website CTR                             | List             |               |
| Website Purchase Roas                   | List             |               |
| Ad Set                                  |                  |               |                       |
| Campaign                                |                  |               |                       |
