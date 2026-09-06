

# Zoom connector for Amazon AppFlow
<a name="connectors-zoom"></a>

Zoom is an online video conferencing solution for individuals and teams. If you're a Zoom user, your account contains data about your resources, such as users, groups, and rooms. You can use Amazon AppFlow to transfer data from Zoom to certain AWS services or other supported applications.

## Amazon AppFlow support for Zoom
<a name="zoom-support"></a>

Amazon AppFlow supports Zoom as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Zoom.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Zoom.

**Supported Zoom plans**  
Amazon AppFlow supports only paid plans for Zoom, such as Pro, Business, or Enterprise. You can’t use Amazon AppFlow to transfer data from a Zoom account that subscribes to the free Basic plan. For more information about Zoom plans, see [Plans & Pricing](https://zoom.us/pricing) on the Zoom website.

## Before you begin
<a name="zoom-prereqs"></a>

To use Amazon AppFlow to transfer data from Zoom to supported destinations, you must meet these requirements:
+ You have an account with Zoom that contains the data that you want to transfer. For more information about the Zoom data objects that Amazon AppFlow supports, see [Supported objects](#zoom-objects).
+ In the Zoom App Marketplace, you've created an OAuth app for Amazon AppFlow. This app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For more information, see [Build an App](https://marketplace.zoom.us/docs/guides/build/) in the Zoom Developers Docs.
+ You've configured If the app with the following settings:
  + You've disabled the option to publish to the Zoom App Marketplace.
  + You've added the recommended scopes below.
  + You've added one or more redirect URLs for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Zoom. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

Note the values for client ID and client secret from your OAuth app settings. You provide these values to Amazon AppFlow when you connect to your Zoom account.

### Recommended scopes
<a name="zoom-scopes"></a>

Your OAuth app must allow the necessary scopes for the Zoom APIs. These scopes permit Amazon AppFlow to securely access your data in Zoom. We recommend that you enable the scopes below so that Amazon AppFlow can access all supported data objects.

If you want to allow fewer scopes, you can omit any scopes that apply to objects that you don't want to transfer.

You can add scopes by managing your app in the Zoom App Marketplace.
+ `group:master`
+ `group:read:admin`
+ `group:write:admin`
+ `report:master`
+ `report:read:admin`
+ `report_chat:read:admin`
+ `role:master`
+ `role:read:admin`
+ `role:write:admin`
+ `room:master`
+ `room:read:admin`
+ `room:write:admin`
+ `user:master`
+ `user:read:admin`
+ `user:write:admin`

For more information about these scopes, see [OAuth Scopes](https://marketplace.zoom.us/docs/guides/auth/oauth/oauth-scopes/) in the Zoom Developers Docs.

## Connecting Amazon AppFlow to your Zoom account
<a name="zoom-connecting"></a>

To connect Amazon AppFlow to your Zoom account, provide the client credentials from your OAuth app. Amazon AppFlow uses these credentials to access your data. If you haven't yet configured your Zoom account for Amazon AppFlow integration, see [Before you begin](#zoom-prereqs).

**To connect to Zoom**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Zoom**.

1. Choose **Create connection**.

1. In the **Connect to Zoom** window, for **Client ID** and **Client secret**, enter the client credentials from your OAuth app.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**. A **Sign in** window opens.

1. Enter your user name and password to sign in to your Zoom account.

1. When prompted, verify your sign-in attempt with a one-time passcode.

1. Authorize Amazon AppFlow to access your Zoom account.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Zoom as the data source, you can select this connection.

## Transferring data from Zoom with a flow
<a name="zoom-transfer-data"></a>

To transfer data from Zoom, create an Amazon AppFlow flow, and choose Zoom as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Zoom, see [Supported objects](#zoom-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#zoom-destinations).

## Supported destinations
<a name="zoom-destinations"></a>

When you create a flow that uses Zoom as the data source, you can set the destination to any of the following connectors: 
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
<a name="zoom-objects"></a>

When you create a flow that uses Zoom as the data source, you can transfer any of the following data objects to supported destinations:



- ** Daily Report**
  - **** Field**:** Date / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Meeting Minutes / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Meetings / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Month Year / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** New Users / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Participants / **** Data type**:** Integer / **** Supported filters**:** 

- ** Group**
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Members / **** Data type**:** Integer / **** Supported filters**:** 

- ** Group Admin**
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 

- ** Group Member**
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** Integer / **** Supported filters**:** 

- ** Role**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Members / **** Data type**:** Integer / **** Supported filters**:** 

- ** User**
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Custom Attributes / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Department / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Employee Unique Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Group Ids / **** Data type**:** ByteArray / **** Supported filters**:** 
  - **** Field**:** Host Key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** IM Group Ids / **** Data type**:** ByteArray / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Client Version / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Login Time / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Personal Meeting ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Plan United Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Role Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Timezone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Verified / **** Data type**:** Integer / **** Supported filters**:** 

- ** Zoom Room**
  - **** Field**:** Activation Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Location Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Room Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Unassigned Rooms / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO

