# Google Analytics 4 connector for Amazon AppFlow

Google Analytics 4 is an analytics service that tracks and reports metrics about visitor
interactions with your apps and websites. These metrics include page views, active users, and
events. You can use Amazon AppFlow to transfer data from Google Analytics 4 to certain AWS services or
other supported applications.

###### Note

The Google Analytics 4 connector transfers data only from Google Analytics 4 properties. If
you want to transfer data from Universal Analytics properties instead, use the [Google Analytics connector](google-analytics.md "google-analytics.md").

In time, Google Analytics will end support for Universal Analytics properties, and that
platform will fully support only Google Analytics 4 properties. For more information, see [Introducing the next generation
of Analytics, Google Analytics 4 (GA4)](https://support.google.com/analytics/answer/10089681?hl=en "https://support.google.com/analytics/answer/10089681?hl=en").

## Amazon AppFlow support for Google Analytics 4

Amazon AppFlow supports Google Analytics 4 as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Google Analytics 4.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Google Analytics 4.

## Before you begin

To use Amazon AppFlow to transfer data from Google Analytics 4 to supported destinations, you must meet these
requirements:

- You have a Google Analytics account with one or more data streams that collect the data
  that you want to transfer. For more information about the Google Analytics 4 data objects that
  Amazon AppFlow supports, see [Supported objects](#google-analytics-4-objects "#google-analytics-4-objects").
- You have a Google Cloud Platform account and a Google Cloud project.
- In your Google Cloud project, you've enabled the following APIs:

      + Google Analytics API
      + Google Analytics Admin API
      + Google Analytics Data API

  For the steps to enable these APIs, see [Enable and disable APIs](https://support.google.com/googleapi/answer/6158841 "https://support.google.com/googleapi/answer/6158841") in
  the API Console Help for Google Cloud Platform.

- In your Google Cloud project, you've configured an OAuth consent screen for external
  users. For information about the OAuth consent screen, see [Setting up your OAuth consent
  screen](https://support.google.com/cloud/answer/10311615# "https://support.google.com/cloud/answer/10311615#") in the Google Cloud Platform Console Help.
- In your Google Cloud project, you've configured an OAuth 2.0 client ID. For the steps to
  create an OAuth 2.0 client ID, see [Setting up OAuth
  2.0](https://support.google.com/cloud/answer/6158849?hl=en#zippy= "https://support.google.com/cloud/answer/6158849?hl=en#zippy=") in the Google Cloud Platform Console Help.

The OAuth 2.0 client ID must have one or more authorized redirect URLs for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Google Analytics 4. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

Note the client ID and client secret from the settings for your OAuth 2.0 client ID. When
you connect to your Google Cloud project, you provide these values to Amazon AppFlow.

## Connecting Amazon AppFlow to Google Analytics 4

To connect Amazon AppFlow to Google Analytics 4, provide the client credentials from the OAuth 2.0
client ID from your Google Cloud project. Amazon AppFlow uses these credentials to access your data. If
you haven't yet configured your Google Cloud project for Amazon AppFlow integration, see [Before you begin](#google-analytics-4-prereqs "#google-analytics-4-prereqs").

###### To connect to Google Analytics 4

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Google Analytics 4**.
4. Choose **Create connection**.
5. In the **Connect to Google Analytics 4** window, enter the following
   information:
   - **Access type** – Choose **offline**.
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
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. 9. In the window that appears, sign in to your Google account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Google Analytics 4 as the data source, you can select this connection.

## Transferring data from Google Analytics 4 with a flow

To transfer data from Google Analytics 4, create an Amazon AppFlow flow, and choose Google Analytics 4 as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Google Analytics 4, see [Supported objects](#google-analytics-4-objects "#google-analytics-4-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#google-analytics-4-destinations "#google-analytics-4-destinations").

## Supported destinations

When you create a flow that uses Google Analytics 4 as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Google Analytics 4 as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                  | **Field**            | **Data type**      | **Supported filters** |
| --------------------------- | -------------------- | ------------------ | --------------------- |
| Core Report                 |                      |                    |                       |
| Real-Time Report            | Dimension:appVersion | String             | CONTAINS, EQUAL_TO    |
| Dimension:audienceId        | String               | CONTAINS, EQUAL_TO |
| Dimension:audienceName      | String               | CONTAINS, EQUAL_TO |
| Dimension:city              | String               | CONTAINS, EQUAL_TO |
| Dimension:cityId            | String               | CONTAINS, EQUAL_TO |
| Dimension:country           | String               | CONTAINS, EQUAL_TO |
| Dimension:countryId         | String               | CONTAINS, EQUAL_TO |
| Dimension:deviceCategory    | String               | CONTAINS, EQUAL_TO |
| Dimension:eventName         | String               | CONTAINS, EQUAL_TO |
| Dimension:minutesAgo        | String               | CONTAINS, EQUAL_TO |
| Dimension:platform          | String               | CONTAINS, EQUAL_TO |
| Dimension:streamId          | String               | CONTAINS, EQUAL_TO |
| Dimension:streamName        | String               | CONTAINS, EQUAL_TO |
| Dimension:unifiedScreenName | String               | CONTAINS, EQUAL_TO |
| Metrics:activeUsers         | String               |                    |
| Metrics:conversions         | String               |                    |
| Metrics:eventCount          | String               |                    |
| Metrics:screenPageViews     | String               |                    |
