

# Domo connector for Amazon AppFlow
<a name="connectors-domo"></a>

Domo is a business intelligence solution. If you're a Domo user, your account contains data about your Domo resources, such as your datasets and data permissions policies. You can use Amazon AppFlow to transfer data from Domo to certain AWS services or other supported applications.

## Amazon AppFlow support for Domo
<a name="domo-support"></a>

Amazon AppFlow supports Domo as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Domo.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Domo.

## Before you begin
<a name="domo-prereqs"></a>

To use Amazon AppFlow to transfer data from Domo to supported destinations, you must meet these requirements:
+ You have an account with Domo that contains the data that you want to transfer. For more information about the Domo data objects that Amazon AppFlow supports, see [Supported objects](#domo-objects).
+ On the Domo for Developers site, you've created a client for Amazon AppFlow. The client provides the credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For the steps to create a client, see [API Authentication Quickstart](https://developer.domo.com/docs/authentication/quickstart-5) in the Domo for Developers documentation.

From the client settings, note client ID and secret because you provide these values in the connection settings in Amazon AppFlow.

## Connecting Amazon AppFlow to your Domo account
<a name="domo-connecting"></a>

To connect Amazon AppFlow to your Domo account, provide the client ID and secret from your client so that Amazon AppFlow can access your data. If you haven't yet configured your Domo account for Amazon AppFlow integration, see [Before you begin](#domo-prereqs).

**To connect to Domo**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Domo**.

1. Choose **Create connection**.

1. In the **Connect to Domo** window, enter the following information:
   + **Client ID** – The client ID from your Domo client.
   + **Client secret** – The secret from your Domo client.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Domo as the data source, you can select this connection.

## Transferring data from Domo with a flow
<a name="domo-transfer-data"></a>

To transfer data from Domo, create an Amazon AppFlow flow, and choose Domo as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Domo, see [Supported objects](#domo-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#domo-destinations).

When transferring dataset data objects, the limit is 1000 records per page. Pagination is not supported for data-permission-policy data objects, and the lambda limit is 5.5 MB.

## Supported destinations
<a name="domo-destinations"></a>

When you create a flow that uses Domo as the data source, you can set the destination to any of the following connectors: 
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
<a name="domo-objects"></a>

When you create a flow that uses Domo as the data source, you can transfer any of the following data objects to supported destinations:



- ** Data Permission Policy**
  - **** Field**:** Filters / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Groups / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Users / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Virtual Users / **** Data type**:** List / **** Supported filters**:** 

- ** Dataset**
  - **** Field**:** Columns / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** CreatedAt / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PDP Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Rows / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** String / **** Supported filters**:** 

