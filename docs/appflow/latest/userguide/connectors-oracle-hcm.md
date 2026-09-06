

# Oracle HCM connector for Amazon AppFlow
<a name="connectors-oracle-hcm"></a>

Oracle Human Capital Management (HCM) is a cloud-based application for human resources (HR) processes. You can use Amazon AppFlow to transfer data from Oracle HCM to certain AWS services or other supported applications.

## Amazon AppFlow support for Oracle HCM
<a name="oracle-hcm-support"></a>

Amazon AppFlow supports Oracle HCM as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Oracle HCM.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Oracle HCM.

## Before you begin
<a name="oracle-hcm-prereqs"></a>

To use Amazon AppFlow to transfer data from Oracle HCM to supported destinations, you must have an account with Oracle HCM that contains the data that you want to transfer. 

## Connecting Amazon AppFlow to your Oracle HCM account
<a name="oracle-hcm-connecting"></a>

To connect Amazon AppFlow to your Oracle HCM account, provide your account credentials and instance URL.

**To connect to Oracle HCM**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Oracle HCM**.

1. Choose **Create connection**.

1. In the **Connect to Oracle HCM** window, enter the following information:
   + **User name** – The user name for your Oracle HCM account.
   + **Password** – The password for your Oracle HCM account.
   + **Oraclehcm Instance URL** – The URL of your Oracle HCM instance.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Oracle HCM as the data source, you can select this connection.

## Transferring data from Oracle HCM with a flow
<a name="oracle-hcm-transfer-data"></a>

To transfer data from Oracle HCM, create an Amazon AppFlow flow, and choose Oracle HCM as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

## Supported destinations
<a name="oracle-hcm-destinations"></a>

When you create a flow that uses Oracle HCM as the data source, you can set the destination to any of the following connectors: 
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