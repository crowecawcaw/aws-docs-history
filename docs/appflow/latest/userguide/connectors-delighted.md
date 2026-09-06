

# Delighted connector for Amazon AppFlow
<a name="connectors-delighted"></a>

Delighted is a cloud-based survey tool that helps its users distribute surveys and then collect and analyze the feedback. If you're a Delighted user, then your account contains data about your survey responses. You can use Amazon AppFlow to transfer data from Delighted to certain AWS services or other supported applications.

## Amazon AppFlow support for Delighted
<a name="delighted-support"></a>

Amazon AppFlow supports Delighted as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Delighted.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Delighted.

## Before you begin
<a name="delighted-prereqs"></a>

To use Amazon AppFlow to transfer data from Delighted to supported destinations, you must have an account with Delighted that contains the data that you want to transfer. For more information about the Delighted data objects that Amazon AppFlow supports, see [Supported objects](#delighted-objects).

From your account settings, note the API key. You provide this value to Amazon AppFlow when you create a connection to your Delighted account. For more information about Delighted API keys, see [Authentication](https://app.delighted.com/docs/api?gclid=Cj0KCQiAq5meBhCyARIsAJrtdr7AtSu0W6hS8OmoyWdqLMzzNUNTd9TQ8DoGMwsRitprPQrZNCMXZ-gaAqbDEALw_wcB#authentication) in the Delighted API documentation.

## Connecting Amazon AppFlow to your Delighted account
<a name="delighted-connecting"></a>

To connect Amazon AppFlow to your Delighted account, provide the API key from your Delighted account settings so that Amazon AppFlow can access your data.

**To connect to Delighted**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Delighted**.

1. Choose **Create connection**.

1. In the **Connect to Delighted** window, for **API Key**, enter a test or live API key from your Delighted account.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Delighted as the data source, you can select this connection.

## Transferring data from Delighted with a flow
<a name="delighted-transfer-data"></a>

To transfer data from Delighted, create an Amazon AppFlow flow, and choose Delighted as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Delighted, see [Supported objects](#delighted-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#delighted-destinations).

## Supported destinations
<a name="delighted-destinations"></a>

When you create a flow that uses Delighted as the data source, you can set the destination to any of the following connectors: 
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
<a name="delighted-objects"></a>

When you create a flow that uses Delighted as the data source, you can transfer any of the following data objects to supported destinations:



- ** Bounce**
  - **** Field**:** bounced\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** person\_id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** until / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

- ** Metric**
  - **** Field**:** detractor\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** detractor\_percent / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** nps / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** passive\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** passive\_percent / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** promoter\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** promoter\_percent / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** response\_count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** trend / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** until / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

- ** People**
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** last\_responded\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** last\_sent\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** next\_survey\_scheduled\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** phone\_number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** until / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

- ** Survey Response**
  - **** Field**:** additional\_answers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** comment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** notes / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** permalink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** person / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** person\_email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** person\_id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** person\_properties / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** score / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** survey\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** trend / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** until / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** updated\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** updated\_since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** updated\_until / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

- ** Unsubscribe**
  - **** Field**:** email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** person\_id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** unsubscribed\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** until / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

