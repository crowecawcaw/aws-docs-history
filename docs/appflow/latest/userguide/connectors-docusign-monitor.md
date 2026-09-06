

# DocuSign Monitor connector for Amazon AppFlow
<a name="connectors-docusign-monitor"></a>

DocuSign Monitor provides data about digital agreements that are processed through DocuSign. If you're a DocuSign user, your account contains monitoring data about your DocuSign activity. You can use Amazon AppFlow to transfer your monitoring data to certain AWS services or other supported applications.

## Amazon AppFlow support for DocuSign Monitor
<a name="docusign-monitor-support"></a>

Amazon AppFlow supports DocuSign Monitor as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from DocuSign Monitor.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to DocuSign Monitor.



## Before you begin
<a name="docusign-monitor-prereqs"></a>

To use Amazon AppFlow to transfer data from DocuSign Monitor to supported destinations, you must meet these requirements:
+ You have an account with DocuSign that contains the data that you want to transfer. For more information about the DocuSign Monitor data objects that Amazon AppFlow supports, see [Supported objects](#docusign-monitor-objects).
+ In the settings for your Docusign account, you've created an app and integration key for Amazon AppFlow. The app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For more information, see [Configure your app](https://developers.docusign.com/platform/configure-app/) in the DocuSign Developer documentation.
+ In the settings for your app, you've done the following:
  + Created a secret key.
  + Added a redirect URL for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from DocuSign Monitor. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

From your app settings, note your integration key and secret key because you specify these values in the connection settings in Amazon AppFlow.

## Connecting Amazon AppFlow to your DocuSign account
<a name="docusign-monitor-connecting"></a>

To connect Amazon AppFlow to your DocuSign account, provide the integration key and secret key from your app so that Amazon AppFlow can access your data. If you haven't yet configured your DocuSign account for Amazon AppFlow integration, see [Before you begin](#docusign-monitor-prereqs).

**To connect to DocuSign Monitor**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **DocuSign Monitor**.

1. Choose **Create connection**.

1. In the **Connect to DocuSign Monitor** window, enter the following information:
   + **Client ID** – The integration key from your app settings.
   + **Client secret** – The secret key from your app settings.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**.

1. In the window that appears, sign in to your DocuSign account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses DocuSign Monitor as the data source, you can select this connection.

## Transferring data from DocuSign Monitor with a flow
<a name="docusign-monitor-transfer-data"></a>



To transfer data from DocuSign Monitor, create an Amazon AppFlow flow, and choose DocuSign Monitor as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for DocuSign Monitor, see [Supported objects](#docusign-monitor-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#docusign-monitor-destinations).

## Supported destinations
<a name="docusign-monitor-destinations"></a>

When you create a flow that uses DocuSign Monitor as the data source, you can set the destination to any of the following connectors: 
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
<a name="docusign-monitor-objects"></a>

When you create a flow that uses Docusign Monitor as the data source, you can transfer any of the following data objects to supported destinations:



- ** Monitoring Data**
  - **** Field**:** accountId / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** action / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** affectedUserId / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** affectedUserIsMemberOfDomain / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** application / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** begin\_end\_time / **** Data type**:** DateTime / **** Supported filters**:** BETWEEN
  - **** Field**:** browser / **** Data type**:** String / **** Supported filters**:** CONTAINS
  - **** Field**:** city / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** country / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** customerVisible / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** device / **** Data type**:** String / **** Supported filters**:** CONTAINS
  - **** Field**:** environment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** eventId / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** field / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** integratorKey / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** ipAddress / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** ipAddressLocation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** isUserMemberOfDomain / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** latitude / **** Data type**:** Double / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** longitude / **** Data type**:** Double / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** object / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** organizationId / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** os / **** Data type**:** String / **** Supported filters**:** CONTAINS
  - **** Field**:** property / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** proxyLevel / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** proxyStatus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** proxyType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** referencedUserId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** referencedUserIsMemberOfDomain / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** result / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** site / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** state / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** timestamp / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** traceToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** userAgent / **** Data type**:** String / **** Supported filters**:** CONTAINS
  - **** Field**:** userAgentClientInfo / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** userId / **** Data type**:** String / **** Supported filters**:** CONTAINS, EQUAL\_TO, NOT\_EQUAL\_TO
  - **** Field**:** version / **** Data type**:** String / **** Supported filters**:** 

