

# Blackbaud Raiser's Edge NXT connector for Amazon AppFlow
<a name="connectors-blackbaudraisersedgenxt"></a>

Blackbaud Raiser's Edge NXT is a customer relationship management (CRM) software as a service (SaaS) solution for nonprofit organizations. If you’re a Blackbaud Raiser's Edge NXT user, your account contains data on prospects, analytics, gift management, and more. You can use Amazon AppFlow to transfer data from Blackbaud Raiser's Edge NXT to certain AWS services or other supported applications.

## Amazon AppFlow support for Blackbaud Raiser's Edge NXT
<a name="blackbaudraisersedgenxt-support"></a>

Amazon AppFlow supports Blackbaud Raiser's Edge NXT as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Blackbaud Raiser's Edge NXT.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Blackbaud Raiser's Edge NXT.

## Before you begin
<a name="blackbaudraisersedgenxt-prereqs"></a>

To use Amazon AppFlow to transfer data from Blackbaud Raiser's Edge NXT to supported destinations, you must meet these requirements:
+ You have an account with Blackbaud Raiser's Edge NXT that contains the data that you want to transfer. For more information about the Blackbaud Raiser's Edge NXT data objects that Amazon AppFlow supports, see [Supported objects](#blackbaudraisersedgenxt-objects).
+ In your Blackbaud SKY Developer account, you've created a SKY developer app for Amazon AppFlow. The app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. You can use default settings for the Grant type, the authorization tokens URL, and the authorization code URL, or use your own. For information about how to create a developer app, see [Applications](https://developer.blackbaud.com/skyapi/docs/applications) in the SKY API documentation. 
+ In the setting for Scopes, you've defined access to Blackbaud data with the option **Full data access.**
+ You've configured the app with one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Blackbaud Raiser's Edge NXT. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

Note the client ID, client secret, and subscription key from the settings for your app. You provide these values to Amazon AppFlow when you create your connection.

## Connecting Amazon AppFlow to your Blackbaud Raiser's Edge NXT account
<a name="blackbaudraisersedgenxt-connecting"></a>

To connect Amazon AppFlow to your Blackbaud Raiser's Edge NXT account, provide details from your SKY developer app so that Amazon AppFlow can access your data. If you haven't yet configured your Blackbaud Raiser's Edge NXT account for Amazon AppFlow integration, see [Before you begin](#blackbaudraisersedgenxt-prereqs).

**To connect to Blackbaud Raiser's Edge NXT**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Blackbaud Raiser's Edge NXT**.

1. Choose **Create connection**.

1. In the **Connect to Blackbaud Raiser's Edge NXT** window, enter the following information:
   + **Connection name** — Enter a name for your connection. 
   + **Client ID ** — The client ID in your Blackbaud Raiser's Edge NXT project.
   + **Client secret ** — The client secret in your Blackbaud Raiser's Edge NXT project.
   + **Subscription key ** — The subscription key in your Blackbaud Raiser's Edge NXT project.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. Choose **Connect**.

1. In the window that appears, sign in to your Blackbaud Raiser's Edge NXT account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Blackbaud Raiser's Edge NXT as the data source, you can select this connection.

## Transferring data from Blackbaud Raiser's Edge NXT with a flow
<a name="blackbaudraisersedgenxt-transfer-data"></a>

To transfer data from Blackbaud Raiser's Edge NXT, create an Amazon AppFlow flow, and choose Blackbaud Raiser's Edge NXT as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Blackbaud Raiser's Edge NXT, see [Supported objects](#blackbaudraisersedgenxt-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#blackbaudraisersedgenxt-destinations).

## Supported destinations
<a name="blackbaudraisersedgenxt-destinations"></a>

When you create a flow that uses Blackbaud Raiser's Edge NXT as the data source, you can set the destination to any of the following connectors: 
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
<a name="blackbaudraisersedgenxt-objects"></a>

When you create a flow that uses Blackbaud Raiser's Edge NXT as the data source, you can transfer any of the following data objects to supported destinations:



- ** Action**
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Completed / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Completed Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Computed Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** End Time / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Fundraisers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Location / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Opportunity ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Outcome / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Priority / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Start Time / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status Code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Summary / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Address**
  - **** Field**:** Address Lines / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** City / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Country / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** County / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Do Not Mail / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** End / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Formatted Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Postal Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Preferred / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Seasonal End / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Seasonal Start / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Start / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Appeal**
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** End Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Goal / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Lookup ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Start Date / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Campaign**
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** End Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Goal / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Lookup ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Start Date / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Constituent**
  - **** Field**:** Address / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Age / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Birthdate / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Constituent Code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Custom Field Category / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Deceased / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** First / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Former Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Fundraiser Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Gender / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gives Anonymously / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Deceased / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Lookup ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Marital Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Middle / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Online Presence / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Postal Code / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Preferred Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Spouse / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Suffix / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Suffix 2 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title 2 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Custom Field**
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Comment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Gift ID / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Parent ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Education**
  - **** Field**:** Campus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Class Of Degree / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Entered / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Date Graduated / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Date Left / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Degree / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Faculty / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** GPA / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Known Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Majors / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Minors / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Primary / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Registration Number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** School / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Social Organization / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** String / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subject Of Study / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** class Of / **** Data type**:** String / **** Supported filters**:** 

- ** Email Address**
  - **** Field**:** Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Do Not Email / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Primary / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Event**
  - **** Field**:** Attended Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Attending Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Capacity / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Category / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** End Date / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** End Time / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Event Category / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Event ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Goal / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Invited Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Lookup ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Percent Of Goal / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Revenue / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** Start Date / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Start Date From / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Start Date To / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Start Time / **** Data type**:** String / **** Supported filters**:** 

- ** Event Participant**
  - **** Field**:** Attended / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Attended Filter / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Class Of / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Contact ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Do Not Call / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Do Not Email / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Donations / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email Eligible Filter / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Fees Paid Filter / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Former Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Guests / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Host / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Invitation Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Is Constituent / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Constituent Filter / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Lookup ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Memberships / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Middle Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name Tag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Online Data Health / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Participant Option ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Participant Options / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Participation Level / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Participation Level / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Phone Call Eligible Filter / **** Data type**:** Boolean  / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Preferred Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** RSVP Date / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** RSVP Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Registration Form / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Registration Form IDs / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Registration Form Include Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Revenue / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** Seat / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Suffix / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Summary Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Total Paid / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** Total Registration Fees / **** Data type**:** Double / **** Supported filters**:** 

- ** Fund**
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** End Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Fund ID / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Goal / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Lookup ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Start Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Fundraiser Assignment**
  - **** Field**:** Amount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Appeal ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Campaign ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** End / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Fund ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Fundraiser ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Start / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Gift**
  - **** Field**:** Acknowledgement Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Acknowledgements / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Amount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Appeal ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Balance / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Batch Number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Campaign ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Constituency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** End Gift Amount / **** Data type**:** Double / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** End Gift Date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Fund ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Fundraisers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Gift Splits / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Gift Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gift Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Anonymous / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Linked Gifts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Lookup ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Origin / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Payments / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Post Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Post Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Receipt Status / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Receipts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Reference / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Soft Credits / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Start Gift Amount / **** Data type**:** Double / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Start Gift Date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Subtype / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Gift Batch**
  - **** Field**:** Actual Amount / **** Data type**:** Double / **** Supported filters**:** 
  - **** Field**:** Added By / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Approved / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Batch Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Batch Number / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created By / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created On / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Has Exceptions / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Approved / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Number Of Gifts / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Search Text / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Membership**
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Dues / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Expires / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Joined / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Members / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Program / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Standing / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Subcategory / **** Data type**:** String / **** Supported filters**:** 

- ** Note**
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Summary / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Text / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Online Presence**
  - **** Field**:** Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Primary / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Opportunity**
  - **** Field**:** Ask Amount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Ask Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Campaign ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Deadline / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Expected Amount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Expected Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Fund ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Funded Amount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Funded Date / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Fundraisers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Linked Gifts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** List ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Purpose / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 

- ** Package**
  - **** Field**:** Appeal ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Default Gift Aamount / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** End / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Goal / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Include Inactive / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Lookup ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Notes / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Recipient Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Start / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Phone**
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Do Not Call / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Inactive / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Primary / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

- ** Relationship**
  - **** Field**:** Comment / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Constituent ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Added / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Modified / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** End / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Constituent Head Of Household / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Organization Contact / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Primary Business / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Spouse / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Is Spouse Head Of Household / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Last Modified / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Organization Contact Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Position / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Reciprocal Relationship ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Reciprocal Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Relation ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Start / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 

