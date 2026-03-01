# Adobe Analytics connector for Amazon AppFlow

Adobe Analytics is a business analysis software as a service (SaaS) solution. If you’re an Adobe Analytics user, your account contains business data, analytics, and more. You can use Amazon AppFlow to transfer data from Adobe Analytics to certain AWS services or other supported applications.

## Amazon AppFlow support for Adobe Analytics

Amazon AppFlow supports Adobe Analytics as follows.

**Supported as a data source?**

Yes. You can use Amazon AppFlow to transfer data from Adobe Analytics.

**Supported as a data destination?**

No. You can't use Amazon AppFlow to transfer data to Adobe Analytics.

## Before you begin

To use Amazon AppFlow to transfer data from Adobe Analytics to supported destinations, you must meet these
requirements:

- You have an account with Adobe Analytics that contains the data that you want to transfer. For more
  information about the Adobe Analytics data objects that Amazon AppFlow supports, see [Supported objects](#adobeanalytics-objects "#adobeanalytics-objects").
- In your Adobe Analytics account, you've created an app for Amazon AppFlow. The app provides the
  client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated
  calls to your account. For information about how to create an app, see [Add a new app](https://experienceleague.adobe.com/docs/mobile-services/using/manage-apps-ug/t-new-app.html?lang=en "https://experienceleague.adobe.com/docs/mobile-services/using/manage-apps-ug/t-new-app.html?lang=en") in the Adobe Analytics documentation.
- You've configured the app with a redirect URL for Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Adobe Analytics. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

Note the client ID and client secret from your app settings. You provide these values to
Amazon AppFlow when you create your connection.

### Connecting Amazon AppFlow to your Adobe Analytics account

To connect Amazon AppFlow to your Adobe Analytics account, provide the client credentials from
your Adobe Analytics app so that Amazon AppFlow can access your data. If you haven't yet configured
your Adobe Analytics account for Amazon AppFlow integration, see [Before you begin](#adobeanalytics-prereqs "#adobeanalytics-prereqs").

###### To connect to Adobe Analytics

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Adobe Analytics**.
4. Choose **Create connection**.
5. In the **Connect to Adobe Analytics** window, enter the following
   information:
   - **Connection name** — A name for the connection.
   - **Client ID** — The client ID in your Adobe Analytics
     app.
   - **Client secret** — The client secret in your
     Adobe Analytics app.
   - **X-API-KEY** — Re-enter the client ID in this field.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. Choose **Connect**. 8. In the window that appears, sign in to your Adobe Analytics account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Adobe Analytics as the data source, you can select this connection.

### Transferring data from Adobe Analytics with a flow

To transfer data from Adobe Analytics, create an Amazon AppFlow flow, and choose Adobe Analytics as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Adobe Analytics, see [Supported objects](#adobeanalytics-objects "#adobeanalytics-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#adobeanalytics-destinations "#adobeanalytics-destinations").

### Supported destinations

When you create a flow that uses Adobe Analytics as the data source, you can set the destination to any of the following connectors:

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

### Supported objects

When you create a flow that uses Adobe Analytics as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                         | **Field**                | **Data type** | **Supported filters** |
| ---------------------------------- | ------------------------ | ------------- | --------------------- |
| Annotation                         | Apply To All Reports     | Boolean       |                       |
| Approved                           | Boolean                  |               |
| Color                              | String                   |               |
| Company Id                         | Integer                  |               |
| Created Date                       | DateTime                 |               |
| Date Range                         | String                   |               |
| Description                        | String                   |               |
| Favorite                           | Boolean                  |               |
| Filter By Date Range               | String                   | EQUAL_TO      |
| Filter By Ids                      | String                   | EQUAL_TO      |
| Filter By Modified After           | DateTime                 | EQUAL_TO      |
| Id                                 | String                   |               |
| Include Type                       | String                   | EQUAL_TO      |
| Locale                             | String                   | EQUAL_TO      |
| Modified By Id                     | String                   |               |
| Modified Date                      | DateTime                 |               |
| Name                               | String                   |               |
| Owner                              | Struct                   |               |
| Owner FullName                     | String                   |               |
| Report Suite Name                  | String                   |               |
| Rsid                               | String                   |               |
| Scope                              | Struct                   |               |
| Shares                             | List                     |               |
| Sort Property                      | String                   | EQUAL_TO      |
| System User Owned                  | Boolean                  |               |
| Tags                               | List                     |               |
| Usage Summary                      | Struct                   |               |
| Usage Summary With Relevancy Score | String                   |               |
| Calculated Metric                  | Approved                 | Boolean       | EQUAL_TO              |
| Categories                         | List                     |               |
| Compatibility                      | Struct                   |               |
| Created                            | DateTime                 |               |
| Definition                         | Struct                   |               |
| Description                        | String                   |               |
| Favorite                           | Boolean                  | EQUAL_TO      |
| Filter By Ids                      | String                   | EQUAL_TO      |
| Id                                 | String                   |               |
| Include Type                       | String                   | EQUAL_TO      |
| Locale                             | String                   | EQUAL_TO      |
| Modified                           | DateTime                 |               |
| Name                               | String                   | EQUAL_TO      |
| Owner                              | Struct                   |               |
| Owner Full Name                    | String                   |               |
| Owner Id                           | Integer                  | EQUAL_TO      |
| Polarity                           | String                   |               |
| Precision                          | Integer                  |               |
| Report Suite Name                  | String                   |               |
| Rsid                               | String                   |               |
| Rsids                              | String                   | EQUAL_TO      |
| Site Title                         | String                   |               |
| Sort Direction                     | String                   | EQUAL_TO      |
| Sort Property                      | String                   | EQUAL_TO      |
| Tag Names                          | String                   | EQUAL_TO      |
| Tags                               | List                     |               |
| To Be Used In Rs Id                | String                   | EQUAL_TO      |
| Type                               | String                   |               |
| Calculated Metric Function         | Category                 | String        |                       |
| Definition                         | Struct                   |               |
| Description                        | String                   |               |
| Example                            | String                   |               |
| Example Key                        | String                   |               |
| Id                                 | String                   |               |
| Locale                             | String                   | EQUAL_TO      |
| Name                               | String                   |               |
| Namespace                          | String                   |               |
| Persistable                        | Boolean                  |               |
| Component Metadata Share           | Access Level             | String        |                       |
| Component Id                       | String                   |               |
| Component Type                     | String                   |               |
| Ims Org Id                         | String                   |               |
| Include Type                       | String                   | EQUAL_TO      |
| Share From Ims Id                  | String                   |               |
| Share Id                           | String                   |               |
| Share To Id                        | Integer                  |               |
| Share To Ims Id                    | String                   |               |
| Share To Login                     | String                   |               |
| Share To Type                      | String                   |               |
| shareToDisplayName                 | String                   |               |
| user Id                            | Integer                  | EQUAL_TO      |
| Component Metadata Tag             | Components               | List          |                       |
| Description                        | String                   |               |
| Id                                 | String                   |               |
| Name                               | String                   |               |
| Date Range                         | Alternate Variable Names | Struct        |                       |
| Approved                           | Boolean                  |               |
| Company ID                         | Integer                  |               |
| Create Date                        | DateTime                 |               |
| Curated Item                       | Boolean                  |               |
| Curated RSID                       | String                   | EQUAL_TO      |
| Definition                         | String                   |               |
| Description                        | String                   |               |
| Disabled Date                      | DateTime                 |               |
| Favorite                           | Boolean                  |               |
| Filter By IDs                      | String                   | EQUAL_TO      |
| Filter By Modified After           | DateTime                 | EQUAL_TO      |
| ID                                 | String                   |               |
| IMS Org ID                         | String                   |               |
| Include Type                       | String                   | EQUAL_TO      |
| Locale                             | String                   | EQUAL_TO      |
| Modified                           | DateTime                 |               |
| Name                               | String                   |               |
| New Definition                     | Boolean                  | EQUAL_TO      |
| Owner                              | Struct                   |               |
| Owner Full Name                    | String                   |               |
| Shares                             | List                     |               |
| Shares Full Name                   | String                   |               |
| System User Owned                  | Boolean                  |               |
| Tags                               | List                     |               |
| Template                           | Boolean                  |               |
| Usage Summary                      | Struct                   |               |
| Usage Summary With Relevancy Score | String                   |               |
| Dimension                          | Allowed For Reporting    | Boolean       |                       |
| Categories                         | List                     |               |
| Category                           | String                   |               |
| Classifiable                       | Boolean                  | EQUAL_TO      |
| Description                        | String                   |               |
| Extra Title Info                   | String                   |               |
| Filter Reportable                  | Boolean                  | EQUAL_TO      |
| ID                                 | String                   |               |
| Locale                             | String                   | EQUAL_TO      |
| Multi Valued                       | Boolean                  |               |
| Name                               | String                   |               |
| None Settings                      | Struct                   |               |
| Parent                             | String                   |               |
| Pathable                           | Boolean                  |               |
| Reportable                         | List                     |               |
| Segmentable                        | Boolean                  | EQUAL_TO      |
| Standard Component                 | Boolean                  |               |
| Support                            | List                     |               |
| Supports Data Governance           | Boolean                  |               |
| Tags                               | List                     |               |
| Title                              | String                   |               |
| Type                               | String                   |               |
| Discovery                          | Companies                | List          |                       |
| IMS Org Id                         | String                   |               |
| Metric                             | Allocation               | Boolean       |                       |
| Allowed For Reporting              | Boolean                  |               |
| Categories                         | List                     |               |
| Category                           | String                   |               |
| Description                        | String                   |               |
| Extra Title Info                   | String                   |               |
| Help Link                          | String                   |               |
| Id                                 | String                   |               |
| Locale                             | String                   | EQUAL_TO      |
| Name                               | String                   |               |
| Polarity                           | String                   |               |
| Precision                          | Integer                  |               |
| Segmentable                        | Boolean                  | EQUAL_TO      |
| Standard Component                 | Boolean                  |               |
| Support                            | List                     |               |
| Supports Data Governance           | Boolean                  |               |
| Tags                               | List                     |               |
| Title                              | String                   |               |
| Type                               | String                   |               |
| calculated                         | Boolean                  |               |
| Project                            | Access Level             | String        |                       |
| Approved                           | Boolean                  |               |
| Company Template                   | Boolean                  |               |
| Complexity                         | Struct                   |               |
| Created                            | DateTime                 |               |
| Definition                         | Struct                   |               |
| Description                        | String                   |               |
| External References                | Struct                   |               |
| Favorite                           | Boolean                  |               |
| Filter By IDs                      | String                   | EQUAL_TO      |
| Id                                 | String                   |               |
| Include Type                       | String                   | EQUAL_TO      |
| Locale                             | String                   | EQUAL_TO      |
| Migrated IDs                       | List                     |               |
| Modified                           | DateTime                 |               |
| Name                               | String                   |               |
| Owner                              | Struct                   |               |
| Owner ID                           | String                   | EQUAL_TO      |
| Report Suite Name                  | String                   |               |
| Rsid                               | String                   |               |
| Shares                             | List                     |               |
| Site Title                         | String                   |               |
| Tags                               | List                     |               |
| Template                           | Boolean                  |               |
| Type                               | String                   |               |
| Usage Summary                      | Struct                   |               |
| versionNotes                       | String                   |               |
| Report Suite                       | Calendar Type            | Struct        |                       |
| Collection Item Type               | String                   |               |
| Currency                           | String                   |               |
| Id                                 | String                   |               |
| Name                               | String                   |               |
| RS Id Contains                     | String                   | EQUAL_TO      |
| RS Ids                             | String                   |               |
| Rsid                               | String                   |               |
| Timezone Zone Info                 | String                   |               |
| Report Top Item                    | Date Range               | String        | EQUAL_TO              |
| End Date                           | DateTime                 | EQUAL_TO      |
| Item Id                            | String                   |               |
| Locale                             | String                   |               |
| Lookup None Values                 | Boolean                  | EQUAL_TO      |
| Search And                         | String                   | EQUAL_TO      |
| Search Not                         | String                   | EQUAL_TO      |
| Search Or                          | String                   | EQUAL_TO      |
| Search Phrase                      | String                   | EQUAL_TO      |
| Start Date                         | DateTime                 | EQUAL_TO      |
| Value                              | String                   |               |
| search-clause                      | String                   |               |
| Segment                            | Categories               | List          |                       |
| Created                            | DateTime                 |               |
| Definition                         | Struct                   |               |
| Definition Last Modified           | DateTime                 |               |
| Description                        | String                   |               |
| Filter By Published Segments       | String                   | EQUAL_TO      |
| Id                                 | String                   |               |
| Include Type                       | String                   | EQUAL_TO      |
| Locale                             | String                   | EQUAL_TO      |
| Modified                           | DateTime                 |               |
| Modified By ID                     | String                   |               |
| Name                               | String                   | EQUAL_TO      |
| Owner                              | Struct                   |               |
| Owner Full Name                    | String                   |               |
| Publishing Status                  | Struct                   |               |
| RSIDs                              | String                   | EQUAL_TO      |
| Report Suite Name                  | String                   |               |
| Rsid                               | String                   | EQUAL_TO      |
| Segment Filter                     | String                   | EQUAL_TO      |
| Site Title                         | String                   |               |
| Sort Direction                     | String                   | EQUAL_TO      |
| Sort Property                      | String                   | EQUAL_TO      |
| Tag Names                          | String                   | EQUAL_TO      |
| Tags                               | List                     |               |
| compatibility                      | Struct                   |               |
| Timezone                           | Current Timezone Offset  | Float         |                       |
| Name                               | String                   |               |
| Timezone Id                        | Integer                  |               |
| Timezone Zoneinfo                  | String                   |               |
| Usage Log                          | Date Created             | DateTime      |                       |
| End Date                           | DateTime                 | EQUAL_TO      |
| Event                              | String                   | EQUAL_TO      |
| Event Description                  | String                   |               |
| Event Type                         | String                   | EQUAL_TO      |
| IP                                 | String                   | EQUAL_TO      |
| IP Address                         | String                   |               |
| Login                              | String                   | EQUAL_TO      |
| Rsid                               | String                   | EQUAL_TO      |
| Start Date                         | DateTime                 | EQUAL_TO      |
| User                               | Admin                    | Boolean       |                       |
| Change Password                    | Boolean                  |               |
| Company ID                         | Integer                  |               |
| Disabled                           | Boolean                  |               |
| Email                              | String                   |               |
| First Name                         | String                   |               |
| Full Name                          | String                   |               |
| IMS User ID                        | String                   |               |
| Last Access                        | DateTime                 |               |
| Last Name                          | String                   |               |
| Login                              | String                   |               |
| Login ID                           | Integer                  |               |
| Phone Number                       | String                   |               |
| Title                              | String                   |               |
| createDate                         | DateTime                 |               |
| tempLoginEnd                       | DateTime                 |               |
