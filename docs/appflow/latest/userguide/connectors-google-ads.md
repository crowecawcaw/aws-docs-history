# Google Ads connector for Amazon AppFlow

Google Ads is a platform that advertisers use to display ads on the web, such as in Google
search results, YouTube videos, mobile apps, and on websites. If you are a Google Ads user, you
can use Amazon AppFlow to transfer data about your account, ad campaigns, and ad groups to certain
AWS services or other supported applications.

###### Topics

- [Google Ads support](#google-ads-support "#google-ads-support")
- [Before you begin](#google-ads-prereqs "#google-ads-prereqs")
- [Connecting Amazon AppFlow to your Google Ads account](#google-ads-connecting "#google-ads-connecting")
- [Transferring data from Google Ads with a flow](#google-ads-import-data "#google-ads-import-data")
- [Supported objects](#google-ads-reference-objects "#google-ads-reference-objects")
- [Supported destinations](#google-ads-reference-destinations "#google-ads-reference-destinations")

## Google Ads support

Amazon AppFlow supports Google Ads as follows.

**Supported as a data source?**

Yes. You can use Amazon AppFlow to transfer data from your Google Ads account.

**Supported as a data destination?**

No. You can't use Amazon AppFlow to transfer data to your Google Ads account.

## Before you begin

To use Amazon AppFlow to transfer data from Google Ads to AWS services, you'll need to meet these
requirements:

- You have a Google Cloud Platform account and a Google Cloud project.
- In your Google Cloud project, you've enabled the Google Ads API. For information on how
  to enable APIs, see [Enable and
  disable APIs](https://support.google.com/googleapi/answer/6158841 "https://support.google.com/googleapi/answer/6158841") in the API Console Help for Google Cloud Platform.
- You have a Google Ads developer token. For information on how to retrieve or create a
  developer token, see [Obtain Your
  Developer Token](https://developers.google.com/google-ads/api/docs/first-call/dev-token "https://developers.google.com/google-ads/api/docs/first-call/dev-token") in the Google Ads API documentation.
- In your Google Cloud project, you've configured an OAuth consent screen for external users
  that meets the following requirements:

      + You've set *amazon.com* as an authorized domain.
      + You've set *Google Ads API* as an authorized
       scope.

  For information about the OAuth consent screen, see [Setting up your OAuth consent
  screen](https://support.google.com/cloud/answer/10311615# "https://support.google.com/cloud/answer/10311615#") in the Google Cloud Platform Console Help.

- In your Google Cloud project, you've configured an OAuth 2.0 client ID. For information on
  how to create one, see [Setting up OAuth
  2.0](https://support.google.com/cloud/answer/6158849?hl=en#zippy= "https://support.google.com/cloud/answer/6158849?hl=en#zippy=") in the Google Cloud Platform Console Help.

The OAuth 2.0 client ID must have one or more authorized redirect URLs for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Google Ads. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

From your Google Ads settings, note your developer token. From the settings for your OAuth
2.0 client ID in your Google Cloud project, note your client ID and client secret. You will
provide these values to Amazon AppFlow when you connect to your Google Cloud project.

## Connecting Amazon AppFlow to your Google Ads account

To connect Amazon AppFlow to your Google Ads account, provide details from the Google Cloud project
so that Amazon AppFlow can access your Google Ads data. If you haven't yet configured your Google Cloud
project for Amazon AppFlow integration, see [Before you begin](#google-ads-prereqs "#google-ads-prereqs").

###### To connect to Google Ads

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Google Ads**.
4. Choose **Create connection**.
5. In the **Connect to Google Ads** window, enter the following
   information:
   - **Access type** – Choose **offline**.
   - **Client ID** – The client ID of the OAuth 2.0 client ID in your
     Google Cloud project.
   - **Client secret** – The client secret of the OAuth 2.0 client ID
     in your Google Cloud project.
   - **Google Ads developer token** – The developer token from your
     Google Ads account.
   - **Google Ads instance URL** – Choose
     **https://googleads.googleapis.com**.
   - **Google Ads API version** – Choose
     **v9**.
   - **Manager account ID** – Optionally, the account ID of a Google
     Ads manager account that you want to connect with Amazon AppFlow.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. A **Sign in with Google** window
opens. 9. Choose your Google account, and sign in. 10. On the page titled **amazon.com wants to access your Google Account**,
choose Continue.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Google Ads as the data source, you can select this connection.

## Transferring data from Google Ads with a flow

To transfer data from Google Ads, create an Amazon AppFlow flow, and choose Google Ads as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose which data object you want to transfer. For the objects
that Amazon AppFlow supports for Google Ads, see [Supported objects](#google-ads-reference-objects "#google-ads-reference-objects").

Also choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#google-ads-reference-destinations "#google-ads-reference-destinations").

## Supported objects

When you create a flow that uses Google Ads as the data source, you can transfer any of the
following data objects to supported destinations:

- Account
- Account Budget
- Campaign
- Campaign Budget
- Ad Group
- Ad Group Ad

## Supported destinations

When you create a flow that uses Google Ads as the data source, you can set the destination to any of the following connectors:

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
