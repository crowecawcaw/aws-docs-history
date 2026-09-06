

# Zendesk Sunshine connector for Amazon AppFlow
<a name="connectors-zendesk-sunshine"></a>

Zendesk Sunshine is an application that helps builders create custom experiences on the Zendesk platform for ticketing and customer service. If you're a Zendesk Sunshine user, your account contains data about your Zendesk objects and their relationships. You can use Amazon AppFlow to transfer data from Zendesk Sunshine to certain AWS services or other supported applications.

## Amazon AppFlow support for Zendesk Sunshine
<a name="zendesk-sunshine-support"></a>

Amazon AppFlow supports Zendesk Sunshine as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Zendesk Sunshine.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Zendesk Sunshine.

## Before you begin
<a name="zendesk-sunshine-prereqs"></a>

To use Amazon AppFlow to transfer data from Zendesk Sunshine to supported destinations, you must meet these requirements:
+ You have an account with Zendesk that contains the data that you want to transfer. For more information about the Zendesk Sunshine data objects that Amazon AppFlow supports, see [Supported objects](#zendesk-sunshine-objects).
+ In your account, you've activated custom objects. For the steps to activate, see [Enabling custom objects](https://developer.zendesk.com/documentation/custom-data/custom-objects/getting-started-with-custom-objects/#enabling-custom-objects) in the Zendesk Developers documentation.
+ In your account settings, you've created an OAuth client for Amazon AppFlow. The OAuth client provides the client credentials that Amazon AppFlow uses to access your data securely with authenticated calls to your account.
+ You've configured your OAuth client with one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Zendesk Sunshine. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

In the settings for your OAuth client, note the client ID and client secret. You provide these values to Amazon AppFlow when you connect to your Zendesk account.

## Connecting Amazon AppFlow to Zendesk Sunshine
<a name="zendesk-sunshine-connecting"></a>

To connect Amazon AppFlow to Zendesk Sunshine, provide the client credentials from your OAuth client so that Amazon AppFlow can access your data. If you haven't yet configured your Zendesk Sunshine project for Amazon AppFlow integration, see [Before you begin](#zendesk-sunshine-prereqs).

**To connect to Zendesk Sunshine**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Zendesk Sunshine**.

1. Choose **Create connection**.

1. In the **Connect to Zendesk Sunshine** window, enter the following information:
   + **Custom authorization tokens URL** and **Custom authorization code URL** – For each of these fields, enter your Zendesk subdomain. You can find the subdomain in the URL that you visit when you sign in to Zendesk. For example, in the account URL `https://my-account.zendesk.com`, the subdomain is `my-account`.
   + **Client ID** and **Client secret** – The client credentials that Zendesk assigned to your OAuth client.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**.

1. In the window that appears, sign in to your Zendesk account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Zendesk Sunshine as the data source, you can select this connection.

## Transferring data from Zendesk Sunshine with a flow
<a name="zendesk-sunshine-transfer-data"></a>

To transfer data from Zendesk Sunshine, create an Amazon AppFlow flow, and choose Zendesk Sunshine as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Zendesk Sunshine, see [Supported objects](#zendesk-sunshine-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#zendesk-sunshine-destinations).

## Supported destinations
<a name="zendesk-sunshine-destinations"></a>

When you create a flow that uses Zendesk Sunshine as the data source, you can set the destination to any of the following connectors: 
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
<a name="zendesk-sunshine-objects"></a>

When you create a flow that uses Zendesk Sunshine as the data source, you can transfer any of the following data objects to supported destinations:



- ** Custom Object Type Permission**
  - **** Field**:** Data
  - **** Data type**:** Struct
  - **** Supported filters**:** 

- ** Custom Relationship Type Permission**
  - **** Field**:** Data
  - **** Data type**:** Struct
  - **** Supported filters**:** 

- ** Object Record**
  - **** Field**:** Attributes / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO, BETWEEN, LESS\_THAN
  - **** Field**:** External Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO, BETWEEN, LESS\_THAN

- ** Object Type**
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Schema / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** String / **** Supported filters**:** 

- ** Relationship Type**
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Target / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** String / **** Supported filters**:** 

- ** Relationship Type Record**
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Relationship Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Target / **** Data type**:** String / **** Supported filters**:** 

