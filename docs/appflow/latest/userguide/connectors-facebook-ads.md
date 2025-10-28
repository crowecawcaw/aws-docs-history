# Facebook Ads connector for Amazon AppFlow

You can use the Facebook Ads connector in Amazon AppFlow to transfer data about the ads that you run
with the Facebook Marketing API. The Marketing API is a series of Graph API endpoints that create
and manage ads on Facebook and Instagram. After you connect Amazon AppFlow to your Facebook developer
account, you can transfer data about your ads, campaigns, budgets, and more.

###### Topics

- [Facebook Ads support](#facebook-ads-support "#facebook-ads-support")
- [Before you begin](#facebook-ads-prereqs "#facebook-ads-prereqs")
- [Connecting Amazon AppFlow to the Facebook Marketing API](#facebook-ads-connecting "#facebook-ads-connecting")
- [Transferring data from the Facebook Marketing API with a
  flow](#facebook-ads-import-data "#facebook-ads-import-data")
- [Supported objects](#facebook-ads-reference-objects "#facebook-ads-reference-objects")
- [Supported destinations](#facebook-ads-reference-destinations "#facebook-ads-reference-destinations")

## Facebook Ads support

The following list summarizes how Amazon AppFlow supports the Facebook Marketing API through the
Facebook Ads connector.

**Supported as a data source?**

Yes. You can use Amazon AppFlow to transfer data about your Facebook ads from the Marketing
API.

**Supported as a data destination?**

No. You can't use Amazon AppFlow to transfer data to the Marketing API or your Facebook developer
account.

**Supported versions**

Amazon AppFlow supports the following versions of the Marketing API:

- v16.0
- v15.0
- v14.0

For more information about Marketing API versions, see [Changelog](https://developers.facebook.com/docs/graph-api/changelog "https://developers.facebook.com/docs/graph-api/changelog") in the Meta
for Developers documentation.

## Before you begin

To use Amazon AppFlow to transfer data from the Marketing API to supported destinations, you'll need
to meet these requirements:

- You have a Meta for Developers account.
- Your account contains an app with its type set to _Business_. For information about creating an app, see [Create an App](https://developers.facebook.com/docs/development/create-an-app "https://developers.facebook.com/docs/development/create-an-app") in
  the Meta for Developers App Development documentation.
- Your Meta for Developers app includes the _Facebook
  Login_ product, which you've configured to meet the following additional
  requirements:

      + Client OAuth login is enabled
      + Web OAuth login is enabled
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

- Your Meta for Developers app includes the _Marketing API_
  product, which you use to manage the ads that Amazon AppFlow transfers data about.

## Connecting Amazon AppFlow to the Facebook Marketing API

To connect Amazon AppFlow to data about your Facebook ads, create an Amazon AppFlow connection where you
provide details about your Meta for Developers app. If you haven't yet configured your app for
Amazon AppFlow integration, see [Before you begin](#facebook-ads-prereqs "#facebook-ads-prereqs").

###### To connect to Facebook Ads

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Facebook Ads**.
4. Choose **Create connection**.
5. In the **Connect to Facebook Ads** window, enter the following
   information:
   - **Custom authorization code URL** – Specify the Marketing API
     version that you use in your Facebook developer app to complete the URL shown in the console:

   `https://www.facebook.com/`version`/dialog/oauth`

   For example, if you use v14.0, the URL is
   `https://www.facebook.com/v14.0/dialog/oauth`.

   For the Marketing API versions that Amazon AppFlow supports, see [Facebook Ads support](#facebook-ads-support "#facebook-ads-support").
   - **Client ID** – The App ID that's assigned to your Meta for
     Developers app.
   - **Client secret** – The App secret that's assigned to your Meta
     for Developers app.
   - **Facebook Instance URL** – Choose
     **https://graph.facebook.com**.
   - **Facebook API version** – Choose the Marketing API version that
     you use. This version must match the one that you specified for **Custom
     authorization code URL**.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Facebook Ads as the data source, you can select this connection.

## Transferring data from the Facebook Marketing API with a

flow

To transfer data about your Facebook ads from the Marketing API, create an Amazon AppFlow flow, and
choose Facebook Ads as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose which data object you want to transfer. For most
Facebook Ads objects, you must choose two values: one for **Choose Facebook Ads
object**, and another for **Choose Facebook Ads subobject**. The
subobject is an individual instance of the object. For example, if the object that you choose is
**Campaigns**, then the subobject is the specific campaign to transfer data
from. For the objects that Amazon AppFlow supports for Facebook Ads, see [Supported objects](#facebook-ads-reference-objects "#facebook-ads-reference-objects").

Also choose the destination where you want to transfer the data object that you selected.
For information on how to configure your destination, see [Supported destinations](#facebook-ads-reference-destinations "#facebook-ads-reference-destinations").

## Supported objects

When you create a flow that uses Facebook Ads as the data source, you can transfer any of
the following data objects:

- Account
- Campaigns
- Ad Sets
- Campaign Budget
- Ads
- Ad Creatives

For more information about these objects and the data that they contain, see [Ad Campaign
Structure](https://developers.facebook.com/docs/marketing-api/campaign-structure "https://developers.facebook.com/docs/marketing-api/campaign-structure") in the Meta for Developers Marketing API documentation.

## Supported destinations

When you create a flow that uses Facebook Ads as the data source, you can set the destination to any of the following connectors:

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
