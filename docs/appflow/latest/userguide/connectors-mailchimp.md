

# Mailchimp connector for Amazon AppFlow
<a name="connectors-mailchimp"></a>

Mailchimp is a marketing automation platform and email marketing service. If you're a Mailchimp user, your account contains data about your email campaigns, such as open and click details, segments, and automations. You can use Amazon AppFlow to transfer data from Mailchimp to certain AWS services or other supported applications.

## Amazon AppFlow support for Mailchimp
<a name="mailchimp-support"></a>

Amazon AppFlow supports Mailchimp as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Mailchimp.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Mailchimp.



## Before you begin
<a name="mailchimp-prereqs"></a>

To use Amazon AppFlow to transfer data from Mailchimp to supported destinations, you must meet these requirements:
+ You have an account with Mailchimp that contains the data that you want to transfer. For more information about the Mailchimp data objects that Amazon AppFlow supports, see [Supported objects](#mailchimp-objects).
+ In your account, you've created an API key. For the steps to create one, see [About API Keys](https://mailchimp.com/help/about-api-keys/) in the Mailchimp Help Center.

Note the API key from your account settings. You provide it to Amazon AppFlow when you connect to your Mailchimp account.

## Connecting Amazon AppFlow to your Mailchimp account
<a name="mailchimp-connecting"></a>

To connect Amazon AppFlow to your Mailchimp account, provide your API key so that Amazon AppFlow can access your data. If you haven't yet configured your Mailchimp account for Amazon AppFlow integration, see [Before you begin](#mailchimp-prereqs).

**To connect to Mailchimp**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Mailchimp**.

1. Choose **Create connection**.

1. In the **Connect to Mailchimp** window, enter the following information:
   + **API Key** – The API key from your Mailchimp account settings.
   + **Instance URL** – The Mailchimp Marketing API URL that provides access to your Mailchimp data. These URLs have the form `https://{{data-center}}.api.mailchimp.com`, where *data-center* is the data center for your account. For more information, see [API structure]() in the Mailchimp Marketing API documentation.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Mailchimp as the data source, you can select this connection.

## Transferring data from Mailchimp with a flow
<a name="mailchimp-transfer-data"></a>



To transfer data from Mailchimp, create an Amazon AppFlow flow, and choose Mailchimp as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Mailchimp, see [Supported objects](#mailchimp-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#mailchimp-destinations).

## Supported destinations
<a name="mailchimp-destinations"></a>

When you create a flow that uses Mailchimp as the data source, you can set the destination to any of the following connectors: 
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
<a name="mailchimp-objects"></a>

When you create a flow that uses Mailchimp as the data source, you can transfer any of the following data objects to supported destinations:



- ** Abuse Report**
  - **** Field**:** Campaign ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** List Is Active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Merge Field / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Vip / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Automation**
  - **** Field**:** Create Time / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN, GREATER\_THAN
  - **** Field**:** Email Sent / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Recipient / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Report Summary / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Setting / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Start Time / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN, GREATER\_THAN
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tracking / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Trigger Setting / **** Data type**:** Struct / **** Supported filters**:** 

- ** Campaign**
  - **** Field**:** Ab Split Opts / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Archive Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Content Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Create Time / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN, GREATER\_THAN
  - **** Field**:** Delivery Status / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Email Sent / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Folder ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Long Archive Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Member ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Need Block Refresh / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Parent Campaign ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Recipient / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Report Summary / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Resendable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Rss Opts / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Send Time / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN, GREATER\_THAN
  - **** Field**:** Setting / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Social Card / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Sort Field / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tracking / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Variate Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Web ID / **** Data type**:** Integer / **** Supported filters**:** 

- ** Click Detail**
  - **** Field**:** Ab Split / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Campaign ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Click Percentage / **** Data type**:** Float / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Click / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Click / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Unique Click / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Unique Click Percentage / **** Data type**:** Float / **** Supported filters**:** 
  - **** Field**:** Url / **** Data type**:** String / **** Supported filters**:** 

- ** List**
  - **** Field**:** Beamer Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Campaign Default / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Campaign Last Sent / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN, GREATER\_THAN
  - **** Field**:** Contact / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Date Created / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN, GREATER\_THAN
  - **** Field**:** Double Optin / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Email Type Option / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Has Ecommerce Store / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Has Welcome / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Include Total Contact / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** List Rating / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Marketing Permission / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Module / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Notify On Subscribe / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Notify On Unsubscribe / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Permission Reminder / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Sort Field / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Stats / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Subscribe Url Short / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Use Archive Bar / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Visibility / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Web\_ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** subscribe Url Long / **** Data type**:** String / **** Supported filters**:** 

- ** Open Detail**
  - **** Field**:** Campaign ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Contact Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** List is Active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Merge Field / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Open / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Open Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Vip / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Segment**
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN, GREATER\_THAN
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Include Cleaned / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Include Unsubscribed / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Member Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Option / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN, GREATER\_THAN

- ** Segment Member**
  - **** Field**:** Email Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Client / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Include Cleaned / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Include Unsubscribed / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Interest / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Ip Opt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ip Signup / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Language / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Changed / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Note / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Location / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Member Rating / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Merge Field / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Stats / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timestamp Opt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timestamp Signup / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Unique Email ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Vip / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Store**
  - **** Field**:** Address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Automation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Connected Site / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Currency Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Domain / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Syncing / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** List Is Active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Money Format / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Platform / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Primary Locale / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timezone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** String / **** Supported filters**:** 

- ** Unsubscribed**
  - **** Field**:** Campaign ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** List Is Active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Merge Field / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timestamp / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Vip / **** Data type**:** Boolean / **** Supported filters**:** 

