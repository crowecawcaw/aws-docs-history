

# HubSpot connector for Amazon AppFlow
<a name="connectors-hubspot"></a>

HubSpot is a customer relations management (CRM) solution that supports marketing, sales, customer service, and content management. After you connect Amazon AppFlow your HubSpot account, you can use HubSpot as a data source or destination in your flows. Run these flows to transfer data between HubSpot and AWS services or other supported applications.

## Amazon AppFlow support for HubSpot
<a name="hubspot-support"></a>

Amazon AppFlow supports HubSpot as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from HubSpot.

**Supported as a data destination?**  
Yes. You can use Amazon AppFlow to transfer data to HubSpot.

**Supported API versions**  
Amazon AppFlow can retrieve your data by sending requests to the following versions of the HubSpot API:  
+ v3
+ v2
+ v1

## Before you begin
<a name="hubspot-prereqs"></a>

To use Amazon AppFlow to transfer data from HubSpot to supported destinations, you must meet these requirements:
+ You have an account with HubSpot that contains the data that you want to transfer. For more information about the HubSpot data objects that Amazon AppFlow supports, see [Supported objects](#hubspot-objects).
+ You have an App Developers account with HubSpot Developers.
+ In HubSpot Developers, you've created an app for Amazon AppFlow. The app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For the steps to create an app, see [Creating and installing apps](https://developers.hubspot.com/docs/api/creating-an-app) in the HubSpot Developers documentation.
+ You've configured your app as follows:
  + You've specified a redirect URL for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from HubSpot. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
  + You've permitted the following scopes:
    + `automation`
    + `content`
    + `crm.lists.read`
    + `crm.lists.write`
    + `crm.objects.companies.read`
    + `crm.objects.companies.write`
    + `crm.objects.contacts.read`
    + `crm.objects.contacts.write`
    + `crm.objects.custom.read`
    + `crm.objects.custom.write`
    + `crm.objects.deals.read`
    + `crm.objects.deals.write`
    + `crm.objects.owners.read`
    + `crm.schemas.custom.read`
    + `e-commerce`
    + `forms`
    + `oauth`
    + `sales-email-read`
    + `tickets`

    For more information about these scopes, see [Scopes](https://developers.hubspot.com/docs/api/working-with-oauth#scopes) in the HubSpot Developers documentation.

From your app settings, note your client ID and client secret because you specify these values in the connection settings in Amazon AppFlow.

## Connecting Amazon AppFlow to your HubSpot account
<a name="hubspot-connecting"></a>

To connect Amazon AppFlow to your HubSpot account, provide details from your HubSpot Developers app so that Amazon AppFlow can access your data. If you haven't yet configured your HubSpot account for Amazon AppFlow integration, see [Before you begin](#hubspot-prereqs).

**To connect to HubSpot**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **HubSpot**.

1. Choose **Create connection**.

1. In the **Connect to HubSpot** window, provide the client credentials from your app for **Client ID** and **Client secret**.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your HubSpot account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses HubSpot as the data source, you can select this connection.

## Transferring data to or from HubSpot with a flow
<a name="hubspot-transfer-data"></a>

To transfer data to or from HubSpot, create an Amazon AppFlow flow, and choose HubSpot as the data source or destination. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure a flow that uses HubSpot as the data source, you choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for HubSpot, see [Supported objects](#hubspot-objects). You also choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#hubspot-destinations).

## Supported destinations
<a name="hubspot-destinations"></a>

When you create a flow that uses HubSpot as the data source, you can set the destination to any of the following connectors: 
+ [Amazon Lookout for Metrics](lookout.md)
+ [Amazon Redshift](redshift.md)
+ [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md)
+ [Amazon S3](s3.md)
+ [HubSpot](#connectors-hubspot)
+ [Marketo](marketo.md)
+ [Salesforce](salesforce.md)
+ [SAP OData](sapodata.md)
+ [Snowflake](snowflake.md)
+ [Upsolver](upsolver.md)
+ [Zendesk](zendesk.md)
+ [Zoho CRM](connectors-zoho-crm.md)

## Supported objects
<a name="hubspot-objects"></a>

When you create a flow that uses HubSpot as the data source, you can transfer any of the following data objects to supported destinations:


**HubSpot API v3**  


- ** Call**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Company**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Contact**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Custom Object**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Deal**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Email**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Meeting**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Note**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Owner**
  - **** Field**:** Archived / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Firstname / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Lastname / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Teams / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** User Id / **** Data type**:** Integer / **** Supported filters**:** 

- ** Postal Mail**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Product**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Task**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Ticket**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** WorkFlow**
  - **** Field**:** Contact List Id's / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Inserted At / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Persona Tag Id's / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** Integer / **** Supported filters**:** 




**HubSpot API v2**  


- ** Form**
  - **** Field**:** Always Create New Company / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Business Unit Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Captcha Enabled / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Cloneable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Create Marketable Contact / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Css Class / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Custom Uid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Deletable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** DeletedAt / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Edit Version / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Editable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** FormFieldGroups / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Guid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ignore Current Values / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Inline Message / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Internal Updated At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Is Published / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Kickback Emails Json / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Kickback email work flow Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Method / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Notify Recipients / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Parent Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Payment Session Template Ids / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Portable Key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Portal Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Publish At / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Published At / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Redirect / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Selected External Options / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Style / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Submit Text / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Thank You Message Json / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Theme Color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Theme Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Unpublish At / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** Long / **** Supported filters**:** 




**HubSpot API v1**  


- ** CRM\_Pipeline**
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Display Order / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Label / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Object Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ObjectTypeId / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Pipeline Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Stages / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** Long / **** Supported filters**:** 

- ** Campaign**
  - **** Field**:** App Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** App Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Updated Time / **** Data type**:** String / **** Supported filters**:** 

- ** Contact\_List**
  - **** Field**:** Archived / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Author Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Dynamic / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Filters / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Ils Filter Branch / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Internal / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Limit Exempt / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** List Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** List Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Meta Data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Parent Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Portal Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Read Only / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Team Ids / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** Long / **** Supported filters**:** 

- ** Email\_Event**
  - **** Field**:** App Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** App Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Attempt / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Browser / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Device Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Drop Message / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Drop Reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Campaign Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Filtered Event / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** From / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Location / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Portal Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Recipient / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Reply To / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Response / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Sent By / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Smtp Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subject / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Suppressed Message / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Suppressed Reason / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** User Agent / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** bcc / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** cc / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** duration / **** Data type**:** Integer / **** Supported filters**:** 

