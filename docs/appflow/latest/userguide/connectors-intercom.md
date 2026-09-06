

# Intercom connector for Amazon AppFlow
<a name="connectors-intercom"></a>

Intercom is a customer engagement solution. It helps organizations learn who is using a website or product so that the organization can engage those users with targeted messages and support. If you're an Intercom user, then your account contains data about your contacts, conversations, customer segments, and more. You can use Amazon AppFlow to transfer data from Intercom to certain AWS services or other supported applications.

## Amazon AppFlow support for Intercom
<a name="intercom-support"></a>

Amazon AppFlow supports Intercom as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Intercom.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Intercom.

## Before you begin
<a name="intercom-prereqs"></a>

To use Amazon AppFlow to transfer data from Intercom to supported destinations, you must meet these requirements:
+ You have an account with Intercom that contains the data that you want to transfer. For more information about the Intercom data objects that Amazon AppFlow supports, see [Supported objects](#intercom-objects).
+ In your Intercom account, you've created an app for Amazon AppFlow. The app provides the credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For the steps to create an app, see [How do I create an app?](https://www.intercom.com/help/en/articles/1827298-how-do-i-create-an-app) in the Intercom Help Center.
+ You've configured the app with a redirect URL for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Intercom. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

**Note**  
You must add your connecting profile region redirect URL (or URLs) to the list of redirect URLs in your Intercom app. If you don’t make this addition, the app defaults to the first redirect URL in the list, and your connection will fail. For more information, see [ Redirect URLs ]( https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/setting-up-oauth/#redirect-urls ) in the Intercom Developer Platform Help Center.

From the settings for your app, note the client ID and client Secret. You provide these values to Amazon AppFlow when you connect to your Intercom account.

## Connecting Amazon AppFlow to your Intercom account
<a name="intercom-connecting"></a>

To connect Amazon AppFlow to your Intercom account, provide the client credentials from your Intercom app so that Amazon AppFlow can access your data. If you haven't yet configured your Intercom account for Amazon AppFlow integration, see [Before you begin](#intercom-prereqs).

**To connect to Intercom**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Intercom**.

1. Choose **Create connection**.

1. In the **Connect to Intercom** window, enter the following information:
   + **Authorization tokens URL** — Choose the URL based on the data host region where you use Intercom (Europe, US, Australia).
   + **Authorization code URL** — Choose the URL based on the data host region where you use Intercom (Europe, US, Australia).
   + **Client ID** — The client ID from your Intercom app.
   + **Client secret** — The client secret from your Intercom app.
   + ****Instance URL**** — Choose the URL based on the data host region where you use Intercom (Europe, US, Australia).

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your Intercom account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Intercom as the data source, you can select this connection.

## Transferring data from Intercom with a flow
<a name="intercom-transfer-data"></a>

To transfer data from Intercom, create an Amazon AppFlow flow, and choose Intercom as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Intercom, see [Supported objects](#intercom-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#intercom-destinations).

## Supported destinations
<a name="intercom-destinations"></a>

When you create a flow that uses Intercom as the data source, you can set the destination to any of the following connectors: 
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
<a name="intercom-objects"></a>

When you create a flow that uses Intercom as the data source, you can transfer any of the following data objects to supported destinations:



- ** Admin**
  - **** Field**:** Avatar / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Away Mode Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Away Mode Reassign / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Has Inbox Seat / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Job Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Team Ids / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Company**
  - **** Field**:** App Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Company Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Custom Attributes / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Industry / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Request At / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Monthly Spend / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Plan / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Remote Created At / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Segments / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Session Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Size / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** User Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Website / **** Data type**:** String / **** Supported filters**:** 

- ** Contact**
  - **** Field**:** Android App Name / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Android App Version / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Android Device / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Android Last Seen At / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Android Os Version / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Android Sdk Version / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Avatar / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Browser / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Browser Language / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Browser Version / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** City / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Companies / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Country / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Created At / **** Data type**:** Date / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO
  - **** Field**:** Custom Attributes / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** External Id / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Has Hard Bounced / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Ios App Name / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Ios App Version / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ios Device / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ios Last Seen At / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Ios Os Version / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Ios Sdk Version / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Language Override / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Last Contacted At / **** Data type**:** Date / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO
  - **** Field**:** Last Email Clicked At / **** Data type**:** Date / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO
  - **** Field**:** Last Email Opened At / **** Data type**:** Date / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO
  - **** Field**:** Last Replied At / **** Data type**:** Date / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO
  - **** Field**:** Last Seen At / **** Data type**:** Date / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO
  - **** Field**:** Location / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Marked Email As Spam / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Notes / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Opted Out Subscription Types / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Os / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Owner Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Phone / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Referrer / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Region / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Role / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** SMS Content / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Signed Up At / **** Data type**:** Date / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO
  - **** Field**:** Social Profiles / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Unsubscribed From Emails / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Unsubscribed From SMS / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** Date / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO
  - **** Field**:** Utm Campaign / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Utm Content / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Utm Medium / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Utm Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Utm Term / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Workspace Id / **** Data type**:** String / **** Supported filters**:** 

- ** Conversation**
  - **** Field**:** Admin Assignee Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Contacts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Conversation Parts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Conversation Rating / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Count assignments / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Count conversation parts / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Count reopens / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Custom Attributes / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** First Contact Reply / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** First admin reply at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** First assignment at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** First close at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** First contact reply at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Last admin reply at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Last assignment admin reply at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Last assignment at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Last close at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Last closed by Id / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Last contact reply at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Median time to reply / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Open / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Priority / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Rating admin id / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Rating contact id / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Rating remark / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Rating requested at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Rating requested at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Rating score / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Read / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Sla Applied / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Snoozed Until / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Source Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source author email / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source author id / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source author name / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source author type / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source body / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source delivered as / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source subject / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Source url / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Statistics / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Team Assignee Id / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Teammates / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Time to admin reply / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Time to assignment / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Time to first close / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Time to last close / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, LESS\_THAN
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Topics / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** Waiting Since / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN, LESS\_THAN, EQUAL\_TO, NOT\_EQUAL\_TO

- ** Data Attribute**
  - **** Field**:** Admin Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Api Writable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Archived / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Custom / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Data Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Full Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Label / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Model / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Options / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ui Writable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** Date / **** Supported filters**:** 

- ** Segment**
  - **** Field**:** Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Person Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** Date / **** Supported filters**:** 

- ** Tag**
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Team**
  - **** Field**:** Admin Ids / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

