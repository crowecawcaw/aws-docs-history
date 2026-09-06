

# PayPal connector for Amazon AppFlow
<a name="connectors-paypal"></a>

PayPal is a payments system that facilitates online money transfers between parties, such as transfers between customers and online vendors. If you're a PayPal user, your account contains data about your transactions, such as their payers, dates, and statuses. You can use Amazon AppFlow to transfer data from PayPal to certain AWS services or other supported applications.

## Amazon AppFlow support for PayPal
<a name="paypal-support"></a>

Amazon AppFlow supports PayPal as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from PayPal.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to PayPal.

## Before you begin
<a name="paypal-prereqs"></a>

To use Amazon AppFlow to transfer data from PayPal to supported destinations, you must meet these requirements:
+ You have an account with PayPal that contains the data that you want to transfer. For more information about the PayPal data objects that Amazon AppFlow supports, see [Supported objects](#paypal-objects).
+ In PayPal Developer, you've created a REST API app for Amazon AppFlow. The app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For the steps to create an app, see [How do I create REST API credentials?](https://www.paypal.com/us/cshelp/article/how-do-i-create-rest-api-credentials-ts1949) in the PayPal Help Center.
+ You have configured the app with one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from PayPal. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

Note the client ID and secret from the settings for your REST API app. You provide these values to Amazon AppFlow when you connect to your PayPal account.

## Connecting Amazon AppFlow to your PayPal account
<a name="paypal-connecting"></a>

To connect Amazon AppFlow to your PayPal account, provide the client credentials from your REST API app so that Amazon AppFlow can access your data. If you haven't yet configured your PayPal account for Amazon AppFlow integration, see [Before you begin](#paypal-prereqs).

**To connect to PayPal**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **PayPal**.

1. Choose **Create connection**.

1. In the **Connect to PayPal** window, enter the following information:
   + **Authorization tokens URL** – Do one of the following:
     + To connect to a REST API app in the PayPal Live environment, choose **https://api-m.paypal.com/v1/oauth2/token**.
     + To connect to a REST API app in the PayPal Sandbox environment, choose **https://api-m.sandbox.paypal.com/v1/oauth2/token**.
   + **Client ID** – The client ID of your REST API app in PayPal Developer.
   + **Client secret** – The secret of your REST API app in PayPal Developer.
   + **Instance URL** – Do one of the following:
     + To connect to a REST API app in the PayPal Live environment, choose **https://api-m.paypal.com**.
     + To connect to a REST API app in the PayPal Sandbox environment, choose **https://api-m.sandbox.paypal.com**.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your PayPal account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses PayPal as the data source, you can select this connection.

## Transferring data from PayPal with a flow
<a name="paypal-transfer-data"></a>

To transfer data from PayPal, create an Amazon AppFlow flow, and choose PayPal as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for PayPal, see [Supported objects](#paypal-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#paypal-destinations).

## Supported destinations
<a name="paypal-destinations"></a>

When you create a flow that uses PayPal as the data source, you can set the destination to any of the following connectors: 
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
<a name="paypal-objects"></a>

When you create a flow that uses PayPal as the data source, you can transfer any of the following data objects to supported destinations:



- ** Transaction**
  - **** Field**:** Auction Info / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Balance Affecting Records Only / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Cart Info / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Date Range / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** Incentive Info / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Last Refreshed Date Time / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Payer Info / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Payment Instrument Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Shipping Info / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Store ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Store Info / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Terminal ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Transaction Currency / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Transaction ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Transaction Info / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Transaction Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Transaction Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

