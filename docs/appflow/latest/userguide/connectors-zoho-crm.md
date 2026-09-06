

# Zoho CRM connector for Amazon AppFlow
<a name="connectors-zoho-crm"></a>

Zoho CRM is a customer relationship management (CRM) system that helps its users conduct sales, marketing, and customer support. If you're a Zoho CRM user, your account contains data about your campaigns, deals, leads, and more. After you connect Amazon AppFlow your Zoho CRM account, you can use Zoho CRM as a data source or destination in your flows. Run these flows to transfer data between Zoho CRM and AWS services or other supported applications.

## Amazon AppFlow support for Zoho CRM
<a name="zoho-crm-support"></a>

Amazon AppFlow supports Zoho CRM as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Zoho CRM.

**Supported as a data destination?**  
Yes. You can use Amazon AppFlow to transfer data to Zoho CRM.

**Supported API version**  
Amazon AppFlow transfers your data by sending requests to version 2.1 of the Zoho CRM API.

## Before you begin
<a name="zoho-crm-prereqs"></a>

To use Amazon AppFlow to transfer data to or from Zoho CRM, you must meet these requirements:
+ You have a Zoho account, which you use to sign in to Zoho CRM. Your Zoho CRM account contains the data that you want to transfer. 
+ In the Zoho Developer Console, you've created a server-based application for Amazon AppFlow. This application provides the credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For the steps to create an application, see [Register your Application](https://www.zoho.com/crm/developer/docs/api/v2.1/register-client.html) in the Zoho CRM documentation.
+ You've configured the application with one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Zoho CRM. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
+ (Optional) If you want to use your application credentials for all Zoho CRM data centers, you've activated Multi-DC in the application settings, and you've activated all applicable domains.
+ If you want to transfer data to Zoho CRM as the destination, you've stored the data in an Amazon S3 bucket. If you're new to Amazon S3, see [Getting started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) in the *Amazon Simple Storage Service User Guide*.

From your application settings, note the values for client ID and client secret. You provide these values to Amazon AppFlow when you connect to your Zoho CRM account.

## Connecting Amazon AppFlow to your Zoho CRM account
<a name="zoho-crm-connecting"></a>

To connect Amazon AppFlow to your Zoho CRM account, provide details from your Zoho CRM application so that Amazon AppFlow can access your data. If you haven't yet configured your Zoho CRM account for Amazon AppFlow integration, see [Before you begin](#zoho-crm-prereqs).

**To connect to Zoho CRM**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Zoho CRM**.

1. Choose **Create connection**.

1. In the **Connect to Zoho CRM** window, enter the following information:
   + **Authorization tokens URL** – The URL for the supported data hosting region (Europe, US, Australia, India, or Japan).
   + **Authorization code URL** – The URL for authorization code based on the selected data hosting region.
   + **Client ID** – The client ID of the application in your Zoho CRM account.
   + **Client secret** – The client secret of the application in your Zoho CRM account.
   + **Instance URL** – The instance URL based on the selected data hosting region.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**.

1. In the window that appears, sign in to your Zoho CRM account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Zoho CRM as the data source, you can select this connection.

## Transferring data to or from Zoho CRM with a flow
<a name="zoho-crm-transfer-data"></a>

To transfer data to or from Zoho CRM, create an Amazon AppFlow flow, and choose Zoho CRM as the data source or destination. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

## Supported destinations
<a name="zoho-crm-destinations"></a>

When you create a flow that uses Zoho CRM as the data source, you can set the destination to any of the following connectors: 
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
+ [Zoho CRM](#connectors-zoho-crm)