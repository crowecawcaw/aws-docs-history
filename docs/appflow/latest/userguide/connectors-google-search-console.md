# Google Search Console connector for Amazon AppFlow

Google Search Console is a service from Google that allows website owners to optimize and manage
their sites’ presence in Google Search results. If you're a Google Search Console user, your account
contains data about your sites and their search traffic. You can use Amazon AppFlow to transfer data from
Google Search Console to certain AWS services or other supported applications.

## Amazon AppFlow support for Google Search Console

Amazon AppFlow supports Google Search Console as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Google Search Console.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Google Search Console.

## Before you begin

To use Amazon AppFlow to transfer data from Google Search Console to supported destinations, you must meet these
requirements:

- You have a Google Cloud Platform account and a Google Cloud project.
- In Google Search Console, you have one or more verified website properties that have the data
  that you want to transfer. For the steps to add a property, see [Add a website property to
  Search Console](https://support.google.com/webmasters/answer/34592?hl=en "https://support.google.com/webmasters/answer/34592?hl=en") in the Search Console Help. For more information about the
  Google Search Console data objects that Amazon AppFlow supports, see [Supported objects](#google-search-console-objects "#google-search-console-objects").
- In your Google Cloud project, you've enabled the Google Search Console API. For the steps to
  enable it, see [Enable and
  disable APIs](https://support.google.com/googleapi/answer/6158841 "https://support.google.com/googleapi/answer/6158841") in the API Console Help for Google Cloud Platform.
- In your Google Cloud project, you've configured an OAuth consent screen for external users
  that meets the following requirements:

      + You've set *amazon.com* as an authorized domain.
      + You've set *Google Ads API* as an authorized
       scope.

  For information about the OAuth consent screen, see [Setting up your OAuth consent
  screen](https://support.google.com/cloud/answer/10311615# "https://support.google.com/cloud/answer/10311615#") in the Google Cloud Platform Console Help.

- In your Google Cloud project, you've configured an OAuth 2.0 client ID. For the steps to
  create one, see [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849?hl=en#zippy= "https://support.google.com/cloud/answer/6158849?hl=en#zippy=") in the Google Cloud Platform Console Help.

The OAuth 2.0 client ID must have one or more authorized redirect URLs for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Google Search Console. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

Note the client ID and client secret from the settings for your OAuth 2.0 client ID. You
provide these values to Amazon AppFlow when you connect to your Google Cloud project.

## Connecting Amazon AppFlow to your Google Search Console

account

To connect Amazon AppFlow to your Google Search Console account, provide the client credentials from
the OAuth 2.0 client ID from your Google Cloud project. Amazon AppFlow uses these credentials to access
your data. If you haven't yet configured your Google Cloud project for Amazon AppFlow integration, see
[Before you begin](#google-search-console-prereqs "#google-search-console-prereqs").

###### To connect to Google Search Console

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Google Search Console**.
4. Choose **Create connection**.
5. In the **Connect to Google Search Console** window, enter the following
   information:
   - **access_type** – Choose **offline**.
   - **Client ID** – The client ID of the OAuth 2.0 client ID in your
     Google Cloud project.
   - **Client secret** – The client secret of the OAuth 2.0 client ID
     in your Google Cloud project.

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
that uses Google Search Console as the data source, you can select this connection.

## Transferring data from Google Search Console with a flow

To transfer data from Google Search Console, create an Amazon AppFlow flow, and choose Google Search Console as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Google Search Console, see [Supported objects](#google-search-console-objects "#google-search-console-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#google-search-console-destinations "#google-search-console-destinations").

## Supported destinations

When you create a flow that uses Google Search Console as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Google Search Console as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**      | **Field**       | **Data type**      | **Supported filters** |
| --------------- | --------------- | ------------------ | --------------------- | -------------- | -------- | -------- |
| Search Analytic | clicks          | Double             |                       |
| country         | String          | EQUAL_TO           |                       | ctr            | Double   |          |
| device          | String          | EQUAL_TO           |                       | dimension      | String   | EQUAL_TO |
| impressions     | Double          |                    |                       | keys           | List     |          |
| page            | String          | EQUAL_TO, CONTAINS |                       | position       | Double   |          |
| query           | String          | EQUAL_TO, CONTAINS |                       | search_type    | String   | EQUAL_TO |
| start_end_date  | DateTime        | BETWEEN            |
| Site            | permissionLevel | String             |                       |
| siteUrl         | String          |                    |
| Sitemap         | contents        | List               |                       |
| errors          | Long            |                    |                       | isPending      | Boolean  |          |
| isSitemapsIndex | Boolean         |                    |                       | lastDownloaded | DateTime |          |
| lastSubmitted   | DateTime        |                    |                       | path           | String   |          |
| type            | String          |                    |                       | warnings       | Long     |          |
