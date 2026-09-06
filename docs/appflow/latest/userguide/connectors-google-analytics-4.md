

# Google Analytics 4 connector for Amazon AppFlow
<a name="connectors-google-analytics-4"></a>

Google Analytics 4 is an analytics service that tracks and reports metrics about visitor interactions with your apps and websites. These metrics include page views, active users, and events. You can use Amazon AppFlow to transfer data from Google Analytics 4 to certain AWS services or other supported applications.

**Note**  
The Google Analytics 4 connector transfers data only from Google Analytics 4 properties. If you want to transfer data from Universal Analytics properties instead, use the [Google Analytics connector](google-analytics.md).  
In time, Google Analytics will end support for Universal Analytics properties, and that platform will fully support only Google Analytics 4 properties. For more information, see [Introducing the next generation of Analytics, Google Analytics 4 (GA4)](https://support.google.com/analytics/answer/10089681?hl=en).

## Amazon AppFlow support for Google Analytics 4
<a name="google-analytics-4-support"></a>

Amazon AppFlow supports Google Analytics 4 as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Google Analytics 4.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Google Analytics 4.

## Before you begin
<a name="google-analytics-4-prereqs"></a>

To use Amazon AppFlow to transfer data from Google Analytics 4 to supported destinations, you must meet these requirements:
+ You have a Google Analytics account with one or more data streams that collect the data that you want to transfer. For more information about the Google Analytics 4 data objects that Amazon AppFlow supports, see [Supported objects](#google-analytics-4-objects).
+ You have a Google Cloud Platform account and a Google Cloud project.
+ In your Google Cloud project, you've enabled the following APIs:
  + Google Analytics API
  + Google Analytics Admin API
  + Google Analytics Data API

  For the steps to enable these APIs, see [Enable and disable APIs](https://support.google.com/googleapi/answer/6158841) in the API Console Help for Google Cloud Platform.
+ In your Google Cloud project, you've configured an OAuth consent screen for external users. For information about the OAuth consent screen, see [Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615#) in the Google Cloud Platform Console Help.
+ In your Google Cloud project, you've configured an OAuth 2.0 client ID. For the steps to create an OAuth 2.0 client ID, see [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849?hl=en#zippy=) in the Google Cloud Platform Console Help.

  The OAuth 2.0 client ID must have one or more authorized redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Google Analytics 4. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

Note the client ID and client secret from the settings for your OAuth 2.0 client ID. When you connect to your Google Cloud project, you provide these values to Amazon AppFlow.

## Connecting Amazon AppFlow to Google Analytics 4
<a name="google-analytics-4-connecting"></a>

To connect Amazon AppFlow to Google Analytics 4, provide the client credentials from the OAuth 2.0 client ID from your Google Cloud project. Amazon AppFlow uses these credentials to access your data. If you haven't yet configured your Google Cloud project for Amazon AppFlow integration, see [Before you begin](#google-analytics-4-prereqs).

**To connect to Google Analytics 4**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Google Analytics 4**.

1. Choose **Create connection**.

1. In the **Connect to Google Analytics 4** window, enter the following information:
   + **Access type** – Choose **offline**.
   + **Client ID** – The client ID of the OAuth 2.0 client ID in your Google Cloud project.
   + **Client secret** – The client secret of the OAuth 2.0 client ID in your Google Cloud project.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**.

1. In the window that appears, sign in to your Google account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Google Analytics 4 as the data source, you can select this connection.

## Transferring data from Google Analytics 4 with a flow
<a name="google-analytics-4-transfer-data"></a>

To transfer data from Google Analytics 4, create an Amazon AppFlow flow, and choose Google Analytics 4 as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Google Analytics 4, see [Supported objects](#google-analytics-4-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#google-analytics-4-destinations).

## Supported destinations
<a name="google-analytics-4-destinations"></a>

When you create a flow that uses Google Analytics 4 as the data source, you can set the destination to any of the following connectors: 
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
<a name="google-analytics-4-objects"></a>

When you create a flow that uses Google Analytics 4 as the data source, you can transfer any of the following data objects to supported destinations:



- ** Core Report**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Real-Time Report**
  - **** Field**:** Dimension:appVersion / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:audienceId / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:audienceName / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:city / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:cityId / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:country / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:countryId / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:deviceCategory / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:eventName / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:minutesAgo / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:platform / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:streamId / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:streamName / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Dimension:unifiedScreenName / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO
  - **** Field**:** Metrics:activeUsers / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Metrics:conversions / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Metrics:eventCount / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Metrics:screenPageViews / **** Data type**:** String / **** Supported filters**:** 

