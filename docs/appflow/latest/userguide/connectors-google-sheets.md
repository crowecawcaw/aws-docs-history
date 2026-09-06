

# Google Sheets connector for Amazon AppFlow
<a name="connectors-google-sheets"></a>

Google Sheets is a spreadsheet based collaboration service that helps teams share data in real time across multiple devices. If you’re a Google Sheets user, your account contains data about spreadsheets, documents, slides, meetings, security, and more. You can use Amazon AppFlow to transfer data from Google Sheets to certain AWS services or other supported applications.



## Amazon AppFlow support for Google Sheets
<a name="google-sheets-support"></a>

Amazon AppFlow supports Google Sheets as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Google Sheets.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Google Sheets.

Amazon AppFlow currently supports Google Sheets API v4 and Google Drive API v3. 

## Before you begin
<a name="google-sheets-prereqs"></a>

To use Amazon AppFlow to transfer data from Google Sheets to supported destinations, you must meet these requirements:
+ You have a Google account where you sign in to use the Google Sheets app. In your Google account, Google Sheets contains the data that you want to transfer.
+ You have a Google Cloud Platform account and a Google Cloud project.
+ In your Google Cloud project, you've enabled the Google Sheets API and Google Drive APIs. For the steps to enable them, see [Enable and disable APIs](https://support.google.com/googleapi/answer/6158841) in the API Console Help for Google Cloud Platform.
+ In your Google Cloud project, you've configured an OAuth consent screen for external users. For more information about the OAuth consent screen, see [Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615#) in the Google Cloud Platform Console Help.
+ In the OAuth consent screen, you've added the following scopes:
  + The Google Sheets API read-only scope, https://www.googleapis.com/auth/spreadsheets.readonly.
  + The Google Drive API read-only scope, https://www.googleapis.com/auth/drive.readonly.

  For more information about these scopes, see [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes) in the Google Identity documentation.
+ In your Google Cloud project, you've configured an OAuth 2.0 client ID. For the steps to create this client ID, see [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849?hl=en#zippy=) in the Google Cloud Platform Console Help.

  The OAuth 2.0 client ID must have one or more authorized redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Google Sheets. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
+  In addition, set the authorized JavaScript origins URL to the following:

  `https://{{region}}.console.aws.amazon.com`

  Like the *region* in the redirect URLs, the region in the JavaScript origins URL is the code for the AWS region where you use Amazon AppFlow to transfer data from Google Sheets. So if, as above, you’re in the US East (N. Virginia) Region, the URL is the following:

  `https://us-east-1.console.aws.amazon.com`

Note the client ID and client secret from the settings for your OAuth 2.0 client ID. You provide these values to Amazon AppFlow when you connect to your Google Cloud project.

## Connecting Amazon AppFlow to your Google Sheets account
<a name="google-sheets-connecting"></a>

To connect Amazon AppFlow to your Google Sheets account, provide details from your Google Sheets project so that Amazon AppFlow can access your data. If you haven't yet configured your Google Sheets project for Amazon AppFlow integration, see [Before you begin](#google-sheets-prereqs).

**To connect to Google Sheets**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Google Sheets**.

1. Choose **Create connection**.

1. In the **Connect to Google Sheets** window, enter the following information:
   + **Access type** – Choose **offline**.
   + **Client ID** – The client ID of the OAuth 2.0 client ID in your Google Sheets project.
   + **Client secret** – The client secret of the OAuth 2.0 client ID in your Google Sheets project.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your Google Sheets account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Google Sheets as the data source, you can select this connection.

## Transferring data from Google Sheets with a flow
<a name="google-sheets-transfer-data"></a>

To transfer data from Google Sheets, create an Amazon AppFlow flow, and choose Google Sheets as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Google Sheets, see [Supported objects](#google-sheets-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#google-sheets-destinations).

If a flow is left idle for too long, it can time out. To increase the default session time, see [Set session length for Google Cloud services](https://support.google.com/a/answer/9368756) in the Google Workspace Admin Help.

Note also that the Google Sheets API is a shared service. To keep the overall environment functioning smoothly, Google places limits on the number of read requests you’re allowed per minute. If you exceed the limit, Google Sheets will generate an error. To learn more about limits, and about how to request an increase in your limit, see [Usage limits](https://developers.google.com/sheets/api/limits) in the Google Sheets Reference.

## Supported destinations
<a name="google-sheets-destinations"></a>

When you create a flow that uses Google Sheets as the data source, you can set the destination to any of the following connectors: 
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
<a name="google-sheets-objects"></a>

When you create a ﬂow that uses Google Sheets as the data source, you can transfer any of the supported data objects to supported destinations. Other connectors support specific objects, but the Google Sheets connector lacks predefined entities. Instead, it displays entities dynamically, based on the current column headers in the Google Sheets spreadsheet itself.

Note that if you change or update the column headers after creating a flow, you’ll need to either update the headers by using the Amazon AppFlow update flow page, or create a new flow. For information on updating a flow, see [Managing Amazon AppFlow flows ](https://docs.aws.amazon.com/appflow/latest/userguide/flows-manage.html). For information on creating a new flow, see [Creating flows in Amazon AppFlow ](https://docs.aws.amazon.com/appflow/latest/userguide/create-flow.html).