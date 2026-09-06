

# Google BigQuery connector for Amazon AppFlow
<a name="connectors-googlebigquery"></a>

Google BigQuery is a query and analysis solution. If you’re a Google BigQuery user, your account contains data, analytics, and more. You can use Amazon AppFlow to transfer data between Google BigQuery and certain AWS services or other supported applications.

## Amazon AppFlow support for Google BigQuery
<a name="googlebigquery-support"></a>

Amazon AppFlow supports Google BigQuery as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Google BigQuery.

**Supported as a data destination?**  
Yes. You can use Amazon AppFlow to transfer data to Google BigQuery.

## Before you begin
<a name="googlebigquery-prereqs"></a>

To use Amazon AppFlow to transfer data from Google BigQuery to supported destinations, you must meet these requirements:
+ You have an account with Google BigQuery that contains the data that you want to transfer. For more information about the Google BigQuery data objects that Amazon AppFlow supports, see [Supported objects](#googlebigquery-objects).
+ In your Google BigQuery account, you've created an External OAuth2 Google Cloud web app for Amazon AppFlow, and you’ve added the appropriate scopes. The app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For information about how to create an app, see [ Building a Node.js app on App Engine ]( https://cloud.google.com/appengine/docs/standard/nodejs/building-app ) in the Google BigQuery documentation.
+ You've activated the access scopes that provide access to the data that you want to transfer. For more information about Google BigQuery scopes, see [ Comply with OAuth 2.0 policies ]( https://developers.google.com/identity/protocols/oauth2/production-readiness/policy-compliance ) in the *Google Identity Documentation*. 
+ You've configured the app with one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Google BigQuery. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
+ Note the client ID and client secret from the settings for your OAuth 2.0 client ID. You provide these values to Amazon AppFlow when you connect to your Google BigQuery project. 

## Connecting Amazon AppFlow to your Google BigQuery account
<a name="googlebigquery-connecting"></a>

To connect Amazon AppFlow to your Google BigQuery account, provide the client credentials from your Google Cloud web app so that Amazon AppFlow can access your data. If you haven't yet configured your Google BigQuery project for Amazon AppFlow integration, see [Before you begin](#googlebigquery-prereqs).

**To connect to Google BigQuery**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Google BigQuery**.

1. Choose **Create connection**.

1. In the **Connect to Google BigQuery** window, enter the following information:
   + **Connection name** — A name for your connection.
   + **access\_type** — Specify an access type to generate a refresh token. 
   + **Client ID** — The client ID in your Google Cloud web app. 
   + **Client secret** — The client secret in your Google Cloud web app.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. Choose **Connect**.

1. In the window that appears, sign in to your Google BigQuery account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Google BigQuery as the data source, you can select this connection.

## API preference
<a name="googlebigquery-api-preference"></a>

When you use Google BigQuery as either the source or destination, you can configure the **Google BigQuery API preference** setting. Use this setting to specify whether Amazon AppFlow uses synchronous (smaller data transfers) or asynchronous (larger transfers) data transfer when you run your flow.

The Amazon AppFlow console provides this setting on the **Configure flow** page under **Source details** or **Destination details**. To view it, expand the **Additional settings** section.

You can choose one of these options:
+ **Automatic (default)** — For each flow run, Amazon AppFlow selects the type of data transfer to use.
+ **Standard** — Amazon AppFlow uses only Google BigQuery synchronous data transfer. This option optimizes your flow for small to medium-sized data transfers. 
+ **Bulk** — Amazon AppFlow runs Google BigQuery asynchronous data transfers, and it's optimal for large datasets.

## Transferring data to or from Google BigQuery with a flow
<a name="googlebigquery-transfer-data"></a>

To transfer data to or from Google BigQuery, create an Amazon AppFlow flow, and choose Google BigQuery as the data source or destination. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Google BigQuery, see [Supported objects](#googlebigquery-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#googlebigquery-destinations).

## Supported destinations
<a name="googlebigquery-destinations"></a>

When you create a flow that uses Google BigQuery as the data source, you can set the destination to any of the following connectors: 
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
<a name="googlebigquery-objects"></a>

When you create a ﬂow that uses Google BigQuery as the data source, you can transfer any data from any table that you’ve defined. Other connectors support specific objects, but the Google BigQuery connector lacks predefined entities. Instead, it displays entities dynamically, based on the current column headers in the Google BigQuery table itself.