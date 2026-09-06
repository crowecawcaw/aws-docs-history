

# SendGrid connector for Amazon AppFlow
<a name="connectors-sendgrid"></a>

SendGrid is a marketing automation platform and email marketing service. If you're a SendGrid user, your account contains data about your SendGrid activity, such as your lists, segments, and campaigns. You can use Amazon AppFlow to transfer data from SendGrid to certain AWS services or other supported applications.

## Amazon AppFlow support for SendGrid
<a name="sendgrid-support"></a>

Amazon AppFlow supports SendGrid as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from SendGrid.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to SendGrid.



## Before you begin
<a name="sendgrid-prereqs"></a>

To use Amazon AppFlow to transfer data from SendGrid to supported destinations, you must meet these requirements:
+ You have an account with SendGrid that contains the data that you want to transfer. For more information about the SendGrid data objects that Amazon AppFlow supports, see [Supported objects](#sendgrid-objects).
+ You've configured your account with the following settings:
  + You've enabled two-factor authentication. For the steps to enable it, see [Two-Factor Authentication](https://docs.sendgrid.com/ui/account-and-settings/two-factor-authentication) in the SendGrid documentation.
  + You've created an API key that grants full access to your account. For the steps to create one, see [API Keys](https://docs.sendgrid.com/ui/account-and-settings/api-keys) in the SendGrid documentation.

Note the API key from your account settings. You provide it to Amazon AppFlow when you connect to your SendGrid account.

## Connecting Amazon AppFlow to your SendGrid account
<a name="sendgrid-connecting"></a>

To connect Amazon AppFlow to your SendGrid account, provide your API key so that Amazon AppFlow can access your data. If you haven't yet configured your SendGrid account for Amazon AppFlow integration, see [Before you begin](#sendgrid-prereqs).

**To connect to SendGrid**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **SendGrid**.

1. Choose **Create connection**.

1. In the **Connect to SendGrid** window, for **API Key**, enter the API key from your SendGrid account settings.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses SendGrid as the data source, you can select this connection.

## Transferring data from SendGrid with a flow
<a name="sendgrid-transfer-data"></a>



To transfer data from SendGrid, create an Amazon AppFlow flow, and choose SendGrid as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for SendGrid, see [Supported objects](#sendgrid-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#sendgrid-destinations).

## Supported destinations
<a name="sendgrid-destinations"></a>

When you create a flow that uses SendGrid as the data source, you can set the destination to any of the following connectors: 
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
<a name="sendgrid-objects"></a>

When you create a flow that uses SendGrid as the data source, you can transfer any of the following data objects to supported destinations:



- ** Category**
  - **** Field**:** Category
  - **** Data type**:** String
  - **** Supported filters**:** 

- ** Contact**
  - **** Field**:** Address Line 1 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Address Line 2 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Alternate Email / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** City / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Country / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Custom Field / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Event Timestamp / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** Facebook / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Line / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** List Id / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Phone Number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Postal Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Segment Id / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** State Province Region / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Unique Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Whatsapp / **** Data type**:** String / **** Supported filters**:** 

- ** List**
  - **** Field**:** Contact Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 

- ** Marketing Campaign Stats Automation**
  - **** Field**:** Aggregation / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Automation ID / **** Data type**:** List / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Stats / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Step ID / **** Data type**:** String / **** Supported filters**:** 

- ** Marketing Campaign Stats Single Send**
  - **** Field**:** Ab Phase / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ab Variation / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Aggregation / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Single Send ID / **** Data type**:** List / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Stats / **** Data type**:** Struct / **** Supported filters**:** 

- ** Segment**
  - **** Field**:** Contact Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Next Sample Update / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** No Parent List ID / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Parent List ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Parent List ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Query Version / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Sample Updated At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** String / **** Supported filters**:** 

- ** Single Send**
  - **** Field**:** Abtest / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Category / **** Data type**:** List / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Abtest / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Send At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** String / **** Supported filters**:** 

- ** Stats**
  - **** Field**:** Aggregated By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** StartDate / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN, EQUAL\_TO
  - **** Field**:** Stats / **** Data type**:** List / **** Supported filters**:** 

- ** Unsubscribe Group**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Is Default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Last Email Sent At / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Unsubscribe / **** Data type**:** Integer / **** Supported filters**:** 

