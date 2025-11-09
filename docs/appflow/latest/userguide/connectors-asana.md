# Asana connector for Amazon AppFlow

Asana is a cloud-based team collaboration solution that helps teams organize,
plan, and complete tasks and projects. If you're an Asana user, your account contains
data about your workspaces, projects, tasks, teams, and more.
You can use Amazon AppFlow to transfer data from
Asana to certain AWS services or other supported applications.

## Amazon AppFlow support for Asana

Amazon AppFlow supports Asana as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Asana.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Asana.

## Before you begin

To use Amazon AppFlow to transfer data from Asana to supported destinations, you must meet these
requirements:

- You have an account with Asana that contains the data that you want to transfer. For more
  information about the Asana data objects that Amazon AppFlow supports, see [Supported objects](#asana-objects "#asana-objects").
- In your Asana account settings, you've created either of the following
  resources for Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to
  access your data securely when it makes authenticated calls to your account.
  - A Developer App, which supports OAuth 2.0 authentication. For information about how to
    create a Developer App, see [OAuth](https://developers.asana.com/docs/oauth "https://developers.asana.com/docs/oauth") in the Asana Developers documentation.
  - A personal access token. For more information, see [Personal access token](https://developers.asana.com/docs/personal-access-token "https://developers.asana.com/docs/personal-access-token")
    in the Asana Developers documentation.

- If you created an OAuth app, you've configured it with one or more redirect URLs for
  Amazon AppFlow.

Redirect URLs have the following format:

```
https://`region`.console.aws.amazon.com/appflow/oauth
```

In this URL, _region_ is the code for the AWS Region
where you use Amazon AppFlow to transfer data from Asana. For example, the code for the US East (N. Virginia)
Region is `us-east-1`. For that Region, the URL is the following:

```
https://us-east-1.console.aws.amazon.com/appflow/oauth
```

For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](../../../general/latest/gr/appflow.md "../../../general/latest/gr/appflow.md")
in the _AWS General Reference._

If you created a Developer App, note the client ID and client secret. If you created a
personal access token, note the token value. You provide these values to Amazon AppFlow when you connect
to your Asana account.

## Connecting Amazon AppFlow to your Asana

account

To connect Amazon AppFlow to your Asana account, provide the client credentials from
your Developer App, or provide a personal access token. If you haven't yet configured your
Asana account for Amazon AppFlow integration, see [Before you begin](#asana-prereqs "#asana-prereqs").

###### To connect to Asana

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Asana**.
4. Choose **Create connection**.
5. In the **Connect to Asana** window, for **Select
   authentication type**, choose how to authenticate Amazon AppFlow with your Asana
   account when it requests to access your data:
   - Choose **OAuth2** to authenticate Amazon AppFlow with the client ID and client
     secret from an Asana Developer App. Then enter values for **Client ID** and
     **Client secret**.
   - Choose **PAT** to authenticate Amazon AppFlow with a personal access token.
     Then enter the token value for **Personal access token**.

6. In the **Connect to Asana** window, enter the following
   information:
7. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 8. For **Connection name**, enter a name for your connection. 9. Choose **Connect**. 10. In the window that appears, sign in to your Asana account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Asana as the data source, you can select this connection.

## Transferring data from Asana with a flow

To transfer data from Asana, create an Amazon AppFlow flow, and choose Asana as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Asana, see [Supported objects](#asana-objects "#asana-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#asana-destinations "#asana-destinations").

## Supported destinations

When you create a flow that uses Asana as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses Asana as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**               | **Field**             | **Data type**                                             | **Supported filters** |
| ------------------------ | --------------------- | --------------------------------------------------------- | --------------------- |
| Audit Log Event          | actor                 | Struct                                                    |                       |
| actor_type               | String                | EQUAL_TO                                                  |
| context                  | Struct                |                                                           |
| created_at               | DateTime              |                                                           |
| details                  | Struct                |                                                           |
| event_category           | String                |                                                           |
| event_type               | String                | EQUAL_TO                                                  |
| gid                      | String                |                                                           |
| resource                 | Struct                |                                                           |
| start_end_at             | DateTime              | GREATER_THAN_OR_EQUAL_TO, LESS_THAN_OR_EQUAL_TO           |
| Goal                     | current_status_update | Struct                                                    |                       |
| due_on                   | Date                  |                                                           |
| followers                | List                  |                                                           |
| gid                      | String                |                                                           |
| html_notes               | String                |                                                           |
| is_workspace_level       | Boolean               | EQUAL_TO                                                  |
| liked                    | Boolean               |                                                           |
| likes                    | List                  |                                                           |
| metric                   | Struct                |                                                           |
| name                     | String                |                                                           |
| notes                    | String                |                                                           |
| num_likes                | Integer               |                                                           |
| owner                    | Struct                |                                                           |
| resource_type            | String                |                                                           |
| start_on                 | Date                  |                                                           |
| status                   | String                |                                                           |
| team                     | Struct                |                                                           |
| time_period              | Struct                |                                                           |
| workspace                | Struct                |                                                           |
| Portfolio                | color                 | String                                                    |                       |
| created_at               | DateTime              |                                                           |
| created_by               | Struct                |                                                           |
| current_status_update    | Struct                |                                                           |
| custom_field_settings    | List                  |                                                           |
| due_on                   | Date                  |                                                           |
| gid                      | String                |                                                           |
| members                  | List                  |                                                           |
| name                     | String                |                                                           |
| owner                    | Struct                |                                                           |
| permalink_url            | String                |                                                           |
| public                   | Boolean               |                                                           |
| resource_type            | String                |                                                           |
| start_on                 | Date                  |                                                           |
| workspace                | Struct                |                                                           |
| Project                  | archived              | Boolean                                                   | EQUAL_TO              |
| color                    | String                |                                                           |
| completed                | Boolean               |                                                           |
| completed_at             | DateTime              |                                                           |
| completed_by             | Struct                |                                                           |
| created_at               | DateTime              |                                                           |
| created_from_template    | Struct                |                                                           |
| current_status           | Struct                |                                                           |
| current_status_update    | Struct                |                                                           |
| custom_field_settings    | List                  |                                                           |
| custom_fields            | List                  |                                                           |
| default_view             | String                |                                                           |
| due_date                 | Date                  |                                                           |
| due_on                   | Date                  |                                                           |
| followers                | List                  |                                                           |
| gid                      | String                |                                                           |
| html_notes               | String                |                                                           |
| icon                     | String                |                                                           |
| is_template              | Boolean               |                                                           |
| members                  | List                  |                                                           |
| modified_at              | DateTime              |                                                           |
| name                     | String                |                                                           |
| notes                    | String                |                                                           |
| owner                    | Struct                |                                                           |
| permalink_url            | String                |                                                           |
| public                   | Boolean               |                                                           |
| resource_type            | String                |                                                           |
| start_on                 | Date                  |                                                           |
| team                     | Struct                |                                                           |
| workspace                | Struct                |                                                           |
| Section                  | created_at            | DateTime                                                  |                       |
| gid                      | String                |                                                           |
| name                     | String                |                                                           |
| project                  | Struct                |                                                           |
| resource_type            | String                |                                                           |
| Tag                      | color                 | String                                                    |                       |
| created_at               | DateTime              |                                                           |
| followers                | List                  |                                                           |
| gid                      | String                |                                                           |
| name                     | String                |                                                           |
| notes                    | String                |                                                           |
| permalink_url            | String                |                                                           |
| resource_type            | String                |                                                           |
| workspace                | Struct                |                                                           |
| Task                     | approval_status       | String                                                    |                       |
| assignee                 | Struct                |                                                           |
| assignee_section         | Struct                |                                                           |
| assignee_status          | String                |                                                           |
| completed                | Boolean               | EQUAL_TO                                                  |
| completed_at             | DateTime              | LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| completed_by             | Struct                |                                                           |
| completed_on             | Date                  | EQUAL_TO, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| created_at               | DateTime              | LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| custom_fields            | List                  |                                                           |
| dependencies             | List                  |                                                           |
| dependents               | List                  |                                                           |
| due_at                   | DateTime              | LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| due_on                   | Date                  | EQUAL_TO, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| external                 | Struct                |                                                           |
| followers                | List                  |                                                           |
| gid                      | String                |                                                           |
| has_attachment           | Boolean               | EQUAL_TO                                                  |
| hearted                  | Boolean               |                                                           |
| hearts                   | List                  |                                                           |
| html_notes               | String                |                                                           |
| is_blocked               | Boolean               | EQUAL_TO                                                  |
| is_blocking              | Boolean               | EQUAL_TO                                                  |
| is_rendered_as_separator | Boolean               |                                                           |
| is_subtask               | Boolean               | EQUAL_TO                                                  |
| liked                    | Boolean               |                                                           |
| likes                    | List                  |                                                           |
| memberships              | List                  |                                                           |
| modified_at              | DateTime              | LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO           |
| modified_on              | Date                  | EQUAL_TO, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| name                     | String                |                                                           |
| notes                    | String                |                                                           |
| num_hearts               | Integer               |                                                           |
| num_likes                | Integer               |                                                           |
| num_subtasks             | Integer               |                                                           |
| parent                   | Struct                |                                                           |
| permalink_url            | String                |                                                           |
| projects                 | List                  |                                                           |
| resource_subtype         | String                | EQUAL_TO                                                  |
| resource_type            | String                |                                                           |
| start_at                 | DateTime              |                                                           |
| start_on                 | Date                  | EQUAL_TO, LESS_THAN_OR_EQUAL_TO, GREATER_THAN_OR_EQUAL_TO |
| tags                     | List                  |                                                           |
| text                     | String                | EQUAL_TO                                                  |
| workspace                | Struct                |                                                           |
| Team                     | description           | String                                                    |                       |
| gid                      | String                |                                                           |
| html_description         | String                |                                                           |
| name                     | String                |                                                           |
| organization             | Struct                |                                                           |
| permalink_url            | String                |                                                           |
| resource_type            | String                |                                                           |
| visibility               | String                |                                                           |
| User                     | email                 | String                                                    |                       |
| gid                      | String                |                                                           |
| name                     | String                |                                                           |
| photo                    | Struct                |                                                           |
| resource_type            | String                |                                                           |
| workspaces               | List                  |                                                           |
| Workspace                | email_domains         | List                                                      |                       |
| gid                      | String                |                                                           |
| is_organization          | Boolean               |                                                           |
| name                     | String                |                                                           |
| resource_type            | String                |                                                           |
