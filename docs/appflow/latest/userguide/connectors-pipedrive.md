# Pipedrive connector for Amazon AppFlow

Pipedrive is a Customer Relationship Management (CRM) service that helps companies
track and carry out projects. If you’re a Pipedrive user, your account contains data
about connections with your customers and within your organization. This can include deals,
contacts, demos, proposals, and more. You can use Amazon AppFlow to transfer data from Pipedrive
to certain AWS services or other supported applications.

## Amazon AppFlow support for Pipedrive

Amazon AppFlow supports Pipedrive as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Pipedrive.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Pipedrive.

## Before you begin

To use Amazon AppFlow to transfer data from Pipedrive to supported destinations, you must meet these
requirements:

- You have an account with Pipedrive that contains the data that you want to transfer. For more
  information about the Pipedrive data objects that Amazon AppFlow supports, see [Supported objects](#pipedrive-objects "#pipedrive-objects").
- In your Pipedrive account, you've created an unlisted app in Marketplace Manager.
  This app provides the credentials that Amazon AppFlow uses to make authenticated calls to your account
  and securely access your data. For the steps to create an app, see [Creating an
  app](https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app "https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app") in the _Pipedrive Developer
  Documentation_.

You've configured your app as follows:

    + You've specified a redirect URL (also referred to as a *callback
     URL*) for Amazon AppFlow.


    Redirect URLs have the following format:



    ```
    https://`region`.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region
     where you use Amazon AppFlow to transfer data from Pipedrive. For example, the code for the US East (N. Virginia)
     Region is `us-east-1`. For that Region, the URL is the following:



    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
     in the *AWS General Reference.*
    + You've activated the access scopes that provide access to the data that you want to
     transfer. For more information about Pipedrive scopes, see [Scopes and permission explanations](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations "https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations") in the *Pipedrive Developer
     Documentation*.

From the settings for your app, note the client ID and client secret. When you connect to
your Pipedrive account, you provide these values to Amazon AppFlow.

## Connecting Amazon AppFlow to your Pipedrive

account

To connect Amazon AppFlow to your Pipedrive account, provide details from your
Pipedrive project so that Amazon AppFlow can access your data. If you haven't yet configured
your Pipedrive project for Amazon AppFlow integration, see [Before you begin](#pipedrive-prereqs "#pipedrive-prereqs").

###### To connect to Pipedrive

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Pipedrive**.
4. Choose **Create connection**.
5. In the **Connect to Pipedrive** window, enter the following
   information:
   - **Client ID** – The client ID of the OAuth 2.0 client ID in your
     Pipedrive project.
   - **Client secret** – The client secret of the OAuth 2.0 client ID
     in your Pipedrive project.
   - **Instance URL** – The URL of the instance where you want to run
     the operation, for example, https://awsappflow-domain.pipedrive.com.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your Pipedrive account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Pipedrive as the data source, you can select this connection.

## Transferring data from Pipedrive with a flow

To transfer data from Pipedrive, create an Amazon AppFlow flow, and choose Pipedrive as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Pipedrive, see [Supported objects](#pipedrive-objects "#pipedrive-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#pipedrive-destinations "#pipedrive-destinations").

## Supported destinations

When you create a flow that uses Pipedrive as the data source, you can set the destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- [HubSpot](connectors-hubspot.md "connectors-hubspot.md")
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")
- [Zoho CRM](connectors-zoho-crm.md "connectors-zoho-crm.md")

## Supported objects

When you create a flow that uses Pipedrive as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                | **Field**   | **Data type** | **Supported filters** |
| ------------------------- | ----------- | ------------- | --------------------- |
| Activities                |             |               |                       |
| Activity Types            | Active      | Boolean       |                       |
| Add Time                  | DateTime    |               |
| Color                     | String      |               |
| Custom Flag               | Boolean     |               |
| ID                        | Long        |               |
| Icon                      | String      |               |
| Key                       | String      |               |
| Name                      | String      |               |
| Order Number              | Long        |               |
| Update Time               | DateTime    |               |
| CallLogs                  | Activity Id | Long          |                       |
| Company Id                | Long        |               |
| Deal Id                   | Integer     |               |
| Duration                  | String      |               |
| End Time                  | DateTime    |               |
| From Phone Number         | String      |               |
| Has Recording             | Boolean     |               |
| ID                        | String      |               |
| Note                      | String      |               |
| Organization Id           | Integer     |               |
| Outcome                   | String      |               |
| Person Id                 | Integer     |               |
| Start Time                | DateTime    |               |
| To Phone Number           | String      |               |
| User Id                   | Long        |               |
| Currencies                | Active Flag | Boolean       |                       |
| Code                      | String      |               |
| Decimal Points            | Integer     |               |
| ID                        | Integer     |               |
| Is Custom Flag            | Boolean     |               |
| Name                      | String      |               |
| Symbol                    | String      |               |
| Deals                     |             |               |                       |
| Lead Labels               | Add Time    | DateTime      |                       |
| Color                     | String      |               |
| ID                        | Integer     |               |
| Name                      | String      |               |
| Update Time               | DateTime    |               |
| Lead Sources              | Name        | String        |                       |
| Leads                     | Add Time    | DateTime      |                       |
| CC Email                  | String      |               |
| Creator Id                | Long        |               |
| Expected Close Date       | String      |               |
| ID                        | String      |               |
| Is Archived               | Boolean     |               |
| Label Ids                 | String      |               |
| Next Activity Id          | Long        |               |
| Organization Id           | Integer     |               |
| Owner Id                  | Long        |               |
| Person Id                 | Long        |               |
| Source Name               | String      |               |
| Title                     | String      |               |
| Update Time               | DateTime    |               |
| Value                     | Struct      |               |
| Visible To                | String      |               |
| Was Seen                  | Boolean     |               |
| Notes                     |             |               |                       |
| Organization              |             |               |                       |
| Permission Sets           | App         | String        |                       |
| Assignment Count          | Integer     |               |
| Description               | String      |               |
| ID                        | Integer     |               |
| Name                      | String      |               |
| Type                      | String      |               |
| Persons                   |             |               |                       |
| Pipelines                 | Active      | Boolean       |                       |
| Add Time                  | DateTime    |               |
| Deal Probability          | Boolean     |               |
| ID                        | Integer     |               |
| Name                      | String      |               |
| Order Number              | Integer     |               |
| Selected                  | Boolean     |               |
| URL Title                 | String      |               |
| Update Time               | DateTime    |               |
| Products                  |             |               |                       |
| Roles                     | Active Flag | Boolean       |                       |
| Assignment Count          | Integer     |               |
| Description               | String      |               |
| ID                        | Integer     |               |
| Level                     | Integer     |               |
| Name                      | String      |               |
| Parent Role Id            | Integer     |               |
| Sub Role Count            | Integer     |               |
| Stages                    | Active Flag | Boolean       |                       |
| Add Time                  | DateTime    |               |
| Deal Probability          | Integer     |               |
| ID                        | Integer     |               |
| Name                      | String      |               |
| Order Number              | Integer     |               |
| Pipeline Deal Probability | Boolean     |               |
| Pipeline Id               | Integer     |               |
| Pipeline Name             | String      |               |
| Rotten Days               | String      |               |
| Rotten Flag               | Boolean     |               |
| Update Time               | DateTime    |               |
| Users                     | Access      | List          |                       |
| Active Flag               | Boolean     |               |
| Created                   | DateTime    |               |
| Default Currency          | String      |               |
| Email                     | String      |               |
| Has Created Company       | Boolean     |               |
| ID                        | String      |               |
| Icon URL                  | String      |               |
| Is Admin                  | Integer     |               |
| Is You                    | Boolean     |               |
| Language                  | Integer     |               |
| Last Login                | DateTime    |               |
| Locate                    | String      |               |
| Modified                  | DateTime    |               |
| Name                      | String      |               |
| Phone                     | String      |               |
| Role Id                   | Integer     |               |
| Signup Flow Variation     | String      |               |
| Timezone                  | String      |               |
| Timezone Offset           | String      |               |
