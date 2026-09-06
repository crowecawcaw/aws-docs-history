

# Productboard connector for Amazon AppFlow
<a name="connectors-productboard"></a>

Productboard is a product management solution. If you're a Productboard user, your account contains data about the projects in your roadmap, such as products, features, and status. You can use Amazon AppFlow to transfer data from Productboard to certain AWS services or other supported applications.

## Amazon AppFlow support for Productboard
<a name="productboard-support"></a>

Amazon AppFlow supports Productboard as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Productboard.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Productboard.

## Before you begin
<a name="productboard-prereqs"></a>

To use Amazon AppFlow to transfer data from Productboard to supported destinations, you must have an account with Productboard that contains the data that you want to transfer.

From the Public API settings in your account, note the access token because you provide this value to Amazon AppFlow when you connect to Productboard. For the steps to get the token, see [Public API Access Token](https://developer.productboard.com/#section/Authentication/Public-API-Access-Token) in the Productboard API Reference.

## Connecting Amazon AppFlow to your Productboard account
<a name="productboard-connecting"></a>

To connect Amazon AppFlow to your Productboard account, provide the access token from your account settings so that Amazon AppFlow can access your data.

**To connect to Productboard**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Productboard**.

1. Choose **Create connection**.

1. In the **Connect to Productboard** window, for **Access Token**, enter your access token.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Productboard as the data source, you can select this connection.

## Transferring data from Productboard with a flow
<a name="productboard-transfer-data"></a>

To transfer data from Productboard, create an Amazon AppFlow flow, and choose Productboard as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Productboard, see [Supported objects](#productboard-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#productboard-destinations).

## Supported destinations
<a name="productboard-destinations"></a>

When you create a flow that uses Productboard as the data source, you can set the destination to any of the following connectors: 
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
<a name="productboard-objects"></a>

When you create a flow that uses Productboard as the data source, you can transfer any of the following data objects to supported destinations:



- ** Component**
  - **** Field**:** CreatedAt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Parent / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** String / **** Supported filters**:** 

- ** Custom Field Definition**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Custom Field Value**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Feature**
  - **** Field**:** Archived / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** CreatedAt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Owner Email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Parent / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Parent Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Status Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Time Frame / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** String / **** Supported filters**:** 

- ** Feature status**
  - **** Field**:** Completed / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 

- ** Product**
  - **** Field**:** CreatedAt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** String / **** Supported filters**:** 

