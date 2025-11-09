# HubSpot connector for Amazon AppFlow

HubSpot is a customer relations management (CRM) solution that supports marketing,
sales, customer service, and content management. After you connect Amazon AppFlow your HubSpot
account, you can use HubSpot as a data source or destination in your flows. Run these
flows to transfer data between HubSpot and AWS services or other supported
applications.

## Amazon AppFlow support for HubSpot

Amazon AppFlow supports HubSpot as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from HubSpot.

**Supported as a data destination?**
Yes. You can use Amazon AppFlow to transfer data to HubSpot.

**Supported API versions**

Amazon AppFlow can retrieve your data by sending requests to the following versions of the
HubSpot API:

- v3
- v2
- v1

## Before you begin

To use Amazon AppFlow to transfer data from HubSpot to supported destinations, you must meet these
requirements:

- You have an account with HubSpot that contains the data that you want to transfer. For more
  information about the HubSpot data objects that Amazon AppFlow supports, see [Supported objects](#hubspot-objects "#hubspot-objects").
- You have an App Developers account with HubSpot Developers.
- In HubSpot Developers, you've created an app for Amazon AppFlow. The app provides the
  client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated
  calls to your account. For the steps to create an app, see [Creating and installing
  apps](https://developers.hubspot.com/docs/api/creating-an-app "https://developers.hubspot.com/docs/api/creating-an-app") in the HubSpot Developers documentation.
- You've configured your app as follows:
  - You've specified a redirect URL for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://`region`.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, _region_ is the code for the AWS Region
  where you use Amazon AppFlow to transfer data from HubSpot. For example, the code for the US East (N. Virginia)
  Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
  in the _AWS General Reference._
  - You've permitted the following scopes:

        - `automation`
        - `content`
        - `crm.lists.read`
        - `crm.lists.write`
        - `crm.objects.companies.read`
        - `crm.objects.companies.write`
        - `crm.objects.contacts.read`
        - `crm.objects.contacts.write`
        - `crm.objects.custom.read`
        - `crm.objects.custom.write`
        - `crm.objects.deals.read`
        - `crm.objects.deals.write`
        - `crm.objects.owners.read`
        - `crm.schemas.custom.read`
        - `e-commerce`
        - `forms`
        - `oauth`
        - `sales-email-read`
        - `tickets`

    For more information about these scopes, see [Scopes](https://developers.hubspot.com/docs/api/working-with-oauth#scopes "https://developers.hubspot.com/docs/api/working-with-oauth#scopes") in
    the HubSpot Developers documentation.

From your app settings, note your client ID and client secret because you specify these
values in the connection settings in Amazon AppFlow.

## Connecting Amazon AppFlow to your HubSpot

account

To connect Amazon AppFlow to your HubSpot account, provide details from your
HubSpot Developers app so that Amazon AppFlow can access your data. If you haven't yet
configured your HubSpot account for Amazon AppFlow integration, see [Before you begin](#hubspot-prereqs "#hubspot-prereqs").

###### To connect to HubSpot

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **HubSpot**.
4. Choose **Create connection**.
5. In the **Connect to HubSpot** window, provide the client
   credentials from your app for **Client ID** and **Client
   secret**.
6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your HubSpot account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses HubSpot as the data source, you can select this connection.

## Transferring data to or from HubSpot

with a flow

To transfer data to or from HubSpot, create an Amazon AppFlow flow, and choose
HubSpot as the data source or destination. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure a flow that uses HubSpot as the data source, you choose the
data object that you want to transfer. For the objects that Amazon AppFlow supports for
HubSpot, see [Supported objects](#hubspot-objects "#hubspot-objects"). You also choose the destination where you want to
transfer the data object that you selected. For more information about how to configure your
destination, see [Supported destinations](#hubspot-destinations "#hubspot-destinations").

## Supported destinations

When you create a flow that uses HubSpot as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses HubSpot as the data source, you can transfer any of the
following data objects to supported destinations:

| HubSpot API v3   | **Object**        | **Field** | **Data type** | **Supported filters** |
| ---------------- | ----------------- | --------- | ------------- | --------------------- |
| Call             |                   |           |               |
| Company          |                   |           |               |
| Contact          |                   |           |               |
| Custom Object    |                   |           |               |
| Deal             |                   |           |               |
| Email            |                   |           |               |
| Meeting          |                   |           |               |
| Note             |                   |           |               |
| Owner            | Archived          | Boolean   |               |
| Created At       | DateTime          |           |
| Email            | String            |           |
| Firstname        | String            |           |
| Id               | String            |           |
| Lastname         | String            |           |
| Teams            | List              |           |
| Updated At       | DateTime          |           |
| User Id          | Integer           |           |
| Postal Mail      |                   |           |               |
| Product          |                   |           |               |
| Task             |                   |           |               |
| Ticket           |                   |           |               |
| WorkFlow         | Contact List Id's | Struct    |               |
| Enabled          | Boolean           |           |
| Id               | Integer           |           |
| Inserted At      | Integer           |           |
| Name             | String            |           |
| Persona Tag Id's | List              |           |
| Type             | String            |           |
| Updated At       | Integer           |           |

| HubSpot API v2               | **Object**                | **Field** | **Data type** | **Supported filters** |
| ---------------------------- | ------------------------- | --------- | ------------- | --------------------- |
| Form                         | Always Create New Company | Boolean   |               |
| Business Unit Id             | Integer                   |           |
| Captcha Enabled              | Boolean                   |           |
| Cloneable                    | Boolean                   |           |
| Create Marketable Contact    | Boolean                   |           |
| Created At                   | Long                      |           |
| Css Class                    | String                    |           |
| Custom Uid                   | String                    |           |
| Deletable                    | Boolean                   |           |
| DeletedAt                    | Integer                   |           |
| Edit Version                 | Integer                   |           |
| Editable                     | Boolean                   |           |
| FormFieldGroups              | List                      |           |
| Guid                         | String                    |           |
| Ignore Current Values        | Boolean                   |           |
| Inline Message               | String                    |           |
| Internal Updated At          | Long                      |           |
| Is Published                 | Boolean                   |           |
| Kickback Emails Json         | Integer                   |           |
| Kickback email work flow Id  | String                    |           |
| Method                       | String                    |           |
| Name                         | String                    |           |
| Notify Recipients            | String                    |           |
| Parent Id                    | Integer                   |           |
| Payment Session Template Ids | List                      |           |
| Portable Key                 | String                    |           |
| Portal Id                    | Integer                   |           |
| Publish At                   | Integer                   |           |
| Published At                 | Integer                   |           |
| Redirect                     | String                    |           |
| Selected External Options    | List                      |           |
| Style                        | Struct                    |           |
| Submit Text                  | String                    |           |
| Thank You Message Json       | String                    |           |
| Theme Color                  | String                    |           |
| Theme Name                   | String                    |           |
| Unpublish At                 | Integer                   |           |
| Updated At                   | Long                      |           |

| HubSpot API v1     | **Object** | **Field** | **Data type** | **Supported filters** |
| ------------------ | ---------- | --------- | ------------- | --------------------- |
| CRM_Pipeline       | Active     | Boolean   |               |
| Created At         | Long       |           |
| Default            | Boolean    |           |
| Display Order      | Integer    |           |
| Label              | String     |           |
| Object Type        | String     |           |
| ObjectTypeId       | List       |           |
| Pipeline Id        | String     |           |
| Stages             | List       |           |
| Updated At         | Long       |           |
| Campaign           | App Id     | Integer   |               |
| App Name           | String     |           |
| Id                 | String     |           |
| Last Updated Time  | String     |           |
| Contact_List       | Archived   | Boolean   |               |
| Author Id          | String     |           |
| Created At         | Long       |           |
| Dynamic            | Boolean    |           |
| Filters            | List       |           |
| Ils Filter Branch  | String     |           |
| Internal           | Boolean    |           |
| Limit Exempt       | Boolean    |           |
| List Id            | Integer    |           |
| List Type          | String     |           |
| Meta Data          | Struct     |           |
| Name               | String     |           |
| Parent Id          | Integer    |           |
| Portal Id          | Integer    |           |
| Read Only          | Boolean    |           |
| Team Ids           | List       |           |
| Updated At         | Long       |           |
| Email_Event        | App Id     | Integer   |               |
| App Name           | String     |           |
| Attempt            | Integer    |           |
| Browser            | Struct     |           |
| Created            | Integer    |           |
| Device Type        | String     |           |
| Drop Message       | String     |           |
| Drop Reason        | String     |           |
| Email Campaign Id  | Long       |           |
| Filtered Event     | Boolean    |           |
| From               | String     |           |
| Id                 | String     |           |
| Location           | Struct     |           |
| Portal Id          | Integer    |           |
| Recipient          | String     |           |
| Reply To           | List       |           |
| Response           | String     |           |
| Sent By            | Struct     |           |
| Smtp Id            | String     |           |
| Subject            | String     |           |
| Suppressed Message | String     |           |
| Suppressed Reason  | String     |           |
| Type               | String     |           |
| User Agent         | Struct     |           |
| bcc                | List       |           |
| cc                 | List       |           |
| duration           | Integer    |           |
