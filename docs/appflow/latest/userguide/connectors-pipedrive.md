

# Pipedrive connector for Amazon AppFlow
<a name="connectors-pipedrive"></a>

Pipedrive is a Customer Relationship Management (CRM) service that helps companies track and carry out projects. If you’re a Pipedrive user, your account contains data about connections with your customers and within your organization. This can include deals, contacts, demos, proposals, and more. You can use Amazon AppFlow to transfer data from Pipedrive to certain AWS services or other supported applications.

## Amazon AppFlow support for Pipedrive
<a name="pipedrive-support"></a>

Amazon AppFlow supports Pipedrive as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Pipedrive.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Pipedrive.

## Before you begin
<a name="pipedrive-prereqs"></a>

To use Amazon AppFlow to transfer data from Pipedrive to supported destinations, you must meet these requirements:
+ You have an account with Pipedrive that contains the data that you want to transfer. For more information about the Pipedrive data objects that Amazon AppFlow supports, see [Supported objects](#pipedrive-objects).
+ In your Pipedrive account, you've created an unlisted app in Marketplace Manager. This app provides the credentials that Amazon AppFlow uses to make authenticated calls to your account and securely access your data. For the steps to create an app, see [Creating an app](https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app) in the *Pipedrive Developer Documentation*.

  You've configured your app as follows:
  + You've specified a redirect URL (also referred to as a *callback URL*) for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Pipedrive. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
  + You've activated the access scopes that provide access to the data that you want to transfer. For more information about Pipedrive scopes, see [Scopes and permission explanations](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations) in the *Pipedrive Developer Documentation*.

From the settings for your app, note the client ID and client secret. When you connect to your Pipedrive account, you provide these values to Amazon AppFlow.

## Connecting Amazon AppFlow to your Pipedrive account
<a name="pipedrive-connecting"></a>

To connect Amazon AppFlow to your Pipedrive account, provide details from your Pipedrive project so that Amazon AppFlow can access your data. If you haven't yet configured your Pipedrive project for Amazon AppFlow integration, see [Before you begin](#pipedrive-prereqs).

**To connect to Pipedrive**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Pipedrive**.

1. Choose **Create connection**.

1. In the **Connect to Pipedrive** window, enter the following information:
   + **Client ID** – The client ID of the OAuth 2.0 client ID in your Pipedrive project.
   + **Client secret** – The client secret of the OAuth 2.0 client ID in your Pipedrive project.
   + **Instance URL** – The URL of the instance where you want to run the operation, for example, https://awsappflow-domain.pipedrive.com.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your Pipedrive account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Pipedrive as the data source, you can select this connection.

## Transferring data from Pipedrive with a flow
<a name="pipedrive-transfer-data"></a>

To transfer data from Pipedrive, create an Amazon AppFlow flow, and choose Pipedrive as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Pipedrive, see [Supported objects](#pipedrive-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#pipedrive-destinations).

## Supported destinations
<a name="pipedrive-destinations"></a>

When you create a flow that uses Pipedrive as the data source, you can set the destination to any of the following connectors: 
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
<a name="pipedrive-objects"></a>

When you create a flow that uses Pipedrive as the data source, you can transfer any of the following data objects to supported destinations:



- ** Activities**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Activity Types**
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Add Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Custom Flag / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Icon / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Key / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order Number / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Update Time / **** Data type**:** DateTime / **** Supported filters**:** 

- ** CallLogs**
  - **** Field**:** Activity Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Company Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Deal Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Duration / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** End Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** From Phone Number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Has Recording / **** Data type**:** Boolean  / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Organization Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Outcome / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Person Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Start Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** To Phone Number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** User Id / **** Data type**:** Long / **** Supported filters**:** 

- ** Currencies**
  - **** Field**:** Active Flag / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Decimal Points / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Is Custom Flag / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Symbol / **** Data type**:** String / **** Supported filters**:** 

- ** Deals**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Lead Labels**
  - **** Field**:** Add Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update Time / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Lead Sources**
  - **** Field**:** Name
  - **** Data type**:** String
  - **** Supported filters**:** 

- ** Leads**
  - **** Field**:** Add Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CC Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Creator Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Expected Close Date / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Archived / **** Data type**:** Boolean  / **** Supported filters**:** 
  - **** Field**:** Label Ids / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Next Activity Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Organization Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Owner Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Person Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Source Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Visible To / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Was Seen / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Notes**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Organization**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Permission Sets**
  - **** Field**:** App / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Assignment Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Persons**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Pipelines**
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Add Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Deal Probability / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order Number / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Selected / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** URL Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Update Time / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Products**
  - **** Field**:** 
  - **** Data type**:** 
  - **** Supported filters**:** 

- ** Roles**
  - **** Field**:** Active Flag / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Assignment Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Level / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Parent Role Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Sub Role Count / **** Data type**:** Integer / **** Supported filters**:** 

- ** Stages**
  - **** Field**:** Active Flag / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Add Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Deal Probability / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Order Number / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Pipeline Deal Probability / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Pipeline Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Pipeline Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rotten Days / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rotten Flag / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Update Time / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Users**
  - **** Field**:** Access / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Active Flag / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Default Currency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Has Created Company / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Icon URL / **** Data type**:** String  / **** Supported filters**:** 
  - **** Field**:** Is Admin / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Is You / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Language / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Last Login / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Locate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Role Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Signup Flow Variation / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timezone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timezone Offset / **** Data type**:** String / **** Supported filters**:** 

