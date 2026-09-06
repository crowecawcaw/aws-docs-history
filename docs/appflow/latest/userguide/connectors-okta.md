

# Okta connector for Amazon AppFlow
<a name="connectors-okta"></a>

Okta is an identity and access management solution. If you you're an Okta user, your account contains data about your Okta objects, such as your users, groups, devices and applications. You can use Amazon AppFlow to transfer data from Okta to certain AWS services or other supported applications.

## Amazon AppFlow support for Okta
<a name="okta-support"></a>

Amazon AppFlow supports Okta as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Okta.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Okta.

## Before you begin
<a name="okta-prereqs"></a>

To use Amazon AppFlow to transfer data from Okta to supported destinations, you must meet these requirements:
+ You have an account with Okta that contains the data that you want to transfer. For more information about the Okta data objects that Amazon AppFlow supports, see [Supported objects](#okta-objects).
+ In your account , you've created either of the following resources for Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account.
  + An OIDC app integration to support OAuth 2.0 authentication. For the steps to create an app integration, see [Create OIDC app integrations](https://help.okta.com/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_OIDC.htm) in the Okta Help Center.
  + An API token. For the steps to create one, see [Create an API token](https://developer.okta.com/docs/guides/create-an-api-token/main/) in the Okta Help Center.
+ If you created an OIDC app integration, you've configured it with the following settings:
  + The application type is *Web Application*.
  + The activated grant types include *Authorization Code* and *Refresh Token*.
  + The sign-in redirect URIs include one or more URLs for Amazon AppFlow.

    Redirect URLs have the following format:

    ```
    https://{{region}}.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Okta. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*
  + The following scopes are permitted:
    + `okta.apps.read`
    + `okta.devices.read`
    + `okta.groups.read`
    + `okta.users.read`
    + `okta.userTypes.read`

If you created an OIDC app integration, note the client ID and client secret . If you created an API token, note the token value. You provide these values to Amazon AppFlow when you connect to your Okta account.

## Connecting Amazon AppFlow to your Okta account
<a name="okta-connecting"></a>

To connect Amazon AppFlow to your Okta account, provide the client credentials from your app integration, or provide an API token. If you haven't yet configured your Okta account for Amazon AppFlow integration, see [Before you begin](#okta-prereqs).

**To connect to Okta**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Okta**.

1. Choose **Create connection**.

1. In the **Connect to Okta** window, for **Select authentication type**, choose how to authenticate Amazon AppFlow with your Okta account when it requests to access your data:
   + Choose **OAuth2** to authenticate Amazon AppFlow with the client credentials from an OIDC app integration. Then, specify the following:
     + **Authorization tokens URL** and **Authorization code URL** – For each of these fields, do the following: 

       1. Choose the format of your Okta Org URL. For more information, see [Org URLs](https://developer.okta.com/docs/concepts/okta-organizations/#org-urls) in the Okta Developer documentation.

       1. Enter your Okta subdomain. For the steps to look up your subdomain, see [Find your Okta domain](https://developer.okta.com/docs/guides/find-your-domain/main/) in the Okta Developer documentation..
     + **Client ID** – The client ID from your app integration.
     + **Client secret** – The client secret from your app integration.
   + Choose **Okta\_API\_Token** to authenticate Amazon AppFlow with an API token. Then, enter the token value for **Okta API Token**.

1. For **Your Okta Domain URL**, enter your domain URL, such as **{{my-domain}}.okta.com**. For the steps to find your domain, see [Find your Okta domain](https://developer.okta.com/docs/guides/find-your-domain/main/) in the Okta Developer documentation.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**.

1. In the window that appears, sign in to your Okta account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Okta as the data source, you can select this connection.

## Transferring data from Okta with a flow
<a name="okta-transfer-data"></a>



To transfer data from Okta, create an Amazon AppFlow flow, and choose Okta as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Okta, see [Supported objects](#okta-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#okta-destinations).

## Supported destinations
<a name="okta-destinations"></a>

When you create a flow that uses Okta as the data source, you can set the destination to any of the following connectors: 
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
<a name="okta-objects"></a>

When you create a flow that uses Okta as the data source, you can transfer any of the following data objects to supported destinations:



- ** Application**
  - **** Field**:** Accessibility / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Credentials / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Credentials Signing Key ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Embedded / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Features / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Group ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Label / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Updated / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Profile / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Request Object Signing Alg / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Settings / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** User ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Visibility / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** signOnMode / **** Data type**:** String / **** Supported filters**:** 

- ** Device**
  - **** Field**:** Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** IMEI / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Updated / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Manufacturer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Mobile Equipment Identifier (MEID) / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Model / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** OS Version / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Platform / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Profile / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Registered / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Resource Alternate ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Resource Display Name / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Resource ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Resource Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Secure Hardware Present / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Serial Number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Windows Security identifier (SID) / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** macOS UDID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** tpmPublicKeyHash / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Group**
  - **** Field**:** Created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Embedded / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** GUID (objectGUID) of the Windows Group / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Group Description / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Group Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Membership Updated / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Last Updated / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Object Class / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Profile / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SAM Account Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Source ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Windows Domain Qualified Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Windows Group Distinguished Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** User**
  - **** Field**:** Activated / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** City / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Cost Center / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Country Code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Credentials / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Department / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Division / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Embedded Resources / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Employee Number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Honorific Prefix / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Honorific Suffix / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Login / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Updated / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Locale / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Manager Display Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Manager ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Middle Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Mobile Phone / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Nickname / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Occupation / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Organization / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Password Changed / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Postal Address / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Preferred Language / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Primary Phone / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Profile / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Profile URL / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Second Email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Status Changed / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, NOT\_EQUAL\_TO, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN, LESS\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Street Address / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Timezone / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Transitioning to status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Type ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** User Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Username / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Zip Code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** User Type**
  - **** Field**:** Created / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created By / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Updated / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Last Updated By / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Links / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 

