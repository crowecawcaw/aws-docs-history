# Jira Cloud connector for Amazon AppFlow

Jira Cloud is a platform developed by Atlassian. The platform includes issue tracking
products that help teams plan and track their agile projects. If you're a Jira Cloud user,
your account contains data about your projects, such as issues, workflows, and events. You can use
Amazon AppFlow to transfer your Jira Cloud data to certain AWS services or other supported
applications.

## Amazon AppFlow support for Jira Cloud

Amazon AppFlow supports Jira Cloud as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Jira Cloud.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Jira Cloud.

**Supported Jira Cloud products**

Amazon AppFlow uses the Jira REST API to transfer data objects from the Jira Software product. It
does not transfer objects that are unique to the other products in Jira Cloud: Jira
Work Management and Jira Service Management.

Amazon AppFlow only connects to Jira Software on Jira Cloud. Amazon AppFlow doesn't connect to
the on-premise Jira Software Data Center product.

**Supported Jira API version**

Version 2

## Before you begin

To use Amazon AppFlow to transfer data from Jira Cloud to supported destinations, you must meet these
requirements:

- You have an Atlassian account where you use the Jira Software product in
  Jira Cloud.
- In the developer console for your Atlassian account, you've created an OAuth 2.0
  integration app for Amazon AppFlow. This app provides the client credentials that Amazon AppFlow uses to access
  your data securely when it makes authenticated calls to your account. For more information, see
  [Enabling OAuth 2.0 (3LO)](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#enabling-oauth-2-0--3lo- "https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#enabling-oauth-2-0--3lo-") in the Atlassian Developer documentation.

You must configure your app as follows:

    + In the authorization settings, you've specified a callback URL for Amazon AppFlow.


    Redirect URLs have the following format:



    ```
    https://`region`.console.aws.amazon.com/appflow/oauth
    ```

    In this URL, *region* is the code for the AWS Region
     where you use Amazon AppFlow to transfer data from Jira Cloud. For example, the code for the US East (N. Virginia)
     Region is `us-east-1`. For that Region, the URL is the following:



    ```
    https://us-east-1.console.aws.amazon.com/appflow/oauth
    ```

    For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
     in the *AWS General Reference.*
    + In the distribution settings, you've set the distribution status to
     **Sharing**.
    + In the permissions settings, you've added the Jira API, and you've enabled the
     recommended scopes below.

In the settings for your app, note the client ID and client secret because you need them to
create a connection in Amazon AppFlow.

### Recommended scopes

Before Amazon AppFlow can securely access your data in Jira Cloud, the permissions settings
for your OAuth 2.0 integration app must allow the necessary scopes for the Jira API. We
recommend that you enable the scopes below so that Amazon AppFlow can access all supported data objects.

If you want to allow fewer scopes, you can omit any scopes that apply to objects that you
don't want to transfer.

You can add scopes to your app by managing permissions in the Atlassian Developer
console.

- Under **Jira platform REST API** scopes, we recommend that you add all
  scopes.
- Under **Granular scopes**, we recommend that you add the following
  scopes:
  - `read:application-role:jira`
  - `read:audit-log:jira`
  - `read:avatar:jira`
  - `read:field:jira`
  - `read:group:jira`
  - `read:instance-configuration:jira`
  - `read:issue-details:jira`
  - `read:issue-event:jira`
  - `read:issue-link-type:jira`
  - `read:issue-meta:jira`
  - `read:issue-security-level:jira`
  - `read:issue-security-scheme:jira`
  - `read:issue-type-scheme:jira`
  - `read:issue-type-screen-scheme:jira`
  - `read:issue-type:jira`
  - `read:issue.time-tracking:jira`
  - `read:label:jira`
  - `read:notification-scheme:jira`
  - `read:permission:jira`
  - `read:priority:jira`
  - `read:project:jira`
  - `read:project-category:jira`
  - `read:project-role:jira`
  - `read:project-type:jira`
  - `read:project-version:jira`
  - `read:project.component:jir`
  - `read:project.property:jira`
  - `read:resolution:jira`
  - `read:screen:jira`
  - `read:status:jira`
  - `read:user:jira`
  - `read:workflow-scheme:jira`
  - `read:workflow:jira`
  - `read:field-configuration:jira`
  - `read:issue-type-hierarchy:jira`
  - `read:webhook:jira`

## Connecting Amazon AppFlow to your Jira Cloud

account

To connect Amazon AppFlow to your Jira Cloud account, provide details from your OAuth 2.0
integration app so that Amazon AppFlow can access your data. If you haven't yet configured your
Jira Cloud account for Amazon AppFlow integration, see [Before you begin](#jira-cloud-prereqs "#jira-cloud-prereqs").

###### To connect to Jira Cloud

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Jira Cloud**.
4. Choose **Create connection**.
5. In the **Connect to Jira Cloud** window, enter the following
   information:
   - **Client ID** – The client ID from the OAuth 2.0 integration
     app.
   - **Client secret** – The client secret from the OAuth 2.0
     integration app.
   - **Jira Cloud Domain URL** – The URL where you sign in to
     your Jira Cloud account, for example,
     `https://`your-account`.atlassian.net`.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. A window appears that asks if you want to allow
Amazon AppFlow to access your Atlassian account. 9. Choose **Accept**.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Jira Cloud as the data source, you can select this connection.

## Transferring data from Jira Cloud with a flow

To transfer data from Jira Cloud, create an Amazon AppFlow flow, and choose Jira Cloud as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Jira Cloud, see [Supported objects](#jira-cloud-objects "#jira-cloud-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#jira-cloud-destinations "#jira-cloud-destinations").

## Supported objects

When you create a flow that uses Jira Cloud as the data source, you can transfer any of the
following data objects to supported destinations:

| Object                              | Jira API endpointTo retrieve your data, Amazon AppFlow queries the following endpoints in<br>the Jira REST API. The following paths are appended to the base URI<br>`https://`your-account`.atlassian.net/rest/api/2` |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Audit Record                        | `/auditing/record`                                                                                                                                                                                                    |
| Groups                              | `/group/bulk`                                                                                                                                                                                                         |
| Issue                               | `/search`                                                                                                                                                                                                             |
| Issue Events                        | `/events`                                                                                                                                                                                                             |
| Issue Fields                        | `/field`                                                                                                                                                                                                              |
| Issue Field Configurations          | `/fieldconfiguration`                                                                                                                                                                                                 |
| Issue Link Type                     | `/issueLinkType`                                                                                                                                                                                                      |
| Issue Notification Schemes          | `/notificationscheme`                                                                                                                                                                                                 |
| Issue Priority                      | `/priority`                                                                                                                                                                                                           |
| Issue Resolution                    | `/resolution`                                                                                                                                                                                                         |
| Issue Security Scheme               | `/issuesecurityschemes`                                                                                                                                                                                               |
| Issue Type                          | `/issuetype`                                                                                                                                                                                                          |
| Issue Type Scheme                   | `/issuetypescheme`                                                                                                                                                                                                    |
| Issue Type Screen Scheme            | `/issuetypescreenscheme`                                                                                                                                                                                              |
| Jira Settings                       | `/application-properties`                                                                                                                                                                                             |
| Jira Settings Advanced              | `/application-properties/advanced-settings`                                                                                                                                                                           |
| Jira Settings Global                | `/configuration`                                                                                                                                                                                                      |
| Label                               | `/label`                                                                                                                                                                                                              |
| Myself                              | `/myself`                                                                                                                                                                                                             |
| Permission                          | `/mypermissions`                                                                                                                                                                                                      |
| Project                             | `/project/search`                                                                                                                                                                                                     |
| Project Category                    | `/projectCategory`                                                                                                                                                                                                    |
| Project Type                        | `/project/type`                                                                                                                                                                                                       |
| Server Info                         | `/serverInfo`                                                                                                                                                                                                         |
| User                                | `/users`                                                                                                                                                                                                              |
| Workflow                            | `/workflow`                                                                                                                                                                                                           |
| Workflow Scheme                     | `/workflowscheme`                                                                                                                                                                                                     |
| Workflow Scheme Project Association | `/workflowscheme/project`                                                                                                                                                                                             |
| Workflow Status                     | `/status`                                                                                                                                                                                                             |
| Workflow Status Category            | `/statuscategory`                                                                                                                                                                                                     |

For more information about these objects, see the [Jira REST API
v2](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/ "https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/") documentation.

## Supported destinations

When you create a flow that uses Jira Cloud as the data source, you can set the destination to any of the following connectors:

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
