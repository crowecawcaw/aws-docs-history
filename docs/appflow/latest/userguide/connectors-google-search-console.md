

# Google Search Console connector for Amazon AppFlow
<a name="connectors-google-search-console"></a>

Google Search Console is a service from Google that allows website owners to optimize and manage their sites’ presence in Google Search results. If you're a Google Search Console user, your account contains data about your sites and their search traffic. You can use Amazon AppFlow to transfer data from Google Search Console to certain AWS services or other supported applications.

## Amazon AppFlow support for Google Search Console
<a name="google-search-console-support"></a>

Amazon AppFlow supports Google Search Console as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Google Search Console.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Google Search Console.

## Before you begin
<a name="google-search-console-prereqs"></a>

To use Amazon AppFlow to transfer data from Google Search Console to supported destinations, you must meet these requirements:
+ You have a Google Cloud Platform account and a Google Cloud project.
+ In Google Search Console, you have one or more verified website properties that have the data that you want to transfer. For the steps to add a property, see [Add a website property to Search Console](https://support.google.com/webmasters/answer/34592?hl=en) in the Search Console Help. For more information about the Google Search Console data objects that Amazon AppFlow supports, see [Supported objects](#google-search-console-objects).
+ In your Google Cloud project, you've enabled the Google Search Console API. For the steps to enable it, see [Enable and disable APIs](https://support.google.com/googleapi/answer/6158841) in the API Console Help for Google Cloud Platform.
+ In your Google Cloud project, you've configured an OAuth consent screen for external users that meets the following requirements:
  + You've set *amazon.com* as an authorized domain.
  + You've set *Google Ads API* as an authorized scope.

  For information about the OAuth consent screen, see [Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615#) in the Google Cloud Platform Console Help.
+ In your Google Cloud project, you've configured an OAuth 2.0 client ID. For the steps to create one, see [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849?hl=en#zippy=) in the Google Cloud Platform Console Help.

  The OAuth 2.0 client ID must have one or more authorized redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Google Search Console. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

Note the client ID and client secret from the settings for your OAuth 2.0 client ID. You provide these values to Amazon AppFlow when you connect to your Google Cloud project.

## Connecting Amazon AppFlow to your Google Search Console account
<a name="google-search-console-connecting"></a>

To connect Amazon AppFlow to your Google Search Console account, provide the client credentials from the OAuth 2.0 client ID from your Google Cloud project. Amazon AppFlow uses these credentials to access your data. If you haven't yet configured your Google Cloud project for Amazon AppFlow integration, see [Before you begin](#google-search-console-prereqs).

**To connect to Google Search Console**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Google Search Console**.

1. Choose **Create connection**.

1. In the **Connect to Google Search Console** window, enter the following information:
   + **access\_type** – Choose **offline**.
   + **Client ID** – The client ID of the OAuth 2.0 client ID in your Google Cloud project.
   + **Client secret** – The client secret of the OAuth 2.0 client ID in your Google Cloud project.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**. A **Sign in with Google** window opens.

1. Choose your Google account, and sign in.

1. On the page titled **amazon.com wants to access your Google Account**, choose Continue.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Google Search Console as the data source, you can select this connection.

## Transferring data from Google Search Console with a flow
<a name="google-search-console-transfer-data"></a>



To transfer data from Google Search Console, create an Amazon AppFlow flow, and choose Google Search Console as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Google Search Console, see [Supported objects](#google-search-console-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#google-search-console-destinations).

## Supported destinations
<a name="google-search-console-destinations"></a>

When you create a flow that uses Google Search Console as the data source, you can set the destination to any of the following connectors: 
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
<a name="google-search-console-objects"></a>

When you create a flow that uses Google Search Console as the data source, you can transfer any of the following data objects to supported destinations:



- ** Search Analytic**
  - **** Field**:** clicks / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** country / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ctr / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** device / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** dimension / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** impressions / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** keys / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** page / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS
  - **** Field**:** position / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** query / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS
  - **** Field**:** search\_type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** start\_end\_date / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN

- ** Site**
  - **** Field**:** permissionLevel / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** siteUrl / **** Data type**:** String / **** Supported filters**:** 

- ** Sitemap**
  - **** Field**:** contents / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** errors / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** isPending / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** isSitemapsIndex / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** lastDownloaded / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** lastSubmitted / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** path / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** warnings / **** Data type**:** Long / **** Supported filters**:** 

