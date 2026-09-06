

# Typeform connector for Amazon AppFlow
<a name="connectors-typeform"></a>

Typeform is an online survey tool. If you're a Typeform user, your account contains data about your survey forms and responses. You can use Amazon AppFlow to transfer data from Typeform to certain AWS services or other supported applications.

## Amazon AppFlow support for Typeform
<a name="typeform-support"></a>

Amazon AppFlow supports Typeform as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Typeform.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Typeform.

## Before you begin
<a name="typeform-prereqs"></a>

To use Amazon AppFlow to transfer data from Typeform to supported destinations, you must meet these requirements:
+ You have an account with Typeform that contains the data that you want to transfer. For more information about the Typeform data objects that Amazon AppFlow supports, see [Supported objects](#typeform-objects).
+ In the settings of your account, you've created either of the following resources for Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account.
  + A developer app to provide OAuth 2.0 authentication. For the steps to create a developer app, see [Create an application in the Typeform admin panel](https://developer.typeform.com/get-started/applications/#1-create-an-application-in-the-typeform-admin-panel) in the documentation for Typeform Developers Platform.
  + A personal token. For the steps to create one, see [Personal access token for Typeform's APIs](https://developer.typeform.com/get-started/personal-access-token) in the documentation for Typeform Developers Platform.
+ If you created a developer app, you've configured it with a redirect URL for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Typeform. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
+ If you created a personal token, you've included the scopes that provide access to the data objects that you want to transfer. For information about Typeform scopes, see [OAuth scopes for your applications](https://developer.typeform.com/get-started/scopes/) in the documentation for Typeform Developers Platform.

If you created a developer app, note the client ID and client secret. If you created a personal token, note the token value. You provide these values to Amazon AppFlow when you connect to your Typeform account.

## Connecting Amazon AppFlow to your Typeform account
<a name="typeform-connecting"></a>

To connect Amazon AppFlow to your Typeform account, provide details from your Typeform project so that Amazon AppFlow can access your data. If you haven't yet configured your Typeform project for Amazon AppFlow integration, see [Before you begin](#typeform-prereqs).

**To connect to Typeform**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Typeform**.

1. Choose **Create connection**.

1. In the **Connect to Typeform** window, for **Select authentication type**, choose how to authenticate Amazon AppFlow with your Typeform account when it requests to access your data:
   + Choose **OAuth2** to authenticate Amazon AppFlow with the credentials from a developer app. Then, enter values for **Client ID** and **Client secret**.
   + Choose **PAT** to authenticate Amazon AppFlow with a personal access token. Then, enter the token value for **Personal access token**.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Depending on the authentication type that you chose, do one of the following:
   + If you chose **OAuth2**, choose **Continue**. Then, in the window that appears, sign in to your Typeform account, and grant access to Amazon AppFlow.
   + If you chose **PAT**, choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Typeform as the data source, you can select this connection.

## Transferring data from Typeform with a flow
<a name="typeform-transfer-data"></a>

To transfer data from Typeform, create an Amazon AppFlow flow, and choose Typeform as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Typeform, see [Supported objects](#typeform-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#typeform-destinations).

## Supported destinations
<a name="typeform-destinations"></a>

When you create a flow that uses Typeform as the data source, you can set the destination to any of the following connectors: 
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
<a name="typeform-objects"></a>

When you create a flow that uses Typeform as the data source, you can transfer any of the following data objects to supported destinations:



- ** Form**
  - **** Field**:** \_links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** last\_updated\_at / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** search / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS
  - **** Field**:** self / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** theme / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** workspace\_id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Form Insight**
  - **** Field**:** fields / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** form / **** Data type**:** Struct / **** Supported filters**:** 

- ** Response**
  - **** Field**:** answers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** calculated / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** completed / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** hidden / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** landed\_at / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** landing\_id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** metadata / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** query / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO, CONTAINS
  - **** Field**:** response\_id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** submitted\_at / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** token / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** until / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO

